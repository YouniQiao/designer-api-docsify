# RatingModifier

Defines Rating Modifier

@extends RatingAttribute @implements AttributeModifier&lt;RatingAttribute&gt;

**Inheritance/Implementation:** RatingModifier extends [RatingAttribute](../arkts-components/arkts-arkui-rating-attribute.md#ratingattribute) and implements AttributeModifier<RatingAttribute>

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(instance: RatingAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | [RatingAttribute](../arkts-components/arkts-arkui-rating-attribute.md) | Yes |  |
