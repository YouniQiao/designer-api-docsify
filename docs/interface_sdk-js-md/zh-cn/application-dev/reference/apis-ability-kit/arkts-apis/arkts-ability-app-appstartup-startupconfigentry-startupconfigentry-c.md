# StartupConfigEntry

本模块提供[应用启动框架](../../../application-models/app-startup.md)配置的能力。

**起始版本：** 12

**系统能力：** SystemCapability.Ability.AppStartup

## 导入模块

```TypeScript
import { StartupConfigEntry } from 'kits/@kit.AbilityKit';
```

## onConfig

```TypeScript
onConfig?(): StartupConfig
```

在回调[AbilityStage.onCreate](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)前，若该AbilityStage对应的HAP中启动框架配置 文件中[定义了启动框架配置](../../../application-models/app-startup.md#定义启动参数配置)，则会触发该回调。开发者可以在该回调中设置启动框架配置信息，详细使用方法可参考[设置启动参数](../../../application-models/app-startup.md#设置启动参数)章节。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**返回值：**

| 类型 |
| --- |
| [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) |

## onRequestCustomMatchRule

```TypeScript
onRequestCustomMatchRule(want: Want): string
```

在回调[AbilityStage.onCreate](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)前，若该AbilityStage对应的HAP中启动框架配置 文件中[定义了启动框架配置](../../../application-models/app-startup.md#定义启动参数配置)，则会在 StartupConfigEntry.onConfig后触发该回调。开发者可以在该回调中，可以根据调用方传入启动UIAbility的Want中的不同参数来返回不同的自定义匹配规则。启动框架会将其与启动任务配置的matchRules中customization字段进行匹配。若匹配成功，任务将在自动模 式执行。详细匹配规则请参考[添加任务匹配规则](../../../application-models/app-startup.md#添加任务匹配规则)章节。该接口通常用于无法直接通过uri、action或意图名称规则来匹配启动任务的场景，可以使用本接口对匹配规则进一步细化。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |
