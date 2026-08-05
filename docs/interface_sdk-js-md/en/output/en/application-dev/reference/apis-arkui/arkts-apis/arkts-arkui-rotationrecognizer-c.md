# RotationRecognizer

Implements a rotation gesture recognizer. Inherits from [GestureRecognizer]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** RotationRecognizer extends [GestureRecognizer](arkts-arkui-component/gesture-gesturerecognizer-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare class RotationRecognizer extends GestureRecognizer--><!--Device-unnamed-declare class RotationRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAngle

```TypeScript
getAngle(): number
```

Obtains the minimum angle change required for the rotation gesture to be recognized.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RotationRecognizer-getAngle(): number--><!--Device-RotationRecognizer-getAngle(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Minimum angle change required for the rotation gesture to be recognized, in degrees (deg). |

