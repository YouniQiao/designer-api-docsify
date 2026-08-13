# SwipeRecognizer

Implements a swipe gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer).

**Inheritance/Implementation:** SwipeRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer)

**Since:** 18

**Deprecated since:** -1

<!--Device-unnamed-declare class SwipeRecognizer--><!--Device-unnamed-declare class SwipeRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): SwipeDirection
```

Obtains the direction for recognizing swipe gestures.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SwipeRecognizer-getDirection(): SwipeDirection--><!--Device-SwipeRecognizer-getDirection(): SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwipeDirection](arkts-arkui-swipedirection-e.md) |

## getVelocityThreshold

```TypeScript
getVelocityThreshold(): number
```

Obtains the minimum velocity required for the swipe gesture to be recognized.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SwipeRecognizer-getVelocityThreshold(): number--><!--Device-SwipeRecognizer-getVelocityThreshold(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
