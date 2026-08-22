# GestureCollectInterceptCallback

```TypeScript
export type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,
    touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention
```

Defines the callback type used in onGestureCollectIntercept.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,    touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention--><!--Device-unnamed-export type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,    touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recognizers | Array&lt;[GestureRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | the gesture recognizers of the component on the response chain. |
| touchRecognizers | Array&lt;[TouchRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | No | the touch recognizers of the component on the response chain. |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureCollectIntervention](../../apis-arkui/arkts-apis/arkts-arkui-gesturecollectintervention-e.md) | the gesture intervention. |

