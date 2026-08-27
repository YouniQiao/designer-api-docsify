# PathModifier

Defines Path Modifier

@extends PathAttribute @implements AttributeModifier&lt;PathAttribute&gt;

**Inheritance/Implementation:** PathModifier extends [PathAttribute](../arkts-components/arkts-arkui-path-attribute.md#pathattribute) and implements AttributeModifier<PathAttribute>

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(instance: PathAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | [PathAttribute](../arkts-components/arkts-arkui-path-attribute.md) | Yes |  |
