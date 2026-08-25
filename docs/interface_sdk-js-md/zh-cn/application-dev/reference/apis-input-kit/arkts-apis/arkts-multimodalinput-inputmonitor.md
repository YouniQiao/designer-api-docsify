# @ohos.multimodalInput.inputMonitor(输入监听)

输入监听模块，提供了监听输入设备事件的能力。输入设备事件当前包括触屏输入事件、鼠标输入事件和触控板输入事件。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offtouch) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offmouse) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offpinch) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offpinch) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offrotate) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offthreefingersswipe) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offfourfingersswipe) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offthreefingerstap) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offfingerprint) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offswipeinward) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offtouchscreenswipe) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offtouchscreenpinch) |
| [off(输入监听)](arkts-input-inputmonitor-off-f-sys.md#offkeypressed) |
| [offFingerprint(输入监听)](arkts-input-inputmonitor-offfingerprint-f-sys.md) |
| [offFourFingersSwipe(输入监听)](arkts-input-inputmonitor-offfourfingersswipe-f-sys.md) |
| [offKeyPressed(输入监听)](arkts-input-inputmonitor-offkeypressed-f-sys.md) |
| [offMouse(输入监听)](arkts-input-inputmonitor-offmouse-f-sys.md) |
| [offPinch(输入监听)](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [offPinch(输入监听)](arkts-input-inputmonitor-offpinch-f-sys.md) |
| [offRotate(输入监听)](arkts-input-inputmonitor-offrotate-f-sys.md) |
| [offSwipeInward(输入监听)](arkts-input-inputmonitor-offswipeinward-f-sys.md) |
| [offThreeFingersSwipe(输入监听)](arkts-input-inputmonitor-offthreefingersswipe-f-sys.md) |
| [offThreeFingersTap(输入监听)](arkts-input-inputmonitor-offthreefingerstap-f-sys.md) |
| [offTouch(输入监听)](arkts-input-inputmonitor-offtouch-f-sys.md) |
| [offTouchscreenPinch(输入监听)](arkts-input-inputmonitor-offtouchscreenpinch-f-sys.md) |
| [offTouchscreenSwipe(输入监听)](arkts-input-inputmonitor-offtouchscreenswipe-f-sys.md) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#ontouch) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onmouse) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onmouse) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onpinch) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onpinch) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onrotate) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onthreefingersswipe) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onfourfingersswipe) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onthreefingerstap) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onfingerprint) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onswipeinward) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#ontouchscreenswipe) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#ontouchscreenpinch) |
| [on(输入监听)](arkts-input-inputmonitor-on-f-sys.md#onkeypressed) |
| [onFingerprint(输入监听)](arkts-input-inputmonitor-onfingerprint-f-sys.md) |
| [onFourFingersSwipe(输入监听)](arkts-input-inputmonitor-onfourfingersswipe-f-sys.md) |
| [onKeyPressed(输入监听)](arkts-input-inputmonitor-onkeypressed-f-sys.md) |
| [onMouse(输入监听)](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [onMouse(输入监听)](arkts-input-inputmonitor-onmouse-f-sys.md) |
| [onPinch(输入监听)](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [onPinch(输入监听)](arkts-input-inputmonitor-onpinch-f-sys.md) |
| [onRotate(输入监听)](arkts-input-inputmonitor-onrotate-f-sys.md) |
| [onSwipeInward(输入监听)](arkts-input-inputmonitor-onswipeinward-f-sys.md) |
| [onThreeFingersSwipe(输入监听)](arkts-input-inputmonitor-onthreefingersswipe-f-sys.md) |
| [onThreeFingersTap(输入监听)](arkts-input-inputmonitor-onthreefingerstap-f-sys.md) |
| [onTouch(输入监听)](arkts-input-inputmonitor-ontouch-f-sys.md) |
| [onTouchscreenPinch(输入监听)](arkts-input-inputmonitor-ontouchscreenpinch-f-sys.md) |
| [onTouchscreenSwipe(输入监听)](arkts-input-inputmonitor-ontouchscreenswipe-f-sys.md) |
| [queryTouchEvents(输入监听)](arkts-input-inputmonitor-querytouchevents-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [TouchEventReceiver(输入监听)](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) |
<!--DelEnd-->
