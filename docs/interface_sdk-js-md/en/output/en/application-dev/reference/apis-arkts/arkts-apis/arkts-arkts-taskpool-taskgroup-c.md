# TaskGroup

Implements a task group, in which tasks are associated with each other and all tasks are executed at a time. If all the tasks are executed normally, an array of task results is returned asynchronously, and the sequence of elements in the array is the same as the sequence of tasks added by calling [addTask]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. If any task fails, the corresponding exception is thrown. If multiple tasks in the task group fail, the exception of the first failed task is thrown. A task group can be executed for multiple times, but no task can be added after the task group is executed.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-class TaskGroup--><!--Device-taskpool-class TaskGroup-End-->

**System capability:** SystemCapability.Utils.Lang

## addTask

```TypeScript
addTask(func: Function, ...args: Object[]): void
```

Adds the function to be executed to this task group. Before using this API, you must create a **TaskGroup** instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void--><!--Device-TaskGroup-addTask(func: Function, ...args: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | Function that must be decorated using \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. For details about the supported return value types, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| args | Object[] | Yes | Arguments of the function. For details about the supported parameter types, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. The default value is **undefined**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) | The function is not marked as concurrent. |

**Example**

```TypeScript
@Concurrent
function printArgs(args: number): number {
  console.info("printArgs: " + args);
  return args;
}

let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
taskGroup.addTask(printArgs, 100); // 100: test number
```

## addTask

```TypeScript
addTask(task: Task): void
```

Adds a created task to this task group. Before using this API, you must create a **TaskGroup** instance. Tasks in another task group, serial queue, or asynchronous queue, dependent tasks, continuous tasks, tasks that have been executed, and periodic tasks cannot be added to the task group.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-addTask(task: Task): void--><!--Device-TaskGroup-addTask(task: Task): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Task to be added to the task group. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) | The function is not marked as concurrent. |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) | The periodic task cannot be executed again.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) | The task cannot be executed by two APIs.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 18 and later |

**Example**

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

## constructor

```TypeScript
constructor()
```

Constructor used to create a **TaskGroup** instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-constructor()--><!--Device-TaskGroup-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Example**

```TypeScript
let taskGroup = new taskpool.TaskGroup();
```

## constructor

```TypeScript
constructor(name: string)
```

A constructor used to create a **TaskGroup** instance, with the task group name specified.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-constructor(name: string)--><!--Device-TaskGroup-constructor(name: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Task group name. |

**Example**

```TypeScript
let taskGroupName: string = "groupName";
let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup(taskGroupName);
let name: string = taskGroup.name;
```

## name

```TypeScript
name: string
```

Name of the task group specified when the task group is created.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskGroup-name: string--><!--Device-TaskGroup-name: string-End-->

**System capability:** SystemCapability.Utils.Lang

