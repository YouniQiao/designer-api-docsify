# StartupTask

The module provides capabilities related to startup tasks in  
[AppStartup](../../../application-models/app-startup.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare class StartupTask--><!--Device-unnamed-declare class StartupTask-End-->

**System capability:** SystemCapability.Ability.AppStartup

## Modules to Import

```TypeScript
import { StartupTask } from 'kits/@kit.AbilityKit';
```

## init

```TypeScript
init(context: AbilityStageContext): Promise<Any> | Promise<void>
```

启动任务执行的初始化业务。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>--><!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [AbilityStageContext](arkts-ability-abilitystagecontext-c.md) | Yes | AbilityStage的上下文环境。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Any&gt; | Promise对象，返回启动任务执行结果对象。 |

## onDependencyCompleted

```TypeScript
onDependencyCompleted(dependency: string, result: Any): void
```

当依赖的启动任务执行完成时该方法将会被调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void--><!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dependency | string | Yes | 依赖的启动任务名称。 |
| result | Any | Yes | 依赖启动任务执行的结果。 |

