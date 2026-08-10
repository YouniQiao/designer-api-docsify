# ProgressStyleOptions

进度条样式选项。

继承自[CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md)。

**Inheritance/Implementation:** ProgressStyleOptions extends [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface ProgressStyleOptions extends CommonProgressStyleOptions--><!--Device-unnamed-declare interface ProgressStyleOptions extends CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleCount

```TypeScript
scaleCount?: number
```

设置环形进度条总刻度数。

默认值：120 

取值范围：[2, min(width, height)*π/scaleWidth]，超出取值范围时，样式显示为环形无刻度进度条。

在scaleCount和scaleWidth都与默认值相等的情况下，设置组件宽度或高度小于77vp会显示为环形无刻度进度条。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressStyleOptions-scaleCount?: number--><!--Device-ProgressStyleOptions-scaleCount?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleWidth

```TypeScript
scaleWidth?: Length
```

设置环形进度条刻度粗细（不支持百分比设置）。

默认值：2.0vp

取值范围：大于0的数值。

超出取值范围或设置非法值时按默认值处理。

刻度粗细大于进度条宽度时，使用系统默认粗细。

在scaleCount和scaleWidth都与默认值相等的情况下，设置组件宽度或高度小于77vp会显示为环形无刻度进度条。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressStyleOptions-scaleWidth?: Length--><!--Device-ProgressStyleOptions-scaleWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

设置进度条宽度（不支持百分比设置）。

默认值：4.0vp

取值范围：大于0的数值。

超出取值范围或设置非法值时按默认值处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ProgressStyleOptions-strokeWidth?: Length--><!--Device-ProgressStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

