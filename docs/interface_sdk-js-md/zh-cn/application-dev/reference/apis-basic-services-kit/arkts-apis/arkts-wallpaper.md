# @ohos.wallpaper(壁纸)

壁纸管理服务为OpenHarmony系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。

> **说明：**&gt;
> 当前页面仅包含本模块的系统接口，其他公开接口参见[@ohos.wallpaper (壁纸)](#ohoswallpaper壁纸)。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Wallpaper

## 导入模块

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getColors(壁纸)](arkts-basicservices-wallpaper-getcolors-f.md) |
| [getColors(壁纸)](arkts-basicservices-wallpaper-getcolors-f.md) |
| [getFile(壁纸)](arkts-basicservices-wallpaper-getfile-f.md) |
| [getFile(壁纸)](arkts-basicservices-wallpaper-getfile-f.md) |
| [getId(壁纸)](arkts-basicservices-wallpaper-getid-f.md) |
| [getId(壁纸)](arkts-basicservices-wallpaper-getid-f.md) |
| [getMinHeight(壁纸)](arkts-basicservices-wallpaper-getminheight-f.md) |
| [getMinHeight(壁纸)](arkts-basicservices-wallpaper-getminheight-f.md) |
| [getMinWidth(壁纸)](arkts-basicservices-wallpaper-getminwidth-f.md) |
| [getMinWidth(壁纸)](arkts-basicservices-wallpaper-getminwidth-f.md) |
| [isChangePermitted(壁纸)](arkts-basicservices-wallpaper-ischangepermitted-f.md) |
| [isChangePermitted(壁纸)](arkts-basicservices-wallpaper-ischangepermitted-f.md) |
| [isOperationAllowed(壁纸)](arkts-basicservices-wallpaper-isoperationallowed-f.md) |
| [isOperationAllowed(壁纸)](arkts-basicservices-wallpaper-isoperationallowed-f.md) |
| [off(壁纸)](arkts-basicservices-wallpaper-off-f.md#offcolorchange) |
| [on(壁纸)](arkts-basicservices-wallpaper-on-f.md#oncolorchange) |
| [reset(壁纸)](arkts-basicservices-wallpaper-reset-f.md) |
| [reset(壁纸)](arkts-basicservices-wallpaper-reset-f.md) |
| [setWallpaper(壁纸)](arkts-basicservices-wallpaper-setwallpaper-f.md) |
| [setWallpaper(壁纸)](arkts-basicservices-wallpaper-setwallpaper-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getColorsSync(壁纸)](arkts-basicservices-wallpaper-getcolorssync-f-sys.md) |
| [getImage(壁纸)](arkts-basicservices-wallpaper-getimage-f-sys.md) |
| [getImage(壁纸)](arkts-basicservices-wallpaper-getimage-f-sys.md) |
| [getMinHeightSync(壁纸)](arkts-basicservices-wallpaper-getminheightsync-f-sys.md) |
| [getMinWidthSync(壁纸)](arkts-basicservices-wallpaper-getminwidthsync-f-sys.md) |
| [getPixelMap(壁纸)](arkts-basicservices-wallpaper-getpixelmap-f-sys.md) |
| [getPixelMap(壁纸)](arkts-basicservices-wallpaper-getpixelmap-f-sys.md) |
| [getWallpaperByState(壁纸)](arkts-basicservices-wallpaper-getwallpaperbystate-f-sys.md) |
| off(壁纸) |
| on(壁纸) |
| [restore(壁纸)](arkts-basicservices-wallpaper-restore-f-sys.md) |
| [restore(壁纸)](arkts-basicservices-wallpaper-restore-f-sys.md) |
| [setAllWallpapers(壁纸)](arkts-basicservices-wallpaper-setallwallpapers-f-sys.md) |
| [setCustomWallpaper(壁纸)](arkts-basicservices-wallpaper-setcustomwallpaper-f-sys.md) |
| [setCustomWallpaper(壁纸)](arkts-basicservices-wallpaper-setcustomwallpaper-f-sys.md) |
| [setImage(壁纸)](arkts-basicservices-wallpaper-setimage-f-sys.md) |
| [setImage(壁纸)](arkts-basicservices-wallpaper-setimage-f-sys.md) |
| [setVideo(壁纸)](arkts-basicservices-wallpaper-setvideo-f-sys.md) |
| [setVideo(壁纸)](arkts-basicservices-wallpaper-setvideo-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [RgbaColor(壁纸)](arkts-basicservices-wallpaper-rgbacolor-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [WallpaperInfo(壁纸)](arkts-basicservices-wallpaper-wallpaperinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [WallpaperType(壁纸)](arkts-basicservices-wallpaper-wallpapertype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FoldState(壁纸)](arkts-basicservices-wallpaper-foldstate-e-sys.md) |
| [RotateState(壁纸)](arkts-basicservices-wallpaper-rotatestate-e-sys.md) |
| [WallpaperResourceType(壁纸)](arkts-basicservices-wallpaper-wallpaperresourcetype-e-sys.md) |
<!--DelEnd-->
