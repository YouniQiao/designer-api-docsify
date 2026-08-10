# ShouldBuiltInRecognizerParallelWithCallback

```TypeScript
export type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

Defines the callback type used in shouldBuiltInRecognizerParallelWith.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer--><!--Device-unnamed-export type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| current | [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | Yes | the current gesture recognizer of the component |
| others | Array&lt;[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | the gesture recognizers of the component on the response chain |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | gesture recognizer of the component |

