---
title: "Daily Builds"
type: document
doc_set: QGC
doc_version: Stable_V5.0
section: releases
source_url: "https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/releases/daily_builds.html"
upstream_repo: "mavlink/qgroundcontrol"
upstream_path: "releases/daily_builds.md"
upstream_commit: "cb6ee485e0e11c74ed667ca573e7593f770da436"
ingested: 2026-07-28
tags:
  - docs/qgc
  - docs/qgc/releases
---

# Daily Builds

Daily Builds of _QGroundControl_ have the absolute latest set of [new features](../releases/daily_build_new_features.md).

::: warning
Daily Builds are less tested than stable builds.
Use at your own risk.
:::

These can be downloaded from the links below (install as described in [Download and Install](../getting_started/download_and_install.md)):

- Windows
	- [x86_64](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl-installer-AMD64.exe)
	- [Arm_64](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl-installer-ARM64.exe)
- [OS X](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl.dmg)
- Linux - (See installation instructions below)
  - [Linux x86_64](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl-x86_64.AppImage)
  - [Linux aarch64](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl-aarch64.AppImage)
- [Android](https://d176tv9ibo4jno.cloudfront.net/builds/master/QGroundControl.apk)
- iOS is currently unavailable

## Linux Installation Instructions

1. Make the AppImage executable
```
chmod +x QGroundControl-<arch>.AppImage
```

2. Enable serial-port access
Add your user to the dialout group so you can talk to USB devices without root:

```
sudo usermod -aG dialout "$(id -un)"
```

::: info
At login, your shell takes a snapshot of your user and group memberships. Because you just changed groups, you need a fresh login shell to pick up “dialout” access. Logging out and back in reloads that snapshot, so you get the new permissions.
:::


3. (Optional) Disable ModemManager
On some Ubuntu-based systems, ModemManager can claim serial ports that QGC needs. If you don't use it elsewhere, mask or remove it.
```
# preferred: stop and mask the service
sudo systemctl mask --now ModemManager.service

# or, if you’d rather remove the package
sudo apt remove --purge modemmanager
```

4. Run QGroundControl
Either double-click the AppImage in your file manager or launch it from a terminal:

```
./QGroundControl-<arch>.AppImage
```
