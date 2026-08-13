#!/usr/bin/env python3
"""Post the English changelog to Discord when a release is published.

Reads the release body (bilingual markdown) from CHANGELOG_FILE,
extracts the English section, and posts it as a Discord embed
(markdown-supported, 4096-char description limit).

Env vars:
  DISCORD_WEBHOOK   Discord webhook URL (from repo secret)
  CHANGELOG_FILE    Path to the release body markdown (default /tmp/changelog.md)
  VERSION_NAME      Version name (e.g. 26.8.10)
  RELEASE_TAG       Release tag (e.g. v26.8.10)
  RELEASE_URL       GitHub release URL

The User-Agent header is set to avoid Cloudflare 403 (code 1010) blocks
on the default Python-urllib UA.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error


def extract_english(body: str) -> str:
    """Extract the English section from the bilingual changelog.

    Body format:
        # <version>
        ## English
        ...english content...
        ---
        ## 简体中文
        ...
    Returns the english content (without the ## English header).
    Falls back to the full body (minus the top heading) if no marker.
    """
    m = re.search(r'## English\s*\n(.*?)(?:\n---\s*\n|\Z)', body, re.DOTALL)
    if m:
        return m.group(1).strip()
    return re.sub(r'^# .+\n*', '', body).strip()


def main() -> int:
    webhook = os.environ.get("DISCORD_WEBHOOK", "").strip()
    if not webhook:
        print("::warning::DISCORD_APP_WEBHOOK secret not set; skipping Discord notification")
        return 0

    changelog_file = os.environ.get("CHANGELOG_FILE", "/tmp/changelog.md")
    version = os.environ.get("VERSION_NAME", "")
    release_url = os.environ.get("RELEASE_URL", "")

    try:
        with open(changelog_file, encoding="utf-8") as f:
            body = f.read()
    except FileNotFoundError:
        print(f"::error::Changelog file not found: {changelog_file}")
        return 1

    english = extract_english(body)

    # Append a markdown download link for the APK at the bottom.
    apk_url = os.environ.get("APK_DOWNLOAD_URL", "").strip()
    if apk_url:
        english = english.rstrip() + "\n\n**Download APK**: [BreezeLauncher-default-release.apk](" + apk_url + ")"

    # Discord embed description limit: 4096 chars
    if len(english) > 4090:
        english = english[:4087] + "..."

    embed = {
        "title": f"BreezeLauncher {version}" if version else "BreezeLauncher",
        "description": english,
        "color": 3447003,  # sky blue (#1ABC9C-ish)
    }
    if release_url:
        embed["url"] = release_url

    payload = {"embeds": [embed]}
    data = json.dumps(payload).encode()

    req = urllib.request.Request(
        webhook,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "BreezeLauncher-CI/1.0",
        },
        method="POST",
    )

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
