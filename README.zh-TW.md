# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

[English](README.md) | [简体中文](README.zh-CN.md) | **繁體中文**

---

BreezeLauncher 是一款面向 Android 平台 Minecraft 的現代化高效能啟動器。它提供流暢的原生體驗，用於管理遊戲版本、模組、帳戶和存檔——基於 Jetpack Compose UI 與 C++ 原生核心構建，關鍵邏輯運行在 native 層。

本倉庫託管**持續整合**流水線，負責構建並發布已簽署的 APK 產物。原始碼在獨立的私有倉庫中開發，從不存放於此。

## 功能特色

- **多版本管理** — 並行安裝、隔離與切換多個 Minecraft 版本
- **原生模組載入** — 透過預載入器子系統在執行時載入 C++ 模組，內建模組選單用於開關與設定
- **內建模組** — 開箱即用的 FPS 顯示、縮放、視角鎖定等
- **帳戶管理** — 微軟 / Xbox Live 登入，權杖持久化與自動重新整理
- **存檔與資源管理** — 建立、編輯、匯入、匯出存檔與資源包
- **相容框架** — 可選的獨立預載入器 App，用於執行 LeviLaunchroid 相容的原生模組
- **多套件名構建** — CI 並行產出三個已簽署變體（預設、相容預載入器、偽裝跑分類），源自同一份程式碼樹

## 下載

預構建的發布版 APK 發布在 [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) 頁面，提供三個變體：

| 變體 | 套件名 | 用途 |
|------|--------|------|
| `default` | `com.wisebreeze.launcher` | 標準構建 |
| `preloader` | `org.levimc.launcher` | LeviLaunchroid 相容構建 |
| `antutu` | `com.antutu.ABenchMark` | 偽裝跑分類構建 |

## 開源程式碼致謝

BreezeLauncher 基於以下開源專案構建：

**AndroidX / Jetpack**
- [AndroidX](https://developer.android.com/jetpack/androidx) — AppCompat、Activity、Fragment、Annotation、Browser、ConstraintLayout、Core Splashscreen、Dynamic Animation、Preference、Lifecycle、Room、SQLite、Work Manager
- [Jetpack Compose](https://developer.android.com/jetpack/compose) — UI 工具包（Compose UI、Material3、Material Icons）
- [AndroidX Media3](https://developer.android.com/media/media3) — 媒體播放（ExoPlayer、UI）
- [AndroidX Games Activity](https://developer.android.com/games/agk/activity) — 原生 Activity 封裝

**Kotlin / 構建**
- [Kotlin](https://kotlinlang.org/) — 程式語言與 Compose 編譯器外掛
- [Android Gradle Plugin](https://developer.android.com/build) — 構建系統
- [Google Services Gradle Plugin](https://developers.google.com/android/guides/google-services-plugin) — Firebase 設定

**網路 / HTTP**
- [OkHttp](https://square.github.io/okhttp/) — HTTP 用戶端
- [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) — 舊版 HTTP 用戶端
- [Java-WebSocket](https://github.com/TooTallNate/Java-WebSocket) — WebSocket 用戶端
- [CloudburstMC Bedrock protocol](https://github.com/CloudburstMC/Network) — 基岩版協定庫

**密碼學**
- [Bouncy Castle](https://www.bouncycastle.org/) — Java 加密提供者（bcprov-jdk15on）
- [Conscrypt](https://github.com/google/conscrypt) — Android TLS 提供者
- [Spongy Castle](https://github.com/rtyley/spongycastle) — Bouncy Castle 的 Android 重新打包版（core、prov、pkix）

**Firebase / Google 服務**
- [Firebase](https://firebase.google.com/) — Analytics、Crashlytics（含 NDK）、Cloud Messaging、Instance ID
- [Google Play Services Games v2](https://developers.google.com/games/services/v2/android) — 遊戲服務
- [Google Play Billing](https://developer.android.com/google/play/billing) — 應用程式內購買
- [Material Components for Android](https://github.com/material-components/material-components-android)

**UI / 媒體 / 工具**
- [Coil](https://coil-kt.github.io/coil/) — 圖片載入（coil-compose、coil-network-okhttp）
- [EasyCrop](https://github.com/mr0xf00/easycrop) — 圖片裁剪
- [Reorderable](https://github.com/Calvin-LL/Reorderable) — Compose 拖曳排序
- [ZXing](https://github.com/zxing/zxing) — 二維碼生成
- [Gson](https://github.com/google/gson) — JSON 序列化
- [Simple XML](https://simple.sourceforge.net/) — XML 序列化
- [Guava](https://github.com/google/guava) — 核心工具庫
- [JetBrains Annotations](https://github.com/JetBrains/java-annotations)

**系統 / Shell**
- [Shizuku](https://github.com/RikkaApps/Shizuku) — 特權 Shell 服務（API + provider）
- [xCrash](https://github.com/RadiantByte/xCrash) — 原生崩潰捕獲
- [SLF4J](https://www.slf4j.org/) — 日誌門面

**Web / 嵌入式引擎**
- [Mozilla GeckoView](https://mozilla.github.io/geckoview/) — 嵌入式 Web 引擎（arm64-v8a）

**原生（C++）子模組**
- [preloader-android](https://github.com/wisebreeze/preloader-android) — 原生模組載入子系統
- [libHttpClient](https://github.com/microsoft/libHttpClient) — 微軟 HTTP 用戶端（C++）
- [BreezeAPI](https://github.com/wisebreeze/BreezeAPI) — 後端 API 綁定（C++）
- [nlohmann/json](https://github.com/nlohmann/json) — 現代 C++ JSON 庫
- [Google Play Games C SDK](https://developers.google.com/games/services/v2/native) — 經由 libHttpClient

## 授權條款

版權所有 © 2026 wisebreeze。保留所有權利。

未經版權所有者事先書面許可，嚴禁對本軟體（整體或部分）進行複製、修改、分發或逆向工程。
