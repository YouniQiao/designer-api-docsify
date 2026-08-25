# GestureGroupHandler

手势组处理器对象类型。

**继承/实现关系：** GestureGroupHandler extends [GestureHandler](arkts-arkui-gesture-gesturehandler-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: GestureGroupGestureHandlerOptions)
```

手势组处理器的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](arkts-arkui-gesture-gesturegroupgesturehandleroptions-i.md) | 否 |

## onCancel

```TypeScript
onCancel(event: VoidCallback): this
```

设置手势组处理器取消回调。顺序组合手势（[GestureMode](arkts-arkui-gesture-gesturemode-e.md).Sequence）取消后触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
