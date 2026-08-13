# @ohos.display

屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 汇总

### 函数

| 名称 |
| --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md#convertGlobalToRelativeCoordinate) |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md#convertRelativeToGlobalCoordinate) |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createVirtualScreen) |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md#destroyVirtualScreen) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getAllDisplay) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getAllDisplay) |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md#getAllDisplayPhysicalResolution) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md#getBrightnessInfo) |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md#getCurrentFoldCreaseRegion) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getDefaultDisplay) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getDefaultDisplay) |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md#getDefaultDisplaySync) |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md#getDisplayByIdSync) |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md#getFoldDisplayMode) |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md#getFoldStatus) |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md#getPrimaryDisplaySync) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#isCaptured) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#isCaptured) |
| [isFoldable](arkts-arkui-display-isfoldable-f.md#isFoldable) |
| [makeUnique](arkts-arkui-display-makeunique-f.md#makeUnique) |
| [offAdd](arkts-arkui-display-offadd-f.md#offAdd) |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offBrightnessInfoChange) |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offCaptureStatusChange) |
| [offChange](arkts-arkui-display-offchange-f.md#offChange) |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offFoldAngleChange) |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offFoldDisplayModeChange) |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offFoldStatusChange) |
| [offRemove](arkts-arkui-display-offremove-f.md#offRemove) |
| [off_add](arkts-arkui-display-offadd-f.md) |
| [off_brightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md) |
| [off_captureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md) |
| off_change |
| [off_foldAngleChange](arkts-arkui-display-offfoldanglechange-f.md) |
| [off_foldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md) |
| off_foldStatusChange |
| off_remove |
| [onAdd](arkts-arkui-display-onadd-f.md#onAdd) |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onBrightnessInfoChange) |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#onCaptureStatusChange) |
| [onChange](arkts-arkui-display-onchange-f.md#onChange) |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md#onChangeWithAttribute) |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onFoldAngleChange) |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onFoldDisplayModeChange) |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onFoldStatusChange) |
| [onRemove](arkts-arkui-display-onremove-f.md#onRemove) |
| [on_add](arkts-arkui-display-onadd-f.md) |
| [on_brightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md) |
| [on_captureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md) |
| on_change |
| [on_foldAngleChange](arkts-arkui-display-onfoldanglechange-f.md) |
| [on_foldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md) |
| on_foldStatusChange |
| on_remove |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md#setVirtualScreenSurface) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addVirtualScreenBlocklist（系统接口）) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addVirtualScreenSurface（系统接口）) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasPrivateWindow（系统接口）) |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offPrivateModeChange（系统接口）) |
| [off_privateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md) |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onPrivateModeChange（系统接口）) |
| [on_privateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md) |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removeVirtualScreenBlocklist（系统接口）) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removeVirtualScreenSurface（系统接口）) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode（系统接口）) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode（系统接口）) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setFoldStatusLocked（系统接口）) |
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
