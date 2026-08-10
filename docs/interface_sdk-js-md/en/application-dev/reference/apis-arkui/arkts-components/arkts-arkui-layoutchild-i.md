# LayoutChild

布局和测量发生时，框架传递给子组件的信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

<!--Device-unnamed-declare interface LayoutChild--><!--Device-unnamed-declare interface LayoutChild-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layout

```TypeScript
layout(childLayoutInfo: LayoutInfo)
```

在 onLayout 回调中调用此布局方法，将布局信息分配给子组件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-layout(childLayoutInfo: LayoutInfo)--><!--Device-LayoutChild-layout(childLayoutInfo: LayoutInfo)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| childLayoutInfo | [LayoutInfo](arkts-arkui-layoutinfo-i.md) | Yes |  |

## measure

```TypeScript
measure(childConstraint: ConstraintSizeOptions)
```

在 onMeasure 回调中调用此 measure 方法以提供子组件的尺寸。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-measure(childConstraint: ConstraintSizeOptions)--><!--Device-LayoutChild-measure(childConstraint: ConstraintSizeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| childConstraint | [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | Yes |  |

## borderInfo

```TypeScript
borderInfo: LayoutBorderInfo
```

子组件边框信息

**Type:** [LayoutBorderInfo](arkts-arkui-layoutborderinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-borderInfo: LayoutBorderInfo--><!--Device-LayoutChild-borderInfo: LayoutBorderInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constraint

```TypeScript
constraint: ConstraintSizeOptions
```

子组件约束

**Type:** [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-constraint: ConstraintSizeOptions--><!--Device-LayoutChild-constraint: ConstraintSizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string
```

子组件id

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-id: string--><!--Device-LayoutChild-id: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

子组件名字

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-name: string--><!--Device-LayoutChild-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position: Position
```

子组件位置信息

**Type:** [Position](../arkts-apis/arkts-arkui-position-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** Measurable/Layoutable

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LayoutChild-position: Position--><!--Device-LayoutChild-position: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

