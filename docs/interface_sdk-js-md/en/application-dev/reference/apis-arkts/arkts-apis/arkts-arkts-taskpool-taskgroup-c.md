# TaskGroup

Implements a task group, in which tasks are associated with each other and all tasks are executed at a time. If all the tasks are executed normally, an array of task results is returned asynchronously, and the sequence of elements in the array is the same as the sequence of tasks added by calling [addTask](#addtask). If any task fails, the corresponding exception is thrown. If multiple tasks in the task group fail, the exception of the first failed task is thrown. A task group can be executed for multiple times, but no task can be added after the task group is executed.

**Since:** 10

<!--Device-taskpool-class TaskGroup--><!--Device-taskpool-class TaskGroup-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## addTask

```TypeScript
addTask(func: Function, ...args: Object[]): void
```

Adds the function to be executed to this task group. Before using this API, you must create a **TaskGroup** instance.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void--><!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | Function that must be decorated using [@Concurrent](../../../arkts-utils/taskpool-introduction.md#concurrent-decorator). For details about the supported return value types, see Sequenceable Data Types. |
| args | Object[] | Yes | Arguments of the function. For details about the supported parameter types, see Sequenceable Data Types. The default value is **undefined**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) | The function is not marked as concurrent. |

**Examples**

```TypeScript
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup.addTask(printArgs, 100); // 100: test number
```

```TypeScript
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
let task: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
taskGroup.addTask(task);
```

## addTask

```TypeScript
addTask(task: Task): void
```

Adds a created task to this task group. Before using this API, you must create a **TaskGroup** instance. Tasks in another task group, serial queue, or asynchronous queue, dependent tasks, continuous tasks, tasks that have been executed, and periodic tasks cannot be added to the task group.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-addTask(task: Task): void--><!--Device-TaskGroup-addTask(task: Task): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | Task | Yes | Task to be added to the task group. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) | The function is not marked as concurrent. |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) | The periodic task cannot be executed again.<br>**Applicable version:** 12 and later |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |

**Examples**

See [addTask](#addtask)

## constructor

```TypeScript
constructor()
```

Constructor used to create a **TaskGroup** instance.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-constructor()--><!--Device-TaskGroup-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

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
constructor(name: string)
```

A constructor used to create a **TaskGroup** instance, with the task group name specified.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-constructor(name: string)--><!--Device-TaskGroup-constructor(name: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Task group name. |

**Examples**

See [constructor](#constructor)

## name

```TypeScript
name: string
```

Name of the task group specified when the task group is created.

**Type:** string

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-name: string--><!--Device-TaskGroup-name: string-End-->

**System capability:** SystemCapability.Utils.Lang

