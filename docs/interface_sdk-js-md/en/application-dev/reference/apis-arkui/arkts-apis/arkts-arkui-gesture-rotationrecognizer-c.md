# RotationRecognizer

旋转手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。

**Inheritance/Implementation:** RotationRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RotationRecognizer extends GestureRecognizer--><!--Device-unnamed-export declare class RotationRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAngle

```TypeScript
getAngle(): double
```

返回预设旋转手势识别器触发旋转手势最小改变度数阈值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationRecognizer-getAngle(): double--><!--Device-RotationRecognizer-getAngle(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | 预设旋转手势识别器触发旋转手势最小改变度数阈值，单位为deg。&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;当输入的改变度数的值小于等于0或大于360时，会被转化为默认值，默认值为1。 |

