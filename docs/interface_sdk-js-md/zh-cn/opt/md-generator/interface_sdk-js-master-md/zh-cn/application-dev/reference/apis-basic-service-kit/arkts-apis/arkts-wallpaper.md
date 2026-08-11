# @ohos.wallpaper(壁纸)

壁纸管理服务为OpenHarmony系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。

> **说明：**
> 
> 当前页面仅包含本模块的系统接口，其他公开接口参见[@ohos.wallpaper (壁纸)](arkts-wallpaper.md)。

**起始版本：** 7

<!--Device-unnamed-declare namespace wallpaper--><!--Device-unnamed-declare namespace wallpaper-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

## 汇总

### 函数

| 名称 |
| --- |
| [getColors](arkts-basicservices-wallpaper-getcolors-f.md#getcolors) |
| [getColors](arkts-basicservices-wallpaper-getcolors-f.md#getcolors-1) |
| [getFile](arkts-basicservices-wallpaper-getfile-f.md#getfile) |
| [getFile](arkts-basicservices-wallpaper-getfile-f.md#getfile-1) |
| [getId](arkts-basicservices-wallpaper-getid-f.md#getid) |
| [getId](arkts-basicservices-wallpaper-getid-f.md#getid-1) |
| [getMinHeight](arkts-basicservices-wallpaper-getminheight-f.md#getminheight) |
| [getMinHeight](arkts-basicservices-wallpaper-getminheight-f.md#getminheight-1) |
| [getMinWidth](arkts-basicservices-wallpaper-getminwidth-f.md#getminwidth) |
| [getMinWidth](arkts-basicservices-wallpaper-getminwidth-f.md#getminwidth-1) |
| [isChangePermitted](arkts-basicservices-wallpaper-ischangepermitted-f.md#ischangepermitted) |
| [isChangePermitted](arkts-basicservices-wallpaper-ischangepermitted-f.md#ischangepermitted-1) |
| [isOperationAllowed](arkts-basicservices-wallpaper-isoperationallowed-f.md#isoperationallowed) |
| [isOperationAllowed](arkts-basicservices-wallpaper-isoperationallowed-f.md#isoperationallowed-1) |
| [off](arkts-basicservices-wallpaper-off-f.md#off) |
| [on](arkts-basicservices-wallpaper-on-f.md#on) |
| [reset](arkts-basicservices-wallpaper-reset-f.md#reset) |
| [reset](arkts-basicservices-wallpaper-reset-f.md#reset-1) |
| [setWallpaper](arkts-basicservices-wallpaper-setwallpaper-f.md#setwallpaper) |
| [setWallpaper](arkts-basicservices-wallpaper-setwallpaper-f.md#setwallpaper-1) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getColorsSync](arkts-basicservices-wallpaper-getcolorssync-f-sys.md#getcolorssync) |
| [getImage](arkts-basicservices-wallpaper-getimage-f-sys.md#getimage) |
| [getImage](arkts-basicservices-wallpaper-getimage-f-sys.md#getimage-1) |
| [getMinHeightSync](arkts-basicservices-wallpaper-getminheightsync-f-sys.md#getminheightsync) |
| [getMinWidthSync](arkts-basicservices-wallpaper-getminwidthsync-f-sys.md#getminwidthsync) |
| [getPixelMap](arkts-basicservices-wallpaper-getpixelmap-f-sys.md#getpixelmap) |
| [getPixelMap](arkts-basicservices-wallpaper-getpixelmap-f-sys.md#getpixelmap-1) |
| [getWallpaperByState](arkts-basicservices-wallpaper-getwallpaperbystate-f-sys.md#getwallpaperbystate) |
| [off](arkts-basicservices-wallpaper-off-f-sys.md#off-1) |
| [on](arkts-basicservices-wallpaper-on-f-sys.md#on-1) |
| [restore](arkts-basicservices-wallpaper-restore-f-sys.md#restore) |
| [restore](arkts-basicservices-wallpaper-restore-f-sys.md#restore-1) |
| [setAllWallpapers](arkts-basicservices-wallpaper-setallwallpapers-f-sys.md#setallwallpapers) |
| [setCustomWallpaper](arkts-basicservices-wallpaper-setcustomwallpaper-f-sys.md#setcustomwallpaper) |
| [setCustomWallpaper](arkts-basicservices-wallpaper-setcustomwallpaper-f-sys.md#setcustomwallpaper-1) |
| [setImage](arkts-basicservices-wallpaper-setimage-f-sys.md#setimage) |
| [setImage](arkts-basicservices-wallpaper-setimage-f-sys.md#setimage-1) |
| [setVideo](arkts-basicservices-wallpaper-setvideo-f-sys.md#setvideo) |
| [setVideo](arkts-basicservices-wallpaper-setvideo-f-sys.md#setvideo-1) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [RgbaColor](arkts-basicservices-wallpaper-rgbacolor-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [WallpaperInfo](arkts-basicservices-wallpaper-wallpaperinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [WallpaperType](arkts-basicservices-wallpaper-wallpapertype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FoldState](arkts-basicservices-wallpaper-foldstate-e-sys.md) |
| [RotateState](arkts-basicservices-wallpaper-rotatestate-e-sys.md) |
| [WallpaperResourceType](arkts-basicservices-wallpaper-wallpaperresourcetype-e-sys.md) |
<!--DelEnd-->
