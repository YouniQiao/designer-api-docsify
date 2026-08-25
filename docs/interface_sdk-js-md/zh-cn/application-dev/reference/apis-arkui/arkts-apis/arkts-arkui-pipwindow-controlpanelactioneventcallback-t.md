# ControlPanelActionEventCallback

```TypeScript
type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void
```

描述画中画控制面板控件动作事件回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [PiPActionEventType](arkts-arkui-pipwindow-pipactioneventtype-t.md) | 是 |
| status | number | 否 |
