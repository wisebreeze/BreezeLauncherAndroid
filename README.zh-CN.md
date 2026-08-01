# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

[English](README.md) | **简体中文** | [繁體中文](README.zh-TW.md)

---

BreezeLauncher 是一款面向 Android 平台 Minecraft 的现代化高性能启动器。它提供流畅的原生体验，用于管理游戏版本、模组、账户和存档——基于 Jetpack Compose UI 与 C++ 原生核心构建，关键逻辑运行在 native 层。

本仓库托管**持续集成**流水线，负责构建并发布已签名的 APK 产物。源代码在独立的私有仓库中开发，从不存放于此。

## 功能特色

- **多版本管理** — 并行安装、隔离与切换多个 Minecraft 版本
- **原生模组加载** — 通过预加载器子系统在运行时加载 C++ 模组，内置模组菜单用于开关与配置
- **内置模组** — 开箱即用的 FPS 显示、缩放、视角锁定等
- **账户管理** — 微软 / Xbox Live 登录，令牌持久化与自动刷新
- **存档与资源管理** — 创建、编辑、导入、导出存档与资源包
- **兼容框架** — 可选的独立预加载器 App，用于运行 LeviLaunchroid 兼容的原生模组
- **多包名构建** — CI 并行产出三个已签名变体（默认、兼容预加载器、伪装跑分类），源自同一份代码树

## 下载

预构建的发布版 APK 发布在 [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) 页面，提供三个变体：

| 变体 | 包名 | 用途 |
|------|------|------|
| `default` | `com.wisebreeze.launcher` | 标准构建 |
| `preloader` | `org.levimc.launcher` | LeviLaunchroid 兼容构建 |
| `antutu` | `com.antutu.ABenchMark` | 伪装跑分类构建 |

## 许可证

版权所有 © 2026 wisebreeze。保留所有权利。

未经版权所有者事先书面许可，严禁对本软件（整体或部分）进行复制、修改、分发或逆向工程。
