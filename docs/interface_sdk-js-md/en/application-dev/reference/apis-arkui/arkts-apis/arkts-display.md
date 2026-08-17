# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 23

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
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md#convertglobaltorelativecoordinate) | Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the screen specified by **displayId**). This API supports only coordinate conversion between the primary screen and extended screen. If **displayId** is not passed, the coordinates are converted relative to the screen where the global coordinates are located. If the global coordinates are not on any screen, the coordinates are converted relative to the primary screen by default. |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md#convertrelativetoglobalcoordinate) | Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen. |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createvirtualscreen) | Creates a virtual screen. This API uses a promise to return the result. |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md#destroyvirtualscreen) | Destroys a virtual screen. This API uses a promise to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md#getalldisplay) | Obtains all Display objects. This API uses a promise to return the result. |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md#getalldisplayphysicalresolution) | Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays) | Obtains all Display objects. This API uses a promise to return the result. |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md#getbrightnessinfo) | Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md#brightnessinfo) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md#getcurrentfoldcreaseregion) | Obtains the crease region of the foldable device in the current display mode. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay) | Obtains the default Display object. This API uses an asynchronous callback to return the result. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md#getdefaultdisplay) | Obtains the default Display object. This API uses a promise to return the result. |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync) | Obtains the **Display** object of the screen where the application is located. If multiple abilities of an application are on different screens, the **Display** object of the main screen is returned. If multiple abilities of an application are on the same screen, the **Display** object of the screen is returned. |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md#getdisplaybyidsync) | Obtains a Display object based on the display ID. |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md#getfolddisplaymode) | Obtains the display mode of this foldable device. |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md#getfoldstatus) | Obtains the fold status of this foldable device. |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md#getprimarydisplaysync) | Obtains the information about the primary display. For devices other than 2-in-1 devices, the Display object obtained is the built-in screen. For 2-in-1 devices with an external screen, the Display object obtained is the primary screen. For 2-in-1 devices without an external screen, the Display object obtained is the built-in screen. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured) | Checks whether the device's screen content is being captured. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md#iscaptured) | Check whether the device is captured, projected, or recorded by any app in the bundle name list. |
| [isFoldable](arkts-arkui-display-isfoldable-f.md#isfoldable) | Checks whether this device is foldable. |
| [makeUnique](arkts-arkui-display-makeunique-f.md#makeunique) | Sets the screen to independent display mode. This API uses a promise to return the result. |
| [offAdd](arkts-arkui-display-offadd-f.md#offadd) | Unregister the callback for display add events. |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offbrightnessinfochange) | Unregister the callback for brightness info changes. |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offcapturestatuschange) | Unregister the callback for the status of the device's screen content is being captured. |
| [offChange](arkts-arkui-display-offchange-f.md#offchange) | Unregister the callback for display changes. |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offfoldanglechange) | Unregister the callback for fold angle changes. |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offfolddisplaymodechange) | Unregister the callback for fold display mode changes. |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offfoldstatuschange) | Unregister the callback for fold status changes. |
| [offRemove](arkts-arkui-display-offremove-f.md#offremove) | Unregister the callback for display remove events. |
| [off_add](arkts-arkui-display-offadd-f.md#offadd) | Unsubscribes from display changes. |
| [off_brightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md#offbrightnessinfochange) | Unsubscribes from events related to screen brightness information changes. |
| [off_captureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md#offcapturestatuschange) | Unsubscribes from events indicating the status of the device's screen content is being captured. |
| [off_change](arkts-arkui-display-offchange-f.md#offchange) | Unsubscribes from display changes. |
| [off_foldAngleChange](arkts-arkui-display-offfoldanglechange-f.md#offfoldanglechange) | Unsubscribes from folding angle change events of the foldable device. |
| [off_foldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md#offfolddisplaymodechange) | Unsubscribes from display mode change events of the foldable device. |
| [off_foldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md#offfoldstatuschange) | Unsubscribes from fold status change events of the foldable device. |
| [off_remove](arkts-arkui-display-offremove-f.md#offremove) | Unsubscribes from display changes. |
| [onAdd](arkts-arkui-display-onadd-f.md#onadd) | Register the callback for display add events. |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onbrightnessinfochange) | Register the callback for brightness info changes. |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#oncapturestatuschange) | Register the callback for the status of the device's screen content is being captured. |
| [onChange](arkts-arkui-display-onchange-f.md#onchange) | Register the callback for display changes. |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md#onchangewithattribute) | Subscribes to changes of specified attributes of a display. |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onfoldanglechange) | Register the callback for fold angle changes. |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onfolddisplaymodechange) | Register the callback for fold display mode changes. |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onfoldstatuschange) | Register the callback for fold status changes. |
| [onRemove](arkts-arkui-display-onremove-f.md#onremove) | Register the callback for display remove events. |
| [on_add](arkts-arkui-display-onadd-f.md#onadd) | Subscribes to display changes. |
| [on_brightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md#onbrightnessinfochange) | Subscribes to events related to screen brightness information changes. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md#brightnessinfo) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| [on_captureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md#oncapturestatuschange) | Subscribes to events indicating the status of the device's screen content is being captured. |
| [on_change](arkts-arkui-display-onchange-f.md#onchange) | Subscribes to display changes. |
| [on_foldAngleChange](arkts-arkui-display-onfoldanglechange-f.md#onfoldanglechange) | Subscribes to folding angle change events of the foldable device. Note that there are two folding angles for dual- fold axis devices. When oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively. |
| [on_foldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md#onfolddisplaymodechange) | Subscribes to display mode change events of the foldable device. To subscribe to fold status change events of foldable devices, use [display.on('foldStatusChange')](arkts-arkui-display-onadd-f.md#onadd). The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status. |
| [on_foldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md#onfoldstatuschange) | Subscribes to fold status change events of the foldable device. To subscribe to display mode change events of foldable devices, use [display.on('foldDisplayModeChange')](arkts-arkui-display-onadd-f.md#onadd) . The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status. To check whether the content is displayed on the inner or outer screen of the foldable device, use [display.on('foldDisplayModeChange')](arkts-arkui-display-onadd-f.md#onadd) . |
| [on_remove](arkts-arkui-display-onremove-f.md#onremove) | Subscribes to display changes. |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md#setvirtualscreensurface) | Sets a surface for a virtual screen. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md#addvirtualscreenblocklist) | Adds windows to the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addvirtualscreensurface) | Add surface for the virtual screen. |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md#hasprivatewindow) | Checks whether there is a visible privacy window on a display. The window privacy mode can be set by calling setWindowPrivacyMode(). The content in the privacy window cannot be captured or recorded. |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offprivatemodechange) | Unregister the callback for private mode changes. |
| [off_privateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md#offprivatemodechange) | Unsubscribes from privacy mode changes of this display. |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onprivatemodechange) | Register the callback for private mode changes. |
| [on_privateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md#onprivatemodechange) | Subscribes to privacy mode changes of this display. When there is a privacy window in the foreground of the display , the display is in privacy mode, and the content in the privacy window cannot be captured or recorded. |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md#removevirtualscreenblocklist) | Removes windows from the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md#removevirtualscreensurface) | Remove surface for the virtual screen. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode) | Sets the display mode of the foldable device. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md#setfolddisplaymode-system-api) | Sets the display mode of the foldable device, with the reason for the change specified. |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md#setfoldstatuslocked) | Sets whether to lock the current fold status of the foldable device. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) | Describes the screen brightness information. The information comes from the underlying screen data. |
| [CutoutInfo](arkts-arkui-display-cutoutinfo-i.md) | Describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display. |
| [Display](arkts-arkui-display-display-i.md) | Implements a Display instance, with attributes and APIs defined. Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getalldisplays) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync) to obtain a Display instance. |
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
| [Display](arkts-arkui-display-display-i-sys.md) | Implements a Display instance, with attributes and APIs defined. Before calling any API in Display, you must use [getAllDisplays()](arkts-arkui-display-getalldisplays-f.md#getalldisplays) or [getDefaultDisplaySync()](arkts-arkui-display-getdefaultdisplaysync-f.md#getdefaultdisplaysync) to obtain a Display instance. |
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

