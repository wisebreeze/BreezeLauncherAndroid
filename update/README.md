# Update Manifest

This directory holds the app-update manifest (`update.json`) and per-version
changelogs (`changeLog/<versionName>.md`) that are mirrored to the Gitee
configuration repository
[`wisebreeze/BreezeLauncherApp`](https://gitee.com/wisebreeze/BreezeLauncherApp)
by the `release-on-tag.yml` workflow when a release is published.

The Android app fetches `update.json` from Gitee at launch (once per day) via
`AppUpdateChecker` and renders the changelog Markdown inside `UpdateDialog`.

## File layout

```
update/
├── update.json                  # Main manifest consumed by the app
├── changeLog/
│   ├── README.md                # Naming convention for changelog files
│   └── <versionName>.md         # One Markdown file per released version
└── README.md                    # This file
```

## `update.json` schema

| Field                         | Type    | Required | Description                                                                                          |
|-------------------------------|---------|----------|------------------------------------------------------------------------------------------------------|
| `version`                     | String  | yes      | Human-readable version name, e.g. `"26.7.17"`.                                                       |
| `versionCode`                 | Int     | yes      | Monotonically increasing integer version code.                                                       |
| `forceUpdate`                 | Boolean | no       | When `true`, **every** older client is forced to update (ignores "Ignore"). Defaults to `false`.    |
| `forceUpdateBelowVersionCode` | Int     | no       | Clients whose `versionCode` is **strictly less than** this value are forced to update. Use this to force-update only versions below a threshold (e.g. a security fix). Defaults to `Int.MAX_VALUE` (no effect) when absent. |
| `download`                    | String  | yes      | APK download URL.                                                                                    |
| `md5`                         | String  | no       | MD5 of the APK for integrity verification. Empty string skips verification.                          |
| `changeLog`                   | String  | yes      | Absolute URL to the Markdown changelog for this version.                                             |

### Force-update semantics

A client is considered force-updated when **either** condition holds:

```
forceUpdate == true
  OR
localVersionCode < forceUpdateBelowVersionCode
```

When force-update is in effect, the update dialog hides the "Later" and
"Ignore" buttons and cannot be dismissed.

### Example

Force-update every client older than `260700` to `26.7.17`:

```json
{
  "version": "26.7.17",
  "versionCode": 260717,
  "forceUpdate": false,
  "forceUpdateBelowVersionCode": 260700,
  "download": "https://github.com/wisebreeze/BreezeLauncher/releases/download/artifact/BreezeLauncher-release.apk",
  "md5": "",
  "changeLog": "https://gitee.com/wisebreeze/BreezeLauncherApp/raw/main/changeLog/26.7.17.md"
}
```

## Workflow

`.github/workflows/release-on-tag.yml` mirrors the contents of this
directory to the root of the Gitee `BreezeLauncherApp` repository when a
release is published. It can also be triggered manually from the Actions
tab with an existing release tag.

The workflow requires the `GITEE_TOKEN` repository secret to be set to a Gitee
personal access token with `projects` push scope.
