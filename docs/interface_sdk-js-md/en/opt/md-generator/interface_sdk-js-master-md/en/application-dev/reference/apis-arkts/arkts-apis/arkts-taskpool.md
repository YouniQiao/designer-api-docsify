# @ohos.taskpool

TaskPool provides a multi-thread running environment for applications. It helps reduce resource consumption and improve system performance. It also frees you from caring about the thread lifecycle. You can use the TaskPool APIs to create background tasks and perform operations on them, for example, executing or canceling a task. Theoretically,you can create an unlimited number of tasks, but this is not recommended due to memory limitations. In addition, you are not advised performing blocking operations in a task, especially indefinite blocking. Long-time blocking operations occupy worker threads and may block other task scheduling, adversely affecting your application performance.You can determine the execution sequence of tasks with the same priority. They are executed in the same sequence as you call the task execution APIs. The default task priority is MEDIUM.If the number of tasks to be executed is greater than the number of worker threads in the task pool, the task pool scales out based on load balancing to minimize the waiting duration. Similarly, when the number of tasks to be executed falls below the number of worker threads, the task pool scales in to reduce the number of worker threads.For details about the error codes returned by TaskPool APIs, see  
[Utils Error Codes](../../../reference/apis-arkts/errorcode-utils.md).For details about the precautions for using TaskPool, see  
[Precautions for TaskPool](../../../arkts-utils/taskpool-introduction.md#precautions-for-taskpool).The following concepts are used in this topic:

- Task group task: task in a [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md).  
- Serial queue task: task in a [SequenceRunner](arkts-arkts-taskpool-sequencerunner-c.md).  
- Asynchronous queue task: task in an [AsyncRunner](arkts-arkts-taskpool-asyncrunner-c.md).  
- Periodic task: task executed by calling  
[executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md#executeperiodically).

**Since:** 9

<!--Device-unnamed-declare namespace taskpool--><!--Device-unnamed-declare namespace taskpool-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel) |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel-1) |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel-2) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-1) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-2) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-3) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-4) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-5) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-6) |
| [execute](arkts-arkts-taskpool-execute-f.md#execute-7) |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md#executedelayed) |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md#executedelayed-1) |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md#executeperiodically) |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md#executeperiodically-1) |
| [getTask](arkts-arkts-taskpool-gettask-f.md#gettask) |
| [getTaskPoolInfo](arkts-arkts-taskpool-gettaskpoolinfo-f.md#gettaskpoolinfo) |
| [isConcurrent](arkts-arkts-taskpool-isconcurrent-f.md#isconcurrent) |
| [terminateTask](arkts-arkts-taskpool-terminatetask-f.md#terminatetask) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AsyncRunner](arkts-arkts-taskpool-asyncrunner-c.md) |
| [GenericsTask](arkts-arkts-taskpool-genericstask-c.md) |
| [LongTask](arkts-arkts-taskpool-longtask-c.md) |
| [SequenceRunner](arkts-arkts-taskpool-sequencerunner-c.md) |
| [Task](arkts-arkts-taskpool-task-c.md) |
| [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) |
| [TaskInfo](arkts-arkts-taskpool-taskinfo-c.md) |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) |
| [ThreadInfo](arkts-arkts-taskpool-threadinfo-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Configs](arkts-arkts-taskpool-configs-i.md) |
| [TaskResult](arkts-arkts-taskpool-taskresult-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Priority](arkts-arkts-taskpool-priority-e.md) |
| [State](arkts-arkts-taskpool-state-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) |
| [CallbackFunctionWithError](arkts-arkts-taskpool-callbackfunctionwitherror-t.md) |
