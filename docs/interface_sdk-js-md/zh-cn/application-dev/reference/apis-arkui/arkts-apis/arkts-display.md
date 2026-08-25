# @ohos.display

屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。

**起始版本：** 7

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md) |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md) |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md) |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md) |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md) |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md) |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md) |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md) |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md) |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md) |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md) |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md) |
| [isFoldable](arkts-arkui-display-isfoldable-f.md) |
| [makeUnique](arkts-arkui-display-makeunique-f.md) |
| [off](arkts-arkui-display-off-f.md#offadd-remove-change) |
| [off](arkts-arkui-display-off-f.md#offadd-remove-change) |
| [off](arkts-arkui-display-off-f.md#offadd-remove-change) |
| [off](arkts-arkui-display-off-f.md#offfoldstatuschange) |
| [off](arkts-arkui-display-off-f.md#offfoldanglechange) |
| [off](arkts-arkui-display-off-f.md#offcapturestatuschange) |
| [off](arkts-arkui-display-off-f.md#offfolddisplaymodechange) |
| [off](arkts-arkui-display-off-f.md#offbrightnessinfochange) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onfoldstatuschange) |
| [on](arkts-arkui-display-on-f.md#onfoldanglechange) |
| [on](arkts-arkui-display-on-f.md#oncapturestatuschange) |
| [on](arkts-arkui-display-on-f.md#onfolddisplaymodechange) |
| [on](arkts-arkui-display-on-f.md#onbrightnessinfochange) |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md) |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md) |
| off |
| on |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md) |
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
