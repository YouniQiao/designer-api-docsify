# Task

Enumerates tasks, which can be executed for multiple times, placed in a task group, serial queue, or asynchronous queue for execution, or added with dependencies for execution.

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## addDependency

```TypeScript
addDependency(...tasks: Task[]): void
```

Adds dependent tasks for this task. Before using this API, you must create a **Task** instance. The task and its dependent tasks cannot be a task in a task group, serial queue, or asynchronous queue, a task that has been executed, or a periodic task. A task with a dependency relationship (a task that depends on another task or a task that is depended on) cannot be executed multiple times.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tasks | [Task[]](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200026](../errorcode-utils.md#10200026-task-with-a-cyclic-dependency) |
| [10200052](../errorcode-utils.md#10200052-periodic-task-cannot-have-dependencies) |
| [10200056](../errorcode-utils.md#10200056-asynchronous-queue-task-cannot-have-dependencies) |

## constructor

```TypeScript
constructor(func: Function, ...args: Object[])
```

A constructor used to create a **Task** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |

## constructor

```TypeScript
constructor(name: string, func: Function, ...args: Object[])
```

A constructor used to create a **Task** instance, with the task name specified.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [name](#name) | string | Yes |
| func | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |

## isCanceled

```TypeScript
static isCanceled(): boolean
```

Checks whether the running task is canceled. Before using this method, you need to create a **Task** object.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isDone

```TypeScript
isDone(): boolean
```

Checks whether the task is complete.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## onEnqueued

```TypeScript
onEnqueued(callback: CallbackFunction): void
```

Register a callback function and call it when a task is enqueued. The registration must be carried out before the task is executed. Otherwise, an exception is thrown.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-no-callback-function-is-registered-for-a-listening-task) |

## onExecutionFailed

```TypeScript
onExecutionFailed(callback: CallbackFunctionWithError): void
```

Register a callback function and call it when a task fails to be executed(Periodic tasks are not supported). The registration must be carried out before the task is executed. Otherwise, an exception is thrown.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CallbackFunctionWithError](arkts-arkts-taskpool-callbackfunctionwitherror-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-no-callback-function-is-registered-for-a-listening-task) |

## onExecutionSucceeded

```TypeScript
onExecutionSucceeded(callback: CallbackFunction): void
```

Register a callback function and call it when a task is executed successfully. The registration must be carried out before the task is executed. Otherwise, an exception is thrown.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-no-callback-function-is-registered-for-a-listening-task) |

## onReceiveData

```TypeScript
onReceiveData(callback?: Function): void
```

Registers a callback for a task to receive and process data from the worker thread. Before using this API, you must create a Task instance. NOTE: If multiple callbacks are registered for the same task, only the last registration takes effect.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Function | No |

## onStartExecution

```TypeScript
onStartExecution(callback: CallbackFunction): void
```

Register a callback function and call it when the execution of a task starts. The registration must be carried out before the task is executed. Otherwise, an exception is thrown.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-no-callback-function-is-registered-for-a-listening-task) |

## removeDependency

```TypeScript
removeDependency(...tasks: Task[]): void
```

Removes dependent tasks for this task. Before using this method, you need to construct a **Task** object.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tasks | [Task[]](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200027](../errorcode-utils.md#10200027-dependency-does-not-exist) |
| [10200052](../errorcode-utils.md#10200052-periodic-task-cannot-have-dependencies) |
| [10200056](../errorcode-utils.md#10200056-asynchronous-queue-task-cannot-have-dependencies) |

## sendData

```TypeScript
static sendData(...args: Object[]): void
```

Sends data to the host thread and triggers the registered callback. Before calling this method, you need to construct a **Task** object.

> **NOTE：**&gt;
> - The API should be called in the TaskPool thread.&gt;
> - Do not use this API in a callback function. Otherwise, messages may fail to be passed to the host thread.&gt;
> - Do not use this API in an asynchronous function. Otherwise, messages may fail to be passed to the host
> thread. If this API is used in an asynchronous function, use **await** to ensure that the asynchronous function
> is executed synchronously in the task.&gt;
> - Before calling this API, ensure that the callback function for processing data has been registered in the
> host thread.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200022](../errorcode-utils.md#10200022-functions-not-called-in-taskpool) |
| [10200023](../errorcode-utils.md#10200023-functions-not-called-in-concurrent-functions) |
| [10200024](../errorcode-utils.md#10200024-functions-not-registered-in-the-host-thread) |

## setCloneList

```TypeScript
setCloneList(cloneList: Object[] | ArrayBuffer[]): void
```

Sets the task clone list. Before using this method, you need to construct a **Task** object.

> **NOTE：**&gt;
> This API must be used together with the
> [@Sendable decorator](../../../arkts-utils/arkts-sendable.md#sendable-decorator). Otherwise, an exception is
> thrown. You are advised to use this decorator to avoid exceptions.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cloneList | Object[] \| ArrayBuffer[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200029](../errorcode-utils.md#10200029-arraybuffer-cannot-be-set-as-both-transferlist-and-clonelist) |

## setTransferList

```TypeScript
setTransferList(transfer?: ArrayBuffer[]): void
```

Sets the task transfer list. Before using this API, you must create a **Task** instance. If this API is not called, the ArrayBuffer in the data is transferred by default.

> **NOTE：**&gt;
> This API is used to set the task transfer list in the form of **ArrayBuffer** in the task pool. The
> **ArrayBuffer** instance does not copy the content in the task to the worker thread during transfer. Instead,
> it transfers the buffer control right to the worker thread. After the transfer, the **ArrayBuffer** instance
> becomes invalid. An empty **ArrayBuffer** will not be transferred.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200029](../errorcode-utils.md#10200029-arraybuffer-cannot-be-set-as-both-transferlist-and-clonelist) |

## arguments

```TypeScript
arguments?: Object[]
```

Arguments of the function. For details about the supported parameter types, see [Sequenceable Data Types](../../../reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).This API can be used in atomic services since API version 11.

**Type:** Object[]

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## cpuDuration

```TypeScript
cpuDuration: number
```

CPU time of the task. in ms. You are advised not to change the value.This API can be used in atomic services since API version 11.

**Type:** number

**Default:** 0

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## function

```TypeScript
function: Function
```

Function to be passed in during task creation. For details about the supported return value types of the function, see [Sequenceable Data Types](../../../reference/apis-arkts/js-apis-taskpool.md#sequenceable-data-types).This API can be used in atomic services since API version 11.

**Type:** Function

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## ioDuration

```TypeScript
ioDuration: number
```

Asynchronous I/O time of the task. in ms. You are advised not to change the value.This API can be used in atomic services since API version 11.

**Type:** number

**Default:** 0

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## name

```TypeScript
name: string
```

Name of the task specified when the task is created. You are advised not to change the value.This API can be used in atomic services since API version 11.

**Type:** string

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## taskId

```TypeScript
taskId: number
```

Task ID, which is globally unique by default. You are advised not to change the value.This API can be used in atomic services since API version 18.

**Type:** number

**Default:** 0

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Utils.Lang

## totalDuration

```TypeScript
totalDuration: number
```

Total execution time of the task. in ms. You are advised not to change the value.This API can be used in atomic services since API version 11.

**Type:** number

**Default:** 0

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang
