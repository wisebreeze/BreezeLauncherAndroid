# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

[English](README.md) | [简体中文](README.zh-CN.md) | **繁體中文**

---

BreezeLauncher 是一款面向 Android 平台 Minecraft 的現代化高效能啟動器。它提供流暢的原生體驗，用於管理遊戲版本、模組、帳戶和存檔。

> [!IMPORTANT]
> **免責聲明**
>
> BreezeLauncher **與 Mojang Studios、Microsoft 或任何其他第三方均無關聯、未獲認可、也未受其贊助**。本作品**非官方 Minecraft 產品**，也**非任何第三方專案的官方倉庫**。Minecraft 是 Mojang Studios 的商標。所有產品名稱、徽標和品牌均歸其各自所有者所有。

## 使用前提

- 需在同一裝置上從 **Google Play** 購買並下載的**正版 Minecraft**。BreezeLauncher **僅**支援啟動 Google Play 版本的 Minecraft，不支援其他來源的版本。

## 功能特色

- **多版本管理** — 並行安裝、隔離與切換多個 Minecraft 版本
- **模組載入** — 執行時載入模組，內建模組選單用於開關與設定
- **內建模組** — 開箱即用的 FPS 顯示、縮放、視角鎖定、陀螺儀瞄準、虛擬游標、自動衝刺、快速丟棄、CPS 計數器等
- **遊戲內懸浮面板** — 遊戲執行時疊加懸浮面板，無需退出遊戲即可管理模組、聽音樂、聊天、瀏覽網頁、檢視控制台與快速設定
- **帳戶管理** — 微軟 / Xbox Live 登入，權杖自動重新整理
- **存檔與資源管理** — 建立、編輯、匯入、匯出存檔、資源包與結構
- **世界編輯器** — 編輯玩家資料、結構與 NBT 資料，全庫搜尋 NBT 記錄，管理多人與無敵設定，生成超平坦世界
- **音樂播放器** — 搜尋並播放音樂，支援歌單、歌詞與背景播放
- **內建瀏覽器** — 在啟動器內瀏覽網頁，無需離開遊戲
- **社群** — 分享與發現使用者創作的模組、資源包與其他資源
- **模組商店** — 直接從 CurseForge 瀏覽並安裝模組
- **伺服器列表** — 儲存並探測基岩版伺服器，一鍵加入
- **聊天** — 世界頻道與私聊，附帶線上使用者列表
- **AI 助手** — 應用內 AI 助手，回答問題與執行任務
- **截圖** — 擷取並管理遊戲內截圖
- **更新日誌** — 檢視最新的 Minecraft 更新日誌
- **靜默更新** — 透過 Shizuku 在背景安裝應用更新，無需彈窗確認
- **多語言** — 15 種語言完整本地化

## 下載

預構建的發布版 APK 發布在 [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) 頁面。

## 開源程式碼致謝

BreezeLauncher 基於以下開源專案構建：

**AndroidX / Jetpack**
- [AndroidX](https://developer.android.com/jetpack/androidx) — Android 核心庫
- [Jetpack Compose](https://developer.android.com/jetpack/compose) — UI 工具包
- [AndroidX Media3](https://developer.android.com/media/media3) — 媒體播放
- [AndroidX Games Activity](https://developer.android.com/games/agk/activity) — 遊戲 Activity 封裝

**Kotlin / 構建**
- [Kotlin](https://kotlinlang.org/) — 程式語言
- [Android Gradle Plugin](https://developer.android.com/build) — 構建系統
- [Google Services Gradle Plugin](https://developers.google.com/android/guides/google-services-plugin) — Firebase 設定

**網路 / HTTP**
- [OkHttp](https://square.github.io/okhttp/) — HTTP 用戶端
- [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) — 舊版 HTTP 用戶端
- [Java-WebSocket](https://github.com/TooTallNate/Java-WebSocket) — WebSocket 用戶端
- [CloudburstMC Bedrock protocol](https://github.com/CloudburstMC/Network) — 基岩版協定庫

**密碼學**
- [Bouncy Castle](https://www.bouncycastle.org/) — 加密提供者
- [Conscrypt](https://github.com/google/conscrypt) — TLS 提供者
- [Spongy Castle](https://github.com/rtyley/spongycastle) — Bouncy Castle 的 Android 版

**Firebase / Google 服務**
- [Firebase](https://firebase.google.com/) — 分析、崩潰報告、訊息推送
- [Google Play Services Games v2](https://developers.google.com/games/services/v2/android) — 遊戲服務
- [Google Play Billing](https://developer.android.com/google/play/billing) — 應用程式內購買
- [Material Components for Android](https://github.com/material-components/material-components-android)

**UI / 媒體 / 工具**
- [Coil](https://coil-kt.github.io/coil/) — 圖片載入
- [EasyCrop](https://github.com/mr0xf00/easycrop) — 圖片裁剪
- [Reorderable](https://github.com/Calvin-LL/Reorderable) — 拖曳排序
- [ZXing](https://github.com/zxing/zxing) — 二維碼生成
- [Gson](https://github.com/google/gson) — JSON 序列化
- [Simple XML](https://simple.sourceforge.net/) — XML 序列化
- [Guava](https://github.com/google/guava) — 核心工具庫
- [JetBrains Annotations](https://github.com/JetBrains/java-annotations)

**系統 / Shell**
- [Shizuku](https://github.com/RikkaApps/Shizuku) — 特權 Shell 服務
- [xCrash](https://github.com/RadiantByte/xCrash) — 崩潰捕獲
- [SLF4J](https://www.slf4j.org/) — 日誌

**子模組**
- [LeviLaunchroid](https://github.com/LiteLDev/LeviLaunchroid) — 上游啟動器與預載入器子系統
- [preloader-android](https://github.com/wisebreeze/preloader-android) — 模組載入子系統
- [libHttpClient](https://github.com/microsoft/libHttpClient) — 微軟 HTTP 用戶端
- [BreezeAPI](https://github.com/wisebreeze/BreezeAPI) — 後端 API 綁定
- [nlohmann/json](https://github.com/nlohmann/json) — JSON 庫
- [Google Play Games C SDK](https://developers.google.com/games/services/v2/native) — 遊戲服務

## 授權條款

版權所有 © 2026 wisebreeze。保留所有權利。

未經版權所有者事先書面許可，嚴禁對本軟體（整體或部分）進行複製、修改、分發或逆向工程。
