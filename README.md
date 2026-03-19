# 🔐 Meta-Business-Suit-SSL-Pinning-Bypass
📡 Intercept Meta Business Suite network traffic on Android device

## 📌 Latest Tested App Version
- 🎯 Business Suite version: **545.0.0.49.109**
- Architecture: **arm64-v8a, armeabi-v7a**
- For any inquiries, please contact me on Telegram [https://t.me/DarknessKing999](https://t.me/DarknessKing999)

## 🎥 Evidence
![Business Suite Android](assets/v545.jpg)

## ✅ Other Apps
1. [Facebook Android](https://github.com/shajon-dev/Facebook-SSL-Pinning-Bypass)
2. [Facebook iOS](https://github.com/shajon-dev/iOS-Facebook-SSL-Pinning-Bypass)
3. [Messenger Android](https://github.com/shajon-dev/Messenger-SSL-Pinning-Bypass)
4. [Messenger iOS](https://github.com/shajon-dev/iOS-Messenger-SSL-Pinning-Bypass)
5. [Instagram Android](https://github.com/shajon-dev/Instagram-SSL-Pinning-Bypass)
6. [Instagram iOS](https://github.com/shajon-dev/iOS-Instagram-SSL-Pinning-Bypass)
7. [Threads Android](https://github.com/shajon-dev/Threads-SSL-Pinning-Bypass)
8. [Threads iOS](https://github.com/shajon-dev/iOS-Threads-SSL-Pinning-Bypass)

## 📱 Requirements
1. 🔓 Rooted Android phone or Emulator with root access (ldplayer9 / nox player)
2. 🛠️ ADB tools installed on your computer
3. 🔄 ProxyPin or Reqable App for traffic capture

## 🔧 Setup Process
 1. 🔧 **Replace patched `libstartup.so`** with the original file at: `/data/data/com.facebook.pages.app/lib-compressed/libstartup.so`
 2. 📲 **Use ADB command** to push the patched library:
    ```
    adb push D:\patched\libstartup.so /data/data/com.facebook.pages.app/lib-compressed/libstartup.so
    ```
 4. Use any packet capture tool to monitor Business Suite network traffic.

## 📦 For Demo - Download Official APKs
**📥 Download Meta Business Suite 500.0.0.68.109 from official sources:**

- **🔧 arm64-v8a (64-bit):** [https://www.apkmirror.com/apk/facebook-2/pages-manager/meta-business-suite-500-0-0-68-109-release/meta-business-suite-500-0-0-68-109-7-android-apk-download/](https://www.apkmirror.com/apk/facebook-2/pages-manager/meta-business-suite-500-0-0-68-109-release/meta-business-suite-500-0-0-68-109-7-android-apk-download/)

- **🔧 armeabi-v7a (32-bit):** [https://www.apkmirror.com/apk/facebook-2/pages-manager/meta-business-suite-500-0-0-68-109-release/meta-business-suite-500-0-0-68-109-13-android-apk-download/](https://www.apkmirror.com/apk/facebook-2/pages-manager/meta-business-suite-500-0-0-68-109-release/meta-business-suite-500-0-0-68-109-13-android-apk-download/)

**📂 Free Patched `libstartup.so` files are available in the `libs/` folder**
**📜 Consolidated login scripts are available in the `login.sh` file**

## Looking for leatest version patched `libstartup.so`? Contact me on Telegram
<p align="left">
  <a href="https://t.me/DarknessKing999" target="_blank">
    <img src="https://img.shields.io/badge/💬_Chat_on_Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=121212&color=26A5E4&logoWidth=20" alt="Telegram" style="border-radius: 8px;"/>
  </a>
</p>

## 🎥 Tutorial Preview

<p align="center">
  <a href="https://youtube.com/shorts/-Tm5d5DqtWI?feature=shared" target="_blank">
    <img src="https://img.youtube.com/vi/-Tm5d5DqtWI/maxresdefault.jpg" alt="Tutorial Video" width="700" />
  </a>
</p>

## 📜 License

This project is licensed under the  
**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License.

You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit to the original author (S. SHAJON).
- NonCommercial — You may not use this project for commercial or professional purposes.

⚠ Commercial or professional use requires prior written permission from the author.

🔗 Full License: https://creativecommons.org/licenses/by-nc/4.0/
