# ParticlePropertyUpdaterConfigs

设置粒子属性更新器配置。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface ParticlePropertyUpdaterConfigs<T>--><!--Device-unnamed-interface ParticlePropertyUpdaterConfigs<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.CURVE]

```TypeScript
[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>
```

表示变化方式为曲线变化时，属性变化的配置。数组类型表示当前属性可以设置多段动画，如0ms-3000ms，3000ms-5000ms，5000ms-8000ms分别设置动画。T为number。

**Type:** Array&lt;ParticlePropertyAnimation&lt;T&gt;&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>--><!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.NONE]

```TypeScript
[ParticleUpdater.NONE]: void
```

无变化。

**Type:** void

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.NONE]: void--><!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.NONE]: void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [ParticleUpdater.RANDOM]

```TypeScript
[ParticleUpdater.RANDOM]: ParticleTuple<T, T>
```

表示变化方式为匀速变化时，每秒的变化差值为设置区间随机生成的值。

目标属性值为当前属性值叠加变化差值。如当前属性值为0.2，config取[0.1,1.0]:

1、如果变化差值在区间[0.1,1.0]取随机值0.5，则目标属性值为0.2+0.5 = 0.7；

2、变化差值也可以取负值。如当前属性值为0.2，config为 [-3.0,2.0],如果变化差值在区间[-3.0,2.0]取随机值-2.0，则目标属性值为0.2-2.0 = -1.8。

**说明：**

config配置的是变化差值的取值范围，差值的最大最小值没有约束。但是如果当前属性值叠加差值大于属性最大值，目标属性值取属性最大值；如果当前属性值叠加差值小于属性最小值，目标属性值取属性最小值。T为number。

例如：opacity的取值范围[0.0,1.0]则当当前属性值叠加差值超过1.0，则取1.0。

**Type:** [ParticleTuple](../arkts-apis/arkts-arkui-particletuple-t.md)&lt;T, T&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.RANDOM]: ParticleTuple<T, T>--><!--Device-ParticlePropertyUpdaterConfigs-[ParticleUpdater.RANDOM]: ParticleTuple<T, T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

