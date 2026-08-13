# LongPressRecognizer

Implements a long press gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer).

**Inheritance/Implementation:** LongPressRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer)

**Since:** 18

**Deprecated since:** -1

<!--Device-unnamed-declare class LongPressRecognizer--><!--Device-unnamed-declare class LongPressRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAllowableMovement

```TypeScript
getAllowableMovement(): number
```

Obtains the maximum movement distance allowed for gesture recognition by the long press gesture recognizer.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LongPressRecognizer-getAllowableMovement(): number--><!--Device-LongPressRecognizer-getAllowableMovement(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDuration

```TypeScript
getDuration(): number
```

Obtains the minimum duration required for the long press gesture to be recognized.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LongPressRecognizer-getDuration(): number--><!--Device-LongPressRecognizer-getDuration(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isRepeat

```TypeScript
isRepeat(): boolean
```

Checks whether the long press gesture recognizer is set to trigger repeated callbacks.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LongPressRecognizer-isRepeat(): boolean--><!--Device-LongPressRecognizer-isRepeat(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
