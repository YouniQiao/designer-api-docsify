# TapRecognizer

点击手势识别器对象，继承自[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。

**Inheritance/Implementation:** TapRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapRecognizer extends GestureRecognizer--><!--Device-unnamed-export declare class TapRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getTapCount

```TypeScript
getTapCount(): int
```

返回预设点击手势识别器连续点击次数阈值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapRecognizer-getTapCount(): int--><!--Device-TapRecognizer-getTapCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | 预设点击手势识别器连续点击次数阈值。&lt;br/&gt;取值范围：[0, +∞) |

