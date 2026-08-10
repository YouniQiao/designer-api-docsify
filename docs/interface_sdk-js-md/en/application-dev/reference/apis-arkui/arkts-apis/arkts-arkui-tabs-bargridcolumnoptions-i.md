# BarGridColumnOptions

TabBar栅格化方式设置的对象，包括栅格模式下的column边距和间隔，以及小、中、大屏下，页签占用的columns数量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface BarGridColumnOptions--><!--Device-unnamed-export interface BarGridColumnOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: Dimension
```

栅格模式下的column间隔（不支持百分比设置）。单位：vp。 默认值： 24。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 24vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-gutter?: Dimension--><!--Device-BarGridColumnOptions-gutter?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lg

```TypeScript
lg?: int
```

大屏下，页签占用的columns数量，必须是非负偶数。大屏为大于等于840vp但小于1024vp。取值范围为全体整数，默认值为-1，代表页签占用TabBar全部宽度。 默认值： -1。

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-lg?: int--><!--Device-BarGridColumnOptions-lg?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: Dimension
```

栅格模式下的column边距（不支持百分比设置）。单位: vp。 默认值： 24。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 24vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-margin?: Dimension--><!--Device-BarGridColumnOptions-margin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## md

```TypeScript
md?: int
```

中屏下，页签占用的columns数量，必须是非负偶数。中屏为大于等于600vp但小于800vp。取值范围为全体整数，默认值为-1，代表页签占用TabBar全部宽度。 默认值： -1。

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-md?: int--><!--Device-BarGridColumnOptions-md?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sm

```TypeScript
sm?: int
```

小屏下，页签占用的columns数量，必须是非负偶数。小屏为大于等于320vp但小于600vp。取值范围为全体整数，默认值为-1，代表页签占用TabBar全部宽度。 默认值： -1。

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarGridColumnOptions-sm?: int--><!--Device-BarGridColumnOptions-sm?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

