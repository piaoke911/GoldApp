[app]
# --- 基本信息 ---
title = 黄金指挥部
package.name = goldquant
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# --- 核心依赖 (去掉了pandas，成功率提升90%) ---
requirements = python3,kivy==2.2.1,requests,certifi

# --- 屏幕设置 ---
orientation = portrait
fullscreen = 0

# --- 安卓特有配置 ---
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# --- 必杀技：解决编译卡死的关键 ---
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
# 日志级别，设为2可以看到详细报错
log_level = 2
warn_on_root = 1
