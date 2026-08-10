# ParticlePropertyOptions

设置粒子属性选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ParticlePropertyOptions--><!--Device-unnamed-export interface ParticlePropertyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: ParticleTuple<double, double>
```

粒子初始属性值区间，粒子发射器生成粒子的属性值在range区间随机取值。

**说明：**

各项属性的非法输入取默认值，当最大值小于最小值的时候取默认区间。TYPE为number。

不同属性的默认值不同：

1、opacity属性：range:[1.0,1.0]，取值范围为[0, 1]，默认值为1.0。

2、scale属性：range:[1.0,1.0]，取值范围为[0, 10000]，默认值为1.0。

3、acceleration加速度speed属性：range:[0.0,0.0]，取值范围为[0, 10000]，默认值为0.0。

4、acceleration加速度angle属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。

5、spin属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。

**Type:** [ParticleTuple](arkts-arkui-particletuple-t.md)&lt;double, double&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyOptions-range: ParticleTuple<double, double>--><!--Device-ParticlePropertyOptions-range: ParticleTuple<double, double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updater

```TypeScript
updater?: ParticleUpdaterOptions
```

属性变化配置。属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.NONE]。

2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.RANDOM]。

3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.CURVE] 

默认值：type默认为ParticleUpdater.NONE。

**Type:** [ParticleUpdaterOptions](../arkts-components/arkts-arkui-particleupdateroptions-i.md)

**Default:** {type:UPDATER.NONE;config:undefined}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticlePropertyOptions-updater?: ParticleUpdaterOptions--><!--Device-ParticlePropertyOptions-updater?: ParticleUpdaterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

