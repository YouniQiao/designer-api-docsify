# @ohos.multimodalInput.inputMonitor

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad. > **NOTE：**> > - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global > touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace inputMonitor--><!--Device-unnamed-declare namespace inputMonitor-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputMonitor } from 'inputMonitor';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [offFingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offFingerprint) | Cancels listening for fingerprint key events. |
| [offFourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offFourFingersSwipe) | Cancel listening touchPad four finger swipe events. |
| [offKeyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offKeyPressed) | Disables listening for release events of specified keys. |
| [offMouse](arkts-input-inputmonitor-offmouse-f-sys.md#offMouse) | Cancel listening for mouse input events. |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch) | Cancel listening for touchPad pinch events. |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch-(System-API)) | Cancel listening for touchPad fingers pinch events. |
| [offRotate](arkts-input-inputmonitor-offrotate-f-sys.md#offRotate) | Cancel listening for touchPad fingers rotate events. |
| [offSwipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offSwipeInward) | Cancel listening touchPad swipe inward events. |
| [offThreeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offThreeFingersSwipe) | Cancel listening touchPad three fingers swipe events. |
| [offThreeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offThreeFingersTap) | Cancel listening touchPad three fingers tap events. |
| [offTouch](arkts-input-inputmonitor-offtouch-f-sys.md#offTouch) | Cancel listening for touch input events. |
| [offTouchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offTouchscreenPinch) | Disables listening touchscreen pinch gesture events. |
| [offTouchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offTouchscreenSwipe) | Disables listening touchscreen swipe gesture events. |
| off_fingerprint | Disables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| off_fourFingersSwipe | Disables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| off_keyPressed | Cancels listening for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API must be used together with **inputMonitor.on ('keyPressed')**. This API uses an asynchronous callback to return the result. |
| off_mouse | Disables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| off_pinch | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md#off_pinch-1) | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| off_rotate | Disables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| off_swipeInward | Cancels listening for inward swipe events. This API uses an asynchronous callback to return the result. |
| off_threeFingersSwipe | Disables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| off_threeFingersTap | Disables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| off_touch | Cancels listening for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| off_touchscreenPinch | Disables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| off_touchscreenSwipe | Disables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| [onFingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onFingerprint) | Enables listening for fingerprint key events. |
| [onFourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onFourFingersSwipe) | Listens for touchPad four fingers swipe events. |
| [onKeyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onKeyPressed) | Enables listening for release events of specified keys, such as the logo, power, and volume keys. |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse) | Listens for mouse input events. |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse-(System-API)) | Listens for mouse input events when the mouse arrow is within the specified rectangular area. |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch) | Listens for touchPad pinch events. |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch-(System-API)) | Listens for touchPad fingers pinch events. |
| [onRotate](arkts-input-inputmonitor-onrotate-f-sys.md#onRotate) | Listens for touchPad fingers rotate events. |
| [onSwipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onSwipeInward) | Enables listening touchPad swipe inward events. |
| [onThreeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onThreeFingersSwipe) | Listens for touchPad three fingers swipe events. |
| [onThreeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onThreeFingersTap) | Listens for touchPad three fingers tap events. |
| [onTouch](arkts-input-inputmonitor-ontouch-f-sys.md#onTouch) | Listens for touch input events. |
| [onTouchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#onTouchscreenPinch) | Enables listening touchscreen pinch gesture events. |
| [onTouchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#onTouchscreenSwipe) | Enables listening touchscreen swipe gesture events. |
| on_fingerprint | Enables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| on_fourFingersSwipe | Enables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| on_keyPressed | Listens for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API uses an asynchronous callback to return the result. |
| on_mouse | Enables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md#on_mouse-1) | Enables listening for mouse events. When the mouse pointer moves to the specified rectangular area, a callback is triggered. This API uses an asynchronous callback to return the result. |
| on_pinch | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md#on_pinch-1) | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| on_rotate | Enables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| on_swipeInward | Listens for inward swipe events. This API uses an asynchronous callback to return the result. |
| on_threeFingersSwipe | Enables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| on_threeFingersTap | Enables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| on_touch | Listens for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| on_touchscreenPinch | Enables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| on_touchscreenSwipe | Enables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| [queryTouchEvents](arkts-input-inputmonitor-querytouchevents-f-sys.md#queryTouchEvents) | Queries recent touchscreen input events. A maximum of 100 events can be queried. Since API version 26.0.0, a maximum of 60 events can be queried. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) | Callback used to return the touch event. |
<!--DelEnd-->

