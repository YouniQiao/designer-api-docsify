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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| particles | [Particles](arkts-arkui-particles-i.md)&lt;PARTICLE, COLOR_UPDATER, OPACITY_UPDATER, SCALE_UPDATER, ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER, SPIN_UPDATER&gt; | Yes | Array of particles. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AccelerationOptions](arkts-arkui-accelerationoptions-i.md) | Particle acceleration. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the > outer element's @since version number is higher than inner elements'. This does not affect interface usability. |
| [DisturbanceFieldOptions](arkts-arkui-disturbancefieldoptions-i.md) | Defines particle disturbance Field params. |
| [EmitterOptions](arkts-arkui-emitteroptions-i.md) | Particle emitter configuration. |
| [EmitterParticleOptions](arkts-arkui-emitterparticleoptions-i.md) | Defines parameters of particles used by emitters. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [EmitterProperty](arkts-arkui-emitterproperty-i.md) | Defines the emitter property. |
| [FieldRegion](arkts-arkui-fieldregion-i.md) | Defines the area information of the particle field. |
| [ImageParticleParameters](arkts-arkui-imageparticleparameters-i.md) | Defines the parameters for an image-like particle. |
| [ParticleAnnulusRegion](arkts-arkui-particleannulusregion-i.md) | Configures the annular emitter area. > **NOTE：**> > - If the value of outerRadius or innerRadius is less than 0 or uses the percentage unit, the value is considered as > 0. > > - If the value of outerRadius is less than that of innerRadius, the smaller value is used as the new inner radius > and the larger value is used as the new outer radius. > > - If the value of endAngle is less than that of startAngle, the smaller value is used as the new start angle and > the larger value is used as the new end angle. > >  |
| [ParticleColorOptions](arkts-arkui-particlecoloroptions-i.md) | The color changes randomly, with the per-second change difference being a value randomly generated from the range. The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [ParticleColorPropertyOptions](arkts-arkui-particlecolorpropertyoptions-i.md) | Defines the particle color property updater configs which can support generics. |
| [ParticleColorPropertyUpdaterConfigs](arkts-arkui-particlecolorpropertyupdaterconfigs-i.md) | Defines the particle color property updater configs. |
| [ParticleColorUpdaterOptions](arkts-arkui-particlecolorupdateroptions-i.md) | How the color property is updated. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [ParticleConfigs](arkts-arkui-particleconfigs-i.md) | Defines the particle configs. |
| [ParticleOptions](arkts-arkui-particleoptions-i.md) | Defines the ParticleOptions Interface. |
| [ParticlePropertyAnimation](arkts-arkui-particlepropertyanimation-i.md) | Defines the particle property lifecycle. |
| [ParticlePropertyOptions](arkts-arkui-particlepropertyoptions-i.md) | Defines the particle property Options. |
| [ParticlePropertyUpdaterConfigs](arkts-arkui-particlepropertyupdaterconfigs-i.md) | Defines the particle property updater configs. |
| [Particles](arkts-arkui-particles-i.md) | Defines the particle array. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [ParticleUpdaterOptions](arkts-arkui-particleupdateroptions-i.md) | Defines the particle updater options. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [PointParticleParameters](arkts-arkui-pointparticleparameters-i.md) | Defines the parameters for a point-like particle. |
| [RippleFieldOptions](arkts-arkui-ripplefieldoptions-i.md) | Defines ripple field options. |
| [VelocityFieldOptions](arkts-arkui-velocityfieldoptions-i.md) | Parameter used to describe the velocity field of particles. |
| [VelocityOptions](arkts-arkui-velocityoptions-i.md) | Defines velocity options. * > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer > element's @since version number is higher than inner elements'. This does not affect interface usability. |

### Types

| Name | Description |
| --- | --- |
| [ParticleTuple](arkts-arkui-particletuple-t.md) | Defines a pair of given type for particle. |
| [PositionT](arkts-arkui-positiont-t.md) | Defines the PositionT type. |
| [SizeT](arkts-arkui-sizet-t.md) | Defines the SizeT type. |
| [Vector2T](arkts-arkui-vector2t-t.md) | Defines the Vector2T type. The Vector2T type contains two attribute values: x and y. |

### Enums

| Name | Description |
| --- | --- |
| [DistributionType](arkts-arkui-distributiontype-e.md) | Enumerates the color distribution types of a particle. |
| [DisturbanceFieldShape](arkts-arkui-disturbancefieldshape-e.md) | Defines particle disturbance shape. |
| [ParticleEmitterShape](arkts-arkui-particleemittershape-e.md) | Enumerates the emitter shapes of a particle. |
| [ParticleType](arkts-arkui-particletype-e.md) | Enumerates the particle types. |
| [ParticleUpdater](arkts-arkui-particleupdater-e.md) | Enumerates the updater types of a particle. |

