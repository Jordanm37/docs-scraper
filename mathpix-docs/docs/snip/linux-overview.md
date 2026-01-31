---
title:  Snip for Linux
url: https://mathpix.com/docs/snip/linux-overview
---

* [Docs](/docs)  >
* [Snip](/docs/snip/overview)  >
* [Snip on desktop](snip-for-desktop)  >
* [Linux](linux-overview)

# Snip for Linux

The Linux app is distributed in form of AppImage and can be downloaded from [Mathpix.com](https://mathpix.com/) or via your terminal.

Please note that Snip is a system tray app. If you are running GNOME, which does not support the system tray, we recommend [downloading this extension](https://extensions.gnome.org/extension/1031/topicons/).

If you are running Wayland, for security reasons it will not allow you to use our app (the screen will turn black when you try to take a screenshot). In this case, we recommend switching desktop session to another one (Xorg, Kde, Xfce, LXDE) or using [our web app](https://snip.mathpix.com) instead.

### 1. Getting Snip app and launching it

1. Open <https://mathpix.com/>
2. Navigate to download buttons and click “Linux”
3. Save AppImage file to the desired location
4. Open “Files” app and navigate to the downloaded file
5. Open its properties, switch to “Permissions” and allow executing file as program
6. Launch the file

### 2. Getting Snip app and launching it from your Terminal (Advanced)

1. Open your terminal. And execute the following
2. `cd ~/Downloads`
3. `wget https://download.mathpix.com/linux/Mathpix_Snipping_Tool-x86_64.v03.00.0050.AppImage -O Mathpix_Snipping_Tool.AppImage` (Note: The link might change, check it on <https://mathpix.com/>)
4. `chmod 777 ./Mathpix_Snipping_Tool.AppImage`
5. `./Mathpix_Snipping_Tool.AppImage`

### 3. Updating app

App has its own update mechanism.  
There is no need to redownload fresh version from site

[<   Windows](/docs/snip/windows-overview)

[Snip on mobile   >](/docs/snip/snip-for-mobile)