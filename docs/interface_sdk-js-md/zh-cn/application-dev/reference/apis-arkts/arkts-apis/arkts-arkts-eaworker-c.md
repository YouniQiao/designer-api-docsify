# EAWorker

A worker that executes tasks concurrently with priority support

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class EAWorker--><!--Device-unnamed-export class EAWorker-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(needInterop: boolean = false)
```

Constructs a new EAWorker instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-constructor(needInterop: boolean = false)--><!--Device-EAWorker-constructor(needInterop: boolean = false)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| needInterop | boolean | 是 | whether interoperability is needed. |

## constructor

```TypeScript
constructor(name: string, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-constructor(name: string, needInterop: boolean = false)--><!--Device-EAWorker-constructor(name: string, needInterop: boolean = false)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | the name of the worker. |
| needInterop | boolean | 是 | whether interoperability is needed. |

## constructor

```TypeScript
constructor(task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a task

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-constructor(task: () => void, needInterop: boolean = false)--><!--Device-EAWorker-constructor(task: () => void, needInterop: boolean = false)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | () =&gt; void | 是 | the task to execute. |
| needInterop | boolean | 是 | whether interoperability is needed. |

## constructor

```TypeScript
constructor(name: string, task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name and task

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-constructor(name: string, task: () => void, needInterop: boolean = false)--><!--Device-EAWorker-constructor(name: string, task: () => void, needInterop: boolean = false)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | the name of the worker. |
| task | () =&gt; void | 是 | the task to execute. |
| needInterop | boolean | 是 | whether interoperability is needed. |

## current

```TypeScript
static current(): EAWorker | undefined
```

Returns the current worker instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-static current(): EAWorker | undefined--><!--Device-EAWorker-static current(): EAWorker | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EAWorker](arkts-arkts-eaworker-c.md) | the current worker instance, or undefined if not in a worker context |

## getName

```TypeScript
getName(): string
```

Returns the name of the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-getName(): string--><!--Device-EAWorker-getName(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the name of the worker |

## getPriority

```TypeScript
getPriority(): WorkerPriority
```

Returns the priority of the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-getPriority(): WorkerPriority--><!--Device-EAWorker-getPriority(): WorkerPriority-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) | the priority of the worker |

## getUncaughtExceptionHandler

```TypeScript
getUncaughtExceptionHandler(): ((error: Error) => void) | undefined
```

Returns the uncaught exception handler for the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-getUncaughtExceptionHandler(): ((error: Error) => void) | undefined--><!--Device-EAWorker-getUncaughtExceptionHandler(): ((error: Error) => void) | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ((error: Error) =&gt; void) | the uncaught exception handler, or undefined if not set |

## getWorkerId

```TypeScript
getWorkerId(): int | undefined
```

Returns the worker ID

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-getWorkerId(): int | undefined--><!--Device-EAWorker-getWorkerId(): int | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the worker ID, or undefined if not started |

## isAlive

```TypeScript
isAlive(): boolean
```

Checks whether the worker is alive

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-isAlive(): boolean--><!--Device-EAWorker-isAlive(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the worker is alive, false otherwise |

## join

```TypeScript
join(): Job<void>
```

Waits for the worker to finish execution

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-join(): Job<void>--><!--Device-EAWorker-join(): Job<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Job](arkts-arkts-job-c.md)&lt;void&gt; | a Job that resolves when the worker has finished |

## main

```TypeScript
static main(): EAWorker
```

Returns the main worker instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-static main(): EAWorker--><!--Device-EAWorker-static main(): EAWorker-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EAWorker](arkts-arkts-eaworker-c.md) | the main worker instance |

## postTask

```TypeScript
postTask(task: () => void): void
```

Posts a task to the worker for execution

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-postTask(task: () => void): void--><!--Device-EAWorker-postTask(task: () => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | () =&gt; void | 是 | the task to post. |

## postToMain

```TypeScript
static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>
```

Posts a task to the main worker and returns a Job with the result

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>--><!--Device-EAWorker-static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| coroFun | Function | 是 | the coroutine function to run on the main worker. |
| args | FixedArray&lt;Any&gt; | 是 | the arguments to pass to the function. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; | a Job that resolves with the function result |

## quit

```TypeScript
quit(): void
```

Terminates the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-quit(): void--><!--Device-EAWorker-quit(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## run

```TypeScript
run<R>(task: Function, ...args: FixedArray<Any>): Job<R>
```

Runs a task on the worker and returns a Job with the result

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-run<R>(task: Function, ...args: FixedArray<Any>): Job<R>--><!--Device-EAWorker-run<R>(task: Function, ...args: FixedArray<Any>): Job<R>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | Function | 是 | the task function to run. |
| args | FixedArray&lt;Any&gt; | 是 | the arguments to pass to the task. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; | a Job that resolves with the task result |

## setPriority

```TypeScript
setPriority(priority: WorkerPriority): void
```

Sets the priority of the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-setPriority(priority: WorkerPriority): void--><!--Device-EAWorker-setPriority(priority: WorkerPriority): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priority | [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) | 是 | the priority to set. |

## setUncaughtExceptionHandler

```TypeScript
setUncaughtExceptionHandler(handler: (error: Error) => void): void
```

Sets the uncaught exception handler for the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-setUncaughtExceptionHandler(handler: (error: Error) => void): void--><!--Device-EAWorker-setUncaughtExceptionHandler(handler: (error: Error) => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | (error: Error) =&gt; void | 是 | the handler to call when an uncaught exception occurs. |

## start

```TypeScript
start(): void
```

Starts the worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EAWorker-start(): void--><!--Device-EAWorker-start(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

