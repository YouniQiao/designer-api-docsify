# GestureCollectInterceptCallback

```TypeScript
declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,
   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention
```

Defines the callback type used in [onGestureCollectIntercept]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention--><!--Device-unnamed-declare type GestureCollectInterceptCallback = (recognizers: Array<GestureRecognizer>,   touchRecognizers?: Array<TouchRecognizer>) => GestureCollectIntervention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recognizers | Array&lt;GestureRecognizer&gt; | Yes | Gesture recognizer objects of the component on the response chain.  |
| touchRecognizers | Array&lt;TouchRecognizer&gt; | No | Touch recognizer objects of the component on the response chain.\_\_\_HTML\_TAG\_USD\_0\_\_\_The default value is **null**.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Gesture collection intervention result.  |

