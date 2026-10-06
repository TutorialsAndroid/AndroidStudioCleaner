# 🧹 AndroidStudioCleaner

<p align="center">
  <img src="android-icon.ico" width="180" alt="AndroidStudioCleaner Logo">
</p>

<p align="center">
  <strong>Clean Gradle Caches & Remove Legacy Android Studio Versions</strong>
</p>

<p align="center">
  A lightweight cross-platform utility (Windows, macOS, Linux) designed for Android developers to recover disk space safely and efficiently.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue">
  <img src="https://img.shields.io/badge/python-3.8%2B-green">
  <img src="https://img.shields.io/badge/license-MIT-yellow">
  <img src="https://img.shields.io/badge/status-stable-brightgreen">
  <img src="https://img.shields.io/github/v/release/TutorialsAndroid/AndroidStudioCleaner">
  <img src="https://img.shields.io/github/downloads/TutorialsAndroid/AndroidStudioCleaner/total">
</p>

---

<p align="center">
  <a href="https://github.com/TutorialsAndroid/AndroidStudioCleaner/releases/download/v1.0.0/AndroidStudioCleaner.exe">
    <strong>⬇ Download AndroidStudioCleaner v1.0.0</strong>
  </a>
</p>

---

## ✨ Overview

Android development tools generate a significant amount of cached and temporary data over time.

Common examples include:

* Gradle dependency caches
* Gradle daemon files
* Gradle wrapper distributions
* Worker caches
* Temporary build artifacts
* Legacy Android Studio configuration folders

It is not uncommon for Android developers to discover that:

```text
C:\Users\<User>\.gradle
```

has grown to:

```text
10 GB
20 GB
30 GB+
```

after months of development.

AndroidStudioCleaner helps recover valuable disk space by safely removing unnecessary files while preserving important configurations.

---

# 🚀 Features

## 📦 Gradle Cleanup

Removes:

```text
.gradle\caches
.gradle\daemon
.gradle\wrapper
.gradle\.tmp
.gradle\workers
.gradle\notifications
```

Benefits:

* Reclaim storage
* Remove stale caches
* Clear unused Gradle artifacts
* Force clean dependency regeneration

---

## 🏗 Android Studio Cleanup

Automatically scans the Android Studio configuration directories for your platform:

**Windows**

```text
%APPDATA%\Google
%LOCALAPPDATA%\Google
```

**macOS**

```text
~/Library/Application Support/Google
~/Library/Caches/Google
~/Library/Logs/Google
```

**Linux**

```text
~/.config/Google
~/.cache/Google
~/.local/share/Google
```

Detects folders such as:

```text
AndroidStudio2024.1
AndroidStudio2025.1
AndroidStudio2025.2
AndroidStudio2026.1.1
```

The utility:

✅ Preserves the latest version

✅ Removes older versions

✅ Prevents accidental deletion when only one version exists

---

## 🎯 Multiple Cleanup Modes

Choose exactly what you want to clean.

### 1️⃣ Full Cleanup

```text
Gradle Cleanup
+
Android Studio Cleanup
```

### 2️⃣ Gradle Cleanup Only

```text
caches
daemon
wrapper
.tmp
workers
notifications
```

### 3️⃣ Android Studio Cleanup Only

```text
Remove old Android Studio versions
Keep latest version
```

---

# 🔒 Safety Features

AndroidStudioCleaner was built with safety as the primary goal.

## Startup Warning

Before cleanup begins:

```text
Close:
• Android Studio
• VS Code
• IntelliJ IDEA
• Running Gradle Builds
• Project Terminals
```

This helps avoid locked files.

---

## Preview Before Deletion

Nothing is deleted immediately.

Users are shown exactly what will be removed.

Example:

```text
============================================================
CLEANUP PREVIEW
============================================================

Gradle folders to delete:

✓ C:\Users\User\.gradle\caches
✓ C:\Users\User\.gradle\wrapper

Old Android Studio versions to delete:

✗ AndroidStudio2025.1
✗ AndroidStudio2025.2

Android Studio versions to keep:

✓ AndroidStudio2026.1.1

============================================================
Continue with cleanup? (Y/N)
```

---

## User Confirmation

Cleanup only begins after explicit approval.

```text
Continue with cleanup? (Y/N)
```

---

## Smart Protection

The utility automatically:

* Skips missing folders
* Handles errors gracefully
* Preserves latest Android Studio version
* Continues cleanup when individual folders fail

---

# 📊 Cleanup Report

After completion:

```text
[DELETED] caches          8.42 GB
[DELETED] wrapper         2.31 GB
[DELETED] daemon          145.20 MB

[DELETED] AndroidStudio2025.1     850 MB
[KEPT   ] AndroidStudio2026.1.1

============================================================
CLEANUP COMPLETED
============================================================

Total Space Recovered: 11.72 GB
```

---

# 🛡 What Gets Deleted

## Gradle

```text
.gradle\caches
.gradle\daemon
.gradle\wrapper
.gradle\.tmp
.gradle\workers
.gradle\notifications
```

## Android Studio

```text
AndroidStudioXXXX.X
```

Older versions only.

Latest version is always preserved.

---

# ❌ What Does NOT Get Deleted

AndroidStudioCleaner never removes:

* Android projects
* Source code
* Git repositories
* Android SDK
* JDK
* Android Studio installation
* Latest Android Studio settings
* Documents
* Downloads

---

# 📥 Installation

## Option 1: Download Executable

Download the latest release:

```text
AndroidStudioCleaner.exe
```

No installation required.

Run directly.

---

## Option 2: Run From Source

### Clone Repository

```bash
git clone https://github.com/yourusername/AndroidStudioCleaner.git
cd AndroidStudioCleaner
```

### Run

```bash
python AndroidStudioCleaner.py
```

---

# 🏗 Build Executable

Using PyInstaller:

```bash
python -m PyInstaller ^
--onefile ^
--icon=androidstudiocleaner.ico ^
AndroidStudioCleaner.py
```

Output:

```text
dist/
└── AndroidStudioCleaner.exe
```

---

# 🖼 Recommended Icon

Use:

```text
androidstudiocleaner.ico
```

Include:

```text
16x16
32x32
48x48
64x64
128x128
256x256
```

for best Windows compatibility.

---

# ⚠ Windows Defender & SmartScreen

You may occasionally see:

```text
Windows protected your PC
```

or

```text
Unknown Publisher
```

This is expected for new unsigned executables.

AndroidStudioCleaner is:

✅ Open Source

✅ Source Available

✅ Buildable From Source

✅ No Network Access

✅ No Data Collection

---

# 🔍 How It Works

1. Scans Gradle folders.
2. Scans Android Studio versions.
3. Displays cleanup preview.
4. Waits for user confirmation.
5. Deletes selected targets.
6. Calculates recovered space.
7. Generates cleanup report.

---

# 🛣 Roadmap

Future improvements:

* Automatic detection of running Android Studio
* Automatic detection of VS Code
* Analyze-only mode
* Export cleanup report
* GUI version
* Progress bar
* Disk usage statistics
* Dark mode desktop application

---

# 🤝 Contributing

Contributions are welcome.

Ideas, bug reports, and pull requests are appreciated.

---

# 📄 License

MIT License

---

# ⭐ Support

If AndroidStudioCleaner helped you recover storage space, please consider starring the repository.

It helps other Android developers discover the project.

---

<p align="center">
Made with ❤️ for Android Developers
</p>
