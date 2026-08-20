# @ohos.display

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

**Since:** 23

<!--Device-unnamed-declare namespace display--><!--Device-unnamed-declare namespace display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [convertGlobalToRelativeCoordinate](arkts-arkui-display-convertglobaltorelativecoordinate-f.md) | Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the screen specified by **displayId**). This API supports only coordinate conversion between the primary screen and extended screen. If **displayId** is not passed, the coordinates are converted relative to the screen where the global coordinates are located. If the global coordinates are not on any screen, the coordinates are converted relative to the primary screen by default. |
| [convertRelativeToGlobalCoordinate](arkts-arkui-display-convertrelativetoglobalcoordinate-f.md) | Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen. |
| [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md) | Creates a virtual screen. This API uses a promise to return the result. |
| [destroyVirtualScreen](arkts-arkui-display-destroyvirtualscreen-f.md) | Destroys a virtual screen. This API uses a promise to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplay](arkts-arkui-display-getalldisplay-f.md) | Obtains all Display objects. This API uses a promise to return the result. |
| [getAllDisplayPhysicalResolution](arkts-arkui-display-getalldisplayphysicalresolution-f.md) | Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md) | Obtains all Display objects. This API uses an asynchronous callback to return the result. |
| [getAllDisplays](arkts-arkui-display-getalldisplays-f.md) | Obtains all Display objects. This API uses a promise to return the result. |
| [getBrightnessInfo](arkts-arkui-display-getbrightnessinfo-f.md) | Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| [getCurrentFoldCreaseRegion](arkts-arkui-display-getcurrentfoldcreaseregion-f.md) | Obtains the crease region of the foldable device in the current display mode. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md) | Obtains the default Display object. This API uses an asynchronous callback to return the result. |
| [getDefaultDisplay](arkts-arkui-display-getdefaultdisplay-f.md) | Obtains the default Display object. This API uses a promise to return the result. |
| [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md) | Obtains the **Display** object of the screen where the application is located. If multiple abilities of an application are on different screens, the **Display** object of the main screen is returned. If multiple abilities of an application are on the same screen, the **Display** object of the screen is returned. |
| [getDisplayByIdSync](arkts-arkui-display-getdisplaybyidsync-f.md) | Obtains a Display object based on the display ID. |
| [getFoldDisplayMode](arkts-arkui-display-getfolddisplaymode-f.md) | Obtains the display mode of this foldable device. |
| [getFoldStatus](arkts-arkui-display-getfoldstatus-f.md) | Obtains the fold status of this foldable device. |
| [getPrimaryDisplaySync](arkts-arkui-display-getprimarydisplaysync-f.md) | Obtains the information about the primary display. For devices other than 2-in-1 devices, the Display object obtained is the built-in screen. For 2-in-1 devices with an external screen, the Display object obtained is the primary screen. For 2-in-1 devices without an external screen, the Display object obtained is the built-in screen. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md) | Checks whether the device's screen content is being captured. |
| [isCaptured](arkts-arkui-display-iscaptured-f.md) | Check whether the device is captured, projected, or recorded by any app in the bundle name list. |
| [isFoldable](arkts-arkui-display-isfoldable-f.md) | Checks whether this device is foldable. |
| [makeUnique](arkts-arkui-display-makeunique-f.md) | Sets the screen to independent display mode. This API uses a promise to return the result. |
| [offAdd](arkts-arkui-display-offadd-f.md) | Unregister the callback for display add events. |
| [offBrightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md) | Unregister the callback for brightness info changes. |
| [offCaptureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md) | Unregister the callback for the status of the device's screen content is being captured. |
| [offChange](arkts-arkui-display-offchange-f.md) | Unregister the callback for display changes. |
| [offFoldAngleChange](arkts-arkui-display-offfoldanglechange-f.md) | Unregister the callback for fold angle changes. |
| [offFoldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md) | Unregister the callback for fold display mode changes. |
| [offFoldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md) | Unregister the callback for fold status changes. |
| [offRemove](arkts-arkui-display-offremove-f.md) | Unregister the callback for display remove events. |
| off_add | Unsubscribes from display changes. |
| [off_brightnessInfoChange](arkts-arkui-display-offbrightnessinfochange-f.md) | Unsubscribes from events related to screen brightness information changes. |
| [off_captureStatusChange](arkts-arkui-display-offcapturestatuschange-f.md) | Unsubscribes from events indicating the status of the device's screen content is being captured. |
| off_change | Unsubscribes from display changes. |
| [off_foldAngleChange](arkts-arkui-display-offfoldanglechange-f.md) | Unsubscribes from folding angle change events of the foldable device. |
| [off_foldDisplayModeChange](arkts-arkui-display-offfolddisplaymodechange-f.md) | Unsubscribes from display mode change events of the foldable device. |
| [off_foldStatusChange](arkts-arkui-display-offfoldstatuschange-f.md) | Unsubscribes from fold status change events of the foldable device. |
| off_remove | Unsubscribes from display changes. |
| [onAdd](arkts-arkui-display-onadd-f.md) | Register the callback for display add events. |
| [onBrightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md) | Register the callback for brightness info changes. |
| [onCaptureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md) | Register the callback for the status of the device's screen content is being captured. |
| [onChange](arkts-arkui-display-onchange-f.md) | Register the callback for display changes. |
| [onChangeWithAttribute](arkts-arkui-display-onchangewithattribute-f.md) | Subscribes to changes of specified attributes of a display. |
| [onFoldAngleChange](arkts-arkui-display-onfoldanglechange-f.md) | Register the callback for fold angle changes. |
| [onFoldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md) | Register the callback for fold display mode changes. |
| [onFoldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md) | Register the callback for fold status changes. |
| [onRemove](arkts-arkui-display-onremove-f.md) | Register the callback for display remove events. |
| on_add | Subscribes to display changes. |
| [on_brightnessInfoChange](arkts-arkui-display-onbrightnessinfochange-f.md) | Subscribes to events related to screen brightness information changes. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value. |
| [on_captureStatusChange](arkts-arkui-display-oncapturestatuschange-f.md) | Subscribes to events indicating the status of the device's screen content is being captured. |
| on_change | Subscribes to display changes. |
| [on_foldAngleChange](arkts-arkui-display-onfoldanglechange-f.md) | Subscribes to folding angle change events of the foldable device. Note that there are two folding angles for dual- fold axis devices. When oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively. |
| [on_foldDisplayModeChange](arkts-arkui-display-onfolddisplaymodechange-f.md) | Subscribes to display mode change events of the foldable device. |
| [on_foldStatusChange](arkts-arkui-display-onfoldstatuschange-f.md) | Subscribes to fold status change events of the foldable device. |
| on_remove | Subscribes to display changes. |
| [setVirtualScreenSurface](arkts-arkui-display-setvirtualscreensurface-f.md) | Sets a surface for a virtual screen. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [addVirtualScreenBlocklist](arkts-arkui-display-addvirtualscreenblocklist-f-sys.md) | Adds windows to the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [addVirtualScreenSurface](arkts-arkui-display-addvirtualscreensurface-f-sys.md) | Add surface for the virtual screen. |
| [hasPrivateWindow](arkts-arkui-display-hasprivatewindow-f-sys.md) | Checks whether there is a visible privacy window on a display. The window privacy mode can be set by calling setWindowPrivacyMode(). The content in the privacy window cannot be captured or recorded. |
| [offPrivateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md) | Unregister the callback for private mode changes. |
| [off_privateModeChange](arkts-arkui-display-offprivatemodechange-f-sys.md) | Unsubscribes from privacy mode changes of this display. |
| [onPrivateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md) | Register the callback for private mode changes. |
| [on_privateModeChange](arkts-arkui-display-onprivatemodechange-f-sys.md) | Subscribes to privacy mode changes of this display. When there is a privacy window in the foreground of the display , the display is in privacy mode, and the content in the privacy window cannot be captured or recorded. |
| [removeVirtualScreenBlocklist](arkts-arkui-display-removevirtualscreenblocklist-f-sys.md) | Removes windows from the list of windows that are not allowed to be displayed during casting. This API takes effect only for the main window of an application or system windows. This API uses a promise to return the result. |
| [removeVirtualScreenSurface](arkts-arkui-display-removevirtualscreensurface-f-sys.md) | Remove surface for the virtual screen. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) | Sets the display mode of the foldable device. |
| [setFoldDisplayMode](arkts-arkui-display-setfolddisplaymode-f-sys.md) | Sets the display mode of the foldable device, with the reason for the change specified. |
| [setFoldStatusLocked](arkts-arkui-display-setfoldstatuslocked-f-sys.md) | Sets whether to lock the current fold status of the foldable device. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) | Describes the screen brightness information. The information comes from the underlying screen data. |
| [CutoutInfo](arkts-arkui-display-cutoutinfo-i.md) | Describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display. |
| [Display](arkts-arkui-display-display-i.md) | Implements a Display instance, with attributes and APIs defined. |
| [DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md) | Describes the display mode of a device and the corresponding physical screen resolution information. |
| [FoldCreaseRegion](arkts-arkui-display-foldcreaseregion-i.md) | Describes the crease region of a foldable device. |
| [Position](arkts-arkui-display-position-i.md) | Describes a coordinate position. In the global coordinate system, the origin is the top-left corner of the primary screen. In the relative coordinate system, the origin is the top-left corner of the specified screen. |
| [Rect](arkts-arkui-display-rect-i.md) | Describes a rectangle on the display. |
| [RelativePosition](arkts-arkui-display-relativeposition-i.md) | Describes a coordinate position in the relative coordinate system, with the origin in the top-left corner of the screen specified by **displayId**. |
| [RoundedCorner](arkts-arkui-display-roundedcorner-i.md) | Describes a single rounded corner on the screen. |
| [VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md) | Describes the virtual screen parameters. |
| [WaterfallDisplayAreaRects](arkts-arkui-display-waterfalldisplayarearects-i.md) | Describes the curved area on a waterfall display. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [Display](arkts-arkui-display-display-i-sys.md) | Implements a Display instance, with attributes and APIs defined. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CornerType](arkts-arkui-display-cornertype-e.md) | Enumerates the types of corners on the screen. |
| [DisplaySourceMode](arkts-arkui-display-displaysourcemode-e.md) | Enumerates the display modes for screen content. |
| [DisplayState](arkts-arkui-display-displaystate-e.md) | Enumerates the states of a display. |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) | Enumerates the display modes of a foldable device. |
| [FoldStatus](arkts-arkui-display-foldstatus-e.md) | Enumerates the fold statuses of a foldable device. For dual-fold axis devices, when oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively. |
| [Orientation](arkts-arkui-display-orientation-e.md) | Enumerates the orientations of a display. |
| [ScreenShape](arkts-arkui-display-screenshape-e.md) | Enumerates the screen shapes of a display. |

### Types

| Name | Description |
| --- | --- |
| [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md) | Defines the callback function used to listen for screen brightness information. |

