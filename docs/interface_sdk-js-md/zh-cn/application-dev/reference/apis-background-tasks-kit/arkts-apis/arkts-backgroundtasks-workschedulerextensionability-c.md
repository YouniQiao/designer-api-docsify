# WorkSchedulerExtensionAbility

延迟任务回调，当满足调度条件或调度结束时，系统会回调应用WorkSchedulerExtensionAbility中 [onWorkStart()](#onworkstart)或 [onWorkStop()](#onworkstop)的方法。

**起始版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

## 导入模块

```TypeScript
import { WorkSchedulerExtensionAbility, WorkSchedulerExtensionContext } from 'kits/@kit.BackgroundTasksKit';
```

## onWorkStart

```TypeScript
onWorkStart(work: workScheduler.WorkInfo): void
```

开始延迟任务调度回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| work | workScheduler.WorkInfo | 是 |

## onWorkStop

```TypeScript
onWorkStop(work: workScheduler.WorkInfo): void
```

结束延迟任务调度回调。当延迟任务2分钟超时或应用调用[stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md) 接口取消任务时，触发该回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| work | workScheduler.WorkInfo | 是 |

## context

```TypeScript
context: WorkSchedulerExtensionContext
```

WorkSchedulerExtension的上下文环境，继承自ExtensionContext。

**类型：** [WorkSchedulerExtensionContext](arkts-backgroundtasks-workschedulerextensioncontext-t.md)

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler
