# WindowEventListener

```TypeScript
declare type WindowEventListener = (windowId: int, event: window.WindowEventType) => void
```

窗口生命周期事件通知的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| event | [window.WindowEventType](arkts-arkui-window-windoweventtype-e.md) | 是 |
