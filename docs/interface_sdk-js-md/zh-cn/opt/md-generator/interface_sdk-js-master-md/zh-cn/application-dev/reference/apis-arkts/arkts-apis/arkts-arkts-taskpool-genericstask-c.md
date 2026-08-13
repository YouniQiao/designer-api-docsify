# GenericsTask

表示泛型任务。**GenericsTask**继承自 [Task](arkts-arkts-taskpool-execute-f.md#execute)。 相比创建Task，创建GenericsTask可以在编译阶段校验并发函数的传参和返回值类型。其余行为与Task相同。

**继承/实现关系：** GenericsTask extends [Task](arkts-arkts-taskpool-task-c.md#Task)

**起始版本：** 13

**废弃版本：** -1

<!--Device-taskpool-class GenericsTask--><!--Device-taskpool-class GenericsTask-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(func: (...args: A) => R | Promise<R>, ...args: A)
```

GenericsTask的构造函数，用于创建一个**GenericsTask**对象。

**起始版本：** 13

**废弃版本：** -1

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-GenericsTask-constructor(func: (...args: A) => R | Promise<R>, ...args: A)--><!--Device-GenericsTask-constructor(func: (...args: A) => R | Promise<R>, ...args: A)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |

## 示例

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

## constructor

```TypeScript
constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)
```

GenericsTask的构造函数，用于创建一个**GenericsTask**实例，并可指定任务名称。

**起始版本：** 13

**废弃版本：** -1

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-GenericsTask-constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)--><!--Device-GenericsTask-constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |

## 示例

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
