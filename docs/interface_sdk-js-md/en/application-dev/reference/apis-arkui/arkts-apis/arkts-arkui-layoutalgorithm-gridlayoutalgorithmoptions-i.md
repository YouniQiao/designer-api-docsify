# GridLayoutAlgorithmOptions

设置网格布局算法的列数模板、列间距、行间距。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-interface GridLayoutAlgorithmOptions--><!--Device-unnamed-interface GridLayoutAlgorithmOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
columnsGap?: LengthMetrics
```

列与列之间的间距。非法值：按默认值处理。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-GridLayoutAlgorithmOptions-columnsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithmOptions-columnsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsTemplate

```TypeScript
columnsTemplate?: string | ItemFillPolicy
```

设置当前网格布局的列数。非法值：按默认值处理。

**Type:** string \| ItemFillPolicy

**Default:** '1fr'

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-GridLayoutAlgorithmOptions-columnsTemplate?: string | ItemFillPolicy--><!--Device-GridLayoutAlgorithmOptions-columnsTemplate?: string | ItemFillPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

```TypeScript
rowsGap?: LengthMetrics
```

行与行之间的间距。非法值：按默认值处理。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-GridLayoutAlgorithmOptions-rowsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithmOptions-rowsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

