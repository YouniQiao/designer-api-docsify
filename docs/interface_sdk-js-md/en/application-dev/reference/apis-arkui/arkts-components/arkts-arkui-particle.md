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
| particles | [Particles](arkts-arkui-particles-i.md)&lt;PARTICLE, COLOR_UPDATER, OPACITY_UPDATER, SCALE_UPDATER, ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER, SPIN_UPDATER&gt; | Yes | Array of particles. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AccelerationOptions](arkts-arkui-accelerationoptions-i.md) | Particle acceleration. |
| [DisturbanceFieldOptions](arkts-arkui-disturbancefieldoptions-i.md) | Defines particle disturbance Field params. |
| [EmitterOptions](arkts-arkui-emitteroptions-i.md) | Particle emitter configuration. |
| [EmitterParticleOptions](arkts-arkui-emitterparticleoptions-i.md) | Defines parameters of particles used by emitters. |
| [EmitterProperty](arkts-arkui-emitterproperty-i.md) | Defines the emitter property. |
| [FieldRegion](arkts-arkui-fieldregion-i.md) | Defines the area information of the particle field. |
| [ImageParticleParameters](arkts-arkui-imageparticleparameters-i.md) | Defines the parameters for an image-like particle. @interface ImageParticleParameters |
| [ParticleAnnulusRegion](arkts-arkui-particleannulusregion-i.md) | Configures the annular emitter area. |
| [ParticleColorOptions](arkts-arkui-particlecoloroptions-i.md) | The color changes randomly, with the per-second change difference being a value randomly generated from the range. The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels. |
| [ParticleColorPropertyOptions](arkts-arkui-particlecolorpropertyoptions-i.md) | Defines the particle color property updater configs which can support generics. @interface ParticleColorPropertyOptions |
| [ParticleColorPropertyUpdaterConfigs](arkts-arkui-particlecolorpropertyupdaterconfigs-i.md) | Defines the particle color property updater configs. @interface ParticleColorPropertyUpdaterConfigs |
| [ParticleColorUpdaterOptions](arkts-arkui-particlecolorupdateroptions-i.md) | How the color property is updated. |
| [ParticleConfigs](arkts-arkui-particleconfigs-i.md) | Defines the particle configs. |
| [ParticleOptions](arkts-arkui-particleoptions-i.md) | Defines the ParticleOptions Interface. |
| [ParticlePropertyAnimation](arkts-arkui-particlepropertyanimation-i.md) | Defines the particle property lifecycle. @interface ParticlePropertyAnimation |
| [ParticlePropertyOptions](arkts-arkui-particlepropertyoptions-i.md) | Defines the particle property Options. @interface ParticlePropertyOptions |
| [ParticlePropertyUpdaterConfigs](arkts-arkui-particlepropertyupdaterconfigs-i.md) | Defines the particle property updater configs. @interface ParticlePropertyUpdaterConfigs |
| [Particles](arkts-arkui-particles-i.md) | Defines the particle array. |
| [ParticleUpdaterOptions](arkts-arkui-particleupdateroptions-i.md) | Defines the particle updater options. |
| [PointParticleParameters](arkts-arkui-pointparticleparameters-i.md) | Defines the parameters for a point-like particle. @interface PointParticleParameters |
| [RippleFieldOptions](arkts-arkui-ripplefieldoptions-i.md) | Defines ripple field options. |
| [VelocityFieldOptions](arkts-arkui-velocityfieldoptions-i.md) | Parameter used to describe the velocity field of particles. |
| [VelocityOptions](arkts-arkui-velocityoptions-i.md) | Defines velocity options. |

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

## Examples

This example demonstrates the basic usage of particle animations by initializing particles with circular shapes.

```TypeScript
@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 10// Point radius.
                },
                count: 500, // Total number of particles.
                lifetime: 10000, // Particle lifetime, in ms.
                lifetimeRange: 100// Range of particle lifetime values, in ms.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: [0, 0],
              shape: ParticleEmitterShape.RECTANGLE// Emitter shape.
            },
            color: {
              range: [Color.Red, Color.Yellow], // Initial color range.
              distributionType: DistributionType.GAUSSIAN, // Random distribution of initial color values.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: [
                  {
                    from: Color.White, // Initial value of the change.
                    to: Color.Pink, // Target value of the change.
                    startMillis: 0, // Start time.
                    endMillis: 3000, // End time.
                    curve: Curve.EaseIn// Animation curve.
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
            opacity: {
              range: [0.0, 1.0], // The initial value of particle opacity is randomly generated from the [0.0, 1.0] range.
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            acceleration: {
              // Acceleration. speed indicates the acceleration speed, and angle indicates the acceleration direction.
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.RANDOM, // The speed changes randomly.
                  config: [1, 20]
                }
              },
              angle: {
                range: [90, 90]
              }
            }

          }
        ]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

This example demonstrates the basic usage of particle animations by initializing particles with images.

```TypeScript
@Entry
@Component
struct ParticleExample {
  @State
  myCount: number = 100
  flag: boolean = false;

  build() {
    Column() {
      Stack() {
        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.IMAGE,
                  config: {
                    src: $r("app.media.book"),
                    size: [10, 10]
                  },
                  count: this.myCount,
                  lifetime: 10000,
                  lifetimeRange: 100
                },
                emitRate: 3,
                shape: ParticleEmitterShape.CIRCLE
              },
              color: {
                range: [Color.White, Color.White]
              },
              opacity: {
                range: [1.0, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 1.0,
                      startMillis: 0,
                      endMillis: 6000
                    },
                    {
                      from: 1.0,
                      to: 0,
                      startMillis: 6000,
                      endMillis: 10000
                    }
                  ]
                }
              },
              scale: {
                range: [0.1, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 1.5,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }

                  ]
                }
              },
              acceleration: {
                speed: {
                  range: [3, 9],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 10,
                        to: 20,
                        startMillis: 0,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 10,
                        to: 2,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                },
                angle: {
                  range: [0, 180],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [{
                      from: 1,
                      to: 2,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    },
                      {
                        from: 50,
                        to: -50,
                        startMillis: 1000,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 3,
                        to: 5,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                }
              },
              spin: {
                range: [0.1, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 0,
                      to: 360,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
            }
            , {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.heart'),
                  size: [10, 10]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: [Color.White, Color.White]
            },
            opacity: {
              range: [1.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                ]
              }
            },
            scale: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                ]
              }
            },
            acceleration: {
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
              angle: {
                range: [0, 180],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 10000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              }
            },
            spin: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }, {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.sun'),
                  size: [10, 10]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: [Color.White, Color.White]
            },
            opacity: {
              range: [1.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                ]
              }
            },
            scale: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                ]
              }
            },
            acceleration: {
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
              angle: {
                range: [0, 180],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: [{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 1000,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              }
            },
            spin: {
              range: [0.1, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }
          ]
        }).width(300).height(300)

      }.width(500).height(500).align(Alignment.Center)
    }.width("100%").height("100%")

  }
}
```

This example demonstrates how to change the motion trajectories of particles by applying disturbances through the particle disturbance field.

```TypeScript
@Entry
@Component
struct ParticleExample3 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 10// Point radius.
                },
                count: 500, // Total number of particles.
                lifetime: 10000// Particle lifetime, in ms.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: [0, 0],
              shape: ParticleEmitterShape.RECTANGLE// Emitter shape.
            },
            color: {
              range: [Color.Red, Color.Yellow], // Initial color range.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: [
                  {
                    from: Color.White, // Initial value of the change.
                    to: Color.Pink, // Target value of the change.
                    startMillis: 0, // Start time.
                    endMillis: 3000, // End time.
                    curve: Curve.EaseIn// Animation curve.
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
            opacity: {
              range: [0.0, 1.0], // The initial value of particle opacity is randomly generated from the [0.0, 1.0] range.
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            acceleration: {
              // Acceleration. speed indicates the acceleration speed, and angle indicates the acceleration direction.
              speed: {
                range: [3, 9],
                updater: {
                  type: ParticleUpdater.RANDOM,
                  config: [1, 20]
                }
              },
              angle: {
                range: [90, 90]
              }
            }

          }
        ]
      }).width(300).height(300).disturbanceFields([{
        strength: 10,
        shape: DisturbanceFieldShape.RECT,
        size: { width: 100, height: 100 },
        position: { x: 100, y: 100 },
        feather: 15,
        noiseScale: 10,
        noiseFrequency: 15,
        noiseAmplitude: 5
      }])
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

This example demonstrates how to adjust the position of the particle emitter through emitter().

```TypeScript
@Entry
@Component
struct ParticleExample4 {
  @State emitterProperties: Array<EmitterProperty> = [
    {
      index: 0,
      emitRate: 100,
      position: { x: 60, y: 80 },
      size: { width: 200, height: 200 }
    }
  ];

  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 5// Point radius.
                },
                count: 400, // Total number of particles.
                lifetime: -1// Particle lifetime. The value -1 indicates that the lifetime of the particle is infinite.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: [0, 0], // Emitter position.
              shape: ParticleEmitterShape.CIRCLE// Emitter shape.
            },
            color: {
              range: [Color.Red, Color.Yellow], // Initial color range.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: [
                  {
                    from: Color.White,
                    to: Color.Pink,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                ]
              }
            },
          },
        ]
      })
        .width(300)
        .height(300)
        .emitter(this.emitterProperties)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

This example describes the basic usage of creating a ring emitter.

```TypeScript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ParticleExample5 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: [
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 5 // Dot radius
                },
                count: 2000, // Total number of particles
                lifetime: 10000, // Particle lifetime, in ms.
                lifetimeRange: 100// Range of particle lifetime values, in ms.
              },
              emitRate: 100, // Number of particles emitted per second
              shape: ParticleEmitterShape.ANNULUS, // Ring emitter
              annulusRegion:{
                center:{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)}, // Coordinates of the center of the ring
                innerRadius:LengthMetrics.vp(100), // Outer radius of the ring
                outerRadius:LengthMetrics.vp(120), // Inner radius of the ring
                startAngle:0, // Start angle of the ring
                endAngle:360 // End angle of the ring
              }
            },
            color: {
              range: [Color.Pink, Color.White],
            },
            opacity: {
              range: [0.0, 1.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
            scale: {
              range: [0.0, 0.0],
              updater: {
                type: ParticleUpdater.CURVE,
                config: [
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                ]
              }
            },
          }
        ]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

This example describes the basic usage of updating the ring emitter of a particle animation.

```TypeScript
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct ParticleExample6 {

  @State radius: number = 1;
  @State shape: ParticleEmitterShape = ParticleEmitterShape.ANNULUS;
  @State emitRate: number = 200;
  @State count: number = 2000;
  private timerID: number = -1;
  private centerX: LengthMetrics = LengthMetrics.percent(0.5);
  private centerY: LengthMetrics = LengthMetrics.percent(0.5);
  private inRadius: LengthMetrics = LengthMetrics.vp(120);
  private outRadius: LengthMetrics = LengthMetrics.vp(120);
  private startAngle: number = 0;
  private endAngle: number = 90;
  @State emitterProperties: Array<EmitterProperty> = [
    {
      index: 0,
      emitRate: 100,
      annulusRegion: {
        center:{x:this.centerX, y: this.centerY}, // Center coordinates of the ring
        outerRadius: this.outRadius, // Outer radius of the ring
        innerRadius: this.inRadius, // Inner radius of the ring
        startAngle: -90, // Start angle of the ring
        endAngle: 0 // End angle of the ring
      }
    }
  ]
  @State region: ParticleAnnulusRegion = {
    center:{x:this.centerX, y: this.centerY},
    outerRadius: this.outRadius,
    innerRadius: this.inRadius,
    startAngle: -90,
    endAngle: 0
  }

  aboutToDisappear(): void {
    // Clear the timer when the page is destroyed.
    if (this.timerID != -1) {
      clearInterval(this.timerID);
    }
  }

  build() {
    Column({ space: 10}) {
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)

        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // Particle type.
                  config: {
                    radius: this.radius // Dot radius
                  },
                  count: this.count, // Total number of particles
                  lifetime: -1 // Particle lifecycle. The value -1 indicates that the particle lifecycle is infinite.
                },
                emitRate: this.emitRate, // Number of particles emitted per second
                shape: this.shape, // Shape of the emitter
                annulusRegion: this.region
              },
              color: {
                range: [Color.White, Color.Pink], // Initial color range
              },
            },
          ]
        }).width('100%')
          .height('100%')
          .emitter(this.emitterProperties)
          .onClick(()=>{
            // Clear the existing timer.
            if (this.timerID != -1) {
              clearInterval(this.timerID);
            }

            // Create a timer (update every second).
            this.timerID = setInterval(() => {
              this.emitterProperties = [
                {
                  index: 0,
                  emitRate: this.emitRate,
                  annulusRegion: {
                    center:{x:this.centerX, y: this.centerY},
                    outerRadius: this.outRadius,
                    innerRadius: this.inRadius,
                    startAngle: this.startAngle,
                    endAngle: this.endAngle
                  }
                }
              ];
              if (this.endAngle >= 270) {
                if (this.timerID != -1) {
                  clearInterval(this.timerID);
                }
                return;
              }
              // Update the angle value (30 degrees per second).
              this.startAngle += 30;
              this.endAngle += 30;
            }, 1000);

          })
      }
      .width('100%')
      .height('100%')
      .align(Alignment.Center)
    }
  }
}
```

Starting from API version 22, the ripple field and velocity field can be set for particles. This example shows how to use the rippleFields API to set the ripple field of particles to produce a ripple effect. The velocityFields API is used to set the velocity field of particles, so that the velocity specified by the velocity field is added to the original velocity of particles.

```TypeScript
// xxx.ets
@Entry
@Component
struct ParticleExample {
  @State count: number = 1000
  @State particle: EmitterParticleOptions<ParticleType> = {
    type: ParticleType.POINT, // Particle type.
    config: {
      radius: 1 // Radius of the dot
    },
    count: this.count, // Total number of particles
    lifetime: 9000, //Particle lifetime, in ms
    lifetimeRange: 100 // Range of particle lifetime values, in ms.
  }
  build() {
    Column() {
      Text('Wave field')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: [
            {
              emitter: {
                particle: this.particle,
                emitRate: 10000, //Number of particles emitted per second
                position: [0, 0],
                shape: ParticleEmitterShape.RECTANGLE // Emitter shape.
              },
              color: {
                range: [Color.White, Color.White], // initial color range
              },
              scale: {
                range: [0.2, 1.5], //Initial size range
              },
              opacity : {
                range: [0.2, 0.8], //Initial transparency range
              }
            }
          ]
        }).width(300).height(300)
          .rippleFields([
            {
              amplitude: 120, //Amplitude of the wave field
              wavelength: 500, //Wavelength of the wave field
              waveSpeed: 220, //Wave speed of the wave field
              center: { x: 150, y: 150 }, //Center of the force field of the wave field
              attenuation: 0, //Attenuation coefficient of the wave field over time
              region: {
                //Affected area of the wave field.
                shape: DisturbanceFieldShape.RECT, // Shape of the disturbance field's affected area
                position: { x: 150, y: 150 }, // Center of the disturbance field's affected area
                size: { width: 300, height: 300 } // Size of the disturbance field's affected area
              }
            }
          ])
      }.width("100%").height(300).align(Alignment.Center)
      Text ('Velocity field')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: [
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // Particle type.
                  config: {
                    radius: 2 // Radius of the dot
                  },
                  count: 1000, // Total number of particles
                  lifetime: 1000, // Particle lifetime, in ms
                  lifetimeRange: 0 // Particle lifetime range, in ms
                },
                emitRate: 120, // Number of particles emitted per second
                position: [0, 0],
                size: [300, 300],
                shape: ParticleEmitterShape.RECTANGLE // Emitter shape.
              },
              color: {
                range: [Color.White, Color.White], // initial color range
              },
              opacity: {
                range: [1.0, 1.0],
                updater: {
                  type: ParticleUpdater.CURVE, // Transparency changes by curve
                  config: [
                    {
                      from: 1.0,
                      to: 0.0,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    }
                  ]
                }
              },
            }
          ]
        }).width(300).height(300)
          .margin({ top: 30 })
          .velocityFields([
            {
              velocity: { x: 100, y: 0 }, // Velocity of the velocity field
              region: {
                // Affected area of the velocity field
                shape: DisturbanceFieldShape.RECT, // Shape of the velocity field's affected area
                position: { x: 150, y: 150 }, // Center of the area affected by the velocity field
                size: { width: 200, height: 200 } // Size of the area affected by the velocity field.
              }
            }
          ])
      }.width("100%").height(300).align(Alignment.Center)
    }
  }
}
```
