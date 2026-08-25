# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
| [offAdd](arkts-arkui-display-offadd-f.md) |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md) |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md) |
| [offChange](arkts-arkui-display-offchange-f.md) |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md) |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md) |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md) |
| [offRemove](arkts-arkui-display-offremove-f.md) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onadd-remove-change) |
| [on](arkts-arkui-display-on-f.md#onfoldstatuschange) |
| [on](arkts-arkui-display-on-f.md#onfoldanglechange) |
| [on](arkts-arkui-display-on-f.md#oncapturestatuschange) |
| [on](arkts-arkui-display-on-f.md#onfolddisplaymodechange) |
| [on](arkts-arkui-display-on-f.md#onbrightnessinfochange) |
| [onAdd](arkts-arkui-display-onadd-f.md) |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md) |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md) |
| [onChange](arkts-arkui-display-onchange-f.md) |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md) |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md) |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md) |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md) |
| [onRemove](arkts-arkui-display-onremove-f.md) |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md) |
| [off](arkts-arkui-display-off-f-sys.md#offprivatemodechange) |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md) |
| [on](arkts-arkui-display-on-f-sys.md#onprivatemodechange) |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md) |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md) |
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
### Interfaces(System API)

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
