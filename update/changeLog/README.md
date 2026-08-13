# Changelog Files

Each released version has its own Markdown file named `<versionName>.md`,
for example `26.7.17.md`.

## Naming convention

- File name **must** match the `version` field in `update.json` exactly
  (e.g. `version: "26.7.17"` → `26.7.17.md`).
- Use the bare version name without any prefix or suffix — no `v`, no
  `-release`, no date.

## Bilingual format (mandatory)

Every changelog file **must** contain both an English and a Simplified
Chinese section, separated by a horizontal rule. The app parses the file
at runtime and shows the Chinese section to Simplified / Traditional
Chinese users, and the English section to everyone else. A file with
only one language will leave the other locale's users with no changelog.

### Structure

```markdown
# <versionName>

## English

### New Features

- **Feature title**: One-sentence summary. Detailed explanation of what
  changed and why.

### Fixes

- **Fix title**: What was broken and how it is now resolved.

### Improvements

- **Improvement title**: What was enhanced and the resulting benefit.

### CI / Build

- **Change title**: Build or CI pipeline change.

---

## 简体中文

### 新功能

- **功能标题**：一句话概述。详细说明改了什么、为什么。

### 修复

- **修复标题**：之前什么坏了、现在如何修复。

### 改进

- **改进标题**：改进了什么、带来什么好处。

### CI / 构建

- **变更标题**：构建或 CI 流水线变更。
```

### Rules

1. **Top-level heading** — exactly one `# <versionName>` line at the top.
2. **English section** — starts with `## English` and contains all
   English content until the separator.
3. **Separator** — a single `---` line on its own, between the English
   and Chinese sections. No other `---` lines are allowed inside either
   section (use `###` sub-headings to group content instead).
4. **Chinese section** — starts with `## 简体中文` and contains all
   Simplified Chinese content until end of file.
5. **Sub-headings** — use `###` for category groups (New Features, Fixes,
   Improvements, CI / Build). Omit a sub-heading if it has no entries
   rather than leaving it empty.
6. **List items** — each entry is a `- **Title**: description` bullet.
   The title is bold, followed by a colon and a space, then the
   description. Keep descriptions to 1–3 sentences.
7. **No raw HTML** — Markdown only, so the in-app renderer can display it.
8. **No trailing whitespace** — keep lines clean to avoid diff noise.

### Section order

Always English first, then Chinese. The app identifies sections by the
`## English` and `## 简体中文` markers, not by position, but keeping a
consistent order makes the raw files easier to review.

### Traditional Chinese

There is no separate Traditional Chinese section. The app shows the
Simplified Chinese section to both `zh-CN` and `zh-TW` (and `zh-HK`)
users. If a Traditional Chinese translation is needed in the future,
add a `## 繁體中文` section after `## 简体中文` and update the app's
language-mapping logic.

## When to add a file

The `release-on-tag.yml` workflow automatically creates the changelog
file from the GitHub Release body when a release is published. Write
the release body in the exact bilingual format above and the workflow
will save it verbatim to `changeLog/<versionName>.md`.
