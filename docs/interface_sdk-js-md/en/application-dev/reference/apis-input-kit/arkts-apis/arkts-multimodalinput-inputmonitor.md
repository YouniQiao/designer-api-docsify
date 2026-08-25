# @ohos.multimodalInput.inputMonitor(Input Monitor)

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad.

> **NOTE：**&gt;
> - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global
> touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offtouch) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offmouse) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offpinch) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offpinch) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offrotate) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offthreefingersswipe) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offfourfingersswipe) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offthreefingerstap) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offfingerprint) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offswipeinward) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offtouchscreenswipe) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offtouchscreenpinch) |
| [off(Input Monitor)](arkts-input-inputmonitor-off-f-sys.md#offkeypressed) |
| [offFingerprint(Input Monitor)](arkts-input-inputmonitor-offfingerprint-f-sys.md) |
| [offFourFingersSwipe(Input Monitor)](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md) |
| [offKeyPressed(Input Monitor)](arkts-input-inputmonitor-offkeypressed-f-sys.md) |
| [offMouse(Input Monitor)](arkts-input-inputmonitor-offmouse-f-sys.md) |
| [offPinch(Input Monitor)](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [offPinch(Input Monitor)](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [offRotate(Input Monitor)](arkts-input-inputmonitor-offrotate-f-sys.md) |
| [offSwipeInward(Input Monitor)](arkts-input-inputmonitor-offswipeinward-f-sys.md) |
| [offThreeFingersSwipe(Input Monitor)](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md) |
| [offThreeFingersTap(Input Monitor)](arkts-input-inputmonitor-offthreefingerstap-f-sys.md) |
| [offTouch(Input Monitor)](arkts-input-inputmonitor-offtouch-f-sys.md) |
| [offTouchscreenPinch(Input Monitor)](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md) |
| [offTouchscreenSwipe(Input Monitor)](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#ontouch) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onmouse) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onmouse) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onpinch) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onpinch) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onrotate) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onthreefingersswipe) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onfourfingersswipe) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onthreefingerstap) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onfingerprint) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onswipeinward) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#ontouchscreenswipe) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#ontouchscreenpinch) |
| [on(Input Monitor)](arkts-input-inputmonitor-on-f-sys.md#onkeypressed) |
| [onFingerprint(Input Monitor)](arkts-input-inputmonitor-onfingerprint-f-sys.md) |
| [onFourFingersSwipe(Input Monitor)](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md) |
| [onKeyPressed(Input Monitor)](arkts-input-inputmonitor-onkeypressed-f-sys.md) |
| [onMouse(Input Monitor)](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [onMouse(Input Monitor)](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [onPinch(Input Monitor)](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [onPinch(Input Monitor)](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [onRotate(Input Monitor)](arkts-input-inputmonitor-onrotate-f-sys.md) |
| [onSwipeInward(Input Monitor)](arkts-input-inputmonitor-onswipeinward-f-sys.md) |
| [onThreeFingersSwipe(Input Monitor)](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md) |
| [onThreeFingersTap(Input Monitor)](arkts-input-inputmonitor-onthreefingerstap-f-sys.md) |
| [onTouch(Input Monitor)](arkts-input-inputmonitor-ontouch-f-sys.md) |
| [onTouchscreenPinch(Input Monitor)](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md) |
| [onTouchscreenSwipe(Input Monitor)](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md) |
| [queryTouchEvents(Input Monitor)](arkts-input-inputmonitor-querytouchevents-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TouchEventReceiver(Input Monitor)](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) |
<!--DelEnd-->
