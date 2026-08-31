# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

[English](README.md) | **简体中文** | [繁體中文](README.zh-TW.md)

---

BreezeLauncher 是一款面向 Android 平台 Minecraft 的现代化高性能启动器。它提供流畅的原生体验，用于管理游戏版本、模组、账户和存档——基于 Jetpack Compose UI 与 C++ 原生核心构建，关键逻辑运行在 native 层。

> [!IMPORTANT]
> **免责声明**
>
> BreezeLauncher **与 Mojang Studios、Microsoft 或任何其他第三方均无关联、未获认可、也未受其赞助**。本作品**非官方 Minecraft 产品**，也**非任何第三方项目的官方仓库**。Minecraft 是 Mojang Studios 的商标。所有产品名称、徽标和品牌均归其各自所有者所有。

## 使用前提

- 需在同一设备上从 **Google Play** 购买并下载的**正版 Minecraft**。BreezeLauncher **仅**支持启动 Google Play 版本的 Minecraft，不支持其他来源的版本。

## 功能特色

- **多版本管理** — 并行安装、隔离与切换多个 Minecraft 版本
- **原生模组加载** — 通过预加载器子系统在运行时加载 C++ 模组，内置模组菜单用于开关与配置
- **内置模组** — 开箱即用的 FPS 显示、缩放、视角锁定等
- **账户管理** — 微软 / Xbox Live 登录，令牌持久化与自动刷新
- **存档与资源管理** — 创建、编辑、导入、导出存档与资源包
- **兼容框架** — 可选的独立预加载器 App，用于运行 LeviLaunchroid 兼容的原生模组
- **多包名构建** — CI 并行产出三个已签名变体（默认、兼容预加载器、伪装跑分类），源自同一份代码树

## 下载

预构建的发布版 APK 发布在 [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) 页面。

## 开源代码致谢

BreezeLauncher 基于以下开源项目构建：

**AndroidX / Jetpack**
- [AndroidX](https://developer.android.com/jetpack/androidx) — AppCompat、Activity、Fragment、Annotation、Browser、ConstraintLayout、Core Splashscreen、Dynamic Animation、Preference、Lifecycle、Room、SQLite、Work Manager
- [Jetpack Compose](https://developer.android.com/jetpack/compose) — UI 工具包（Compose UI、Material3、Material Icons）
- [AndroidX Media3](https://developer.android.com/media/media3) — 媒体播放（ExoPlayer、UI）
- [AndroidX Games Activity](https://developer.android.com/games/agk/activity) — 原生 Activity 封装

**Kotlin / 构建**
- [Kotlin](https://kotlinlang.org/) — 编程语言与 Compose 编译器插件
- [Android Gradle Plugin](https://developer.android.com/build) — 构建系统
- [Google Services Gradle Plugin](https://developers.google.com/android/guides/google-services-plugin) — Firebase 配置

**网络 / HTTP**
- [OkHttp](https://square.github.io/okhttp/) — HTTP 客户端
- [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) — 旧版 HTTP 客户端
- [Java-WebSocket](https://github.com/TooTallNate/Java-WebSocket) — WebSocket 客户端
- [CloudburstMC Bedrock protocol](https://github.com/CloudburstMC/Network) — 基岩版协议库

**密码学**
- [Bouncy Castle](https://www.bouncycastle.org/) — Java 加密提供者（bcprov-jdk15on）
- [Conscrypt](https://github.com/google/conscrypt) — Android TLS 提供者
- [Spongy Castle](https://github.com/rtyley/spongycastle) — Bouncy Castle 的 Android 重打包版（core、prov、pkix）

**Firebase / Google 服务**
- [Firebase](https://firebase.google.com/) — Analytics、Crashlytics（含 NDK）、Cloud Messaging、Instance ID
- [Google Play Services Games v2](https://developers.google.com/games/services/v2/android) — 游戏服务
- [Google Play Billing](https://developer.android.com/google/play/billing) — 应用内购买
- [Material Components for Android](https://github.com/material-components/material-components-android)

**UI / 媒体 / 工具**
- [Coil](https://coil-kt.github.io/coil/) — 图片加载（coil-compose、coil-network-okhttp）
- [EasyCrop](https://github.com/mr0xf00/easycrop) — 图片裁剪
- [Reorderable](https://github.com/Calvin-LL/Reorderable) — Compose 拖拽排序
- [ZXing](https://github.com/zxing/zxing) — 二维码生成
- [Gson](https://github.com/google/gson) — JSON 序列化
- [Simple XML](https://simple.sourceforge.net/) — XML 序列化
- [Guava](https://github.com/google/guava) — 核心工具库
- [JetBrains Annotations](https://github.com/JetBrains/java-annotations)

**系统 / Shell**
- [Shizuku](https://github.com/RikkaApps/Shizuku) — 特权 Shell 服务（API + provider）
- [xCrash](https://github.com/RadiantByte/xCrash) — 原生崩溃捕获
- [SLF4J](https://www.slf4j.org/) — 日志门面

**Web / 嵌入式引擎**
- [Mozilla GeckoView](https://mozilla.github.io/geckoview/) — 嵌入式 Web 引擎（arm64-v8a）

**原生（C++）子模块**
- [LeviLaunchroid](https://github.com/LiteLDev/LeviLaunchroid) — 上游启动器与预加载器子系统（Apache-2.0），作者 LeviMC Team
- [preloader-android](https://github.com/wisebreeze/preloader-android) — 原生模组加载子系统（fork 自 LeviLaunchroid）
- [libHttpClient](https://github.com/microsoft/libHttpClient) — 微软 HTTP 客户端（C++）
- [BreezeAPI](https://github.com/wisebreeze/BreezeAPI) — 后端 API 绑定（C++）
- [nlohmann/json](https://github.com/nlohmann/json) — 现代 C++ JSON 库
- [Google Play Games C SDK](https://developers.google.com/games/services/v2/native) — 经由 libHttpClient

**原生（Rust）**
- [XOR-MC-Archive-Decrypt](https://github.com/HTMonkeyG/XOR-MC-Archive-Decrypt) — 网易 MC 基岩版存档 XOR 加密/解密（MIT），作者 HTMonkeyG — 移植为 Rust `libmcarchive.so`

## 许可证

版权所有 © 2026 wisebreeze。保留所有权利。

未经版权所有者事先书面许可，严禁对本软件（整体或部分）进行复制、修改、分发或逆向工程。
