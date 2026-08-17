# ParticlePropertyOptions

Defines the particle property Options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface ParticlePropertyOptions--><!--Device-unnamed-export interface ParticlePropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: ParticleTuple<double, double>
```

Initial range, within which the initial value are randomly generated.

**Type:** [ParticleTuple](arkts-na-particletuple-t.md)&lt;double, double&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyOptions-range: ParticleTuple<double, double>--><!--Device-ParticlePropertyOptions-range: ParticleTuple<double, double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updater

```TypeScript
updater?: ParticleUpdaterOptions
```

Particle property updater.

**Type:** [ParticleUpdaterOptions](arkts-na-particle-particleupdateroptions-i.md)

**Default:** {type:UPDATER.NONE;config:undefined}

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyOptions-updater?: ParticleUpdaterOptions--><!--Device-ParticlePropertyOptions-updater?: ParticleUpdaterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

