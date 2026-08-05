# SwipeRecognizer

Implements a swipe gesture recognizer. Inherits from [GestureRecognizer]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** SwipeRecognizer extends [GestureRecognizer](arkts-arkui-component/gesture-gesturerecognizer-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare class SwipeRecognizer extends GestureRecognizer--><!--Device-unnamed-declare class SwipeRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): SwipeDirection
```

Obtains the direction for recognizing swipe gestures.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SwipeRecognizer-getDirection(): SwipeDirection--><!--Device-SwipeRecognizer-getDirection(): SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Direction for recognizing swipe gestures. |

## getVelocityThreshold

```TypeScript
getVelocityThreshold(): number
```

Obtains the minimum velocity required for the swipe gesture to be recognized.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SwipeRecognizer-getVelocityThreshold(): number--><!--Device-SwipeRecognizer-getVelocityThreshold(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Minimum velocity required for the swipe gesture to be recognized, in vp/s. |

