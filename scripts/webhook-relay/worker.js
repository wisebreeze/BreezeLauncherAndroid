// Cloudflare Worker: forward GitHub push webhook from BreezeLauncher
// (private repo) to BreezeLauncherAndroid's repository_dispatch event.
//
// Setup:
//   1. Deploy this Worker (e.g. `wrangler deploy`).
//   2. Set Worker secret: wrangler secret put BLA_DISPATCH_TOKEN
//      (a GitHub PAT with `repo` scope on BreezeLauncherAndroid)
//   3. In BreezeLauncher repo Settings → Webhooks → Add webhook:
//      - Payload URL: https://<worker-name>.<account>.workers.dev/
//      - Content type: application/json
//      - Events: Just the push event
//      - Secret: a random string, then set it as Worker secret
//        `WEBHOOK_SECRET` (wrangler secret put WEBHOOK_SECRET)
//
// The Worker validates the X-Hub-Signature-256 HMAC against WEBHOOK_SECRET,
// ignores pushes to non-main branches, and fires `repository_dispatch`
// with event type `upstream-changed` on BreezeLauncherAndroid.

const BLA_OWNER = "wisebreeze";
const BLA_REPO = "BreezeLauncherAndroid";
const BLA_EVENT_TYPE = "upstream-changed";

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    // --- Verify HMAC signature ---
    const sig = request.headers.get("X-Hub-Signature-256") || "";
    const body = await request.text();
    const expected = await hmacSha256Hex(env.WEBHOOK_SECRET, body);
    if (sig !== `sha256=${expected}`) {
      return new Response("Invalid signature", { status: 401 });
    }

    // --- Only forward push events ---
    const eventType = request.headers.get("X-GitHub-Event") || "";
    if (eventType !== "push") {
      return new Response("Ignored", { status: 200 });
    }

    let payload;
    try {
      payload = JSON.parse(body);
    } catch {
      return new Response("Bad JSON", { status: 400 });
    }

    // --- Only forward pushes to main ---
    const ref = payload.ref || "";
    if (ref !== "refs/heads/main") {
      return new Response(`Ignored ref: ${ref}`, { status: 200 });
    }

    // --- Fire repository_dispatch on BLA ---
    const after = payload.after || "";
    const resp = await fetch(
      `https://api.github.com/repos/${BLA_OWNER}/${BLA_REPO}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `token ${env.BLA_DISPATCH_TOKEN}`,
          Accept: "application/vnd.github+json",
          "Content-Type": "application/json",
          "User-Agent": "breeze-webhook-relay",
        },
        body: JSON.stringify({
          event_type: BLA_EVENT_TYPE,
          client_payload: {
            sha: after,
            repo: payload.repository?.full_name || "",
            pusher: payload.pusher?.name || "",
            compare: payload.compare || "",
          },
        }),
      }
    );

    return new Response(
      `dispatch ${resp.status} sha=${after.slice(0, 7)}`,
      { status: 200 }
    );
  },
};

async function hmacSha256Hex(key, msg) {
  const enc = new TextEncoder();
  const cryptoKey = await crypto.subtle.importKey(
    "raw",
    enc.encode(key),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sig = await crypto.subtle.sign("HMAC", cryptoKey, enc.encode(msg));
  return [...new Uint8Array(sig)]
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}
