# RowLayoutAlgorithm

Defines the row layout algorithm.@implements LayoutAlgorithm

**Inheritance/Implementation:** RowLayoutAlgorithm implements [LayoutAlgorithm](arkts-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class RowLayoutAlgorithm--><!--Device-unnamed-export declare class RowLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: RowLayoutAlgorithmOptions)
```

constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)--><!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [RowLayoutAlgorithmOptions](arkts-layoutalgorithm-rowlayoutalgorithmoptions-i.md) | No | set properties of row layout algorithm. |

## alignItems

Sets the alignment format of the subassembly in the vertical direction.

**Type:** [VerticalAlign](arkts-enums-verticalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-@Trace public alignItems?: VerticalAlign--><!--Device-RowLayoutAlgorithm-@Trace public alignItems?: VerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

Whether the main axis is reversed.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-@Trace public isReverse?: boolean--><!--Device-RowLayoutAlgorithm-@Trace public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

Alignment mode of the child components along the horizontal axis.

**Type:** [FlexAlign](arkts-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-@Trace public justifyContent?: FlexAlign--><!--Device-RowLayoutAlgorithm-@Trace public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

Horizontal layout element spacing.

**Type:** [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-@Trace public space?: LengthMetrics--><!--Device-RowLayoutAlgorithm-@Trace public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

