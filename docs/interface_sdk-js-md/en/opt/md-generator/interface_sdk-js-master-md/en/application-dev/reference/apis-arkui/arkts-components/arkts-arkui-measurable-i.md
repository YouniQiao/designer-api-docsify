# Measurable

Provides the child component position information.

**Since:** 10

<!--Device-unnamed-declare interface Measurable--><!--Device-unnamed-declare interface Measurable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getBorderWidth

```TypeScript
getBorderWidth() : DirectionalEdgesT<number>
```

Obtains the border widths of the child component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Measurable-getBorderWidth() : DirectionalEdgesT<number>--><!--Device-Measurable-getBorderWidth() : DirectionalEdgesT<number>-End-->

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Measurable-getMargin() : DirectionalEdgesT<number>--><!--Device-Measurable-getMargin() : DirectionalEdgesT<number>-End-->

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Measurable-getPadding() : DirectionalEdgesT<number>--><!--Device-Measurable-getPadding() : DirectionalEdgesT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DirectionalEdgesT](../arkts-apis/arkts-arkui-directionaledgest-i.md)&lt;number&gt; |

## measure

```TypeScript
measure(constraint: ConstraintSizeOptions) : MeasureResult
```

Imposes size constraints on the child component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Measurable-measure(constraint: ConstraintSizeOptions) : MeasureResult--><!--Device-Measurable-measure(constraint: ConstraintSizeOptions) : MeasureResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| constraint | [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MeasureResult](arkts-arkui-measureresult-i.md) |

## uniqueId

```TypeScript
uniqueId?: number
```

Unique ID that the system assigns to the child component. The value range is all integers.

**Type:** number

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Measurable-uniqueId?: number--><!--Device-Measurable-uniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
