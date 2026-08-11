# RowLayoutAlgorithm

Defines the row layout algorithm.

**Inheritance/Implementation:** RowLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class RowLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class RowLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: RowLayoutAlgorithmOptions)
```

constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)--><!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [RowLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-rowlayoutalgorithmoptions-i.md) | No | set properties of row layout algorithm. |

## alignItems

```TypeScript
public alignItems?: VerticalAlign
```

Sets the alignment format of the subassembly in the vertical direction.

**Type:** [VerticalAlign](arkts-arkui-enums-verticalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign--><!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign-End-->

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

<!--Device-RowLayoutAlgorithm-public isReverse?: boolean--><!--Device-RowLayoutAlgorithm-public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
public justifyContent?: FlexAlign
```

Alignment mode of the child components along the horizontal axis.

**Type:** [FlexAlign](arkts-arkui-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign--><!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
public space?: LengthMetrics
```

Horizontal layout element spacing.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RowLayoutAlgorithm-public space?: LengthMetrics--><!--Device-RowLayoutAlgorithm-public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

