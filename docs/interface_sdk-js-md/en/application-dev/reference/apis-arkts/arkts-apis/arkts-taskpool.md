# @ohos.taskpool

/*
 Copyright (c) 2022 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace taskpool--><!--Device-unnamed-declare namespace taskpool-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'taskpool';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel) | Cancels a task in the task pool. If the task is in the internal queue of the task pool, the task will not be executed after being canceled, and an exception indicating task cancellation is returned. If the task has been distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and the execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation status. In other words, **taskpool.cancel** takes effect for calls of **taskpool.execute**, **taskpool.executeDelayed**, or **taskpool.executePeriodically**. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt; [taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md#TaskResult)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result. |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel) | Cancels a task group in the task pool. If a task group is canceled before all the tasks in it are finished, **undefined** is returned. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt; [taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md#TaskResult)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result. |
| [cancel](arkts-arkts-taskpool-cancel-f.md#cancel) | Cancels a task in the task pool by task ID. If the task is in the internal queue of the task pool, the task will not be executed after being canceled, and an exception indicating task cancellation is returned. If the task has been distributed to the worker thread of the task pool, canceling the task does not affect the task execution, and the execution result is returned in the catch branch. You can use **isCanceled()** to check the task cancellation status. **taskpool.cancel** takes effect for the previous calls of **taskpool.execute** or **taskpool.executeDelayed**. If **taskpool.cancel** is called by other threads, note that the cancel operation, which is asynchronous, may take effect for later calls of **taskpool.execute** or **taskpool.executeDelayed**. Starting from API version 20, after performing a cancel operation, you can use the generic type BusinessError&lt; [taskpool.TaskResult](arkts-arkts-taskpool-taskresult-i.md#TaskResult)&gt; in the catch branch to obtain the exception information thrown by the task or the final execution result. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Places a function to be executed in the internal queue of the task pool. The function is not executed immediately. It waits to be distributed to the worker thread for execution. In this mode, the function cannot be canceled. This API uses a promise to return the result. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Verifies the passed-in parameter types and return value type of a concurrent function, and places the function in the queue of the task pool. This API uses a promise to return the result. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Places a task in the internal queue of the task pool. The task will not be executed immediately; instead, it waits to be distributed to a worker thread for execution. In the current mode, you can set the task priority and cancel the task. Note that the task cannot belong to a task group, serial queue, or asynchronous queue. For non-continuous tasks, this API can be called multiple times. This API uses a promise to return the result. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Places the generic task in the internal queue of the task pool. The parameter type and return value type of the task are not verified. This API uses a promise to return the result. The verification of the **execute** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Places a task group in the internal queue of the task pool. The tasks in the task group are not executed immediately. They wait to be distributed to the worker thread for execution. After all tasks in the task group are executed, a result array is returned. This mode is applicable to the execution of associated tasks. This API uses a promise to return the result. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Execute a concurrent task with Configs. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Execute a concurrent generics task with Configs. |
| [execute](arkts-arkts-taskpool-execute-f.md#execute) | Execute a concurrent task group with Configs. |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md#executeDelayed) | Executes a task after a given delay. In this execution mode, you can set the task priority and call **cancel()** to cancel the execution. The task cannot be a task in a task group, serial queue, or asynchronous queue, or a periodic task. This API can be called only once for a continuous task, but multiple times for a non-continuous task. This API uses a promise to return the result. |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md#executeDelayed) | Executes the generic task with a delay without verifying the parameter type and return value type of the task. This API uses a promise to return the result. The verification of the **executeDelayed** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**. |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md#executePeriodically) | Executes a task periodically. In this execution mode, you can set the task priority and call **cancel()** to cancel the execution. A periodic task cannot be a task in a task group, serial queue, or asynchronous queue. It cannot call **execute()** again or have a dependency relationship. |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md#executePeriodically) | Executes a generic task periodically, without verifying the parameter type and return value type of the task. The verification of the **executePeriodically** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**. |
| [getTask](arkts-arkts-taskpool-gettask-f.md#getTask) | Obtains the corresponding task instance by task ID, or by task ID and task name. > **NOTE：**> > - If no task instance is found based on the input task ID, **undefined** is returned. > > - If the corresponding task instance can be queried based on the input task ID but the thread that calls the > **getTask** method is different from the thread that creates the task instance, **undefined** is returned. > > - If taskId and taskName are both passed, and the name of the task instance queried via task ID does not match > the provided task name, **undefined** is returned. |
| [getTaskPoolInfo](arkts-arkts-taskpool-gettaskpoolinfo-f.md#getTaskPoolInfo) | Obtains the thread information and task information of the task pool. |
| [isConcurrent](arkts-arkts-taskpool-isconcurrent-f.md#isConcurrent) | Checks whether a function is a concurrent function. |
| [terminateTask](arkts-arkts-taskpool-terminatetask-f.md#terminateTask) | Terminates a continuous task in the task pool. It is called after the continuous task is complete. After the task is terminated, the thread that executes the task may be reclaimed. |

### Classes

| Name | Description |
| --- | --- |
| [AsyncRunner](arkts-arkts-taskpool-asyncrunner-c.md) | Implements an asynchronous queue, for which you can specify the task execution concurrency and queuing policy. |
| [GenericsTask](arkts-arkts-taskpool-genericstask-c.md) | Implements a generic task. **GenericsTask** inherits from [Task](arkts-arkts-taskpool-execute-f.md#execute). During the creation of a generic task, the passed-in parameter types and return value types of concurrent functions are verified in the compilation phase. Other behaviors are the same as those during the creation of a task. |
| [LongTask](arkts-arkts-taskpool-longtask-c.md) | Describes a continuous task. **LongTask** inherits from [Task](arkts-arkts-taskpool-execute-f.md#execute). No upper limit is set for the execution time of a continuous task, and no timeout exception is thrown if a continuous task runs for a long period of time. However, a continuous task cannot be executed in a task group or executed for multiple times. The thread for executing a continuous task exists until [terminateTask](arkts-arkts-taskpool-terminatetask-f.md#terminateTask) is called after the execution is complete. The thread is reclaimed when it is idle. |
| [SequenceRunner](arkts-arkts-taskpool-sequencerunner-c.md) | Implements a serial queue, in which all tasks are executed in sequence. |
| [Task](arkts-arkts-taskpool-task-c.md) | Enumerates tasks, which can be executed for multiple times, placed in a task group, serial queue, or asynchronous queue for execution, or added with dependencies for execution. |
| [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Implements a task group, in which tasks are associated with each other and all tasks are executed at a time. If all the tasks are executed normally, an array of task results is returned asynchronously, and the sequence of elements in the array is the same as the sequence of tasks added by calling [addTask](arkts-arkts-taskpool-taskgroup-c.md#addTask). If any task fails, the corresponding exception is thrown. If multiple tasks in the task group fail, the exception of the first failed task is thrown. A task group can be executed for multiple times, but no task can be added after the task group is executed. |
| [TaskInfo](arkts-arkts-taskpool-taskinfo-c.md) | Describes the internal information about a task. |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) | Describes the internal information about a task pool. |
| [ThreadInfo](arkts-arkts-taskpool-threadinfo-c.md) | Describes the internal information about a worker thread. |

### Interfaces

| Name | Description |
| --- | --- |
| [Configs](arkts-arkts-taskpool-configs-i.md) | Defines the task configs interface |
| [TaskResult](arkts-arkts-taskpool-taskresult-i.md) | Describes the supplementary information captured in **BusinessError** in the catch branch after a task in the waiting or execution phase is canceled. In other scenarios, the task result is **undefined**. |

### Enums

| Name | Description |
| --- | --- |
| [Priority](arkts-arkts-taskpool-priority-e.md) | Enumerates the priorities available for created tasks. The task priority applies during task execution. The worker thread priority is updated with the task priority. For details about the mappings, see QoS Level. |
| [State](arkts-arkts-taskpool-state-e.md) | Enumerates the task states. After a task is created and **execute()** is called, the task is placed in the internal queue of the task pool and the state is **WAITING**. When the task is being executed by the worker thread of the task pool, the state changes to **RUNNING**. After the task is executed and the result is returned, the state is reset to **WAITING**. When the task is proactively canceled, the state changes to **CANCELED**. |

### Types

| Name | Description |
| --- | --- |
| [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | Describes a callback function. |
| [CallbackFunctionWithError](arkts-arkts-taskpool-callbackfunctionwitherror-t.md) | Describes a callback function with an error message. |

