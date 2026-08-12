# ColumnLayoutAlgorithm

Defines the column layout algorithm.

**Inheritance/Implementation:** ColumnLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md#LayoutAlgorithm)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ColumnLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class ColumnLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: ColumnLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)--><!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ColumnLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-columnlayoutalgorithmoptions-i.md) | No | set properties of column layout algorithm. |

## alignItems

```TypeScript
public alignItems?: HorizontalAlign
```

Alignment format of the subassembly in the horizontal direction.

**Type:** [HorizontalAlign](arkts-arkui-enums-horizontalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-public alignItems?: HorizontalAlign--><!--Device-ColumnLayoutAlgorithm-public alignItems?: HorizontalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

```TypeScript
public isReverse?: boolean
```

Whether the main axis is reversed.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-public isReverse?: boolean--><!--Device-ColumnLayoutAlgorithm-public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
public justifyContent?: FlexAlign
```

Alignment mode of the child components along the vertical axis.

**Type:** [FlexAlign](arkts-arkui-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-public justifyContent?: FlexAlign--><!--Device-ColumnLayoutAlgorithm-public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
public space?: LengthMetrics
```

Vertical layout element spacing.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-public space?: LengthMetrics--><!--Device-ColumnLayoutAlgorithm-public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

