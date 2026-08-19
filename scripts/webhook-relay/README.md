# Breeze Webhook Relay

Cloudflare Worker that forwards `push` webhooks from the private
**BreezeLauncher** repo to **BreezeLauncherAndroid**'s
`repository_dispatch` event, triggering the Android CI build — without
adding any workflow file to the private repo.

## Architecture

```
push to BreezeLauncher (private)
        │
        │ GitHub webhook (X-Hub-Signature-256 HMAC)
        ▼
Cloudflare Worker (this repo: scripts/webhook-relay/worker.js)
        │  • verifies HMAC signature
        │  • filters: only push events, only refs/heads/main
        │  • POSTs repository_dispatch to BLA
        ▼
BreezeLauncherAndroid → Android CI (repository_dispatch: upstream-changed)
```

## One-time setup

### 1. Deploy the Worker

```bash
cd scripts/webhook-relay
npx wrangler deploy
```

Note the deployed URL, e.g.
`https://breeze-webhook-relay.<your-account>.workers.dev/`.

### 2. Set Worker secrets

```bash
# A GitHub PAT with `repo` scope on BreezeLauncherAndroid.
# The ghp_ token used for cloning/pushing works.
npx wrangler secret put BLA_DISPATCH_TOKEN

# A random string — generate with: openssl rand -hex 32
npx wrangler secret put WEBHOOK_SECRET
```

### 3. Configure the webhook on BreezeLauncher

GitHub → **wisebreeze/BreezeLauncher** → Settings → Webhooks → Add webhook:

| Field | Value |
|---|---|
| Payload URL | `https://breeze-webhook-relay.<account>.workers.dev/` |
| Content type | `application/json` |
| Secret | the same `WEBHOOK_SECRET` from step 2 |
| Which events | Just the `push` event |
| Active | ✓ |

### 4. Verify

Push any commit to `main` on BreezeLauncher. Within ~2 seconds you
should see:

- A `200` delivery in the webhook's "Recent Deliveries" tab.
- A new "Android CI" run on BreezeLauncherAndroid triggered by
  `repository_dispatch`.

## Behavior

- **Signature verification**: requests without a valid
  `X-Hub-Signature-256` matching `WEBHOOK_SECRET` are rejected with
  `401`.
- **Event filter**: only `push` events are forwarded; `ping` and
  others return `200 Ignored`.
- **Branch filter**: only `refs/heads/main` triggers a build; pushes
  to other branches return `200 Ignored ref: ...`.
- **Payload**: the dispatch carries `sha`, `repo`, `pusher`, and
  `compare` URL in `client_payload` for traceability.

## Files

- `worker.js` — the Worker logic.
- `wrangler.toml` — Cloudflare Worker config.
