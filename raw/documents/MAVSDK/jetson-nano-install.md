---
title: "Jetson Nano Install"
type: document
doc_set: MAVSDK
doc_version: MAVSDK-Python 3.17.2
section: root
source_url: "http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/jetson-nano-install.html"
upstream_repo: "mavlink/MAVSDK-Python"
upstream_path: "jetson-nano-install.md"
ingested: 2026-07-28
tags:
  - docs/mavsdk
  - docs/mavsdk/root
---

# Jetson Nano Install

## Ubuntu 18.04

To install MAVSDK-Python on a Jetson Nano with Ubuntu 18.04 (which is old and pas end-of-life, by the way), you need to get a newer version of Python 3 and make sure pip is up-to-date.

Install Python 3.8:

```
sudo apt update
sudo apt install python3.8
```

Upgrade pip:

```
python3.8 -m pip install --upgrade pip
```

Now install mavsdk:

```
python3.8 -m pip install --upgrade mavsdk
```

## Ubuntu 20.04

The normal instructions should work with Ubuntu 20.04:

Install mavsdk:

```
python3 -m pip install --upgrade mavsdk
```
