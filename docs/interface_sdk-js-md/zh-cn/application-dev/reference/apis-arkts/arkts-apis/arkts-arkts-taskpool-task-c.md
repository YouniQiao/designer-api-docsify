# Task

调用Task中的任何接口前必须先使用构造函数创建Task对象。任务可以多次执行，也可以放入任务组、串行队列或异步队列执行，还支持添加依赖关系。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## addDependency

```TypeScript
addDependency(...tasks: Task[]): void
```

为当前任务添加对其他任务的依赖。使用该方法前需先构造**Task**实例。该任务和被依赖的任务不能是任务组任务、串行队列任务、 异步队列任务、已执行任务或周期任务。存在依赖关系的任务（依赖其他任务的任务或被依赖的任务）执行后不可再次执行。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tasks | [Task[]](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200026](../errorcode-utils.md#10200026-当前任务存在循环依赖) |
| [10200052](../errorcode-utils.md#10200052-周期性任务不能具有依赖项) |
| [10200056](../errorcode-utils.md#10200056-任务已被asyncrunner执行) |

## constructor

```TypeScript
constructor(func: Function, ...args: Object[])
```

Task的构造函数。

**起始版本：** 9

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

## constructor

```TypeScript
constructor(name: string, func: Function, ...args: Object[])
```

Task的构造函数用于创建任务，并可指定任务名称。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |
| func | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |

## isCanceled

```TypeScript
static isCanceled(): boolean
```

检查当前正在运行的任务是否已取消。使用此方法前，需要先创建一个**Task**对象。

> **说明：**&gt;
> isCanceled方法需要和taskpool.cancel方法搭配使用，如果不调用cancel方法，isCanceled方法默认返回false。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isDone

```TypeScript
isDone(): boolean
```

检查任务是否已完成。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## onEnqueued

```TypeScript
onEnqueued(callback: CallbackFunction): void
```

注册回调函数，任务入队时将调用该函数。需在调用execute前注册，否则会抛异常。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-已执行的任务不支持注册监听器) |

## onExecutionFailed

```TypeScript
onExecutionFailed(callback: CallbackFunctionWithError): void
```

注册回调函数，任务执行失败时调用该回调函数（周期任务不支持）。需在调用execute前注册，否则会抛异常。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CallbackFunctionWithError](arkts-arkts-taskpool-callbackfunctionwitherror-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-已执行的任务不支持注册监听器) |

## onExecutionSucceeded

```TypeScript
onExecutionSucceeded(callback: CallbackFunction): void
```

注册一个回调函数，并在任务执行成功时调用它（周期任务不支持）。需在调用execute前注册，否则会抛异常。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-已执行的任务不支持注册监听器) |

## onReceiveData

```TypeScript
onReceiveData(callback?: Function): void
```

为任务注册回调函数，接收并处理任务池工作线程的数据。使用此方法前，需构造Task。

> **说明：**&gt;
> 该方法与[sendData](#senddata)配对使用。&gt;
> 不支持为同一任务定义多种回调函数。如果多次赋值，只有最后一次赋值的回调函数会生效。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Function | 否 |

## onStartExecution

```TypeScript
onStartExecution(callback: CallbackFunction): void
```

注册回调函数，任务开始执行前将调用该函数。需在调用execute前注册，否则会抛异常。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200034](../errorcode-utils.md#10200034-已执行的任务不支持注册监听器) |

## removeDependency

```TypeScript
removeDependency(...tasks: Task[]): void
```

删除当前任务对其他任务的依赖。在使用该方法之前，需要先构造**Task**对象。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tasks | [Task[]](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200027](../errorcode-utils.md#10200027-依赖关系不存在) |
| [10200052](../errorcode-utils.md#10200052-周期性任务不能具有依赖项) |
| [10200056](../errorcode-utils.md#10200056-任务已被asyncrunner执行) |

## sendData

```TypeScript
static sendData(...args: Object[]): void
```

任务执行过程中向宿主线程发送消息并触发已注册的回调函数。使用此方法前需构造**Task**对象。

> **说明：**&gt;
> - 该接口应在taskpool的线程中调用。&gt;
> - 避免在回调函数中调用该方法，否则可能导致消息无法传递到宿主线程。&gt;
> - 避免在异步函数中调用该方法，否则可能导致消息无法传递到宿主线程。如果在异步函数中使用，
> 则需要使用**await**来确保该异步函数在任务中同步执行完成。&gt;
> - 调用该接口时，请确保处理数据的回调函数已在宿主线程注册。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200022](../errorcode-utils.md#10200022-未在任务池中调用的函数) |
| [10200023](../errorcode-utils.md#10200023-未在并发函数中调用的函数) |
| [10200024](../errorcode-utils.md#10200024-未在宿主线程中注册的函数) |

## setCloneList

```TypeScript
setCloneList(cloneList: Object[] | ArrayBuffer[]): void
```

设置任务的拷贝列表。在使用该方法前，需先构造**Task**对象。

> **说明：**&gt;
> - 此接口与[setTransferList](#settransferlist)互斥：同一个ArrayBuffer不能同时设置在transfer列表和clone列表中。&gt;
> 该接口需搭配
> [@Sendable装饰器](../../../arkts-utils/arkts-sendable.md#sendable装饰器)使用，否则会抛异常。建议开发者使用该装饰器以避免异常。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cloneList | Object[] \| ArrayBuffer[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200029](../errorcode-utils.md#10200029-无法将arraybuffer同时设置为transferlist和clonelist) |

## setTransferList

```TypeScript
setTransferList(transfer?: ArrayBuffer[]): void
```

设置任务的传输列表。使用该方法前需要先构造**Task**。不调用该接口，则传给任务的数据中的ArrayBuffer默认transfer转移。

> **说明：**&gt;
> - 此接口与[setCloneList](#setclonelist)互斥：同一个ArrayBuffer不能同时设置在transfer列表和clone列表中。&gt;
> 此接口可以设置任务池中ArrayBuffer的transfer列表，transfer列表中的ArrayBuffer对象在传输时不会复制buffer内容到工作线程，
> 而是转移buffer控制权至工作线程，传输后当前的ArrayBuffer失效。若ArrayBuffer为空，则不会transfer转移。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200029](../errorcode-utils.md#10200029-无法将arraybuffer同时设置为transferlist和clonelist) |

## arguments

```TypeScript
arguments?: Object[]
```

创建任务传入函数所需的参数，支持的参数类型请参考[序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。默认值为undefined。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** Object[]

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## cpuDuration

```TypeScript
cpuDuration: number
```

执行任务CPU耗时。单位：ms。不建议修改此值。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** number

**默认值：** 0

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## function

```TypeScript
function: Function
```

待执行的函数，必须使用[@Concurrent装饰器](../../../arkts-utils/taskpool-introduction.md#concurrent装饰器)装饰， 支持的函数返回值类型请参考[序列化支持类型](../../../reference/apis-arkts/js-apis-taskpool.md#序列化支持类型)。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** Function

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## ioDuration

```TypeScript
ioDuration: number
```

执行任务异步IO耗时。单位：ms。不建议修改此值。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** number

**默认值：** 0

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
name: string
```

创建任务时指定的任务名称。不建议修改此值。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** string

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## taskId

```TypeScript
taskId: number
```

任务的ID。系统默认提供全局唯一值，不建议修改此值。从API version 18开始，该接口支持在原子化服务中使用。

**类型：** number

**默认值：** 0

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## totalDuration

```TypeScript
totalDuration: number
```

执行任务总耗时。单位：ms。不建议修改此值。从API version 11开始，该接口支持在原子化服务中使用。

**类型：** number

**默认值：** 0

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
