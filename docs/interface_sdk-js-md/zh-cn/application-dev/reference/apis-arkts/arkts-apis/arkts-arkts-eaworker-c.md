# EAWorker

支持优先级的并发任务执行器，以独占线程模式执行异步任务。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(needInterop: boolean = false)
```

构造一个EAWorker实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needInterop | boolean | 是 |

## constructor

```TypeScript
constructor(name: string, needInterop: boolean = false)
```

构造一个指定名称的EAWorker实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| needInterop | boolean | 是 |

## constructor

```TypeScript
constructor(task: () => void, needInterop: boolean = false)
```

构造一个包含任务函数的EAWorker实例，在调用start方法后执行指定任务。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | () = & gt; void | 是 |
| needInterop | boolean | 是 |

## constructor

```TypeScript
constructor(name: string, task: () => void, needInterop: boolean = false)
```

构造一个指定名称并包含任务函数的EAWorker实例，在调用start方法后执行指定任务。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| task | () = & gt; void | 是 |
| needInterop | boolean | 是 |

## current

```TypeScript
static current(): EAWorker | undefined
```

返回当前线程的Worker实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [EAWorker](arkts-arkts-eaworker-c.md) \| undefined |

## getName

```TypeScript
getName(): string
```

返回Worker的名称。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getPriority

```TypeScript
getPriority(): WorkerPriority
```

返回Worker的优先级。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) |

## getUncaughtExceptionHandler

```TypeScript
getUncaughtExceptionHandler(): ((error: Error) => void) | undefined
```

返回Worker的未捕获异常处理器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [function](arkts-arkts-taskpool-task-c.md) \| undefined |

## getWorkerId

```TypeScript
getWorkerId(): int | undefined
```

返回Worker的ID。未调用start方法时返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## isAlive

```TypeScript
isAlive(): boolean
```

检查Worker是否存活（已启动）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## join

```TypeScript
join(): Job<void>
```

等待Worker执行完成。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;void&gt; |

## main

```TypeScript
static main(): EAWorker
```

返回主线程的Worker实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [EAWorker](arkts-arkts-eaworker-c.md) |

## postTask

```TypeScript
postTask(task: () => void): void
```

向Worker提交执行任务。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | () = & gt; void | 是 |

## postToMain

```TypeScript
static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>
```

向主线程提交任务，并返回包含结果的Job。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| coroFun | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; |

## quit

```TypeScript
quit(): void
```

终止Worker。等待当前所有任务完成后，停止任务循环并销毁线程资源。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## run

```TypeScript
run<R>(task: Function, ...args: FixedArray<Any>): Job<R>
```

在Worker上运行任务，并返回包含结果的Job。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; |

## setPriority

```TypeScript
setPriority(priority: WorkerPriority): void
```

设置Worker的优先级。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| priority | [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) | 是 |

## setUncaughtExceptionHandler

```TypeScript
setUncaughtExceptionHandler(handler: (error: Error) => void): void
```

设置Worker的未捕获异常处理器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | (error: Error) = & gt; void | 是 |

## start

```TypeScript
start(): void
```

启动Worker，开始接收和执行任务。EAWorker实例仅能启动一次。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
