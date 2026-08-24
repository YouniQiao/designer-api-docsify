# AsyncRunner

Implements an asynchronous queue, for which you can specify the task execution concurrency and queuing policy.

**Since:** 18

<!--Device-taskpool-export class AsyncRunner--><!--Device-taskpool-export class AsyncRunner-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor(runningCapacity: number, waitingCapacity?: number)
```

A constructor used to create an **AsyncRunner** instance. It constructs a non-global asynchronous queue. Even when the parameters passed are the same, it returns different asynchronous queues.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| runningCapacity | number | Yes | Maximum number of tasks that can run concurrently. The value must be a positive integer. If a negative number is passed, an error is reported. If a non-integer is passed, the value is rounded down. |
| waitingCapacity | number | No | Maximum number of tasks that can be queued. The value must be greater than or equal to 0. If a negative number is passed, an error is reported. If a non-integer is passed, the value is rounded down. The default value is **0**, indicating that there is no limit to the number of tasks that can wait. If a value greater than 0 is passed, tasks will be discarded from the front of the queue once the queue size exceeds this limit, implementing a discard policy. |

**Examples**

```TypeScript
@Concurrent
function printArgs(args: number): number {
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

let task1: taskpool.Task = new taskpool.GenericsTask<[string], string>(printArgs, "this is my first LongTask");

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

A constructor used to create an **AsyncRunner** instance. It constructs a global asynchronous queue. If the queue name is the same as an existing name, the same asynchronous queue is returned.

> **NOTE：**&gt;
> - The bottom layer uses the singleton mode to ensure that the same instance is obtained when an asynchronous
> queue with the same name is created.&gt;
> - The task execution concurrency and waiting capacity cannot be modified.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of an asynchronous queue. |
| runningCapacity | number | Yes | Maximum number of tasks that can run concurrently. The value must be a positive integer. If a negative number is passed, an error is reported. If a non-integer is passed, the value is rounded down. |
| waitingCapacity | number | No | Maximum number of tasks that can be queued. The value must be greater than or equal to 0. If a negative number is passed, an error is reported. If a non-integer is passed, the value is rounded down. The default value is **0**, indicating that there is no limit to the number of tasks that can wait. If a value greater than 0 is passed, tasks will be discarded from the front of the queue once the queue size exceeds this limit, implementing a discard policy. |

**Examples**

See [constructor](#constructor)

## execute

```TypeScript
execute(task: Task, priority?: Priority): Promise<Object>
```

Adds a task to the asynchronous queue for execution. Before using this API, you must create an **AsyncRunner** instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Tasks in a task group cannot be added to the asynchronous queue.&gt;
> - Tasks in a serial queue cannot be added to the asynchronous queue.&gt;
> - Tasks in other asynchronous queues cannot be added to the asynchronous queue.&gt;
> - Periodic tasks cannot be added to the asynchronous queue.&gt;
> - Delayed tasks cannot be added to the asynchronous queue.&gt;
> - Tasks that depend others cannot be added to the asynchronous queue.&gt;
> - Tasks that have been executed cannot be added to the asynchronous queue.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | Task | Yes | Task to be added to the asynchronous queue. |
| priority | Priority | No | Priority of the task. The default value is **taskpool.Priority.MEDIUM**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object&gt; | Promise used to return the task execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) | An exception occurred during serialization. |
| [10200025](../errorcode-utils.md#10200025-failed-to-add-a-task-with-dependent-tasks-to-the-queue) | dependent task not allowed. |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) | The periodic task cannot be executed again. |
| [10200054](../errorcode-utils.md#10200054-asynchronous-queue-task-discarded) | The asyncRunner task is discarded. |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) | The task cannot be executed by two APIs. |

**Examples**

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
async function asyRunner() {
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

async function asyRunner2() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
  for (let i = 0; i < 20; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    });
  }
}
```

