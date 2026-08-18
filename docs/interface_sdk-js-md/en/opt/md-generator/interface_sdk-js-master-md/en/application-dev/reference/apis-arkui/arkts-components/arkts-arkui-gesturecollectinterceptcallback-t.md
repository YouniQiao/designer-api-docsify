# GestureCollectInterceptCallback

```TypeScript
declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,
   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention
```

Defines the callback type used in [onGestureCollectIntercept](arkts-arkui-commonmethod-c.md#ongesturecollectintercept).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention--><!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recognizers | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes |
| touchRecognizers | Array&lt;[TouchRecognizer](../arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureCollectIntervention](../arkts-apis/arkts-arkui-gesturecollectintervention-e.md) |
