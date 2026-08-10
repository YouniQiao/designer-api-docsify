# LinearGradientBlurOptions

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface LinearGradientBlurOptions--><!--Device-unnamed-declare interface LinearGradientBlurOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: GradientDirection
```

渐变模糊方向。

默认值：

GradientDirection.Bottom

**Type:** [GradientDirection](../arkts-apis/arkts-arkui-gradientdirection-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinearGradientBlurOptions-direction: GradientDirection--><!--Device-LinearGradientBlurOptions-direction: GradientDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fractionStops

```TypeScript
fractionStops: FractionStop[]
```

数组中保存的每一个二元数组（取值0-1，小于0则为0，大于1则为1）表示[模糊程度, 模糊位置]；模糊位置需严格递增，开发者传入的数据不符合规范会记录日志，渐变模糊数组中二元数组个数必须大于等于2，否则渐变模糊不生效。

**Type:** [FractionStop](arkts-arkui-fractionstop-t.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LinearGradientBlurOptions-fractionStops: FractionStop[]--><!--Device-LinearGradientBlurOptions-fractionStops: FractionStop[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

