# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

[English](README.md) | **简体中文** | [繁體中文](README.zh-TW.md)

---

BreezeLauncher 是一款面向 Android 平台 Minecraft 的现代化高性能启动器。它提供流畅的原生体验，用于管理游戏版本、模组、账户和存档。

> [!IMPORTANT]
> **免责声明**
>
> BreezeLauncher **与 Mojang Studios、Microsoft 或任何其他第三方均无关联、未获认可、也未受其赞助**。本作品**非官方 Minecraft 产品**，也**非任何第三方项目的官方仓库**。Minecraft 是 Mojang Studios 的商标。所有产品名称、徽标和品牌均归其各自所有者所有。

## 使用前提

- 需在同一设备上从 **Google Play** 购买并下载的**正版 Minecraft**。BreezeLauncher **仅**支持启动 Google Play 版本的 Minecraft，不支持其他来源的版本。

## 功能特色

- **多版本管理** — 并行安装、隔离与切换多个 Minecraft 版本
- **模组加载** — 运行时加载模组，内置模组菜单用于开关与配置
- **内置模组** — 开箱即用的 FPS 显示、缩放、视角锁定、陀螺仪瞄准、虚拟光标、自动冲刺、快速丢弃、CPS 计数器等
- **游戏内悬浮面板** — 游戏运行时叠加悬浮面板，无需退出游戏即可管理模组、听音乐、聊天、浏览网页、查看控制台与快速设置
- **账户管理** — 微软 / Xbox Live 登录，令牌自动刷新
- **存档与资源管理** — 创建、编辑、导入、导出存档、资源包与结构
- **世界编辑器** — 编辑玩家数据、结构与 NBT 数据，全库搜索 NBT 记录，管理多人与无敌设置，生成超平坦世界
- **音乐播放器** — 搜索并播放音乐，支持歌单、歌词与后台播放
- **内置浏览器** — 在启动器内浏览网页，无需离开游戏
- **社区** — 分享与发现用户创作的模组、资源包与其他资源
- **模组商店** — 直接从 CurseForge 浏览并安装模组
- **服务器列表** — 保存并探测基岩版服务器，一键加入
- **聊天** — 世界频道与私聊，附带在线用户列表
- **AI 助手** — 应用内 AI 助手，回答问题与执行任务
- **截图** — 截取并管理游戏内截图
- **更新日志** — 查看最新的 Minecraft 更新日志
- **静默更新** — 通过 Shizuku 在后台安装应用更新，无需弹窗确认
- **多语言** — 15 种语言完整本地化

## 下载

预构建的发布版 APK 发布在 [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) 页面。

## 开源代码致谢

BreezeLauncher 基于以下开源项目构建：

**AndroidX / Jetpack**
- [AndroidX](https://developer.android.com/jetpack/androidx) — Android 核心库
- [Jetpack Compose](https://developer.android.com/jetpack/compose) — UI 工具包
- [AndroidX Media3](https://developer.android.com/media/media3) — 媒体播放
- [AndroidX Games Activity](https://developer.android.com/games/agk/activity) — 游戏 Activity 封装

**Kotlin / 构建**
- [Kotlin](https://kotlinlang.org/) — 编程语言
- [Android Gradle Plugin](https://developer.android.com/build) — 构建系统
- [Google Services Gradle Plugin](https://developers.google.com/android/guides/google-services-plugin) — Firebase 配置

**网络 / HTTP**
- [OkHttp](https://square.github.io/okhttp/) — HTTP 客户端
- [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) — 旧版 HTTP 客户端
- [Java-WebSocket](https://github.com/TooTallNate/Java-WebSocket) — WebSocket 客户端
- [CloudburstMC Bedrock protocol](https://github.com/CloudburstMC/Network) — 基岩版协议库

**密码学**
- [Bouncy Castle](https://www.bouncycastle.org/) — 加密提供者
- [Conscrypt](https://github.com/google/conscrypt) — TLS 提供者
- [Spongy Castle](https://github.com/rtyley/spongycastle) — Bouncy Castle 的 Android 版

**Firebase / Google 服务**
- [Firebase](https://firebase.google.com/) — 分析、崩溃报告、消息推送
- [Google Play Services Games v2](https://developers.google.com/games/services/v2/android) — 游戏服务
- [Google Play Billing](https://developer.android.com/google/play/billing) — 应用内购买
- [Material Components for Android](https://github.com/material-components/material-components-android)

**UI / 媒体 / 工具**
- [Coil](https://coil-kt.github.io/coil/) — 图片加载
- [EasyCrop](https://github.com/mr0xf00/easycrop) — 图片裁剪
- [Reorderable](https://github.com/Calvin-LL/Reorderable) — 拖拽排序
- [ZXing](https://github.com/zxing/zxing) — 二维码生成
- [Gson](https://github.com/google/gson) — JSON 序列化
- [Simple XML](https://simple.sourceforge.net/) — XML 序列化
- [Guava](https://github.com/google/guava) — 核心工具库
- [JetBrains Annotations](https://github.com/JetBrains/java-annotations)

**系统 / Shell**
- [Shizuku](https://github.com/RikkaApps/Shizuku) — 特权 Shell 服务
- [xCrash](https://github.com/RadiantByte/xCrash) — 崩溃捕获
- [SLF4J](https://www.slf4j.org/) — 日志

**子模块**
- [LeviLaunchroid](https://github.com/LiteLDev/LeviLaunchroid) — 上游启动器与预加载器子系统
- [preloader-android](https://github.com/wisebreeze/preloader-android) — 模组加载子系统
- [libHttpClient](https://github.com/microsoft/libHttpClient) — 微软 HTTP 客户端
- [BreezeAPI](https://github.com/wisebreeze/BreezeAPI) — 后端 API 绑定
- [nlohmann/json](https://github.com/nlohmann/json) — JSON 库
- [Google Play Games C SDK](https://developers.google.com/games/services/v2/native) — 游戏服务

## 许可证

版权所有 © 2026 wisebreeze。保留所有权利。

未经版权所有者事先书面许可，严禁对本软件（整体或部分）进行复制、修改、分发或逆向工程。
