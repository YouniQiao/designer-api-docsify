# ParticleUpdaterOptions

颜色属性变化配置。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ParticleUpdaterOptions--><!--Device-unnamed-export interface ParticleUpdaterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## config

```TypeScript
config: ParticlePropertyUpdaterConfigs
```

属性变化配置。属性变化类型type有三类：

1、当type为ParticleUpdater.NONE，表示无变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.NONE]。

2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.RANDOM]。

3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为  
[ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md/arkts-arkui-particlepropertyupdaterconfigs-i.md)[ParticleUpdater.CURVE]。   
**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** [ParticlePropertyUpdaterConfigs](../arkts-components/arkts-arkui-particlepropertyupdaterconfigs-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleUpdaterOptions-config: ParticlePropertyUpdaterConfigs--><!--Device-ParticleUpdaterOptions-config: ParticlePropertyUpdaterConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: ParticleUpdater
```

表示颜色属性变化类型。 

默认值：type默认为ParticleUpdater.NONE。 **原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** [ParticleUpdater](arkts-arkui-particle-particleupdater-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParticleUpdaterOptions-type: ParticleUpdater--><!--Device-ParticleUpdaterOptions-type: ParticleUpdater-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

