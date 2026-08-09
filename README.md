# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

**English** | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

---

BreezeLauncher is a modern, high-performance launcher for Minecraft on Android. It provides a smooth, native experience for managing game versions, mods, accounts, and worlds — built with a Jetpack Compose UI and a C++ native core for critical operations.

> [!IMPORTANT]
> **Disclaimer**
>
> BreezeLauncher is **not affiliated with, endorsed by, or sponsored by** Mojang Studios, Microsoft, or any other third party. This is **not an official Minecraft product** and is **not an official repository** of any third-party project. Minecraft is a trademark of Mojang Studios. All product names, logos, and brands are property of their respective owners.

## Features

- **Multi-version management** — install, isolate, and switch between multiple Minecraft versions side by side
- **Native mod loading** — load C++ mods at runtime via a preloader subsystem, with an in-app mod menu for toggling and configuration
- **Built-in mods** — FPS overlay, zoom, snaplook, and more, shipped out of the box
- **Account management** — Microsoft / Xbox Live login with token persistence and automatic refresh
- **World & resource management** — create, edit, import, and export worlds and resource packs
- **Compatibility framework** — optional standalone preloader app for running LeviLaunchroid-compatible native mods
- **Multi-package builds** — parallel CI produces three signed variants (default, preloader-compatible, and benchmark-disguised) from a single source tree

## Downloads

Pre-built release APKs are published on the [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) page. The `default` variant is currently built; the `preloader` and `antutu` variants are temporarily disabled.

| Variant | Package name | Use case |
|---------|--------------|----------|
| `default` | `com.wisebreeze.launcher` | Standard build |
| ~~`preloader`~~ | ~~`org.levimc.launcher`~~ | ~~LeviLaunchroid-compatible build~~ — temporarily disabled |
| ~~`antutu`~~ | ~~`com.antutu.ABenchMark`~~ | ~~Benchmark-disguised build~~ — disabled |

## Open Source Acknowledgements

BreezeLauncher is built on the following open-source projects:

**AndroidX / Jetpack**
- [AndroidX](https://developer.android.com/jetpack/androidx) — AppCompat, Activity, Fragment, Annotation, Browser, ConstraintLayout, Core Splashscreen, Dynamic Animation, Preference, Lifecycle, Room, SQLite, Work Manager
- [Jetpack Compose](https://developer.android.com/jetpack/compose) — UI toolkit (Compose UI, Material3, Material Icons)
- [AndroidX Media3](https://developer.android.com/media/media3) — media playback (ExoPlayer, UI)
- [AndroidX Games Activity](https://developer.android.com/games/agk/activity) — native activity wrapper

**Kotlin / Build**
- [Kotlin](https://kotlinlang.org/) — programming language & Compose compiler plugin
- [Android Gradle Plugin](https://developer.android.com/build) — build system
- [Google Services Gradle Plugin](https://developers.google.com/android/guides/google-services-plugin) — Firebase config

**Networking / HTTP**
- [OkHttp](https://square.github.io/okhttp/) — HTTP client
- [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) — legacy HTTP client
- [Java-WebSocket](https://github.com/TooTallNate/Java-WebSocket) — WebSocket client
- [CloudburstMC Bedrock protocol](https://github.com/CloudburstMC/Network) — Bedrock Edition protocol library

**Cryptography**
- [Bouncy Castle](https://www.bouncycastle.org/) — Java cryptography provider (bcprov-jdk15on)
- [Conscrypt](https://github.com/google/conscrypt) — TLS provider for Android
- [Spongy Castle](https://github.com/rtyley/spongycastle) — Bouncy Castle repackaged for Android (core, prov, pkix)

**Firebase / Google Services**
- [Firebase](https://firebase.google.com/) — Analytics, Crashlytics (incl. NDK), Cloud Messaging, Instance ID
- [Google Play Services Games v2](https://developers.google.com/games/services/v2/android) — games services
- [Google Play Billing](https://developer.android.com/google/play/billing) — in-app purchases
- [Material Components for Android](https://github.com/material-components/material-components-android)

**UI / Media / Utilities**
- [Coil](https://coil-kt.github.io/coil/) — image loading (coil-compose, coil-network-okhttp)
- [EasyCrop](https://github.com/mr0xf00/easycrop) — image cropping
- [Reorderable](https://github.com/Calvin-LL/Reorderable) — drag-to-reorder for Compose
- [ZXing](https://github.com/zxing/zxing) — QR code generation
- [Gson](https://github.com/google/gson) — JSON serialization
- [Simple XML](https://simple.sourceforge.net/) — XML serialization
- [Guava](https://github.com/google/guava) — core utilities
- [JetBrains Annotations](https://github.com/JetBrains/java-annotations)

**System / Shell**
- [Shizuku](https://github.com/RikkaApps/Shizuku) — privileged shell service (API + provider)
- [xCrash](https://github.com/RadiantByte/xCrash) — native crash capture
- [SLF4J](https://www.slf4j.org/) — logging facade

**Web / Embedded Engine**
- [Mozilla GeckoView](https://mozilla.github.io/geckoview/) — embedded web engine (arm64-v8a)

**Native (C++) Submodules**
- [LeviLaunchroid](https://github.com/LiteLDev/LeviLaunchroid) — upstream launcher & preloader subsystem (Apache-2.0), by LeviMC Team
- [preloader-android](https://github.com/wisebreeze/preloader-android) — native mod loading subsystem (forked from LeviLaunchroid)
- [libHttpClient](https://github.com/microsoft/libHttpClient) — Microsoft HTTP client (C++)
- [BreezeAPI](https://github.com/wisebreeze/BreezeAPI) — backend API bindings (C++)
- [nlohmann/json](https://github.com/nlohmann/json) — JSON for Modern C++
- [Google Play Games C SDK](https://developers.google.com/games/services/v2/native) — via libHttpClient

## License

Copyright © 2026 wisebreeze. All rights reserved.

Unauthorized copying, modification, distribution, or reverse engineering of this software, in whole or in part, is strictly prohibited without prior written permission from the copyright holder.
