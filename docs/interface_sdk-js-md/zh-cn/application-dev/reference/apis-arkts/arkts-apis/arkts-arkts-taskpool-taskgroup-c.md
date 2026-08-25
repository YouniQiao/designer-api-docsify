# TaskGroup

表示任务组，一次执行一组任务，适用于执行一组有关联的任务。如果所有任务正常执行，异步执行完毕后返回所有任务结果的数组， 数组中元素的顺序与调用[addTask](#addtask)添加任务的顺序相同。如果任意任务失败， 则会抛出对应异常。如果任务组中存在多个任务失败的情况，则会抛出第一个失败任务的异常。任务组可以多次执行，但执行后不能新增任务。

**起始版本：** 10

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## addTask

```TypeScript
addTask(func: Function, ...args: Object[]): void
```

将待执行的函数添加到任务组中。使用该方法前需要先构造**TaskGroup**实例。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |

## addTask

```TypeScript
addTask(task: Task): void
```

将创建好的任务添加到任务组中。使用此方法前需要先构造**TaskGroup**实例。任务组不能添加其他任务组中的任务、串行队列任务、 异步队列任务、有依赖关系的任务、长时任务、周期任务和已执行的任务。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |

## constructor

```TypeScript
constructor()
```

TaskGroup的构造函数。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(name: string)
```

TaskGroup的构造函数，支持指定任务组名称。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |

## name

```TypeScript
name: string
```

创建任务组时指定的任务组名称。

**类型：** string

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
