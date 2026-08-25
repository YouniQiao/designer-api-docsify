# InputEventType

```TypeScript
declare type InputEventType = TouchEvent | MouseEvent | AxisEvent
```

[postInputEvent](arkts-arkui-buildernode-c.md#postinputevent)的参数，定义要发送的输入事件类型。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 |
| --- |
| [TouchEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-touchevent-touchevent-i.md) |
| [MouseEvent](../arkts-components/arkts-arkui-mouseevent-i.md) |
| [AxisEvent](arkts-arkui-common-axisevent-i.md) |
