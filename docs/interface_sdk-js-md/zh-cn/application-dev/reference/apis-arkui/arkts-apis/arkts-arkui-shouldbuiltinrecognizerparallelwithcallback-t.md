# ShouldBuiltInRecognizerParallelWithCallback

```TypeScript
export type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

Defines the callback type used in shouldBuiltInRecognizerParallelWith.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| current | [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | 是 |
| others | Array&lt;[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) |
