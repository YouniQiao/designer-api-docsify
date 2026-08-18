# EAWorker

A worker that executes tasks concurrently with priority support

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class EAWorker--><!--Device-unnamed-export class EAWorker-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(needInterop: boolean = false)
```

Constructs a new EAWorker instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-constructor(needInterop: boolean = false)--><!--Device-EAWorker-constructor(needInterop: boolean = false)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| needInterop | boolean | Yes | whether interoperability is needed. |

## constructor

```TypeScript
constructor(name: string, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-constructor(name: string, needInterop: boolean = false)--><!--Device-EAWorker-constructor(name: string, needInterop: boolean = false)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | the name of the worker. |
| needInterop | boolean | Yes | whether interoperability is needed. |

## constructor

```TypeScript
constructor(task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a task

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-constructor(task: () => void, needInterop: boolean = false)--><!--Device-EAWorker-constructor(task: () => void, needInterop: boolean = false)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | () =&gt; void | Yes | the task to execute. |
| needInterop | boolean | Yes | whether interoperability is needed. |

## constructor

```TypeScript
constructor(name: string, task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name and task

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-constructor(name: string, task: () => void, needInterop: boolean = false)--><!--Device-EAWorker-constructor(name: string, task: () => void, needInterop: boolean = false)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | the name of the worker. |
| task | () =&gt; void | Yes | the task to execute. |
| needInterop | boolean | Yes | whether interoperability is needed. |

## current

```TypeScript
static current(): EAWorker | undefined
```

Returns the current worker instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-static current(): EAWorker | undefined--><!--Device-EAWorker-static current(): EAWorker | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [EAWorker](arkts-na-eaworker-c.md) | the current worker instance, or undefined if not in a worker context |

## getName

```TypeScript
getName(): string
```

Returns the name of the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-getName(): string--><!--Device-EAWorker-getName(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the name of the worker |

## getPriority

```TypeScript
getPriority(): WorkerPriority
```

Returns the priority of the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-getPriority(): WorkerPriority--><!--Device-EAWorker-getPriority(): WorkerPriority-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [WorkerPriority](arkts-na-eaworker-workerpriority-e.md) | the priority of the worker |

## getUncaughtExceptionHandler

```TypeScript
getUncaughtExceptionHandler(): ((error: Error) => void) | undefined
```

Returns the uncaught exception handler for the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-getUncaughtExceptionHandler(): ((error: Error) => void) | undefined--><!--Device-EAWorker-getUncaughtExceptionHandler(): ((error: Error) => void) | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| ((error: Error) =&gt; void) | the uncaught exception handler, or undefined if not set |

## getWorkerId

```TypeScript
getWorkerId(): int | undefined
```

Returns the worker ID

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-getWorkerId(): int | undefined--><!--Device-EAWorker-getWorkerId(): int | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the worker ID, or undefined if not started |

## isAlive

```TypeScript
isAlive(): boolean
```

Checks whether the worker is alive

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-isAlive(): boolean--><!--Device-EAWorker-isAlive(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the worker is alive, false otherwise |

## join

```TypeScript
join(): Job<void>
```

Waits for the worker to finish execution

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-join(): Job<void>--><!--Device-EAWorker-join(): Job<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Job](arkts-na-job-c.md)&lt;void&gt; | a Job that resolves when the worker has finished |

## main

```TypeScript
static main(): EAWorker
```

Returns the main worker instance

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-static main(): EAWorker--><!--Device-EAWorker-static main(): EAWorker-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [EAWorker](arkts-na-eaworker-c.md) | the main worker instance |

## postTask

```TypeScript
postTask(task: () => void): void
```

Posts a task to the worker for execution

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-postTask(task: () => void): void--><!--Device-EAWorker-postTask(task: () => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | () =&gt; void | Yes | the task to post. |

## postToMain

```TypeScript
static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>
```

Posts a task to the main worker and returns a Job with the result

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>--><!--Device-EAWorker-static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| coroFun | Function | Yes | the coroutine function to run on the main worker. |
| args | FixedArray&lt;Any&gt; | Yes | the arguments to pass to the function. |

**Return value:**

| Type | Description |
| --- | --- |
| [Job](arkts-na-job-c.md)&lt;R&gt; | a Job that resolves with the function result |

## quit

```TypeScript
quit(): void
```

Terminates the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-quit(): void--><!--Device-EAWorker-quit(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## run

```TypeScript
run<R>(task: Function, ...args: FixedArray<Any>): Job<R>
```

Runs a task on the worker and returns a Job with the result

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-run<R>(task: Function, ...args: FixedArray<Any>): Job<R>--><!--Device-EAWorker-run<R>(task: Function, ...args: FixedArray<Any>): Job<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | Function | Yes | the task function to run. |
| args | FixedArray&lt;Any&gt; | Yes | the arguments to pass to the task. |

**Return value:**

| Type | Description |
| --- | --- |
| [Job](arkts-na-job-c.md)&lt;R&gt; | a Job that resolves with the task result |

## setPriority

```TypeScript
setPriority(priority: WorkerPriority): void
```

Sets the priority of the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-setPriority(priority: WorkerPriority): void--><!--Device-EAWorker-setPriority(priority: WorkerPriority): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priority | [WorkerPriority](arkts-na-eaworker-workerpriority-e.md) | Yes | the priority to set. |

## setUncaughtExceptionHandler

```TypeScript
setUncaughtExceptionHandler(handler: (error: Error) => void): void
```

Sets the uncaught exception handler for the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-setUncaughtExceptionHandler(handler: (error: Error) => void): void--><!--Device-EAWorker-setUncaughtExceptionHandler(handler: (error: Error) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | (error: Error) =&gt; void | Yes | the handler to call when an uncaught exception occurs. |

## start

```TypeScript
start(): void
```

Starts the worker

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EAWorker-start(): void--><!--Device-EAWorker-start(): void-End-->

**System capability:** SystemCapability.Utils.Lang

