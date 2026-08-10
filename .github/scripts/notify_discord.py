#!/usr/bin/env python3
"""Post the English changelog to Discord (text only, no APK, no emoji).

Env vars (passed from the workflow):
  DISCORD_WEBHOOK          Discord webhook URL (from repo secret)
  GITHUB_REPOSITORY        owner/repo (auto-set by Actions)
  GITHUB_EVENT_NAME        "push" | "workflow_dispatch" (auto-set)
  GITHUB_BEFORE            previous SHA on push (auto-set)
  GITHUB_SHA               current SHA (auto-set)

The changelog is generated from git log (English conventional-commit
messages). No APK attachment, no emoji — just the version header and
the commit list as a plain-text Discord message.
"""
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone


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

    # Version — matches build.gradle.kts date-based scheme (UTC build date)
    now = datetime.now(timezone.utc)
    year_part = now.year - 2000 if 2000 <= now.year <= 2099 else now.year
    version = f"{year_part}.{now.month}.{now.day}"

    changelog = build_changelog()

    content = f"BreezeLauncher {version}\n\nChangelog:\n{changelog}"

    body = json.dumps({"content": content}).encode()
    headers = {"Content-Type": "application/json"}

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
