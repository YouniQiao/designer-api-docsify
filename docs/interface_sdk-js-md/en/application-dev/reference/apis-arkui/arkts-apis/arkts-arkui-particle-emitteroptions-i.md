# EmitterOptions

Defines the emitter Options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface EmitterOptions--><!--Device-unnamed-export interface EmitterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## annulusRegion

```TypeScript
annulusRegion?: ParticleAnnulusRegion
```

the description of the annulus region. This parameter is valid only for emitter whose shape is annulus.

**Type:** [ParticleAnnulusRegion](../arkts-components/arkts-arkui-particleannulusregion-i.md)

**Default:** {innerRadius:LengthMetrics.vp(0),outerRadius:LengthMetrics.vp(0)}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-annulusRegion?: ParticleAnnulusRegion--><!--Device-EmitterOptions-annulusRegion?: ParticleAnnulusRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## emitRate

```TypeScript
emitRate?: int
```

Emitting rate, that is, the number of particles produced per second.

**Type:** int

**Default:** 5

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-emitRate?: int--><!--Device-EmitterOptions-emitRate?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## particle

```TypeScript
particle: EmitterParticleOptions
```

Set particle config.

**Type:** [EmitterParticleOptions](../arkts-components/arkts-arkui-emitterparticleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-particle: EmitterParticleOptions--><!--Device-EmitterOptions-particle: EmitterParticleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: ParticleTuple<Dimension, Dimension>
```

Position of emitter.The first element means X-axis location.The second element means the Y-axis location.

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;[Dimension](arkts-arkui-dimension-t.md), [Dimension](arkts-arkui-dimension-t.md)&gt;

**Default:** [0,0]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-position?: ParticleTuple<Dimension, Dimension>--><!--Device-EmitterOptions-position?: ParticleTuple<Dimension, Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: ParticleEmitterShape
```

Shape of emitter.

**Type:** [ParticleEmitterShape](../arkts-components/arkts-arkui-particleemittershape-e.md)

**Default:** ParticleEmitterShape.RECTANGLE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-shape?: ParticleEmitterShape--><!--Device-EmitterOptions-shape?: ParticleEmitterShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: ParticleTuple<Dimension, Dimension>
```

Size of emitter.The first element means emitter width.The second element means emitter height.

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;[Dimension](arkts-arkui-dimension-t.md), [Dimension](arkts-arkui-dimension-t.md)&gt;

**Default:** ['100%','100%']

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmitterOptions-size?: ParticleTuple<Dimension, Dimension>--><!--Device-EmitterOptions-size?: ParticleTuple<Dimension, Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

