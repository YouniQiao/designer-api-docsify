# @ohos.multimodalInput.inputMonitor

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad. > **NOTE：**> > - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global > touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 23

<!--Device-unnamed-declare namespace inputMonitor--><!--Device-unnamed-declare namespace inputMonitor-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offFingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offfingerprint) |
| [offFourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offfourfingersswipe) |
| [offKeyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offkeypressed) |
| [offMouse](arkts-input-inputmonitor-offmouse-f-sys.md#offmouse) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch-system-api) |
| [offRotate](arkts-input-inputmonitor-offrotate-f-sys.md#offrotate) |
| [offSwipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offswipeinward) |
| [offThreeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offthreefingersswipe) |
| [offThreeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offthreefingerstap) |
| [offTouch](arkts-input-inputmonitor-offtouch-f-sys.md#offtouch) |
| [offTouchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offtouchscreenpinch) |
| [offTouchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offtouchscreenswipe) |
| [off_fingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offfingerprint) |
| [off_fourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offfourfingersswipe) |
| [off_keyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offkeypressed) |
| [off_mouse](arkts-input-inputmonitor-offmouse-f-sys.md#offmouse) |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch) |
| [off_pinch](arkts-input-inputmonitor-offpinch-f-sys.md#offpinch-system-api) |
| [off_rotate](arkts-input-inputmonitor-offrotate-f-sys.md#offrotate) |
| [off_swipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offswipeinward) |
| [off_threeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offthreefingersswipe) |
| [off_threeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offthreefingerstap) |
| [off_touch](arkts-input-inputmonitor-offtouch-f-sys.md#offtouch) |
| [off_touchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offtouchscreenpinch) |
| [off_touchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offtouchscreenswipe) |
| [onFingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onfingerprint) |
| [onFourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onfourfingersswipe) |
| [onKeyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onkeypressed) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse-system-api) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch-system-api) |
| [onRotate](arkts-input-inputmonitor-onrotate-f-sys.md#onrotate) |
| [onSwipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onswipeinward) |
| [onThreeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onthreefingersswipe) |
| [onThreeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onthreefingerstap) |
| [onTouch](arkts-input-inputmonitor-ontouch-f-sys.md#ontouch) |
| [onTouchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#ontouchscreenpinch) |
| [onTouchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#ontouchscreenswipe) |
| [on_fingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onfingerprint) |
| [on_fourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onfourfingersswipe) |
| [on_keyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onkeypressed) |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse) |
| [on_mouse](arkts-input-inputmonitor-onmouse-f-sys.md#onmouse-system-api) |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch) |
| [on_pinch](arkts-input-inputmonitor-onpinch-f-sys.md#onpinch-system-api) |
| [on_rotate](arkts-input-inputmonitor-onrotate-f-sys.md#onrotate) |
| [on_swipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onswipeinward) |
| [on_threeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onthreefingersswipe) |
| [on_threeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onthreefingerstap) |
| [on_touch](arkts-input-inputmonitor-ontouch-f-sys.md#ontouch) |
| [on_touchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#ontouchscreenpinch) |
| [on_touchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#ontouchscreenswipe) |
| [queryTouchEvents](arkts-input-inputmonitor-querytouchevents-f-sys.md#querytouchevents-system-api) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) |
<!--DelEnd-->
