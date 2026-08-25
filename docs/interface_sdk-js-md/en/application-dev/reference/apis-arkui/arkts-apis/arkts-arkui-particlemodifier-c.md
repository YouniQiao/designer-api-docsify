# ParticleModifier

Defines Particle Modifier@extends ParticleAttribute @implements AttributeModifier&lt;ParticleAttribute&gt;

**Inheritance/Implementation:** ParticleModifier extends [ParticleAttribute](../arkts-components/arkts-arkui-particle-attribute.md#particleattribute) and implements AttributeModifier<ParticleAttribute>

**Since:** 23

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(particleAttribute: ParticleAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| particleAttribute | [ParticleAttribute](../arkts-components/arkts-arkui-particle-attribute.md) | Yes |
