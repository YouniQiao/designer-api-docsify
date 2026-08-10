# EmitterParticleOptions

粒子配置。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface EmitterParticleOptions<PARTICLE extends ParticleType>--><!--Device-unnamed-interface EmitterParticleOptions<PARTICLE extends ParticleType>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## config

```TypeScript
config: ParticleConfigs[PARTICLE]
```

表示对应类型的配置。

config类型和type值有关联：

1. 如果type为ParticleType.POINT，则config类型为[PointParticleParameters](arkts-arkui-pointparticleparameters-i.md) 。2. 如果type为ParticleType.IMAGE，则config类型为[ImageParticleParameters](arkts-arkui-imageparticleparameters-i.md) 。

**Type:** ParticleConfigs[PARTICLE]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EmitterParticleOptions-config: ParticleConfigs[PARTICLE]--><!--Device-EmitterParticleOptions-config: ParticleConfigs[PARTICLE]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: number
```

表示发射的粒子总数，count取值>=-1,当count为-1表示粒子总数无限大。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EmitterParticleOptions-count: number--><!--Device-EmitterParticleOptions-count: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lifetime

```TypeScript
lifetime?: number
```

表示单个粒子的生命周期，默认值1000（即1000ms，1s），lifetime>=-1。当lifetime为-1表示粒子生命周期无限大。当lifetime<-1，取默认值。

**说明：**如果不需要动画一直播放，建议不要将生命周期设置为-1，可能对性能造成较大影响。

**Type:** number

**Default:** 1000

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EmitterParticleOptions-lifetime?: number--><!--Device-EmitterParticleOptions-lifetime?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lifetimeRange

```TypeScript
lifetimeRange?: number
```

表示粒子生命周期取值范围，设置lifetimeRange后粒子的生命周期为[lifetime-lifetimeRange, lifetime+lifetimeRange]中间的一个随机整数。lifetimeRange默认值为0，取值范围为0到正无穷。设置为负值时取默认值。

**Type:** number

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EmitterParticleOptions-lifetimeRange?: number--><!--Device-EmitterParticleOptions-lifetimeRange?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: PARTICLE
```

表示粒子类型，可以选择图片或者是点。

**Type:** PARTICLE

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EmitterParticleOptions-type: PARTICLE--><!--Device-EmitterParticleOptions-type: PARTICLE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

