# ParticleColorPropertyOptions

Defines the particle color property updater.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface ParticleColorPropertyOptions--><!--Device-unnamed-export interface ParticleColorPropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distributionType

```TypeScript
distributionType?: DistributionType
```

Distribution type of particle color.

**Type:** [DistributionType](arkts-na-particle-distributiontype-e.md)

**Default:** DistributionType.UNIFORM

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleColorPropertyOptions-distributionType?: DistributionType--><!--Device-ParticleColorPropertyOptions-distributionType?: DistributionType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: ParticleTuple<ResourceColor, ResourceColor>
```

Initial color range, within which the initial color is randomly generated.

**Type:** [ParticleTuple](arkts-na-particletuple-t.md)&lt;[ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md), [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleColorPropertyOptions-range: ParticleTuple<ResourceColor, ResourceColor>--><!--Device-ParticleColorPropertyOptions-range: ParticleTuple<ResourceColor, ResourceColor>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updater

```TypeScript
updater?: ParticleColorUpdaterOptions
```

Particle color property updater.

**Type:** [ParticleColorUpdaterOptions](arkts-na-particle-particlecolorupdateroptions-i.md)

**Default:** {type:UPDATER.NONE;config:undefined}

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleColorPropertyOptions-updater?: ParticleColorUpdaterOptions--><!--Device-ParticleColorPropertyOptions-updater?: ParticleColorUpdaterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

