# WindowEventListener

```TypeScript
declare type WindowEventListener = (windowId: int, event: window.WindowEventType) => void
```

窗口生命周期事件通知的回调函数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type WindowEventListener = (windowId: int, event: window.WindowEventType) => void--><!--Device-unnamed-declare type WindowEventListener = (windowId: int, event: window.WindowEventType) => void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 触发事件的窗口id |
| event | window.WindowEventType | Yes | 窗口回调的事件类型 |

