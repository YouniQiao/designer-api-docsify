# ParticleAttribute

The ParticleAttribute.@extends CommonMethod @interface ParticleAttribute

**Inheritance/Implementation:** ParticleAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ParticleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Add particle attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ParticleAttribute](arkts-arkui-particle-particleattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## disturbanceFields

```TypeScript
default disturbanceFields(fields: Array<DisturbanceFieldOptions> | undefined): this
```

Particle disturbance Field.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[DisturbanceFieldOptions](arkts-arkui-particle-disturbancefieldoptions-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## emitter

```TypeScript
default emitter(value: Array<EmitterProperty> | undefined): this
```

Add particle animation component properties.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[EmitterProperty](arkts-arkui-particle-emitterproperty-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## rippleFields

```TypeScript
default rippleFields(fields: Array<RippleFieldOptions> | undefined): this
```

Set ripple fields of particles. The ripple field applies a force that varies in a wave-like pattern to particles within its influence range, creating an effect similar to the spreading of ripples.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[RippleFieldOptions](arkts-arkui-particle-ripplefieldoptions-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## setParticleOptions

```TypeScript
default setParticleOptions(particles: Particles): this
```

Set Particle options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| particles | [Particles](arkts-arkui-particle-particles-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## velocityFields

```TypeScript
default velocityFields(fields: Array<VelocityFieldOptions> | undefined): this
```

Set velocity fields of particles. The velocity field applies a force to particles within its influence range, causing the particles to superimpose the specified velocity of the field onto their original velocity.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[VelocityFieldOptions](arkts-arkui-particle-velocityfieldoptions-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |
