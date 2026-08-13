# GridLayoutAlgorithm

Defines the grid layout algorithm.

**Inheritance/Implementation:** GridLayoutAlgorithm implements [LayoutAlgorithm](arkts-na-layoutalgorithm-i.md#LayoutAlgorithm)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-export declare class GridLayoutAlgorithm--><!--Device-unnamed-export declare class GridLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: GridLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)--><!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridLayoutAlgorithmOptions](arkts-na-layoutalgorithm-gridlayoutalgorithmoptions-i.md) | No | set properties of grid layout algorithm. |

## columnsGap

```TypeScript
@Trace public columnsGap?: LengthMetrics
```

The spacing between columns.

**Type:** [LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public columnsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-@Trace public columnsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsTemplate

```TypeScript
@Trace public columnsTemplate?: string | ItemFillPolicy
```

This parameter specifies the number of columns in the current grid layout.

**Type:** string \| [ItemFillPolicy](arkts-na-units-itemfillpolicy-i.md)

**Default:** '1fr'

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public columnsTemplate?: string | ItemFillPolicy--><!--Device-GridLayoutAlgorithm-@Trace public columnsTemplate?: string | ItemFillPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

```TypeScript
@Trace public rowsGap?: LengthMetrics
```

The spacing between rows.

**Type:** [LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-@Trace public rowsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-@Trace public rowsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

