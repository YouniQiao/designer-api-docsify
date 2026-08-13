# Layoutable

Provides the child component layout information.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare interface Layoutable--><!--Device-unnamed-declare interface Layoutable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getBorderWidth

```TypeScript
getBorderWidth() : DirectionalEdgesT<number>
```

Obtains the border widths of the child component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Layoutable-getBorderWidth() : DirectionalEdgesT<number>--><!--Device-Layoutable-getBorderWidth() : DirectionalEdgesT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DirectionalEdgesT](../arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;number&gt; |

## getMargin

```TypeScript
getMargin() : DirectionalEdgesT<number>
```

Obtains the margin values of the child component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Layoutable-getMargin() : DirectionalEdgesT<number>--><!--Device-Layoutable-getMargin() : DirectionalEdgesT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DirectionalEdgesT](../arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;number&gt; |

## getPadding

```TypeScript
getPadding() : DirectionalEdgesT<number>
```

Obtains the padding values of the child component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Layoutable-getPadding() : DirectionalEdgesT<number>--><!--Device-Layoutable-getPadding() : DirectionalEdgesT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DirectionalEdgesT](../arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;number&gt; |

## layout

```TypeScript
layout(position: Position): void
```

Applies the specified position constraints to the child component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Layoutable-layout(position: Position): void--><!--Device-Layoutable-layout(position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Position](../arkts-apis/arkts-arkui-display-position-i.md) | Yes |

## measureResult

```TypeScript
measureResult: MeasureResult
```

Measurement result of the child component. Unit: vp.

**Type:** [MeasureResult](arkts-arkui-measureresult-i.md)

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Layoutable-measureResult: MeasureResult--><!--Device-Layoutable-measureResult: MeasureResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uniqueId

```TypeScript
uniqueId?: number
```

Unique ID that the system assigns to the child component. The value must be an integer greater than or equal to 0.

**Type:** number

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Layoutable-uniqueId?: number--><!--Device-Layoutable-uniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
