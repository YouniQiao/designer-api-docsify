# PinchRecognizer

捏合手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。

**Inheritance/Implementation:** PinchRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PinchRecognizer extends GestureRecognizer--><!--Device-unnamed-export declare class PinchRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDistance

```TypeScript
getDistance(): double
```

返回预设捏合手势识别器最小识别距离阈值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchRecognizer-getDistance(): double--><!--Device-PinchRecognizer-getDistance(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | 预设捏合手势识别器最小识别距离阈值，单位为vp。&lt;br/&gt;取值范围：[0, +∞) |

