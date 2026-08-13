# SwipeRecognizer

Defines the swipe gesture recognizer.

**Inheritance/Implementation:** SwipeRecognizer extends [GestureRecognizer](arkts-arkui-gesture-gesturerecognizer-c.md#GestureRecognizer)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class SwipeRecognizer--><!--Device-unnamed-export declare class SwipeRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): SwipeDirection
```

Returns the swipe gesture's direction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeRecognizer-getDirection(): SwipeDirection--><!--Device-SwipeRecognizer-getDirection(): SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeDirection](arkts-arkui-gesture-swipedirection-e.md) | the direction of the swipe gesture. |

## getVelocityThreshold

```TypeScript
getVelocityThreshold(): double
```

Returns the swipe gesture's speed. The unit is vp/s.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeRecognizer-getVelocityThreshold(): double--><!--Device-SwipeRecognizer-getVelocityThreshold(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | the velocity threshold of the swipe gesture. |

