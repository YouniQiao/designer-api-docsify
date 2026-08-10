# ShouldRecognizerParallelWithCallback

```TypeScript
declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

手势与响应链上其他组件的手势设置并行关系的回调事件类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer--><!--Device-unnamed-declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| current | [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) | Yes | 当前组件的手势识别器，当前仅支持[GestureType](../arkts-apis/arkts-arkui-gesturecontrol-gesturetype-e.md/arkts-arkui-gesturecontrol-gesturetype-e.md).PAN_GESTURE类型的手势识别器。 |
| others | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | 响应链上优先级高于当前组件的其他组件所持有的同类型[GestureType](../arkts-apis/arkts-arkui-gesturecontrol-gesturetype-e.md/arkts-arkui-gesturecontrol-gesturetype-e.md)的手势识别器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) | 与current识别器绑定并行关系的某个手势识别器。 |

