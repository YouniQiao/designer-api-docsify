# ColumnModifier

Defines Column Modifier

@extends ColumnAttribute @implements AttributeModifier&lt;ColumnAttribute&gt;

**Inheritance/Implementation:** ColumnModifier extends [ColumnAttribute](../arkts-components/arkts-arkui-column-attribute.md#columnattribute) and implements AttributeModifier<ColumnAttribute>

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(instance: ColumnAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | [ColumnAttribute](../arkts-components/arkts-arkui-column-attribute.md) | Yes |  |
