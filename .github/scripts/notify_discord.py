#!/usr/bin/env python3
"""Post a build notification to Discord: changelog + APK attachment.

Env vars (passed from the workflow):
  DISCORD_WEBHOOK          Discord webhook URL (from repo secret)
  APK_FILE                 Path to the built APK (final_name output)
  ARTIFACT_RELEASE_TAG     GitHub release tag holding the APK (default "artifact")
  GITHUB_REPOSITORY        owner/repo (auto-set by Actions)
  GITHUB_EVENT_NAME        "push" | "workflow_dispatch" (auto-set)
  GITHUB_BEFORE            previous SHA on push (auto-set)
  GITHUB_SHA               current SHA (auto-set)

If the APK fits within Discord's attachment limit (24 MiB safe threshold
for unboosted servers), it is attached to the message. Otherwise the
message falls back to a GitHub release download link.
"""
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error
import uuid
from datetime import datetime, timezone

MAX_ATTACHMENT = 24 * 1024 * 1024  # 24 MiB safe threshold (Discord unboosted = 25 MiB)


def build_changelog() -> str:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    before = os.environ.get("GITHUB_BEFORE", "")
    sha = os.environ.get("GITHUB_SHA", "")
    if event == "push" and before and before != "0" * 40:
        rng = f"{before}..{sha}"
    else:
        rng = "HEAD~15..HEAD"
    try:
        res = subprocess.run(
            ["git", "log", "--pretty=format:- %s", "--no-merges", rng],
            capture_output=True, text=True, timeout=10,
        )
        log = res.stdout.strip()
    except Exception:
        log = ""
    if not log:
        log = "- (no changelog available)"
    # Cap at 30 lines to stay within Discord's 2000-char content limit
    lines = log.split("\n")[:30]
    text = "\n".join(lines)
    if len(text) > 1800:
        text = text[:1797] + "..."
    return text


def main() -> int:
    webhook = os.environ.get("DISCORD_WEBHOOK", "").strip()
    if not webhook:
        print("::warning::DISCORD_APP_WEBHOOK secret not set; skipping Discord notification")
        return 0

    apk_file = os.environ.get("APK_FILE", "").strip()
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    release_tag = os.environ.get("ARTIFACT_RELEASE_TAG", "artifact").strip() or "artifact"

    # Version — matches build.gradle.kts date-based scheme (UTC build date)
    now = datetime.now(timezone.utc)
    year_part = now.year - 2000 if 2000 <= now.year <= 2099 else now.year
    version = f"{year_part}.{now.month}.{now.day}"

    changelog = build_changelog()

    apk_size = 0
    if apk_file and os.path.exists(apk_file):
        apk_size = os.path.getsize(apk_file)

    apk_basename = os.path.basename(apk_file) if apk_file else "BreezeLauncher-release.apk"
    download_url = f"https://github.com/{repo}/releases/download/{release_tag}/{apk_basename}"

    lines = [
        f"🚀 **BreezeLauncher v{version}**",
        "",
        "📋 **更新日志 / Changelog:**",
        changelog,
        "",
    ]
    attach_apk = 0 < apk_size <= MAX_ATTACHMENT
    if attach_apk:
        lines.append(f"📦 **安装包:** 见附件 ({apk_size // 1024 // 1024} MB)")
    else:
        lines.append(f"📦 **安装包:** {download_url}")
        if apk_size > MAX_ATTACHMENT:
            lines.append(
                f"⚠️ APK ({apk_size // 1024 // 1024} MB) 超过 Discord 附件限制，请使用上方链接下载。"
            )
    content = "\n".join(lines)

    if attach_apk:
        # Multipart form-data: payload_json + file
        boundary = "----BLA" + uuid.uuid4().hex
        payload_json = json.dumps({"content": content})
        with open(apk_file, "rb") as f:
            apk_data = f.read()
        head = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="payload_json"\r\n'
            f"Content-Type: application/json\r\n\r\n"
            f"{payload_json}\r\n"
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{apk_basename}"\r\n'
            f"Content-Type: application/vnd.android.package-archive\r\n\r\n"
        ).encode()
        tail = f"\r\n--{boundary}--\r\n".encode()
        body = head + apk_data + tail
        headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
        print(f"Attaching APK ({apk_size} bytes) to Discord message")
    else:
        body = json.dumps({"content": content}).encode()
        headers = {"Content-Type": "application/json"}
        print("Sending Discord message without APK attachment (too large or missing)")

    req = urllib.request.Request(webhook, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            resp_text = resp.read().decode(errors="replace")[:300]
            print(f"Discord response: {resp.status} {resp_text}")
    except urllib.error.HTTPError as e:
        resp_text = e.read().decode(errors="replace")[:300]
        print(f"::error::Discord webhook failed: HTTP {e.code} {resp_text}")
        return 1
    except Exception as e:
        print(f"::error::Discord webhook error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
