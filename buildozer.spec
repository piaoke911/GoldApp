[app]
title = 黄金指挥部
package.name = goldquant
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# 第一次打包，需求库务必保持最简！跑通后再加 pandas
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# --- 必杀技：这一行必须生效 ---
p4a.branch = master
# ----------------------------

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
