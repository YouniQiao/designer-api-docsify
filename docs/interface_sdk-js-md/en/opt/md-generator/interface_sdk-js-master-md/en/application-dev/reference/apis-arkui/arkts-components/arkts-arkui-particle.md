# Particle

Defines Particle Component.

## Particle

```TypeScript
Particle(particles: Particles<
      PARTICLE,
      COLOR_UPDATER,
      OPACITY_UPDATER,
      SCALE_UPDATER,
      ACC_SPEED_UPDATER,
      ACC_ANGLE_UPDATER,
      SPIN_UPDATER
    >)
```

create a particle array. Anonymous Object Rectification.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticleInterface-<    PARTICLE extends ParticleType,    COLOR_UPDATER extends ParticleUpdater,    OPACITY_UPDATER extends ParticleUpdater,    SCALE_UPDATER extends ParticleUpdater,    ACC_SPEED_UPDATER extends ParticleUpdater,    ACC_ANGLE_UPDATER extends ParticleUpdater,    SPIN_UPDATER extends ParticleUpdater  >(particles: Particles<      PARTICLE,      COLOR_UPDATER,      OPACITY_UPDATER,      SCALE_UPDATER,      ACC_SPEED_UPDATER,      ACC_ANGLE_UPDATER,      SPIN_UPDATER    >): ParticleAttribute--><!--Device-ParticleInterface-<    PARTICLE extends ParticleType,    COLOR_UPDATER extends ParticleUpdater,    OPACITY_UPDATER extends ParticleUpdater,    SCALE_UPDATER extends ParticleUpdater,    ACC_SPEED_UPDATER extends ParticleUpdater,    ACC_ANGLE_UPDATER extends ParticleUpdater,    SPIN_UPDATER extends ParticleUpdater  >(particles: Particles<      PARTICLE,      COLOR_UPDATER,      OPACITY_UPDATER,      SCALE_UPDATER,      ACC_SPEED_UPDATER,      ACC_ANGLE_UPDATER,      SPIN_UPDATER    >): ParticleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| particles | [Particles](arkts-arkui-particles-i.md)&lt;PARTICLE, COLOR_UPDATER, OPACITY_UPDATER, SCALE_UPDATER, ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER, SPIN_UPDATER&gt; | Yes |

## Summary

- [AccelerationOptions](arkts-arkui-accelerationoptions-i.md)
- [DisturbanceFieldOptions](arkts-arkui-disturbancefieldoptions-i.md)
- [EmitterOptions](arkts-arkui-emitteroptions-i.md)
- [EmitterParticleOptions](arkts-arkui-emitterparticleoptions-i.md)
- [EmitterProperty](arkts-arkui-emitterproperty-i.md)
- [FieldRegion](arkts-arkui-fieldregion-i.md)
- [ImageParticleParameters](arkts-arkui-imageparticleparameters-i.md)
- [ParticleAnnulusRegion](arkts-arkui-particleannulusregion-i.md)
- [ParticleColorOptions](arkts-arkui-particlecoloroptions-i.md)
- [ParticleColorPropertyOptions](arkts-arkui-particlecolorpropertyoptions-i.md)
- [ParticleColorPropertyUpdaterConfigs](arkts-arkui-particlecolorpropertyupdaterconfigs-i.md)
- [ParticleColorUpdaterOptions](arkts-arkui-particlecolorupdateroptions-i.md)
- [ParticleConfigs](arkts-arkui-particleconfigs-i.md)
- [ParticleOptions](arkts-arkui-particleoptions-i.md)
- [ParticlePropertyAnimation](arkts-arkui-particlepropertyanimation-i.md)
- [ParticlePropertyOptions](arkts-arkui-particlepropertyoptions-i.md)
- [ParticlePropertyUpdaterConfigs](arkts-arkui-particlepropertyupdaterconfigs-i.md)
- [Particles](arkts-arkui-particles-i.md)
- [ParticleUpdaterOptions](arkts-arkui-particleupdateroptions-i.md)
- [PointParticleParameters](arkts-arkui-pointparticleparameters-i.md)
- [RippleFieldOptions](arkts-arkui-ripplefieldoptions-i.md)
- [VelocityFieldOptions](arkts-arkui-velocityfieldoptions-i.md)
- [VelocityOptions](arkts-arkui-velocityoptions-i.md)
- [ParticleTuple](arkts-arkui-particletuple-t.md)
- [PositionT](arkts-arkui-positiont-t.md)
- [SizeT](arkts-arkui-sizet-t.md)
- [Vector2T](arkts-arkui-vector2t-t.md)
- [DistributionType](arkts-arkui-distributiontype-e.md)
- [DisturbanceFieldShape](arkts-arkui-disturbancefieldshape-e.md)
- [ParticleEmitterShape](arkts-arkui-particleemittershape-e.md)
- [ParticleType](arkts-arkui-particletype-e.md)
- [ParticleUpdater](arkts-arkui-particleupdater-e.md)
