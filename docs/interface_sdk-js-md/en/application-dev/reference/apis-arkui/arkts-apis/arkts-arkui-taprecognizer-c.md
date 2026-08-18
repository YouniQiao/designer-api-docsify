# TapRecognizer

Implements a tap gesture recognizer object. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#gesturerecognizer).

**Inheritance/Implementation:** TapRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md#gesturerecognizer)

**Since:** 18

<!--Device-unnamed-declare class TapRecognizer--><!--Device-unnamed-declare class TapRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getTapCount

```TypeScript
getTapCount(): number
```

Obtains the number of consecutive taps required for the tap gesture to be recognized.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TapRecognizer-getTapCount(): number--><!--Device-TapRecognizer-getTapCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of consecutive taps required for the tap gesture to be recognized. <br>Value range: [0, +∞) |

