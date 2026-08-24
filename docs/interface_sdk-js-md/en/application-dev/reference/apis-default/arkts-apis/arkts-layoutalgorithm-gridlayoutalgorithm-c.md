# GridLayoutAlgorithm

Defines the grid layout algorithm.@implements LayoutAlgorithm

**Inheritance/Implementation:** GridLayoutAlgorithm implements [LayoutAlgorithm](arkts-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class GridLayoutAlgorithm--><!--Device-unnamed-export declare class GridLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: GridLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)--><!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridLayoutAlgorithmOptions](arkts-layoutalgorithm-gridlayoutalgorithmoptions-i.md) | No | set properties of grid layout algorithm. |

## columnsGap

The spacing between columns.

**Type:** [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public columnsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-@Trace public columnsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsTemplate

This parameter specifies the number of columns in the current grid layout.

**Type:** string \| [ItemFillPolicy](arkts-units-itemfillpolicy-i.md)

**Default:** '1fr'

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public columnsTemplate?: string | ItemFillPolicy--><!--Device-GridLayoutAlgorithm-@Trace public columnsTemplate?: string | ItemFillPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

The spacing between rows.

**Type:** [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public rowsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-@Trace public rowsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

