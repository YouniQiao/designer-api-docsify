# @ohos.multimodalInput.inputMonitor

输入监听模块，提供了监听输入设备事件的能力。输入设备事件当前包括触屏输入事件、鼠标输入事件和触控板输入事件。 > **说明：** > > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。 > > - 文档中“全局”表示整个触控屏或触控板。如监听全局触屏输入事件，表示触摸触控板任何位置时，整个触控板的触屏输入事件均被监听。 > > - 本模块接口均为系统接口。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace inputMonitor--><!--Device-unnamed-declare namespace inputMonitor-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [offFingerprint](arkts-input-inputmonitor-offfingerprint-f-sys.md#offFingerprint（系统接口）) |
| [offFourFingersSwipe](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md#offFourFingersSwipe（系统接口）) |
| [offKeyPressed](arkts-input-inputmonitor-offkeypressed-f-sys.md#offKeyPressed（系统接口）) |
| [offMouse](arkts-input-inputmonitor-offmouse-f-sys.md#offMouse（系统接口）) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch（系统接口）) |
| [offPinch](arkts-input-inputmonitor-offpinch-f-sys.md#offPinch（系统接口）) |
| [offRotate](arkts-input-inputmonitor-offrotate-f-sys.md#offRotate（系统接口）) |
| [offSwipeInward](arkts-input-inputmonitor-offswipeinward-f-sys.md#offSwipeInward（系统接口）) |
| [offThreeFingersSwipe](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md#offThreeFingersSwipe（系统接口）) |
| [offThreeFingersTap](arkts-input-inputmonitor-offthreefingerstap-f-sys.md#offThreeFingersTap（系统接口）) |
| [offTouch](arkts-input-inputmonitor-offtouch-f-sys.md#offTouch（系统接口）) |
| [offTouchscreenPinch](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md#offTouchscreenPinch（系统接口）) |
| [offTouchscreenSwipe](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md#offTouchscreenSwipe（系统接口）) |
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
| [onFingerprint](arkts-input-inputmonitor-onfingerprint-f-sys.md#onFingerprint（系统接口）) |
| [onFourFingersSwipe](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md#onFourFingersSwipe（系统接口）) |
| [onKeyPressed](arkts-input-inputmonitor-onkeypressed-f-sys.md#onKeyPressed（系统接口）) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse（系统接口）) |
| [onMouse](arkts-input-inputmonitor-onmouse-f-sys.md#onMouse（系统接口）) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch（系统接口）) |
| [onPinch](arkts-input-inputmonitor-onpinch-f-sys.md#onPinch（系统接口）) |
| [onRotate](arkts-input-inputmonitor-onrotate-f-sys.md#onRotate（系统接口）) |
| [onSwipeInward](arkts-input-inputmonitor-onswipeinward-f-sys.md#onSwipeInward（系统接口）) |
| [onThreeFingersSwipe](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md#onThreeFingersSwipe（系统接口）) |
| [onThreeFingersTap](arkts-input-inputmonitor-onthreefingerstap-f-sys.md#onThreeFingersTap（系统接口）) |
| [onTouch](arkts-input-inputmonitor-ontouch-f-sys.md#onTouch（系统接口）) |
| [onTouchscreenPinch](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md#onTouchscreenPinch（系统接口）) |
| [onTouchscreenSwipe](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md#onTouchscreenSwipe（系统接口）) |
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
| [queryTouchEvents](arkts-input-inputmonitor-querytouchevents-f-sys.md#queryTouchEvents（系统接口）) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) |
<!--DelEnd-->
