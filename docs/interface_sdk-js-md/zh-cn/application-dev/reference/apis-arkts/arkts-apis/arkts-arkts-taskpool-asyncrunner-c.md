# AsyncRunner

表示异步队列。可以指定任务执行的并发度和排队策略。

**起始版本：** 18

<!--Device-taskpool-export class AsyncRunner--><!--Device-taskpool-export class AsyncRunner-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor(runningCapacity: number, waitingCapacity?: number)
```

AsyncRunner的构造函数，用于创建一个**AsyncRunner**实例。构造一个非全局的异步队列，即使传入的参数相同， 也会返回不同的异步队列。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| runningCapacity | number | 是 | 指定任务执行的最大并发度，该值必须为正整数。如果传入负数，会报错；如果传入非整数， 会向下取整。 |
| waitingCapacity | number | 否 | 指定等待任务的列表容量，该值必须大于等于0。如果传入负数，会报错；如果传入非整数， 会向下取整。默认值为**0**，表示等待任务列表的容量没有限制。如果传入大于0的值，则表示排队策略为丢弃策略，当加入的任务数量 超过该值时，等待列表中处于队头的任务会被丢弃。 |

**示例**

```TypeScript
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, "this is my first Task");
```

```TypeScript
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let taskName: string = "taskName";
let task: taskpool.Task = new taskpool.Task(taskName, printArgs, "this is my first Task");
let name: string = task.name;
```

```TypeScript
@Concurrent
function printArgs(args: string): string {
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

let task1: taskpool.Task = new taskpool.GenericsTask<[string], string>(printArgs, "this is my first GenericsTask");

let task2: taskpool.Task = new taskpool.GenericsTask<[number, string, number], string>(testWithThreeParams, 100, "test", 100);

let task3: taskpool.Task = new taskpool.GenericsTask<[[number, string]], string>(testWithArray, [100, "test"]);
```

```TypeScript
@Concurrent
function printArgs(args: string): string {
  console.info("printArgs: " + args);
  return args;
}

let taskName: string = "taskName";
let task: taskpool.Task = new taskpool.GenericsTask<[string], string>(taskName, printArgs, "this is my first Task");
let name: string = task.name;
```

```TypeScript
let taskGroup = new taskpool.TaskGroup();
```

```TypeScript
let taskGroupName: string = "groupName";
let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup(taskGroupName);
let name: string = taskGroup.name;
```

```TypeScript
let runner: taskpool.SequenceRunner = new taskpool.SequenceRunner();
```

```TypeScript
let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner("runner1", taskpool.Priority.LOW);
```

```TypeScript
let runner: taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
```

```TypeScript
let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
```

## constructor

```TypeScript
constructor(name: string, runningCapacity: number, waitingCapacity?: number)
```

AsyncRunner的构造函数，用于创建一个**AsyncRunner**实例。构造一个全局异步队列，如果队列名称与已有名称相同， 将返回同一个异步队列。

> **说明：**&gt;
> - 底层通过单例模式确保创建同名的异步队列时，获取同一个实例。&gt;
> - 无法修改并发度和等待任务列表容量。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 异步队列的名字。 |
| runningCapacity | number | 是 | 指定任务执行的最大并发度，该值必须为正整数。如果传入负数，会报错；如果传入非整数， 会向下取整。 |
| waitingCapacity | number | 否 | 指定等待任务的列表容量，该值必须大于等于0。如果传入负数，会报错；如果传入非整数， 会向下取整。默认值为**0**，表示等待任务列表的容量没有限制。如果传入大于0的值，则表示排队策略为丢弃策略，当加入的任务数量 超过该值时，等待列表中处于队头的任务会被丢弃。 |

**示例**

参见 [constructor](#constructor)

## execute

```TypeScript
execute(task: Task, priority?: Priority): Promise<Object>
```

执行异步任务。使用该方法前需要先构造**AsyncRunner**实例。使用Promise异步回调。

> **说明：**&gt;
> - 不支持执行任务组中的任务。&gt;
> - 不支持执行串行队列中的任务。&gt;
> - 不支持执行其他异步队列任务。&gt;
> - 不支持执行周期性任务。&gt;
> - 不支持执行延迟任务。&gt;
> - 不支持执行存在依赖的任务。&gt;
> - 不支持执行已执行过的任务。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | Task | 是 | 需要添加到异步队列中的任务。 |
| priority | Priority | 否 | 指定任务的优先级，默认值为**taskpool.Priority.MEDIUM**。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Object&gt; | Promise对象，返回任务执行的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) | An exception occurred during serialization. |
| [10200025](../errorcode-utils.md#10200025-串行队列中添加了存在依赖的任务) | dependent task not allowed. |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) | The periodic task cannot be executed again. |
| [10200054](../errorcode-utils.md#10200054-异步队列任务被丢弃) | The asyncRunner task is discarded. |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) | The task cannot be executed by two APIs. |

**示例**

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

```TypeScript
@Concurrent
function additionDelay(delay: number): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < delay) {
    continue;
  }
}
@Concurrent
function waitForRunner(finalString: string): string {
  return finalString;
}
async function seqRunner() {
  let finalString:string = "";
  let task1:taskpool.Task = new taskpool.Task(additionDelay, 3000);
  let task2:taskpool.Task = new taskpool.Task(additionDelay, 2000);
  let task3:taskpool.Task = new taskpool.Task(additionDelay, 1000);
  let task4:taskpool.Task = new taskpool.Task(waitForRunner, finalString);

  let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner();
  runner.execute(task1).then(() => {
    finalString += 'a';
    console.info("seqrunner: task1 done.");
  });
  runner.execute(task2).then(() => {
    finalString += 'b';
    console.info("seqrunner: task2 done");
  });
  runner.execute(task3).then(() => {
    finalString += 'c';
    console.info("seqrunner: task3 done");
  });
  await runner.execute(task4);
  console.info("seqrunner: task4 done, finalString is " + finalString);
}
```

```TypeScript
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function additionDelay(delay: number): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < delay) {
    continue;
  }
}
async function asyncRunner() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
  for (let i = 0; i < 30; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    }).catch((e: BusinessError) => {
      console.error("asyncRunner: task" + i + " error." + e.code + "-" + e.message);
    });
  }
}

async function asyncRunner2() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
  for (let i = 0; i < 20; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    });
  }
}
```

