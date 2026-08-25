# WorkSchedulerExtensionAbility

Provides callbacks to be invoked when the scheduling conditions are met or the scheduling ends, for example, [onWorkStart()](#onworkstart) or [onWorkStop()](#onworkstop) in WorkSchedulerExtensionAbility.

**Since:** 9

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { WorkSchedulerExtensionAbility, WorkSchedulerExtensionContext } from 'kits/@kit.BackgroundTasksKit';
```

## onWorkStart

```TypeScript
onWorkStart(work: workScheduler.WorkInfo): void
```

Called when the system starts scheduling the deferred task.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| work | workScheduler.WorkInfo | Yes |

## onWorkStop

```TypeScript
onWorkStop(work: workScheduler.WorkInfo): void
```

Called when the system stops scheduling the deferred task. This callback is triggered when the deferred task times out for 2 minutes or the [stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md) API is called to cancel the task.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| work | workScheduler.WorkInfo | Yes |

## context

```TypeScript
context: WorkSchedulerExtensionContext
```

Context of the WorkSchedulerExtensionAbility. This context inherits from ExtensionContext.

**Type:** [WorkSchedulerExtensionContext](arkts-backgroundtasks-workschedulerextensioncontext-t.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler
