# PanListenerCallback

```TypeScript
declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void
```

Pan手势事件监听函数类型。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [GestureEvent](arkts-arkui-gesture-gestureevent-i.md) | 是 |
| current | [GestureRecognizer](arkts-arkui-gesture-gesturerecognizer-c.md) | 是 |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 否 |
