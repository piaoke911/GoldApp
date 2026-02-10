[app]
title = 黄金指挥部
package.name = goldquant
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# 增加了权限和兼容性设置
requirements = python3,kivy,pandas,numpy,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 核心：自动同意协议，防止再次卡死
android.accept_sdk_license = True
p4a.branch = master
