# ShouldBuiltInRecognizerParallelWithCallback

```TypeScript
declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer
```

Represents the callback used to set the parallel relationship between built-in gestures and gestures of other components in the response chain.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| current | [GestureRecognizer](../arkts-apis/arkts-arkui-gesture-gesturerecognizer-c.md) | Yes |
| others | Array & lt;GestureRecognizer & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureRecognizer](../arkts-apis/arkts-arkui-gesture-gesturerecognizer-c.md) |
