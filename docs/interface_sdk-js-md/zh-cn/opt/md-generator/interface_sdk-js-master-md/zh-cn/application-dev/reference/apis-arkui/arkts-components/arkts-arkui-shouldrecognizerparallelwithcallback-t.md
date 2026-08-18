# ShouldRecognizerParallelWithCallback

```TypeScript
declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

手势与响应链上其他组件的手势设置并行关系的回调事件类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer--><!--Device-unnamed-declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| current | [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) | 是 |
| others | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) |
