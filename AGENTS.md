# Agent Guide: Publishing a Version Update

This document is the single source of truth for AI assistants (and humans)
on how to publish a new BreezeLauncher version. Follow it step by step.
Do not improvise.

## Prerequisites

Before publishing, verify:

1. **`artifact` release has a fresh APK.** The `Android CI` workflow on
   this repo (`BreezeLauncherAndroid`) builds the APK and uploads it to
   the `artifact` release. Check
   https://github.com/wisebreeze/BreezeLauncherAndroid/releases/tag/artifact
   and confirm `BreezeLauncher-default-release.apk` was uploaded within
   the last few hours. If it is stale, trigger `Android CI` manually and
   wait for it to finish.
2. **`GITEE_TOKEN` secret is set.** Settings → Secrets and variables →
   Actions → `GITEE_TOKEN` must exist with Gitee `projects` push scope.
   Without it the Gitee mirror step fails.
3. **Source code on `main` is ready.** The `artifact` APK is built from
   the private `BreezeLauncher` repo's `main` branch. Whatever is on
   `main` at build time is what ships.

## Version naming

- **Tag**: `v<versionName>`, e.g. `v26.7.17`. Always lowercase `v`.
- **versionName**: `<yearPart>.<M>.<D>`, where `yearPart = year - 2000`
  for years 2000–2099. Month and day are **not** zero-padded.
  Examples: `26.7.17`, `3010.6.1`.
- **versionCode**: derived automatically by the workflow as
  `<yearPart><MM><DD>` (month/day zero-padded). Example: `26.7.17` →
  `260717`. You do **not** set versionCode manually.

Never reuse a versionName. Once a tag is published it is permanent.

## Publishing steps

### 1. Draft the release

Go to
https://github.com/wisebreeze/BreezeLauncherAndroid/releases/new
(or Releases → Draft a new release).

- **Choose a tag**: type `v<versionName>` (e.g. `v26.7.17`) and select
  "Create new tag: v<versionName> on publish". The tag is created from
  `main` automatically when you publish.
- **Release title**: the bare versionName, e.g. `26.7.17`. (Cosmetic;
  the app does not read it.)
- **Description**: paste the bilingual changelog following the format
  in [update/changeLog/README.md](update/changeLog/README.md). The
  workflow saves this body verbatim as
  `update/changeLog/<versionName>.md`, so it must obey the format spec.
- Do **not** attach the APK manually. The workflow downloads it from
  the `artifact` release and attaches it automatically.
- Do **not** check "Set as the latest release" manually unless you want
  to override GitHub's auto-detection. Usually leave it default.

### 2. Publish

Click **Publish release**. This triggers the `Release on publish`
workflow (`.github/workflows/release-on-tag.yml`), which:

1. Downloads `BreezeLauncher-default-release.apk` from the `artifact`
   release.
2. Attaches it to the newly published release.
3. Saves the release body as `update/changeLog/<versionName>.md` and
   commits to `main`.
4. Computes the APK's MD5.
5. Regenerates `update/update.json` with the new version / versionCode
   / md5 / download URL / changelog URL, preserving the existing
   `forceUpdate` and `forceUpdateBelowVersionCode` fields. Commits to
   `main`.
6. Mirrors `update/` to the Gitee `BreezeLauncherApp` repo
   (`update.json` + `changeLog/*.md`).

### 3. Verify

Watch the workflow run:
https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/release-on-tag.yml

When it finishes, confirm:

- The release page shows `BreezeLauncher-default-release.apk` as an asset.
- `update/update.json` on `main` has the new versionCode and md5.
- `update/changeLog/<versionName>.md` on `main` matches the release body.
- Gitee `update.json` is updated:
  https://gitee.com/wisebreeze/BreezeLauncherApp/raw/main/update.json
- Gitee changelog is reachable:
  https://gitee.com/wisebreeze/BreezeLauncherApp/raw/main/changeLog/<versionName>.md

The Android app fetches `update.json` from Gitee at most once per day per
device, so users see the update within 24 hours.

## Changelog format (mandatory)

Every release body **must** follow the bilingual format below. The app
parses it at runtime by looking for the `## English` and `## 简体中文`
markers; a malformed body leaves some users with no changelog.

**Keep it concise.** Each entry is one short sentence — a title plus a
brief description, no implementation details, no file names, no
internal jargon. Users read this in a small update dialog; long
entries get truncated and ignored.

```markdown
# <versionName>

## English

### New Features

- **Feature title**: One short sentence describing what was added.

### Fixes

- **Fix title**: One short sentence describing what was fixed.

### Improvements

- **Improvement title**: One short sentence describing what was enhanced.

### CI / Build

- **Change title**: One short sentence describing the build/CI change.

---

## 简体中文

### 新功能

- **功能标题**：一句话描述新增了什么。

### 修复

- **修复标题**：一句话描述修复了什么。

### 改进

- **改进标题**：一句话描述改进了什么。

### CI / 构建

- **变更标题**：一句话描述构建/CI 变更。
```

### Rules

1. **One top-level heading** — `# <versionName>` on the first line.
2. **English section** — starts with `## English`, runs until the `---`
   separator.
3. **Separator** — exactly one `---` line between the two sections. No
   other `---` lines inside either section.
4. **Chinese section** — starts with `## 简体中文`, runs to end of file.
5. **Sub-headings** — `### New Features` / `### Fixes` / `### Improvements`
   / `### CI / Build` (and the Chinese equivalents). Omit a sub-heading
   if it has no entries; do not leave it empty.
6. **List items** — `- **Title**: description`. Title bold, colon, space,
   then **one short sentence** (typically under 15 words). No multi-line
   explanations, no code identifiers, no internal class/method names.
7. **No raw HTML** — Markdown only.
8. **No trailing whitespace**.
9. **English first, Chinese second** — always in this order.
10. **Traditional Chinese** — there is no `## 繁體中文` section. The app
    shows the `## 简体中文` section to `zh-CN`, `zh-TW`, and `zh-HK`
    users alike.

### What to write

- **User-facing only.** Write what the user sees or feels. Internal
  refactors, dependency bumps, and code cleanup with no observable
  behavior change do not belong in the changelog.
- **One bullet per user-visible change.** Group multiple commits that
  fix the same symptom into a single bullet.
- **Describe the outcome, not the implementation.** "Fixed some
  CurseForge mods failing to download" is good. "Added fallback to
  `/v1/mods/{modId}/files/{fileId}/download-url` endpoint when
  `downloadUrl` is null" is too detailed for the changelog.
- **Skip the `CI / Build` section** if there are no user-relevant build
  changes.

## Force update

To force every user (or every user below a version floor) to update,
edit `update/update.json` on `main` **after** the release workflow
finishes:

- `forceUpdate: true` — every older client is forced to update.
- `forceUpdateBelowVersionCode: <int>` — only clients whose
  `versionCode` is strictly below this value are forced to update.
  Use this to force-update stragglers without bothering users who are
  already on a recent build.

Both fields are preserved across releases (the workflow copies them
from the previous `update.json`), so you only need to set them once
per force-update campaign and clear them when no longer needed.

Commit the change and push to `main`, then manually trigger the
`Release on publish` workflow (workflow_dispatch) with the current
release tag to re-sync `update.json` to Gitee.

## Common mistakes to avoid

- **Pushing a bare tag without a release.** The workflow triggers on
  `release: published`, not on `push: tags`. A bare `git push --tags`
  does nothing.
- **Attaching the APK manually.** The workflow overwrites it anyway.
  Just let the workflow handle it.
- **Writing the changelog in only one language.** Half your users see
  an empty changelog. Always bilingual.
- **Editing `update.json` or `changeLog/*.md` by hand before
  publishing.** The workflow regenerates them from the release. Hand
  edits get clobbered. Set force-update fields **after** the workflow
  runs.
- **Reusing a versionName.** Tags are immutable. If you need to
  re-release, bump the version (e.g. `26.7.17` → `26.7.18`).
