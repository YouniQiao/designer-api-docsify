# @ohos.screen

The module implements basic screen management. You can use the APIs of this module to obtain a Screen object, listen for screen changes, and create and destroy virtual screens.

**Since:** 23

<!--Device-unnamed-declare namespace screen--><!--Device-unnamed-declare namespace screen-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
import { screenshot } from '@kit.ArkUI';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createVirtualScreen](arkts-arkui-screen-createvirtualscreen-f-sys.md#createvirtualscreen) | Creates a virtual screen. This API uses an asynchronous callback to return the result. |
| [createVirtualScreen](arkts-arkui-screen-createvirtualscreen-f-sys.md#createvirtualscreen-system-api) | Creates a virtual screen. This API uses a promise to return the result. |
| [destroyVirtualScreen](arkts-arkui-screen-destroyvirtualscreen-f-sys.md#destroyvirtualscreen) | Destroys a virtual screen. This API uses an asynchronous callback to return the result. |
| [destroyVirtualScreen](arkts-arkui-screen-destroyvirtualscreen-f-sys.md#destroyvirtualscreen-system-api) | Destroys a virtual screen. This API uses a promise to return the result. |
| [getAllScreens](arkts-arkui-screen-getallscreens-f-sys.md#getallscreens) | Obtains all screens. This API uses an asynchronous callback to return the result. |
| [getAllScreens](arkts-arkui-screen-getallscreens-f-sys.md#getallscreens-system-api) | Obtains all screens. This API uses an asynchronous callback to return the result. |
| [getAllScreens](arkts-arkui-screen-getallscreens-f-sys.md#getallscreens-system-api) | Obtains all screens. This API uses a promise to return the result. |
| [getAllScreens](arkts-arkui-screen-getallscreens-f-sys.md#getallscreens-system-api) | Obtains all screens. This API uses a promise to return the result. |
| [isScreenRotationLocked](arkts-arkui-screen-isscreenrotationlocked-f-sys.md#isscreenrotationlocked) | Checks whether auto rotate is locked. This API uses an asynchronous callback to return the result. |
| [isScreenRotationLocked](arkts-arkui-screen-isscreenrotationlocked-f-sys.md#isscreenrotationlocked-system-api) | Checks whether auto rotate is locked. This API uses a promise to return the result. |
| [makeExpand](arkts-arkui-screen-makeexpand-f-sys.md#makeexpand) | Sets the screen to extended mode. This API uses an asynchronous callback to return the result. |
| [makeExpand](arkts-arkui-screen-makeexpand-f-sys.md#makeexpand-system-api) | Sets the screen to extended mode. This API uses a promise to return the result. |
| [makeMirror](arkts-arkui-screen-makemirror-f-sys.md#makemirror) | Sets the screen to mirror mode. This API uses an asynchronous callback to return the result. |
| [makeMirror](arkts-arkui-screen-makemirror-f-sys.md#makemirror-system-api) | Sets the screen to mirror mode. This API uses a promise to return the result. |
| [makeMirrorWithRegion](arkts-arkui-screen-makemirrorwithregion-f-sys.md#makemirrorwithregion) | Sets a rectangle on the screen to mirror mode. This API uses a promise to return the result. After this API is called, you are advised not to rotate or fold the screen further. Otherwise, the mirrored content may be abnormal. |
| [makeUnique](arkts-arkui-screen-makeunique-f-sys.md#makeunique) | Sets the screen to independent display mode. This API uses a promise to return the result. |
| [offChange](arkts-arkui-screen-offchange-f-sys.md#offchange) | Unregister the callback for screen changes. |
| [offConnect](arkts-arkui-screen-offconnect-f-sys.md#offconnect) | Unregister the callback for screen connection events. |
| [offDisconnect](arkts-arkui-screen-offdisconnect-f-sys.md#offdisconnect) | Unregister the callback for screen disconnection events. |
| [off_change](arkts-arkui-screen-offchange-f-sys.md#offchange) | Unsubscribes from events related to the screen state. |
| [off_connect](arkts-arkui-screen-offconnect-f-sys.md#offconnect) | Unsubscribes from events related to the screen state. |
| [off_disconnect](arkts-arkui-screen-offdisconnect-f-sys.md#offdisconnect) | Unsubscribes from events related to the screen state. |
| [onChange](arkts-arkui-screen-onchange-f-sys.md#onchange) | Register the callback for screen change. |
| [onConnect](arkts-arkui-screen-onconnect-f-sys.md#onconnect) | Register the callback for screen connection events. |
| [onDisconnect](arkts-arkui-screen-ondisconnect-f-sys.md#ondisconnect) | Register the callback for screen disconnection events. |
| [on_change](arkts-arkui-screen-onchange-f-sys.md#onchange) | Subscribes to events related to the screen state. |
| [on_connect](arkts-arkui-screen-onconnect-f-sys.md#onconnect) | Subscribes to events related to the screen state. |
| [on_disconnect](arkts-arkui-screen-ondisconnect-f-sys.md#ondisconnect) | Subscribes to events related to the screen state. |
| [resizeVirtualScreen](arkts-arkui-screen-resizevirtualscreen-f-sys.md#resizevirtualscreen) | Resizes the virtual screen. This API uses a promise to return the result. |
| [setMultiScreenMode](arkts-arkui-screen-setmultiscreenmode-f-sys.md#setmultiscreenmode) | Sets the display mode (mirror or extend) of the secondary screen. This API uses a promise to return the result. If both **primaryScreenId** and **secondaryScreenId** are set to **0**, the content is displayed only on the secondary screen. |
| [setMultiScreenRelativePosition](arkts-arkui-screen-setmultiscreenrelativeposition-f-sys.md#setmultiscreenrelativeposition) | Sets the positions of the primary and secondary screens in extend mode. This API uses a promise to return the result. |
| [setScreenPrivacyMaskImage](arkts-arkui-screen-setscreenprivacymaskimage-f-sys.md#setscreenprivacymaskimage) | Sets a privacy mask image for the screen. This API uses a promise to return the result. |
| [setScreenRotationLocked](arkts-arkui-screen-setscreenrotationlocked-f-sys.md#setscreenrotationlocked) | Sets whether to lock auto rotate. This API uses an asynchronous callback to return the result. |
| [setScreenRotationLocked](arkts-arkui-screen-setscreenrotationlocked-f-sys.md#setscreenrotationlocked-system-api) | Sets whether to lock auto rotate. This API uses a promise to return the result. |
| [setVirtualScreenSurface](arkts-arkui-screen-setvirtualscreensurface-f-sys.md#setvirtualscreensurface) | Sets a surface for a virtual screen. This API uses an asynchronous callback to return the result. |
| [setVirtualScreenSurface](arkts-arkui-screen-setvirtualscreensurface-f-sys.md#setvirtualscreensurface-system-api) | Sets a surface for a virtual screen. This API uses a promise to return the result. |
| [stopExpand](arkts-arkui-screen-stopexpand-f-sys.md#stopexpand) | Stops extended mode. This API uses an asynchronous callback to return the result. |
| [stopExpand](arkts-arkui-screen-stopexpand-f-sys.md#stopexpand-system-api) | Stops extended mode. This API uses a promise to return the result. |
| [stopMirror](arkts-arkui-screen-stopmirror-f-sys.md#stopmirror) | Stops mirror mode. This API uses an asynchronous callback to return the result. |
| [stopMirror](arkts-arkui-screen-stopmirror-f-sys.md#stopmirror-system-api) | Stops mirror mode. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ExpandOption](arkts-arkui-screen-expandoption-i-sys.md) | Defines the parameters for expanding a screen. |
| [MultiScreenPositionOptions](arkts-arkui-screen-multiscreenpositionoptions-i-sys.md) | Describes the screen position information. |
| [OrientationOptions](arkts-arkui-screen-orientationoptions-i-sys.md) | The parameter of setting orientation |
| [Rect](arkts-arkui-screen-rect-i-sys.md) | Describes the rectangle information. |
| [Screen](arkts-arkui-screen-screen-i-sys.md) | Defines the [physical screen](../../../displaymanager/display-terminology.md#physical-screen) instance. Before calling any API in Screen, you must use [getAllScreens()](arkts-arkui-screen-getallscreens-f-sys.md#getallscreens-system-api) or [createVirtualScreen()](arkts-arkui-screen-createvirtualscreen-f-sys.md#createvirtualscreen-system-api) to obtain a Screen instance. |
| [ScreenModeInfo](arkts-arkui-screen-screenmodeinfo-i-sys.md) | Defines the screen mode information. |
| [VirtualScreenOption](arkts-arkui-screen-virtualscreenoption-i-sys.md) | Defines virtual screen parameters. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [MultiScreenMode](arkts-arkui-screen-multiscreenmode-e-sys.md) | Enumerates the display modes of secondary screens. |
| [Orientation](arkts-arkui-screen-orientation-e-sys.md) | Enumerates the screen orientations. |
| [ScreenSourceMode](arkts-arkui-screen-screensourcemode-e-sys.md) | Enumerates the sources of the content displayed on the screen. |
| [ScreenType](arkts-arkui-screen-screentype-e-sys.md) | Enumerates the types of screens. |
<!--DelEnd-->

