# TapRecognizer

点击手势识别器对象，继承自[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。

**Inheritance/Implementation:** TapRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare class TapRecognizer extends GestureRecognizer--><!--Device-unnamed-declare class TapRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getTapCount

```TypeScript
getTapCount(): number
```

返回预设点击手势识别器连续点击次数阈值。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TapRecognizer-getTapCount(): number--><!--Device-TapRecognizer-getTapCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 预设点击手势识别器连续点击次数阈值。&lt;br/&gt;取值范围：[0, +∞) |

