# GestureCollectInterceptCallback

```TypeScript
declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,
   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention
```

定义在[onGestureCollectIntercept](arkts-arkui-commonmethod-c.md#ongesturecollectintercept)中使用的回调类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention--><!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recognizers | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | 响应链上组件的手势识别器对象。 |
| touchRecognizers | Array&lt;[TouchRecognizer](../arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | No | 响应链上组件的触摸识别器对象。<br/>默认值为null。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureCollectIntervention](../arkts-apis/arkts-arkui-gesturecollectintervention-e.md) | 手势收集干预结果。 |

