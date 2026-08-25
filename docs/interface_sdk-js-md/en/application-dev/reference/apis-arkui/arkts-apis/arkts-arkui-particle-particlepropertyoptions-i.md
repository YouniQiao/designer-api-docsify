# ParticlePropertyOptions

Defines the particle property Options. @interface ParticlePropertyOptions

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: ParticleTuple<double, double>
```

Initial range, within which the initial value are randomly generated.

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;double, double&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updater

```TypeScript
updater?: ParticleUpdaterOptions
```

Particle property updater.

**Type:** [ParticleUpdaterOptions](arkts-arkui-particle-particleupdateroptions-i.md)

**Default:** {type:UPDATER.NONE;config:undefined}

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
