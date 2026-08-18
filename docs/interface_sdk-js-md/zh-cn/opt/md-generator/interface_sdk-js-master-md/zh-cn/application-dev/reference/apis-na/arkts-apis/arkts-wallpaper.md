# @ohos.wallpaper

壁纸管理服务为OpenHarmony系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。 > **说明：** > > 当前页面仅包含本模块的系统接口，其他公开接口参见[@ohos.wallpaper (壁纸)](#ohoswallpaper)。

**起始版本：** 23

<!--Device-unnamed-declare namespace wallpaper--><!--Device-unnamed-declare namespace wallpaper-End-->

**系统能力：** SystemCapability.MiscServices.Wallpaper

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [getColors](arkts-na-wallpaper-getcolors-f.md#getcolors) |
| [getColors](arkts-na-wallpaper-getcolors-f.md#getcolors) |
| [getFile](arkts-na-wallpaper-getfile-f.md#getfile) |
| [getFile](arkts-na-wallpaper-getfile-f.md#getfile) |
| [getId](arkts-na-wallpaper-getid-f.md#getid) |
| [getId](arkts-na-wallpaper-getid-f.md#getid) |
| [getMinHeight](arkts-na-wallpaper-getminheight-f.md#getminheight) |
| [getMinHeight](arkts-na-wallpaper-getminheight-f.md#getminheight) |
| [getMinWidth](arkts-na-wallpaper-getminwidth-f.md#getminwidth) |
| [getMinWidth](arkts-na-wallpaper-getminwidth-f.md#getminwidth) |
| [isChangePermitted](arkts-na-wallpaper-ischangepermitted-f.md#ischangepermitted) |
| [isChangePermitted](arkts-na-wallpaper-ischangepermitted-f.md#ischangepermitted) |
| [isOperationAllowed](arkts-na-wallpaper-isoperationallowed-f.md#isoperationallowed) |
| [isOperationAllowed](arkts-na-wallpaper-isoperationallowed-f.md#isoperationallowed) |
| [off_colorChange](arkts-na-wallpaper-offcolorchange-f.md#offcolorchange) |
| [on_colorChange](arkts-na-wallpaper-oncolorchange-f.md#oncolorchange) |
| [reset](arkts-na-wallpaper-reset-f.md#reset) |
| [reset](arkts-na-wallpaper-reset-f.md#reset) |
| [setWallpaper](arkts-na-wallpaper-setwallpaper-f.md#setwallpaper) |
| [setWallpaper](arkts-na-wallpaper-setwallpaper-f.md#setwallpaper) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getColorsSync](arkts-na-wallpaper-getcolorssync-f-sys.md#getcolorssync系统接口) |
| [getImage](arkts-na-wallpaper-getimage-f-sys.md#getimage系统接口) |
| [getImage](arkts-na-wallpaper-getimage-f-sys.md#getimage系统接口) |
| [getMinHeightSync](arkts-na-wallpaper-getminheightsync-f-sys.md#getminheightsync系统接口) |
| [getMinWidthSync](arkts-na-wallpaper-getminwidthsync-f-sys.md#getminwidthsync系统接口) |
| [getPixelMap](arkts-na-wallpaper-getpixelmap-f-sys.md#getpixelmap系统接口) |
| [getPixelMap](arkts-na-wallpaper-getpixelmap-f-sys.md#getpixelmap系统接口) |
| [getWallpaperByState](arkts-na-wallpaper-getwallpaperbystate-f-sys.md#getwallpaperbystate系统接口) |
| [offWallpaperChange](arkts-na-wallpaper-offwallpaperchange-f-sys.md#offwallpaperchange) |
| [off_wallpaperChange](arkts-na-wallpaper-offwallpaperchange-f-sys.md#offwallpaperchange) |
| [onWallpaperChange](arkts-na-wallpaper-onwallpaperchange-f-sys.md#onwallpaperchange) |
| [on_wallpaperChange](arkts-na-wallpaper-onwallpaperchange-f-sys.md#onwallpaperchange) |
| [restore](arkts-na-wallpaper-restore-f-sys.md#restore系统接口) |
| [restore](arkts-na-wallpaper-restore-f-sys.md#restore系统接口) |
| [setAllWallpapers](arkts-na-wallpaper-setallwallpapers-f-sys.md#setallwallpapers系统接口) |
| [setCustomWallpaper](arkts-na-wallpaper-setcustomwallpaper-f-sys.md#setcustomwallpaper系统接口) |
| [setCustomWallpaper](arkts-na-wallpaper-setcustomwallpaper-f-sys.md#setcustomwallpaper系统接口) |
| [setImage](arkts-na-wallpaper-setimage-f-sys.md#setimage系统接口) |
| [setImage](arkts-na-wallpaper-setimage-f-sys.md#setimage系统接口) |
| [setVideo](arkts-na-wallpaper-setvideo-f-sys.md#setvideo系统接口) |
| [setVideo](arkts-na-wallpaper-setvideo-f-sys.md#setvideo系统接口) |
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
