# @ohos.display

屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

**起始版本：** 7

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 汇总

### 函数

| 名称 |
| --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md#convertglobaltorelativecoordinate) |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md#convertrelativetoglobalcoordinate) |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createvirtualscreen) |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md#destroyvirtualscreen) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay-1) |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md#getalldisplayphysicalresolution) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays-1) |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md#getbrightnessinfo) |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md#getcurrentfoldcreaseregion) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay-1) |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync) |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md#getdisplaybyidsync) |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md#getfolddisplaymode) |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md#getfoldstatus) |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md#getprimarydisplaysync) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured-1) |
| [isFoldable](arkts-arkui-display-isfoldable-f.md#isfoldable) |
| [makeUnique](arkts-arkui-display-makeunique-f.md#makeunique) |
| [off](arkts-arkui-display-off-f.md#off) |
| [off](arkts-arkui-display-off-f.md#off-1) |
| [off](arkts-arkui-display-off-f.md#off-2) |
| [off](arkts-arkui-display-off-f.md#off-4) |
| [off](arkts-arkui-display-off-f.md#off-5) |
| [off](arkts-arkui-display-off-f.md#off-6) |
| [off](arkts-arkui-display-off-f.md#off-7) |
| [off](arkts-arkui-display-off-f.md#off-8) |
| [on](arkts-arkui-display-on-f.md#on) |
| [on](arkts-arkui-display-on-f.md#on-1) |
| [on](arkts-arkui-display-on-f.md#on-2) |
| [on](arkts-arkui-display-on-f.md#on-4) |
| [on](arkts-arkui-display-on-f.md#on-5) |
| [on](arkts-arkui-display-on-f.md#on-6) |
| [on](arkts-arkui-display-on-f.md#on-7) |
| [on](arkts-arkui-display-on-f.md#on-8) |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md#onchangewithattribute) |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md#setvirtualscreensurface) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addvirtualscreenblocklist) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addvirtualscreensurface) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasprivatewindow) |
| [off](arkts-arkui-display-off-f-sys.md#off-3) |
| [on](arkts-arkui-display-on-f-sys.md#on-3) |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removevirtualscreenblocklist) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removevirtualscreensurface) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode-1) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setfoldstatuslocked) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) |
| [CutoutInfo](arkts-arkui-display-cutoutinfo-i.md) |
| [Display](arkts-arkui-display-display-i.md) |
| [DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md) |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) |
| [Position](arkts-arkui-display-position-i.md) |
| [Rect](arkts-arkui-display-rect-i.md) |
| [RelativePosition](arkts-arkui-display-relativeposition-i.md) |
| [RoundedCorner](arkts-arkui-display-roundedcorner-i.md) |
| [VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md) |
| [WaterfallDisplayAreaRects](arkts-arkui-display-waterfalldisplayarearects-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Display](arkts-arkui-display-display-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [CornerType](arkts-arkui-display-cornertype-e.md) |
| [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md) |
| [DisplayState](arkts-arkui-display-displaystate-e.md) |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) |
| [FoldStatus](arkts-arkui-display-foldstatus-e.md) |
| [Orientation](arkts-arkui-display-orientation-e.md) |
| [ScreenShape](arkts-arkui-display-screenshape-e.md) |

### 类型

| 名称 |
| --- |
| [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md) |
