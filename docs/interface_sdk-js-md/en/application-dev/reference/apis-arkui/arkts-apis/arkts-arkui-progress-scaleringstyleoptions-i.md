# ScaleRingStyleOptions

环形有刻度样式选项。

继承自[CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)。

**Inheritance/Implementation:** ScaleRingStyleOptions extends [CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScaleRingStyleOptions extends CommonProgressStyleOptions--><!--Device-unnamed-export declare interface ScaleRingStyleOptions extends CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleCount

```TypeScript
scaleCount?: int
```

设置环形进度条总刻度数。取值范围：[2, min(width, height)/scaleWidth/2/π]。默认值：120。&lt;br&gt;超出取值范围时，样式显示为环形无刻度进度条。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleRingStyleOptions-scaleCount?: int--><!--Device-ScaleRingStyleOptions-scaleCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleWidth

```TypeScript
scaleWidth?: Length
```

设置环形进度条刻度粗细（不支持百分比设置）。刻度粗细大于进度条宽度时，为系统默认粗细。默认值：2vp。

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleRingStyleOptions-scaleWidth?: Length--><!--Device-ScaleRingStyleOptions-scaleWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

设置进度条宽度（不支持百分比设置）。默认值：4vp。

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleRingStyleOptions-strokeWidth?: Length--><!--Device-ScaleRingStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

