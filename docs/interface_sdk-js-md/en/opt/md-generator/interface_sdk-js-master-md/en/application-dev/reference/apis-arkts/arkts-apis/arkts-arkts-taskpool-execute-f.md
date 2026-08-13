# execute

## Modules to Import

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## execute

```TypeScript
function execute(func: Function, ...args: Object[]): Promise<Object>
```

Places a function to be executed in the internal queue of the task pool. The function is not executed immediately. It waits to be distributed to the worker thread for execution. In this mode, the function cannot be canceled. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>--><!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

taskpool.execute(printArgs, 100).then((value: Object) => { // 100: test number
  console.info("taskpool result: " + value);
});
```


## execute

```TypeScript
function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>
```

Verifies the passed-in parameter types and return value type of a concurrent function, and places the function in the queue of the task pool. This API uses a promise to return the result.

**Since:** 13

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

@Concurrent
function testWithThreeParams(a: number, b: string, c: number): string {
  return b;
}

@Concurrent
function testWithArray(args: [number, string]): string {
  return "success";
}

taskpool.execute<[number], number>(printArgs, 100).then((value: number) => { // 100: test number
  console.info("taskpool result: " + value); // "taskpool result: 100"
});

taskpool.execute<[number, string, number], string>(testWithThreeParams, 100, "test", 100).then((value: string) => {
  console.info("taskpool result: " + value); // "taskpool result: test"
});

taskpool.execute<[[number, string]], string>(testWithArray, [100, "test"]).then((value: string) => {
  console.info("taskpool result: " + value); // "taskpool result: success"
});
```


## execute

```TypeScript
function execute(task: Task, priority?: Priority): Promise<Object>
```

Places a task in the internal queue of the task pool. The task will not be executed immediately; instead, it waits to be distributed to a worker thread for execution. In the current mode, you can set the task priority and cancel the task. Note that the task cannot belong to a task group, serial queue, or asynchronous queue. For non-continuous tasks, this API can be called multiple times. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
taskpool.execute(task1, taskpool.Priority.LOW).then((value: Object) => {
  console.info("taskpool result1: " + value);
});
taskpool.execute(task2, taskpool.Priority.MEDIUM).then((value: Object) => {
  console.info("taskpool result2: " + value);
});
taskpool.execute(task3, taskpool.Priority.HIGH).then((value: Object) => {
  console.info("taskpool result3: " + value);
});
```


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>
```

Places the generic task in the internal queue of the task pool. The parameter type and return value type of the task are not verified. This API uses a promise to return the result. The verification of the **execute** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**.

**Since:** 13

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let task1: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 300); // 300: test number
taskpool.execute<[number], number>(task1, taskpool.Priority.LOW).then((value: number) => {
  console.info("taskpool result1: " + value);
});
taskpool.execute<[number], number>(task2, taskpool.Priority.MEDIUM).then((value: number) => {
  console.info("taskpool result2: " + value);
});
taskpool.execute<[number], number>(task3, taskpool.Priority.HIGH).then((value: number) => {
  console.info("taskpool result3: " + value);
});
```


## execute

```TypeScript
function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>
```

Places a task group in the internal queue of the task pool. The tasks in the task group are not executed immediately. They wait to be distributed to the worker thread for execution. After all tasks in the task group are executed, a result array is returned. This mode is applicable to the execution of associated tasks. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 10200059 |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): number {
    console.info("printArgs: " + args);
    return args;
}

let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup1.addTask(printArgs, 10); // 10: test number
taskGroup1.addTask(printArgs, 20); // 20: test number
taskGroup1.addTask(printArgs, 30); // 30: test number

let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
taskGroup2.addTask(task1);
taskGroup2.addTask(task2);
taskGroup2.addTask(task3);
taskpool.execute(taskGroup1).then((res: Array<Object>) => {
  console.info("taskpool execute res is:" + res);
});
taskpool.execute(taskGroup2).then((res: Array<Object>) => {
  console.info("taskpool execute res is:" + res);
});
```


## execute

```TypeScript
function execute(task: Task, configs: Configs): Promise<Object>
```

Execute a concurrent task with Configs.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>--><!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 10200058 |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>
```

Execute a concurrent generics task with Configs.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 10200058 |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |


## execute

```TypeScript
function execute(group: TaskGroup, configs: Configs): Promise<Object[]>
```

Execute a concurrent task group with Configs.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 10200059 |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| 10200070 |
