# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from 'display';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md#convertGlobalToRelativeCoordinate) | Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the screen specified by **displayId**). This API supports only coordinate conversion between the primary screen and extended screen. If **displayId** is not passed, the coordinates are converted relative to the screen where the global coordinates are located. If the global coordinates are not on any screen, the coordinates are converted relative to the primary screen by default. |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md#convertRelativeToGlobalCoordinate) | Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen. |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createVirtualScreen) | Creates a virtual screen. This API uses a promise to return the result. |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md#destroyVirtualScreen) | Destroys a virtual screen. This API uses a promise to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getAllDisplay) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getAllDisplay) | Obtains all Display objects. This API uses a promise to return the result. |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md#getAllDisplayPhysicalResolution) | Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) | Obtains all Display objects. This API uses a promise to return the result. |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md#getBrightnessInfo) | Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md#BrightnessInfo) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md#getCurrentFoldCreaseRegion) | Obtains the crease region of the foldable device in the current display mode. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getDefaultDisplay) | Obtains the default Display object. This API uses an asynchronous callback to return the result. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getDefaultDisplay) | Obtains the default Display object. This API uses a promise to return the result. |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md#getDefaultDisplaySync) | Obtains the **Display** object of the screen where the application is located. If multiple abilities of an application are on different screens, the **Display** object of the main screen is returned. If multiple abilities of an application are on the same screen, the **Display** object of the screen is returned. |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md#getDisplayByIdSync) | Obtains a Display object based on the display ID. |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md#getFoldDisplayMode) | Obtains the display mode of this foldable device. |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md#getFoldStatus) | Obtains the fold status of this foldable device. |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md#getPrimaryDisplaySync) | Obtains the information about the primary display. For devices other than 2-in-1 devices, the Display object obtained is the built-in screen. For 2-in-1 devices with an external screen, the Display object obtained is the primary screen. For 2-in-1 devices without an external screen, the Display object obtained is the built-in screen. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#isCaptured) | Checks whether the device's screen content is being captured. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#isCaptured) | Check whether the device is captured, projected, or recorded by any app in the bundle name list. |
| [isFoldable](arkts-arkui-display-isfoldable-f.md#isFoldable) | Checks whether this device is foldable. |
| [makeUnique](arkts-arkui-display-makeunique-f.md#makeUnique) | Sets the screen to independent display mode. This API uses a promise to return the result. |
| [offAdd](arkts-arkui-display-offadd-f.md#offAdd) | Unregister the callback for display add events. |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offBrightnessInfoChange) | Unregister the callback for brightness info changes. |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offCaptureStatusChange) | Unregister the callback for the status of the device's screen content is being captured. |
| [offChange](arkts-arkui-display-offchange-f.md#offChange) | Unregister the callback for display changes. |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offFoldAngleChange) | Unregister the callback for fold angle changes. |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offFoldDisplayModeChange) | Unregister the callback for fold display mode changes. |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offFoldStatusChange) | Unregister the callback for fold status changes. |
| [offRemove](arkts-arkui-display-offremove-f.md#offRemove) | Unregister the callback for display remove events. |
| off_add | Unsubscribes from display changes. |
| off_brightnessInfoChange | Unsubscribes from events related to screen brightness information changes. |
| off_captureStatusChange | Unsubscribes from events indicating the status of the device's screen content is being captured. |
| off_change | Unsubscribes from display changes. |
| off_foldAngleChange | Unsubscribes from folding angle change events of the foldable device. |
| off_foldDisplayModeChange | Unsubscribes from display mode change events of the foldable device. |
| off_foldStatusChange | Unsubscribes from fold status change events of the foldable device. |
| off_remove | Unsubscribes from display changes. |
| [onAdd](arkts-arkui-display-onadd-f.md#onAdd) | Register the callback for display add events. |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onBrightnessInfoChange) | Register the callback for brightness info changes. |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#onCaptureStatusChange) | Register the callback for the status of the device's screen content is being captured. |
| [onChange](arkts-arkui-display-onchange-f.md#onChange) | Register the callback for display changes. |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md#onChangeWithAttribute) | Subscribes to changes of specified attributes of a display. |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onFoldAngleChange) | Register the callback for fold angle changes. |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onFoldDisplayModeChange) | Register the callback for fold display mode changes. |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onFoldStatusChange) | Register the callback for fold status changes. |
| [onRemove](arkts-arkui-display-onremove-f.md#onRemove) | Register the callback for display remove events. |
| on_add | Subscribes to display changes. |
| on_brightnessInfoChange | Subscribes to events related to screen brightness information changes. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md#BrightnessInfo) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| on_captureStatusChange | Subscribes to events indicating the status of the device's screen content is being captured. |
| on_change | Subscribes to display changes. |
| on_foldAngleChange | Subscribes to folding angle change events of the foldable device. Note that there are two folding angles for dual- fold axis devices. When oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively. |
| on_foldDisplayModeChange | Subscribes to display mode change events of the foldable device. To subscribe to fold status change events of foldable devices, use display.on('foldStatusChange'). The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status. |
| on_foldStatusChange | Subscribes to fold status change events of the foldable device. To subscribe to display mode change events of foldable devices, use display.on('foldDisplayModeChange') . The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status. To check whether the content is displayed on the inner or outer screen of the foldable device, use display.on('foldDisplayModeChange') . |
| on_remove | Subscribes to display changes. |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md#setVirtualScreenSurface) | Sets a surface for a virtual screen. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addVirtualScreenBlocklist) | Adds windows to the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addVirtualScreenSurface) | Add surface for the virtual screen. |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasPrivateWindow) | Checks whether there is a visible privacy window on a display. The window privacy mode can be set by calling setWindowPrivacyMode(). The content in the privacy window cannot be captured or recorded. |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offPrivateModeChange) | Unregister the callback for private mode changes. |
| off_privateModeChange | Unsubscribes from privacy mode changes of this display. |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onPrivateModeChange) | Register the callback for private mode changes. |
| on_privateModeChange | Subscribes to privacy mode changes of this display. When there is a privacy window in the foreground of the display , the display is in privacy mode, and the content in the privacy window cannot be captured or recorded. |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removeVirtualScreenBlocklist) | Removes windows from the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removeVirtualScreenSurface) | Remove surface for the virtual screen. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode) | Sets the display mode of the foldable device. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setFoldDisplayMode-(System-API)) | Sets the display mode of the foldable device, with the reason for the change specified. |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setFoldStatusLocked) | Sets whether to lock the current fold status of the foldable device. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) | Describes the screen brightness information. The information comes from the underlying screen data. |
| [CutoutInfo](arkts-arkui-display-cutoutinfo-i.md) | Describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display. |
| [Display](arkts-arkui-display-display-i.md) | Implements a Display instance, with attributes and APIs defined. Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getDefaultDisplaySync) to obtain a Display instance. |
| [DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md) | Describes the display mode of a device and the corresponding physical screen resolution information. |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) | Describes the crease region of a foldable device. |
| [Position](arkts-arkui-display-position-i.md) | Describes a coordinate position. In the global coordinate system, the origin is the top-left corner of the primary screen. In the relative coordinate system, the origin is the top-left corner of the specified screen. |
| [Rect](arkts-arkui-display-rect-i.md) | Describes a rectangle on the display. |
| [RelativePosition](arkts-arkui-display-relativeposition-i.md) | Describes a coordinate position in the relative coordinate system, with the origin in the top-left corner of the screen specified by **displayId**. |
| [RoundedCorner](arkts-arkui-display-roundedcorner-i.md) | Describes a single rounded corner on the screen. |
| [VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md) | Describes the virtual screen parameters. |
| [WaterfallDisplayAreaRects](arkts-arkui-display-waterfalldisplayarearects-i.md) | Describes the curved area on a waterfall display. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [Display](arkts-arkui-display-display-i-sys.md) | Implements a Display instance, with attributes and APIs defined. Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getAllDisplays) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getDefaultDisplaySync) to obtain a Display instance. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CornerType](arkts-arkui-display-cornertype-e.md) | Enumerates the types of corners on the screen. |
| [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md) | Enumerates the display modes for screen content. |
| [DisplayState](arkts-arkui-display-displaystate-e.md) | Enumerates the states of a display. |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) | Enumerates the display modes of a foldable device. > **NOTE：**> For foldable devices where both the inner and outer screens can serve as the primary screen �� like large or wide- > folding models �� the inner screen's display mode is **FOLD_DISPLAY_MODE_FULL**, and the outer screen's display > mode is **FOLD_DISPLAY_MODE_MAIN**. > For foldable devices where the outer screen serves only as an auxiliary display �� like small-folding models �� the > inner screen's display mode is **FOLD_DISPLAY_MODE_MAIN**, and the outer screen's display mode is > **FOLD_DISPLAY_MODE_SUB**. |
| [FoldStatus](arkts-arkui-display-foldstatus-e.md) | Enumerates the fold statuses of a foldable device. For dual-fold axis devices, when oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively. > **NOTE：**> Devices with only one fold axis can be in the **FOLD_STATUS_EXPANDED**, **FOLD_STATUS_FOLDED**, or > **FOLD_STATUS_HALF_FOLDED** state. > Devices with two fold axes can be in any of the states provided in the table above, except for > **FOLD_STATUS_UNKNOWN**, which indicates an unusable fold status. |
| [Orientation](arkts-arkui-display-orientation-e.md) | Enumerates the orientations of a display. |
| [ScreenShape](arkts-arkui-display-screenshape-e.md) | Enumerates the screen shapes of a display. |

### Types

| Name | Description |
| --- | --- |
| [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md) | Defines the callback function used to listen for screen brightness information. |

