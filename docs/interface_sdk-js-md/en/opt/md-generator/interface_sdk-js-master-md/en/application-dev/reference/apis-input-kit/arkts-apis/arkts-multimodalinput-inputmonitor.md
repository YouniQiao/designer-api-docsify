# @ohos.multimodalInput.inputMonitor

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad. > **NOTE：**> > - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global > touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace inputMonitor--><!--Device-unnamed-declare namespace inputMonitor-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offFingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offFingerprint-(System-API)) |
| [offFourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offFourFingersSwipe-(System-API)) |
| [offKeyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offKeyPressed-(System-API)) |
| [offMouse](arkts-input-inputmonitor-offmouse-f-sys.md#offMouse-(System-API)) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch-(System-API)) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch-(System-API)) |
| [offRotate](arkts-input-inputmonitor-offrotate-f-sys.md#offRotate-(System-API)) |
| [offSwipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offSwipeInward-(System-API)) |
| [offThreeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offThreeFingersSwipe-(System-API)) |
| [offThreeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offThreeFingersTap-(System-API)) |
| [offTouch](arkts-input-inputmonitor-offtouch-f-sys.md#offTouch-(System-API)) |
| [offTouchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offTouchscreenPinch-(System-API)) |
| [offTouchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offTouchscreenSwipe-(System-API)) |
| [off_fingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md) |
| [off_fourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md) |
| off_keyPressed |
| [off_mouse](arkts-input-inputmonitor-offmouse-f-sys.md) |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [off_rotate](arkts-input-inputmonitor-offrotate-f-sys.md) |
| [off_swipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md) |
| [off_threeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md) |
| [off_threeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md) |
| [off_touch](arkts-input-inputmonitor-offtouch-f-sys.md) |
| [off_touchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md) |
| [off_touchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md) |
| [onFingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onFingerprint-(System-API)) |
| [onFourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onFourFingersSwipe-(System-API)) |
| [onKeyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onKeyPressed-(System-API)) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse-(System-API)) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse-(System-API)) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch-(System-API)) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch-(System-API)) |
| [onRotate](arkts-input-inputmonitor-onrotate-f-sys.md#onRotate-(System-API)) |
| [onSwipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onSwipeInward-(System-API)) |
| [onThreeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onThreeFingersSwipe-(System-API)) |
| [onThreeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onThreeFingersTap-(System-API)) |
| [onTouch](arkts-input-inputmonitor-ontouch-f-sys.md#onTouch-(System-API)) |
| [onTouchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#onTouchscreenPinch-(System-API)) |
| [onTouchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#onTouchscreenSwipe-(System-API)) |
| [on_fingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md) |
| [on_fourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md) |
| on_keyPressed |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [on_rotate](arkts-input-inputmonitor-onrotate-f-sys.md) |
| [on_swipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md) |
| [on_threeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md) |
| [on_threeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md) |
| [on_touch](arkts-input-inputmonitor-ontouch-f-sys.md) |
| [on_touchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md) |
| [on_touchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md) |
| [queryTouchEvents](arkts-input-inputmonitor-querytouchevents-f-sys.md#queryTouchEvents-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) |
<!--DelEnd-->
