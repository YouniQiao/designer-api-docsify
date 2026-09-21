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

create a particle array.

Anonymous Object Rectification.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| particles | [Particles](arkts-arkui-particle-comp-particles-i.md)&lt;PARTICLE, COLOR_UPDATER, OPACITY_UPDATER, SCALE_UPDATER, ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER, SPIN_UPDATER&gt; | Yes | Array of particles. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AccelerationOptions](arkts-arkui-particle-comp-accelerationoptions-i.md) | Particle acceleration. |
| [DisturbanceFieldOptions](arkts-arkui-particle-comp-disturbancefieldoptions-i.md) | Defines particle disturbance Field params. |
| [EmitterOptions](arkts-arkui-particle-comp-emitteroptions-i.md) | Particle emitter configuration. |
| [EmitterParticleOptions](arkts-arkui-particle-comp-emitterparticleoptions-i.md) | Defines parameters of particles used by emitters. |
| [EmitterProperty](arkts-arkui-particle-comp-emitterproperty-i.md) | Defines the emitter property. |
| [FieldRegion](arkts-arkui-particle-comp-fieldregion-i.md) | Defines the area information of the particle field. |
| [ImageParticleParameters](arkts-arkui-particle-comp-imageparticleparameters-i.md) | Defines the parameters for an image-like particle. @interface ImageParticleParameters |
| [ParticleAnnulusRegion](arkts-arkui-particle-comp-particleannulusregion-i.md) | Configures the annular emitter area. |
| [ParticleColorOptions](arkts-arkui-particle-comp-particlecoloroptions-i.md) | The color changes randomly, with the per-second change difference being a value randomly generated from the range. The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels. |
| [ParticleColorPropertyOptions](arkts-arkui-particle-comp-particlecolorpropertyoptions-i.md) | Defines the particle color property updater configs which can support generics. @interface ParticleColorPropertyOptions |
| [ParticleColorPropertyUpdaterConfigs](arkts-arkui-particle-comp-particlecolorpropertyupdaterconfigs-i.md) | Defines the particle color property updater configs. @interface ParticleColorPropertyUpdaterConfigs |
| [ParticleColorUpdaterOptions](arkts-arkui-particle-comp-particlecolorupdateroptions-i.md) | How the color property is updated. |
| [ParticleConfigs](arkts-arkui-particle-comp-particleconfigs-i.md) | Defines the particle configs. |
| [ParticleOptions](arkts-arkui-particle-comp-particleoptions-i.md) | Defines the ParticleOptions Interface. |
| [ParticlePropertyAnimation](arkts-arkui-particle-comp-particlepropertyanimation-i.md) | Defines the particle property lifecycle. @interface ParticlePropertyAnimation |
| [ParticlePropertyOptions](arkts-arkui-particle-comp-particlepropertyoptions-i.md) | Defines the particle property Options. @interface ParticlePropertyOptions |
| [ParticlePropertyUpdaterConfigs](arkts-arkui-particle-comp-particlepropertyupdaterconfigs-i.md) | Defines the particle property updater configs. @interface ParticlePropertyUpdaterConfigs |
| [Particles](arkts-arkui-particle-comp-particles-i.md) | Defines the particle array. |
| [ParticleUpdaterOptions](arkts-arkui-particle-comp-particleupdateroptions-i.md) | Defines the particle updater options. |
| [PointParticleParameters](arkts-arkui-particle-comp-pointparticleparameters-i.md) | Defines the parameters for a point-like particle. @interface PointParticleParameters |
| [RippleFieldOptions](arkts-arkui-particle-comp-ripplefieldoptions-i.md) | Defines ripple field options. |
| [VelocityFieldOptions](arkts-arkui-particle-comp-velocityfieldoptions-i.md) | Parameter used to describe the velocity field of particles. |
| [VelocityOptions](arkts-arkui-particle-comp-velocityoptions-i.md) | Defines velocity options. |

### Types

| Name | Description |
| --- | --- |
| [ParticleTuple](arkts-arkui-particle-comp-particletuple-t.md) | Defines a pair of given type for particle. |
| [PositionT](arkts-arkui-particle-comp-positiont-t.md) | Defines the PositionT type. |
| [SizeT](arkts-arkui-particle-comp-sizet-t.md) | Defines the SizeT type. |
| [Vector2T](arkts-arkui-particle-comp-vector2t-t.md) | Defines the Vector2T type. The Vector2T type contains two attribute values: x and y. |

### Enums

| Name | Description |
| --- | --- |
| [DistributionType](arkts-arkui-particle-comp-distributiontype-e.md) | Enumerates the color distribution types of a particle. |
| [DisturbanceFieldShape](arkts-arkui-particle-comp-disturbancefieldshape-e.md) | Defines particle disturbance shape. |
| [ParticleEmitterShape](arkts-arkui-particle-comp-particleemittershape-e.md) | Enumerates the emitter shapes of a particle. |
| [ParticleType](arkts-arkui-particle-comp-particletype-e.md) | Enumerates the particle types. |
| [ParticleUpdater](arkts-arkui-particle-comp-particleupdater-e.md) | Enumerates the updater types of a particle. |

## Examples

```TypeScript
### Example 1: Initializing Particles with Circular Shapes

This example demonstrates the basic usage of particle animations by initializing particles with circular shapes.


```

```TypeScript
### Example 2: Initializing Particles with Images

Describes the basic usage of particle animation, where particles are initialized through images. This example configures two different types of image particles to demonstrate the combined effect of multiple particle types.


```

```TypeScript
### Example 3: Changing Motion Trajectories with the Particle Disturbance Field

This example demonstrates the effect of particle motion trajectory changes under the interference of a disturbance field.


```

```TypeScript
### Example 4: Adjusting the Emitter Position

This example demonstrates how to adjust the position of the particle emitter through emitter().


```

```TypeScript
### Example 5: Creating an Annulus Emitter

This example demonstrates how to create a annulus emitter, where particles are statically emitted across the entire annulus range (from the start angle 0 to the end angle 360).


```

```TypeScript
### Example 6: Annulus Emitter Update

This example describes the basic usage of updating the annulus emitter of a particle animation.


```

```TypeScript
### Example 7: Setting Ripple Field and Velocity Field

Since API version 22, particle ripple fields and velocity fields can be set. This example demonstrates how to set a particle ripple field through the rippleFields API to produce an effect similar to ripple diffusion. The velocityFields API is used to set a particle velocity field, so that the velocity specified by the velocity field is superimposed on the original velocity of the particles.
```
