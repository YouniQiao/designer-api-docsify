# ColumnLayoutAlgorithm

Defines the column layout algorithm.

**Inheritance/Implementation:** ColumnLayoutAlgorithm implements [LayoutAlgorithm](arkts-na-layoutalgorithm-i.md#LayoutAlgorithm)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ColumnLayoutAlgorithm--><!--Device-unnamed-export declare class ColumnLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: ColumnLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)--><!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ColumnLayoutAlgorithmOptions](arkts-na-layoutalgorithm-columnlayoutalgorithmoptions-i.md) | No | set properties of column layout algorithm. |

## alignItems

```TypeScript
@Trace public alignItems?: HorizontalAlign
```

Alignment format of the subassembly in the horizontal direction.

**Type:** [HorizontalAlign](arkts-na-enums-horizontalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

```TypeScript
@Trace public isReverse?: boolean
```

Whether the main axis is reversed.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean--><!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
@Trace public justifyContent?: FlexAlign
```

Alignment mode of the child components along the vertical axis.

**Type:** [FlexAlign](arkts-na-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
@Trace public space?: LengthMetrics
```

Vertical layout element spacing.

**Type:** [LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics--><!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

