# StartupTask

The module provides capabilities related to startup tasks in [AppStartup](../../../application-models/app-startup.md).

**起始版本：** 12

**系统能力：** SystemCapability.Ability.AppStartup

## 导入模块

```TypeScript
import { StartupTask } from 'kits/@kit.AbilityKit';
```

## init

```TypeScript
init(context: AbilityStageContext): Promise<Object | void>
```

当所有依赖的启动任务都执行完成后，该方法将会被调用。开发者可以在该回调中执行该启动任务的初始化操作。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [AbilityStageContext](arkts-ability-abilitystagecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object \ | void & gt; |

## onDependencyCompleted

```TypeScript
onDependencyCompleted?(dependency: string, result: Object): void
```

当依赖的启动任务执行完成时该方法将会被调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dependency | string | 是 |
| result | Object | 是 |
