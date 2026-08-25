# cancel

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## cancel

```TypeScript
function cancel(task: Task): void
```

Cancels a task in the task pool. If the task is in the internal queue of the task pool, the task will not be executed after being canceled, and an exception indicating task cancellation is returned. If the task has been distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and the execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation status. In other words, **taskpool.cancel** takes effect for calls of **taskpool.execute**, **taskpool.executeDelayed**, or **taskpool.executePeriodically**. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt;[taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200015](../errorcode-utils.md#10200015-failed-to-cancel-a-task-that-does-not-exist) |
| [10200016](../errorcode-utils.md#10200016-failed-to-cancel-a-task-being-executed) |
| [10200055](../errorcode-utils.md#10200055-asynchronous-queue-task-canceled) |


## cancel

```TypeScript
function cancel(group: TaskGroup): void
```

Cancels a task group in the task pool. If a task group is canceled before all the tasks in it are finished, **undefined** is returned. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt;[taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200018](../errorcode-utils.md#10200018-failed-to-cancel-a-task-group-that-does-not-exist) |


## cancel

```TypeScript
function cancel(taskId: number): void
```

Cancels a task in the task pool by task ID. If the task is in the internal queue of the task pool, the task will not be executed after being canceled, and an exception indicating task cancellation is returned. If the task has been distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and the execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation status. **taskpool.cancel** takes effect for the previous calls of **taskpool.execute** or **taskpool.executeDelayed**. If **taskpool.cancel** is called by other threads, note that the cancel operation, which is asynchronous, may take effect for later calls of **taskpool.execute** or **taskpool.executeDelayed**. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt;[taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200015](../errorcode-utils.md#10200015-failed-to-cancel-a-task-that-does-not-exist) |
| [10200055](../errorcode-utils.md#10200055-asynchronous-queue-task-canceled) |
