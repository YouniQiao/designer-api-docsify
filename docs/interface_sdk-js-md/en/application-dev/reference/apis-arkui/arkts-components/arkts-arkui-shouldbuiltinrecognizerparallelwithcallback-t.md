# ShouldBuiltInRecognizerParallelWithCallback

```TypeScript
declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

Represents the callback used to set the parallel relationship between built-in gestures and gestures of other components in the response chain.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer--><!--Device-unnamed-declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| current | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Built-in gesture recognizer of the current component. Currently only a built- in gesture recognizer of the [GestureType]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_.PAN\_GESTURE type is supported.  |
| others | Array&lt;GestureRecognizer&gt; | Yes | Gesture recognizers of the same type from other components with higher priority in the response chain.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Gesture recognizer that is bound in parallel with the current recognizer.  |

