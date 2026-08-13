# PinchRecognizer

Implements a pinch gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer).

**Inheritance/Implementation:** PinchRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#GestureRecognizer)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-declare class PinchRecognizer--><!--Device-unnamed-declare class PinchRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDistance

```TypeScript
getDistance(): number
```

Obtains the minimum distance required for the pinch gesture to be recognized.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PinchRecognizer-getDistance(): number--><!--Device-PinchRecognizer-getDistance(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Minimum distance required for the pinch gesture to be recognized, in vp. &lt;br&gt;Value range: [0, +∞) |

