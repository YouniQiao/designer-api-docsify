# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 23

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md#convertglobaltorelativecoordinate) |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md#convertrelativetoglobalcoordinate) |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createvirtualscreen) |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md#destroyvirtualscreen) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay) |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay) |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md#getalldisplayphysicalresolution) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays) |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays) |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md#getbrightnessinfo) |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md#getcurrentfoldcreaseregion) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay) |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay) |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync) |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md#getdisplaybyidsync) |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md#getfolddisplaymode) |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md#getfoldstatus) |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md#getprimarydisplaysync) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured) |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured) |
| [isFoldable](arkts-arkui-display-isfoldable-f.md#isfoldable) |
| [makeUnique](arkts-arkui-display-makeunique-f.md#makeunique) |
| [offAdd](arkts-arkui-display-offadd-f.md#offadd) |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offbrightnessinfochange) |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offcapturestatuschange) |
| [offChange](arkts-arkui-display-offchange-f.md#offchange) |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offfoldanglechange) |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offfolddisplaymodechange) |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offfoldstatuschange) |
| [offRemove](arkts-arkui-display-offremove-f.md#offremove) |
| [off_add](arkts-arkui-display-offadd-f.md#offadd) |
| [off_brightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offbrightnessinfochange) |
| [off_captureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offcapturestatuschange) |
| [off_change](arkts-arkui-display-offchange-f.md#offchange) |
| [off_foldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offfoldanglechange) |
| [off_foldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offfolddisplaymodechange) |
| [off_foldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offfoldstatuschange) |
| [off_remove](arkts-arkui-display-offremove-f.md#offremove) |
| [onAdd](arkts-arkui-display-onadd-f.md#onadd) |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onbrightnessinfochange) |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#oncapturestatuschange) |
| [onChange](arkts-arkui-display-onchange-f.md#onchange) |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md#onchangewithattribute) |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onfoldanglechange) |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onfolddisplaymodechange) |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onfoldstatuschange) |
| [onRemove](arkts-arkui-display-onremove-f.md#onremove) |
| [on_add](arkts-arkui-display-onadd-f.md#onadd) |
| [on_brightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onbrightnessinfochange) |
| [on_captureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#oncapturestatuschange) |
| [on_change](arkts-arkui-display-onchange-f.md#onchange) |
| [on_foldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onfoldanglechange) |
| [on_foldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onfolddisplaymodechange) |
| [on_foldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onfoldstatuschange) |
| [on_remove](arkts-arkui-display-onremove-f.md#onremove) |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md#setvirtualscreensurface) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addvirtualscreenblocklist-system-api) |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addvirtualscreensurface-system-api) |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasprivatewindow-system-api) |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offprivatemodechange) |
| [off_privateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offprivatemodechange) |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onprivatemodechange) |
| [on_privateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onprivatemodechange) |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removevirtualscreenblocklist-system-api) |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removevirtualscreensurface-system-api) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode-system-api) |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode-system-api) |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setfoldstatuslocked-system-api) |
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
