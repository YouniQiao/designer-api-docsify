# ParticleColorPropertyOptions

Defines the particle color property updater. @interface ParticleColorPropertyOptions

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distributionType

```TypeScript
distributionType?: DistributionType
```

Distribution type of particle color.

**Type:** [DistributionType](arkts-arkui-particle-distributiontype-e.md)

**Default:** DistributionType.UNIFORM

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: ParticleTuple<ResourceColor, ResourceColor>
```

Initial color range, within which the initial color is randomly generated.

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md), [ResourceColor](arkts-arkui-resourcecolor-t.md)&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updater

```TypeScript
updater?: ParticleColorUpdaterOptions
```

Particle color property updater.

**Type:** [ParticleColorUpdaterOptions](arkts-arkui-particle-particlecolorupdateroptions-i.md)

**Default:** {type:UPDATER.NONE;config:undefined}

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
