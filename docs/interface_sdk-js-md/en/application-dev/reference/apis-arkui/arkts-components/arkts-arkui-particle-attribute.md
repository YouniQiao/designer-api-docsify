# Particle properties/events

Defines the Particle component attribute functions.@extends CommonMethod&lt;ParticleAttribute&gt;

**Inheritance/Implementation:** ParticleAttribute extends CommonMethod<ParticleAttribute>

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## disturbanceFields

```TypeScript
disturbanceFields(fields: Array<DisturbanceFieldOptions>)
```

Sets the disturbance fields.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[DisturbanceFieldOptions](arkts-arkui-disturbancefieldoptions-i.md)&gt; | Yes |

## emitter

```TypeScript
emitter(value: Array<EmitterProperty>)
```

Sets the emitter parameters.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[EmitterProperty](arkts-arkui-emitterproperty-i.md)&gt; | Yes |

## rippleFields

```TypeScript
rippleFields(fields: Array<RippleFieldOptions> | undefined)
```

Sets the particle wave field. The wave field applies a force that changes according to the waveform to particles within the affected range, producing an effect similar to the spreading of ripples.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[RippleFieldOptions](arkts-arkui-ripplefieldoptions-i.md)&gt; \| undefined | Yes |

## velocityFields

```TypeScript
velocityFields(fields: Array<VelocityFieldOptions> | undefined)
```

Sets the particle velocity field. The velocity field applies a force to particles within the affected range, so that the particles move at the velocity specified by the velocity field in addition to their original velocity.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[VelocityFieldOptions](arkts-arkui-velocityfieldoptions-i.md)&gt; \| undefined | Yes |
