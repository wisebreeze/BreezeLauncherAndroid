# BreezeLauncher

[![Build](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml/badge.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20arm64--v8a-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Min SDK](https://img.shields.io/badge/minSDK-26-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)
[![Target SDK](https://img.shields.io/badge/targetSDK-37-green.svg)](https://github.com/wisebreeze/BreezeLauncherAndroid)

**English** | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

---

BreezeLauncher is a modern, high-performance launcher for Minecraft on Android. It provides a smooth, native experience for managing game versions, mods, accounts, and worlds — built with a Jetpack Compose UI and a C++ native core for critical operations.

This repository hosts the **continuous integration** pipeline that builds and releases signed APK artifacts. Source code is developed in a separate private repository and is never stored here.

## Features

- **Multi-version management** — install, isolate, and switch between multiple Minecraft versions side by side
- **Native mod loading** — load C++ mods at runtime via a preloader subsystem, with an in-app mod menu for toggling and configuration
- **Built-in mods** — FPS overlay, zoom, snaplook, and more, shipped out of the box
- **Account management** — Microsoft / Xbox Live login with token persistence and automatic refresh
- **World & resource management** — create, edit, import, and export worlds and resource packs
- **Compatibility framework** — optional standalone preloader app for running LeviLaunchroid-compatible native mods
- **Multi-package builds** — parallel CI produces three signed variants (default, preloader-compatible, and benchmark-disguised) from a single source tree

## Downloads

Pre-built release APKs are published on the [Releases](https://github.com/wisebreeze/BreezeLauncherAndroid/releases) page. Three variants are available:

| Variant | Package name | Use case |
|---------|--------------|----------|
| `default` | `com.wisebreeze.launcher` | Standard build |
| `preloader` | `org.levimc.launcher` | LeviLaunchroid-compatible build |
| `antutu` | `com.antutu.ABenchMark` | Benchmark-disguised build |

## License

Copyright © 2026 wisebreeze. All rights reserved.

Unauthorized copying, modification, distribution, or reverse engineering of this software, in whole or in part, is strictly prohibited without prior written permission from the copyright holder.
