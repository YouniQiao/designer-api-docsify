# GridLayoutAlgorithm

Defines the grid layout algorithm.

**Inheritance/Implementation:** GridLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class GridLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class GridLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: GridLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)--><!--Device-GridLayoutAlgorithm-constructor(option?: GridLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-gridlayoutalgorithmoptions-i.md) | No | set properties of grid layout algorithm. |

## columnsGap

```TypeScript
public columnsGap?: LengthMetrics
```

The spacing between columns.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-public columnsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-public columnsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsTemplate

```TypeScript
public columnsTemplate?: string | ItemFillPolicy
```

This parameter specifies the number of columns in the current grid layout.

**Type:** string \| ItemFillPolicy

**Default:** '1fr'

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-public columnsTemplate?: string | ItemFillPolicy--><!--Device-GridLayoutAlgorithm-public columnsTemplate?: string | ItemFillPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rowsGap

```TypeScript
public rowsGap?: LengthMetrics
```

The spacing between rows.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridLayoutAlgorithm-public rowsGap?: LengthMetrics--><!--Device-GridLayoutAlgorithm-public rowsGap?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

