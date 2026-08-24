# ColumnLayoutAlgorithm

Vertical linear layout algorithm class.

> **NOTE：**&gt;
> The object of the **ColumnLayoutAlgorithm** class can be assigned to a variable of the **LayoutAlgorithm** type as
> the input parameter of the
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md) component to specify the
> layout algorithm.

**Inheritance/Implementation:** ColumnLayoutAlgorithm implements [LayoutAlgorithm](../../apis-default/arkts-apis/arkts-layoutalgorithm-i.md)

**Since:** 24

**Decorator:** @ObservedV2

<!--Device-unnamed-export class ColumnLayoutAlgorithm--><!--Device-unnamed-export class ColumnLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: ColumnLayoutAlgorithmOptions)
```

Constructs the vertical linear layout algorithm class.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)--><!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ColumnLayoutAlgorithmOptions](../../apis-default/arkts-apis/arkts-layoutalgorithm-columnlayoutalgorithmoptions-i.md) | No | Input parameters for constructing the vertical linear layout algorithm, which are used to set the spacing, main axis alignment method, cross axis alignment method, and main axis arrangement direction of the layout algorithm. |

## alignItems

Horizontal alignment mode of all child components.Default value: **HorizontalAlign.Center**Invalid values are treated as the default value.

**Type:** [HorizontalAlign](../../apis-default/arkts-apis/arkts-enums-horizontalalign-e.md)

**Since:** 24

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public alignItems?: HorizontalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

Whether to reverse the vertical arrangement of child components. **true** indicates to reverse the vertical arrangement of child components. **false** indicates to arrange child components in the vertical direction in normal order.Default value: **false**Invalid values are treated as the default value.

**Type:** boolean

**Since:** 24

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean--><!--Device-ColumnLayoutAlgorithm-@Trace public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

Vertical alignment mode of all child components.Default value: **FlexAlign.Start**Invalid values are treated as the default value.

**Type:** [FlexAlign](../../apis-default/arkts-apis/arkts-enums-flexalign-e.md)

**Since:** 24

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign--><!--Device-ColumnLayoutAlgorithm-@Trace public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

Vertical spacing between elements in a vertical layout.Default value: **LengthMetrics.vp(0)**Invalid values are treated as the default value.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics--><!--Device-ColumnLayoutAlgorithm-@Trace public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

