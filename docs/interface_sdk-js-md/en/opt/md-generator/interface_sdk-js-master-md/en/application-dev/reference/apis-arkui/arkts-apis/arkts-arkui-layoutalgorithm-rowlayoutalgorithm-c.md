# RowLayoutAlgorithm

Horizontal linear layout algorithm class.

> **NOTE：**
> 
> The object of the **RowLayoutAlgorithm** class can be assigned to a variable of the **LayoutAlgorithm** type as the
> input parameter of the
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md) component to specify the
> layout algorithm.

**Inheritance/Implementation:** RowLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md#LayoutAlgorithm)

**Since:** 24

**Decorator:** @ObservedV2

<!--Device-unnamed-export class RowLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export class RowLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: RowLayoutAlgorithmOptions)
```

Constructs the horizontal linear layout algorithm class.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)--><!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [RowLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-rowlayoutalgorithmoptions-i.md) | No |

## alignItems

```TypeScript
public alignItems?: VerticalAlign
```

Vertical alignment mode of all child components.

Default value: **VerticalAlign.Center**

Invalid values are treated as the default value.

**Type:** [VerticalAlign](arkts-arkui-verticalalign-e.md)

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign--><!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

```TypeScript
public isReverse?: boolean
```

Whether to reverse the horizontal arrangement of child components. **true** indicates to reverse the horizontal arrangement of child components. The horizontal direction is affected by the common attribute  
[direction](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-location.md#direction). If the  
[direction](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-location.md#direction) attribute takes effect, the arrangement is reversed again. **false** indicates to arrange child components in the horizontal direction in normal order.

Default value: **false**

Invalid values are treated as the default value.

**Type:** boolean

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-RowLayoutAlgorithm-public isReverse?: boolean--><!--Device-RowLayoutAlgorithm-public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
public justifyContent?: FlexAlign
```

Horizontal alignment mode of all child components.

Default value: **FlexAlign.Start**

Invalid values are treated as the default value.

**Type:** [FlexAlign](arkts-arkui-flexalign-e.md)

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign--><!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
public space?: LengthMetrics
```

Horizontal spacing between elements in a horizontal layout.

Default value: **LengthMetrics.vp(0)**

Invalid values are treated as the default value.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-RowLayoutAlgorithm-public space?: LengthMetrics--><!--Device-RowLayoutAlgorithm-public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
