# @ohos.multimodalInput.inputMonitor(Input Monitor)

The **inputMonitor** module implements listening for events of input devices, including the touchscreen, mouse, and touchpad.

> **NOTE：**
> 
> - In this document, **global** indicates the entire touchscreen or touchpad. For example, listening for global
> touch events means to listen for touch events triggered when a user touches at any position on the touchpad.

**Since:** 7

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| off(Input Monitor) | Cancels listening for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| [off(Input Monitor)](arkts-input-multimodalinput-gestureevent-threefingersswipe-i.md) | Disables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| [off(Input Monitor)](arkts-input-multimodalinput-gestureevent-fourfingersswipe-i.md) | Disables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| [off(Input Monitor)](arkts-input-multimodalinput-gestureevent-threefingerstap-i.md) | Disables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| [off(Input Monitor)](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md) | Cancels listening for inward swipe events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Disables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| off(Input Monitor) | Cancels listening for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API must be used together with **inputMonitor.on ('keyPressed')**. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Listens for global touchscreen input events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for global mouse events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for mouse events. When the mouse pointer moves to the specified rectangular area, a callback is triggered. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result. |
| [on(Input Monitor)](arkts-input-multimodalinput-gestureevent-threefingersswipe-i.md) | Enables listening for three-finger swipe events. This API uses an asynchronous callback to return the result. |
| [on(Input Monitor)](arkts-input-multimodalinput-gestureevent-fourfingersswipe-i.md) | Enables listening for four-finger swipe events. This API uses an asynchronous callback to return the result. |
| [on(Input Monitor)](arkts-input-multimodalinput-gestureevent-threefingerstap-i.md) | Enables listening for three-finger tap events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result. |
| [on(Input Monitor)](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md) | Listens for inward swipe events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Enables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result. |
| on(Input Monitor) | Listens for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**, power, or volume key. This API uses an asynchronous callback to return the result. |
| [queryTouchEvents(Input Monitor)](arkts-input-inputmonitor-querytouchevents-f-sys.md) | Queries recent touchscreen input events. A maximum of 100 events can be queried. Since API version 26.0.0, a maximum of 60 events can be queried. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [TouchEventReceiver(Input Monitor)](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) | Callback used to return the touch event. |
<!--DelEnd-->
