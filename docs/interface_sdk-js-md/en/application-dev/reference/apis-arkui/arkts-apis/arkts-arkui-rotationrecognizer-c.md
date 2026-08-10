# RotationRecognizer

旋转手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。

**Inheritance/Implementation:** RotationRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare class RotationRecognizer extends GestureRecognizer--><!--Device-unnamed-declare class RotationRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAngle

```TypeScript
getAngle(): number
```

返回预设旋转手势识别器触发旋转手势最小改变度数阈值。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RotationRecognizer-getAngle(): number--><!--Device-RotationRecognizer-getAngle(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 预设旋转手势识别器触发旋转手势最小改变度数阈值，单位为deg。&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;当输入的改变度数的值小于等于0或大于360时，会被转化为默认值，默认值为1。 |

