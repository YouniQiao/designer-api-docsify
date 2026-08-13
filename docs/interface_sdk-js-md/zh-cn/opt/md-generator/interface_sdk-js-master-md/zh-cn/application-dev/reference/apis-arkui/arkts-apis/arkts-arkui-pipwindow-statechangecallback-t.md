# StateChangeCallback

```TypeScript
type StateChangeCallback = (state: PiPState, reason: string) => void
```

描述画中画生命周期状态变化事件回调。

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-PiPWindow-type StateChangeCallback = (state: PiPState, reason: string) => void--><!--Device-PiPWindow-type StateChangeCallback = (state: PiPState, reason: string) => void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [PiPState](arkts-arkui-pipwindow-pipstate-e.md) | 是 |
| reason | string | 是 |
