# GenericsTask

Implements a generic task. **GenericsTask** inherits from [Task](arkts-arkts-taskpool-execute-f.md#execute). During the creation of a generic task, the passed-in parameter types and return value types of concurrent functions are verified in the compilation phase. Other behaviors are the same as those during the creation of a task.

**Inheritance/Implementation:** GenericsTask extends [Task](arkts-arkts-taskpool-task-c.md#task)

**Since:** 13

<!--Device-taskpool-class GenericsTask--><!--Device-taskpool-class GenericsTask-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(func: (...args: A) => R | Promise<R>, ...args: A)
```

A constructor used to create a **GenericsTask** object.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-GenericsTask-constructor(func: (...args: A) => R | Promise<R>, ...args: A)--><!--Device-GenericsTask-constructor(func: (...args: A) => R | Promise<R>, ...args: A)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |

**Examples**

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

## constructor

```TypeScript
constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)
```

A constructor used to create a **GenericsTask** instance, with the task name specified.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-GenericsTask-constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)--><!--Device-GenericsTask-constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-nonconcurrent-function-error) |

**Examples**

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
