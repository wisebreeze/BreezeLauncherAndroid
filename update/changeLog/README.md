# Changelog Files

Each released version has its own Markdown file named `<versionName>.md`,
for example `26.7.17.md`.

## Naming convention

- File name **must** match the `version` field in `update.json` exactly
  (e.g. `version: "26.7.17"` → `26.7.17.md`).
- Use the bare version name without any prefix or suffix — no `v`, no
  `-release`, no date.

## Content format

Each file is bilingual (English first, then Simplified Chinese) and follows
the structure below. Sections without entries can be omitted.

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

## When to add a file

Add a new `<versionName>.md` here **before** publishing the corresponding
release. The `sync-update-to-gitee.yml` workflow will push it to Gitee, and
`update.json`'s `changeLog` URL must point to the Gitee raw URL for this file.
