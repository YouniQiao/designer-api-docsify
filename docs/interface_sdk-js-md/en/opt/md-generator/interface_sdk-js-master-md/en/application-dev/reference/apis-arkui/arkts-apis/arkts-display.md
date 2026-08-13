# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addVirtualScreenBlocklist-(System-API)) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addVirtualScreenSurface-(System-API)) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasPrivateWindow-(System-API)) |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offPrivateModeChange-(System-API)) |
| [off_privateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md) |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onPrivateModeChange-(System-API)) |
| [on_privateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md) |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removeVirtualScreenBlocklist-(System-API)) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removeVirtualScreenSurface-(System-API)) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode-(System-API)) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode-(System-API)) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setFoldStatusLocked-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Display](arkts-arkui-display-display-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CornerType](arkts-arkui-display-cornertype-e.md) |
| [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md) |
| [DisplayState](arkts-arkui-display-displaystate-e.md) |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) |
| [FoldStatus](arkts-arkui-display-foldstatus-e.md) |
| [Orientation](arkts-arkui-display-orientation-e.md) |
| [ScreenShape](arkts-arkui-display-screenshape-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md) |
