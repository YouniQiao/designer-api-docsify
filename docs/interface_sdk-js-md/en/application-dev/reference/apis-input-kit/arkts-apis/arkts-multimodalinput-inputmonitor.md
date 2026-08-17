# @ohos.multimodalInput.inputMonitor

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad. > **NOTE：**> > - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global > touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 23

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
| [offFingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offfingerprint) | Cancels listening for fingerprint key events. |
| [offFourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offfourfingersswipe) | Cancel listening touchPad four finger swipe events. |
| [offKeyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offkeypressed) | Disables listening for release events of specified keys. |
| [offMouse](arkts-input-inputmonitor-offmouse-f-sys.md#offmouse) | Cancel listening for mouse input events. |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch) | Cancel listening for touchPad pinch events. |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch-system-api) | Cancel listening for touchPad fingers pinch events. |
| [offRotate](arkts-input-inputmonitor-offrotate-f-sys.md#offrotate) | Cancel listening for touchPad fingers rotate events. |
| [offSwipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offswipeinward) | Cancel listening touchPad swipe inward events. |
| [offThreeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offthreefingersswipe) | Cancel listening touchPad three fingers swipe events. |
| [offThreeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offthreefingerstap) | Cancel listening touchPad three fingers tap events. |
| [offTouch](arkts-input-inputmonitor-offtouch-f-sys.md#offtouch) | Cancel listening for touch input events. |
| [offTouchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offtouchscreenpinch) | Disables listening touchscreen pinch gesture events. |
| [offTouchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offtouchscreenswipe) | Disables listening touchscreen swipe gesture events. |
| [off_fingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offfingerprint) | Disables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| [off_fourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offfourfingersswipe) | Disables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| [off_keyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offkeypressed) | Cancels listening for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API must be used together with **inputMonitor.on ('keyPressed')**. This API uses an asynchronous callback to return the result. |
| [off_mouse](arkts-input-inputmonitor-offmouse-f-sys.md#offmouse) | Disables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch) | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch-system-api) | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [off_rotate](arkts-input-inputmonitor-offrotate-f-sys.md#offrotate) | Disables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| [off_swipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offswipeinward) | Cancels listening for inward swipe events. This API uses an asynchronous callback to return the result. |
| [off_threeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offthreefingersswipe) | Disables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| [off_threeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offthreefingerstap) | Disables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| [off_touch](arkts-input-inputmonitor-offtouch-f-sys.md#offtouch) | Cancels listening for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| [off_touchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offtouchscreenpinch) | Disables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| [off_touchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offtouchscreenswipe) | Disables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| [onFingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onfingerprint) | Enables listening for fingerprint key events. |
| [onFourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onfourfingersswipe) | Listens for touchPad four fingers swipe events. |
| [onKeyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onkeypressed) | Enables listening for release events of specified keys, such as the logo, power, and volume keys. |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse) | Listens for mouse input events. |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse-system-api) | Listens for mouse input events when the mouse arrow is within the specified rectangular area. |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch) | Listens for touchPad pinch events. |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch-system-api) | Listens for touchPad fingers pinch events. |
| [onRotate](arkts-input-inputmonitor-onrotate-f-sys.md#onrotate) | Listens for touchPad fingers rotate events. |
| [onSwipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onswipeinward) | Enables listening touchPad swipe inward events. |
| [onThreeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onthreefingersswipe) | Listens for touchPad three fingers swipe events. |
| [onThreeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onthreefingerstap) | Listens for touchPad three fingers tap events. |
| [onTouch](arkts-input-inputmonitor-ontouch-f-sys.md#ontouch) | Listens for touch input events. |
| [onTouchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#ontouchscreenpinch) | Enables listening touchscreen pinch gesture events. |
| [onTouchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#ontouchscreenswipe) | Enables listening touchscreen swipe gesture events. |
| [on_fingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onfingerprint) | Enables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| [on_fourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onfourfingersswipe) | Enables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| [on_keyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onkeypressed) | Listens for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API uses an asynchronous callback to return the result. |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse) | Enables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse-system-api) | Enables listening for mouse events. When the mouse pointer moves to the specified rectangular area, a callback is triggered. This API uses an asynchronous callback to return the result. |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch) | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch-system-api) | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| [on_rotate](arkts-input-inputmonitor-onrotate-f-sys.md#onrotate) | Enables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| [on_swipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onswipeinward) | Listens for inward swipe events. This API uses an asynchronous callback to return the result. |
| [on_threeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onthreefingersswipe) | Enables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| [on_threeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onthreefingerstap) | Enables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| [on_touch](arkts-input-inputmonitor-ontouch-f-sys.md#ontouch) | Listens for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| [on_touchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#ontouchscreenpinch) | Enables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| [on_touchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#ontouchscreenswipe) | Enables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| [queryTouchEvents](arkts-input-inputmonitor-querytouchevents-f-sys.md#querytouchevents) | Queries recent touchscreen input events. A maximum of 100 events can be queried. Since API version 26.0.0, a maximum of 60 events can be queried. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) | Callback used to return the touch event. |
<!--DelEnd-->

