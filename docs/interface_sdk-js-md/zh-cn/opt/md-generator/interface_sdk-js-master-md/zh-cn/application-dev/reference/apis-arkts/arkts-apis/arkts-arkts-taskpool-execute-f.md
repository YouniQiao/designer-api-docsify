# execute

## execute

```TypeScript
function execute(func: Function, ...args: Object[]): Promise<Object>
```

将待执行的函数放入taskpool的内部任务队列，函数不会立即执行，而是等待分发到工作线程执行。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>--><!--Device-taskpool-function execute(func: Function, ...args: Object[]): Promise<Object>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200003-worker初始化失败) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

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

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-taskpool-function execute(task: Task, priority?: Priority): Promise<Object>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200057](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200003-worker初始化失败) |
| [10200051](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

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

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200057](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

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

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200059](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200059-任务组不能重复执行) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

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
  console.info("Succeeded in executing task, res is:" + res);
});
taskpool.execute(taskGroup2).then((res: Array<Object>) => {
  console.info("Succeeded in executing task, res is:" + res);
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

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>--><!--Device-taskpool-function execute(task: Task, configs: Configs): Promise<Object>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200058](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200058-任务执行超时) |
| [10200057](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

```TypeScript
@Concurrent
function printArgs(args: number, time: number): number {
  let start = Date.now();
  while (Date.now() - start < time) {
    continue;
  }
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, 100, 1000);
let config: taskpool.Configs = { timeout: 500, priority: taskpool.Priority.HIGH };
taskpool.execute(task, config).catch((e: BusinessError) => {
  // Failed to execute task. Code: 10200058, message: Task timed out.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
})
try {
  taskpool.execute(task, { timeout: 500 });
} catch (e) {
  // Failed to execute task. Code: 10200057, message: The task cannot be executed by two APIs, the timeout task cannot be executed again.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
}
```


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>
```

将创建好的泛型任务放入taskpool的内部任务队列，使用Promise异步回调。execute任务的类型校验与GenericsTask的构造类型相关联，参数类型和返回值类型需与new GenericsTask时指定的类型保持一致。

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

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>--><!--Device-taskpool-function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200058](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200058-任务执行超时) |
| [10200057](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |

## 示例

```TypeScript
@Concurrent
function printArgs(args: number, time: number): number {
  let start = Date.now();
  while (Date.now() - start < time) {
    continue;
  }
  return args;
}

let task: taskpool.Task = new taskpool.GenericsTask<[number, number], number>(printArgs, 100, 1000);
let config: taskpool.Configs = { timeout: 500, priority: taskpool.Priority.MEDIUM };
taskpool.execute<[number, number], number>(task, config).catch((e: BusinessError) => {
  // Failed to execute task. Code: 10200058, message: Task timed out.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
})
try {
  taskpool.execute<[number, number], number>(task, { timeout: 500 });
} catch (e) {
  // Failed to execute task. Code: 10200057, message: The task cannot be executed by two APIs, the timeout task cannot be executed again.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
}
```


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

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>--><!--Device-taskpool-function execute(group: TaskGroup, configs: Configs): Promise<Object[]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200059](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200059-任务组不能重复执行) |
| [10200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200070-任务组执行超时) |

## 示例

```TypeScript
@Concurrent
function printArgs(args: number, time: number): number {
  let start = Date.now();
  while (Date.now() - start < time) {
    continue;
  }
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup.addTask(printArgs, 10, 1000);
let config: taskpool.Configs = {timeout: 500, priority: taskpool.Priority.HIGH};
taskpool.execute(taskGroup, config).catch((e:BusinessError) => {
  // Failed to execute task. Code: 10200070, message: TaskGroup timed out.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
})
try {
  taskpool.execute(taskGroup, config);
} catch (e) {
  // Failed to execute task. Code: 10200059, message: TaskGroup cannot be re-executed, taskGroup has already set timeout.
  console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
}
```
