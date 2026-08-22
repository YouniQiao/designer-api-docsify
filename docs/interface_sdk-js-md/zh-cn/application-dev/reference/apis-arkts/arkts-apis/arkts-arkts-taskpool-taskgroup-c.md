# TaskGroup

表示任务组，一次执行一组任务，适用于执行一组有关联的任务。如果所有任务正常执行，异步执行完毕后返回所有任务结果的数组， 数组中元素的顺序与调用[addTask](#addtask)添加任务的顺序相同。如果任意任务失败， 则会抛出对应异常。如果任务组中存在多个任务失败的情况，则会抛出第一个失败任务的异常。任务组可以多次执行，但执行后不能新增任务。

**起始版本：** 10

<!--Device-taskpool-class TaskGroup--><!--Device-taskpool-class TaskGroup-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## addTask

```TypeScript
addTask(func: Function, ...args: Object[]): void
```

将待执行的函数添加到任务组中。使用该方法前需要先构造**TaskGroup**实例。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void--><!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | Function | 是 | 待执行的函数，必须使用 [@Concurrent装饰器](../../../arkts-utils/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考 序列化支持类型。 |
| args | Object[] | 是 | 任务执行函数的入参，支持的参数类型请参考 序列化支持类型。默认值为**undefined**。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) | The function is not marked as concurrent. |

**示例**

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

将创建好的任务添加到任务组中。使用此方法前需要先构造**TaskGroup**实例。任务组不能添加其他任务组中的任务、串行队列任务、 异步队列任务、有依赖关系的任务、长时任务、周期任务和已执行的任务。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TaskGroup-addTask(task: Task): void--><!--Device-TaskGroup-addTask(task: Task): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | Task | 是 | 需要添加到任务组中的任务。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) | The function is not marked as concurrent. |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) | The periodic task cannot be executed again.<br>**适用版本：** 12+ |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) | The task cannot be executed by two APIs.<br>**适用版本：** 18+ |

**示例**

参见 [addTask](#addtask)

## constructor

```TypeScript
constructor()
```

TaskGroup的构造函数。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TaskGroup-constructor()--><!--Device-TaskGroup-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

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
constructor(name: string)
```

TaskGroup的构造函数，支持指定任务组名称。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TaskGroup-constructor(name: string)--><!--Device-TaskGroup-constructor(name: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 任务组名称。 |

**示例**

参见 [constructor](#constructor)

## name

```TypeScript
name: string
```

创建任务组时指定的任务组名称。

**类型：** string

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TaskGroup-name: string--><!--Device-TaskGroup-name: string-End-->

**系统能力：** SystemCapability.Utils.Lang

