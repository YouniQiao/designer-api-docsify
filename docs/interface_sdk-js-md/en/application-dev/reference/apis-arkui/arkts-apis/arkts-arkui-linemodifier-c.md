# LineModifier

Defines Line Modifier

@extends LineAttribute @implements AttributeModifier&lt;LineAttribute&gt;

**Inheritance/Implementation:** LineModifier extends [LineAttribute](../arkts-components/arkts-arkui-line-attribute.md#lineattribute) and implements AttributeModifier<LineAttribute>

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(instance: LineAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | [LineAttribute](../arkts-components/arkts-arkui-line-attribute.md) | Yes |  |
