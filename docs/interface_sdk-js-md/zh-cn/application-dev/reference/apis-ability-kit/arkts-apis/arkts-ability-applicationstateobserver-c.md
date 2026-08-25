# ApplicationStateObserver

应用状态监听器，可以作为入参传入 on('applicationState') 方法，监听应用的生命周期变化。  
> **说明：**&gt;
> 本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
## 导入模块  
```ts
import { appManager } from '@kit.AbilityKit';
```

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为14。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityStateChanged

```TypeScript
onAbilityStateChanged(abilityStateData: AbilityStateData): void
```

Ability状态发生变化时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| abilityStateData | [AbilityStateData](arkts-ability-abilitystatedata-c.md) | 是 |

## onAppStarted

```TypeScript
onAppStarted(appStateData: AppStateData): void
```

应用第一个进程创建时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | 是 |

## onAppStopped

```TypeScript
onAppStopped(appStateData: AppStateData): void
```

应用最后一个进程销毁时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | 是 |

## onForegroundApplicationChanged

```TypeScript
onForegroundApplicationChanged(appStateData: AppStateData): void
```

应用前后台状态发生变化时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | 是 |

## onProcessCreated

```TypeScript
onProcessCreated(processData: ProcessData): void
```

进程创建时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | 是 |

## onProcessDied

```TypeScript
onProcessDied(processData: ProcessData): void
```

进程销毁时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | 是 |

## onProcessStateChanged

```TypeScript
onProcessStateChanged(processData: ProcessData): void
```

进程状态更新时执行的回调函数。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | 是 |
