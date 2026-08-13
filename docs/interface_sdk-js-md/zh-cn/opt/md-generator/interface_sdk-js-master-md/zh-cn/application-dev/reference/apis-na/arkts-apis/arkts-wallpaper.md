# @ohos.wallpaper

壁纸管理服务为OpenHarmony系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。 > **说明：** > > 当前页面仅包含本模块的系统接口，其他公开接口参见[@ohos.wallpaper (壁纸)](#@ohos.wallpaper)。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace wallpaper--><!--Device-unnamed-declare namespace wallpaper-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

## 汇总

### 函数

| 名称 |
| --- |
| [getColors](arkts-na-wallpaper-getcolors-f.md#getColors) |
| [getColors](arkts-na-wallpaper-getcolors-f.md#getColors) |
| [getFile](arkts-na-wallpaper-getfile-f.md#getFile) |
| [getFile](arkts-na-wallpaper-getfile-f.md#getFile) |
| [getId](arkts-na-wallpaper-getid-f.md#getId) |
| [getId](arkts-na-wallpaper-getid-f.md#getId) |
| [getMinHeight](arkts-na-wallpaper-getminheight-f.md#getMinHeight) |
| [getMinHeight](arkts-na-wallpaper-getminheight-f.md#getMinHeight) |
| [getMinWidth](arkts-na-wallpaper-getminwidth-f.md#getMinWidth) |
| [getMinWidth](arkts-na-wallpaper-getminwidth-f.md#getMinWidth) |
| [isChangePermitted](arkts-na-wallpaper-ischangepermitted-f.md#isChangePermitted) |
| [isChangePermitted](arkts-na-wallpaper-ischangepermitted-f.md#isChangePermitted) |
| [isOperationAllowed](arkts-na-wallpaper-isoperationallowed-f.md#isOperationAllowed) |
| [isOperationAllowed](arkts-na-wallpaper-isoperationallowed-f.md#isOperationAllowed) |
| [off_colorChange](arkts-na-wallpaper-offcolorchange-f.md#off_colorChange) |
| [on_colorChange](arkts-na-wallpaper-oncolorchange-f.md#on_colorChange) |
| [reset](arkts-na-wallpaper-reset-f.md#reset) |
| [reset](arkts-na-wallpaper-reset-f.md#reset) |
| [setWallpaper](arkts-na-wallpaper-setwallpaper-f.md#setWallpaper) |
| [setWallpaper](arkts-na-wallpaper-setwallpaper-f.md#setWallpaper) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getColorsSync](arkts-na-wallpaper-getcolorssync-f-sys.md#getColorsSync（系统接口）) |
| [getImage](arkts-na-wallpaper-getimage-f-sys.md#getImage（系统接口）) |
| [getImage](arkts-na-wallpaper-getimage-f-sys.md#getImage（系统接口）) |
| [getMinHeightSync](arkts-na-wallpaper-getminheightsync-f-sys.md#getMinHeightSync（系统接口）) |
| [getMinWidthSync](arkts-na-wallpaper-getminwidthsync-f-sys.md#getMinWidthSync（系统接口）) |
| [getPixelMap](arkts-na-wallpaper-getpixelmap-f-sys.md#getPixelMap（系统接口）) |
| [getPixelMap](arkts-na-wallpaper-getpixelmap-f-sys.md#getPixelMap（系统接口）) |
| [getWallpaperByState](arkts-na-wallpaper-getwallpaperbystate-f-sys.md#getWallpaperByState（系统接口）) |
| [offWallpaperChange](arkts-na-wallpaper-offwallpaperchange-f-sys.md#offWallpaperChange（系统接口）) |
| [off_wallpaperChange](arkts-na-wallpaper-offwallpaperchange-f-sys.md) |
| [onWallpaperChange](arkts-na-wallpaper-onwallpaperchange-f-sys.md#onWallpaperChange（系统接口）) |
| [on_wallpaperChange](arkts-na-wallpaper-onwallpaperchange-f-sys.md) |
| [restore](arkts-na-wallpaper-restore-f-sys.md#restore（系统接口）) |
| [restore](arkts-na-wallpaper-restore-f-sys.md#restore（系统接口）) |
| [setAllWallpapers](arkts-na-wallpaper-setallwallpapers-f-sys.md#setAllWallpapers（系统接口）) |
| [setCustomWallpaper](arkts-na-wallpaper-setcustomwallpaper-f-sys.md#setCustomWallpaper（系统接口）) |
| [setCustomWallpaper](arkts-na-wallpaper-setcustomwallpaper-f-sys.md#setCustomWallpaper（系统接口）) |
| [setImage](arkts-na-wallpaper-setimage-f-sys.md#setImage（系统接口）) |
| [setImage](arkts-na-wallpaper-setimage-f-sys.md#setImage（系统接口）) |
| [setVideo](arkts-na-wallpaper-setvideo-f-sys.md#setVideo（系统接口）) |
| [setVideo](arkts-na-wallpaper-setvideo-f-sys.md#setVideo（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [RgbaColor](arkts-na-wallpaper-rgbacolor-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [WallpaperInfo](arkts-na-wallpaper-wallpaperinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [WallpaperType](arkts-na-wallpaper-wallpapertype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FoldState](arkts-na-wallpaper-foldstate-e-sys.md) |
| [RotateState](arkts-na-wallpaper-rotatestate-e-sys.md) |
| [WallpaperResourceType](arkts-na-wallpaper-wallpaperresourcetype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [WallpaperChangeObserver](arkts-na-wallpaper-wallpaperchangeobserver-t.md) |
