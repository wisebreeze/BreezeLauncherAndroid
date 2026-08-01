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

## 授權條款

版權所有 © 2026 wisebreeze。保留所有權利。

未經版權所有者事先書面許可，嚴禁對本軟體（整體或部分）進行複製、修改、分發或逆向工程。
