# @ohos.app.ability.systemConfiguration(系统环境模块)

systemConfiguration模块提供系统环境变化监听回调能力，包括系统深浅色模式、系统语言、系统字体大小缩放比例等变化的回调。例如，通过对系统深浅色模式变化的监听，应用可感知系统的深浅色模式变化，并动态调整自身应用的深浅色主题以适配系统环境。该模块与[EnvironmentCallback](arkts-ability-app-ability-environmentcallback-environmentcallback-c.md)模块的区别在于：  
- systemConfiguration模块：用于监听系统环境变量[Configuration](arkts-ability-app-ability-configuration-configuration-i.md)的变化。  
- [EnvironmentCallback](arkts-ability-app-ability-environmentcallback-environmentcallback-c.md)模块：用于监听某个应用环境变量  
[Configuration](arkts-ability-app-ability-configuration-configuration-i.md)的变化。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { systemConfiguration } from 'kits/@kit.AbilityKit';
```

## 汇总

### 接口

| 名称 |
| --- |
| [UpdatedCallback(系统环境模块)](arkts-ability-systemconfiguration-updatedcallback-i.md) |

### 类型

| 名称 |
| --- |
| [OnColorModeUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-oncolormodeupdatedfn-t.md) |
| [OnFontIdUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onfontidupdatedfn-t.md) |
| [OnFontSizeScaleUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onfontsizescaleupdatedfn-t.md) |
| [OnFontWeightScaleUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onfontweightscaleupdatedfn-t.md) |
| [OnHasPointerDeviceUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onhaspointerdeviceupdatedfn-t.md) |
| [OnLanguageUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onlanguageupdatedfn-t.md) |
| [OnLocaleUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onlocaleupdatedfn-t.md) |
| [OnMCCUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onmccupdatedfn-t.md) |
| [OnMNCUpdatedFn(系统环境模块)](arkts-ability-systemconfiguration-onmncupdatedfn-t.md) |
