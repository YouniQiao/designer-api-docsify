# execute

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## execute

```TypeScript
function execute(func: Function, ...args: Object[]): Promise<Object>
```

将待执行的函数放入taskpool的内部任务队列，函数不会立即执行，而是等待分发到工作线程执行。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>--><!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | 待执行的函数，必须使用 [@Concurrent装饰器](../../../arkts-utils/taskpool-introduction.md#concurrent装饰器)装饰。支持的函数返回值类型请参考 [序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。 |
| args | Object[] | Yes | 任务执行函数的入参，支持的参数类型请参考 [序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。默认值为**undefined**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;unknown&gt; | <br>**Applicable version:** 9 - 11 |
| Promise&lt;Object&gt; | Promise对象，返回任务函数的执行结果。<br>**Applicable version:** 11 and later |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200014 | The function is not marked as concurrent. |
| 10200003 | Worker initialization failed.<br>**Applicable version:** 9 - 11 |
| 10200006 | An exception occurred during serialization. |

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

校验并发函数的参数类型和返回类型后，将函数添加到taskpool的任务队列。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | (...args: A) =&gt; R \| Promise&lt;R&gt; | Yes | 待执行的函数，必须使用 [@Concurrent装饰器](../../../arkts-utils/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考 [序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。 |
| args | A | Yes | 任务执行函数的入参，支持的参数类型请参考 [序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。默认值为**undefined**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;R&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200014 | The function is not marked as concurrent. |
| 10200006 | An exception occurred during serialization. |

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

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级和通过cancel取消任务。使用Promise异步回调。

> **说明：**
> 
> - 任务不能是任务组任务、串行队列任务或异步队列任务。
> - 长时任务只能调用一次，非长时任务可以多次调用执行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes | 需要在任务池中执行的任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 等待执行的任务的优先级，默认值为 **taskpool.Priority.MEDIUM**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;unknown&gt; | <br>**Applicable version:** 9 - 17 |
| Promise&lt;Object&gt; | Promise对象，返回任务函数的执行结果。<br>**Applicable version:** 11 and later |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200014 | The function is not marked as concurrent. |
| 10200003 | Worker initialization failed.<br>**Applicable version:** 9 - 17 |
| 10200051 | The periodic task cannot be executed again.<br>**Applicable version:** 12 and later |
| 10200006 | An exception occurred during serialization. |

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

将创建好的泛型任务放入taskpool的内部任务队列，校验任务的参数类型和返回值类型。使用Promise异步回调。execute任务的校验是结合**new GenericsTask**一起用的，参数、返回值类型需与**new GenericsTask**中的类型保持一致。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes | 需要在任务池中执行的泛型任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 等待执行的任务的优先级，默认值为 **taskpool.Priority.MEDIUM**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;R&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200006 | An exception occurred during serialization. |

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

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后，结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes | 需要在任务池中执行的任务组。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 等待执行的任务组的优先级，该参数默认值为**taskpool.Priority.MEDIUM**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object[]&gt; | Promise对象数组，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200059 | TaskGroup cannot be re-executed.<br>**Applicable version:** 24 and later |
| 10200006 | An exception occurred during serialization. |

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

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级、设置超时时间和通过cancel取消任务。使用Promise异步回调。

> **说明：**
> 
> - 不支持执行任务组任务。
> 
> - 不支持执行串行队列任务。
> 
> - 不支持执行异步队列任务。
> 
> - 不支持执行周期性任务。
> 
> - 不支持执行延迟任务。
> 
> - 不支持执行存在依赖的任务。
> 
> - 不支持任务重复执行。
> 
> - 设置过超时的任务无法被其他任务依赖，也无法依赖其他任务。
> 
> - 如果任务设置了失败监听，任务执行超时了，失败监听不会被触发。
> 
> - 如果任务使用sendData来往宿主线程发消息，任务超时之后，宿主线程不再接收到消息。
> 
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>--><!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes | 需要在任务池中执行的任务。 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes | 该参数可以设置超时时间和任务优先级。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200058 | Task timed out. |
| 10200057 | The task cannot be executed by two APIs. |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200006 | An exception occurred during serialization. |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>
```

将创建好的泛型任务放入taskpool的内部任务队列，不校验任务的参数类型和返回值类型。使用Promise异步回调。execute任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

> **说明：**
> 
> - 不支持执行任务组任务。
> 
> - 不支持执行串行队列任务。
> 
> - 不支持执行异步队列任务。
> 
> - 不支持执行周期性任务。
> 
> - 不支持执行延迟任务。
> 
> - 不支持执行存在依赖的任务。
> 
> - 不支持任务重复执行。
> 
> - 设置过超时的任务无法被其他任务依赖，也无法依赖其他任务。
> 
> - 如果任务设置了失败监听，任务执行超时了，失败监听不会被触发。
> 
> - 如果任务使用sendData来往宿主线程发消息，任务超时之后，宿主线程不再接收到消息。
> 
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes | 需要在任务池中执行的泛型任务。 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes | 该参数可以设置超时时间和任务优先级。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;R&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200058 | Task timed out. |
| 10200057 | The task cannot be executed by two APIs. |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200006 | An exception occurred during serialization. |


## execute

```TypeScript
function execute(group: TaskGroup, configs: Configs): Promise<Object[]>
```

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后，结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。configs配置里可以指定任务组执行的超时时间和优先级。指定的超时时间到了，但是任务组还未完成，则会抛出任务组超时的异常信息。

> **说明：**
> 
> - 不支持任务组重复执行。
> 
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes | 需要在任务池中执行的任务组。 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes | 该参数可以设置超时时间和任务优先级。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object[]&gt; | Promise对象数组，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200059 | TaskGroup cannot be re-executed. |
| 10200006 | An exception occurred during serialization. |
| 10200070 | TaskGroup timed out. |

