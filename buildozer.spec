[app]
title = 黄金指挥部
package.name = goldquant
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# 兄弟，第一次打包，咱们先用这三个基础包，100% 成功后再加 pandas！
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 针对现代手机的最稳配置
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# --- 核心黑科技：解决 10 分钟卡死的开关 ---
android.accept_sdk_license = True
p4a.branch = master
# ---------------------------------------

[buildozer]
log_level = 2
warn_on_root = 1
