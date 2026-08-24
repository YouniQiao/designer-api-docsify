# ColumnLayoutAlgorithm

Defines the column layout algorithm.@implements LayoutAlgorithm

**Inheritance/Implementation:** ColumnLayoutAlgorithm implements [LayoutAlgorithm](arkts-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ColumnLayoutAlgorithm--><!--Device-unnamed-export declare class ColumnLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: ColumnLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)--><!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ColumnLayoutAlgorithmOptions](arkts-layoutalgorithm-columnlayoutalgorithmoptions-i.md) | No | set properties of column layout algorithm. |

## alignItems

Alignment format of the subassembly in the horizontal direction.

**Type:** [HorizontalAlign](arkts-enums-horizontalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

Whether the main axis is reversed.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean--><!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

Alignment mode of the child components along the vertical axis.

**Type:** [FlexAlign](arkts-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

Vertical layout element spacing.

**Type:** [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics--><!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

