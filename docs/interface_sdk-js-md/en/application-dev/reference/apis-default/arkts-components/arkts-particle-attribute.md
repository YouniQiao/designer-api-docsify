# ParticleAttribute

The ParticleAttribute.

@extends CommonMethod @interface ParticleAttribute

**Inheritance/Implementation:** ParticleAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ParticleAttribute--><!--Device-unnamed-export declare interface ParticleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ParticleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-attributeModifier(modifier: AttributeModifier<ParticleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ParticleAttribute-attributeModifier(modifier: AttributeModifier<ParticleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ParticleAttribute](arkts-particle-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## disturbanceFields

```TypeScript
disturbanceFields(fields: Array<DisturbanceFieldOptions> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-disturbanceFields(fields: Array<DisturbanceFieldOptions> | undefined): this--><!--Device-ParticleAttribute-disturbanceFields(fields: Array<DisturbanceFieldOptions> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fields | Array&lt;[DisturbanceFieldOptions](arkts-particle-disturbancefieldoptions-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## emitter

```TypeScript
emitter(value: Array<EmitterProperty> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-emitter(value: Array<EmitterProperty> | undefined): this--><!--Device-ParticleAttribute-emitter(value: Array<EmitterProperty> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[EmitterProperty](arkts-particle-emitterproperty-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## rippleFields

```TypeScript
rippleFields(fields: Array<RippleFieldOptions> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-rippleFields(fields: Array<RippleFieldOptions> | undefined): this--><!--Device-ParticleAttribute-rippleFields(fields: Array<RippleFieldOptions> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fields | Array&lt;[RippleFieldOptions](arkts-particle-ripplefieldoptions-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setParticleOptions

```TypeScript
setParticleOptions(particles: Particles): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-setParticleOptions(particles: Particles): this--><!--Device-ParticleAttribute-setParticleOptions(particles: Particles): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| particles | [Particles](arkts-particle-particles-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## velocityFields

```TypeScript
velocityFields(fields: Array<VelocityFieldOptions> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ParticleAttribute-velocityFields(fields: Array<VelocityFieldOptions> | undefined): this--><!--Device-ParticleAttribute-velocityFields(fields: Array<VelocityFieldOptions> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fields | Array&lt;[VelocityFieldOptions](arkts-particle-velocityfieldoptions-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set velocity fields of particles. The velocity field applies a force to particles within its influence range, causing the particles to superimpose the specified velocity of the field onto their original velocity.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleAttribute-default--><!--Device-ParticleAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

