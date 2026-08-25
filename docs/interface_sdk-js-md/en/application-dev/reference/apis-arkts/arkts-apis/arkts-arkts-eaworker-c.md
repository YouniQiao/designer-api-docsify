# EAWorker

A worker that executes tasks concurrently with priority support

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| needInterop | boolean | Yes |

## constructor

```TypeScript
constructor(name: string, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| needInterop | boolean | Yes |

## constructor

```TypeScript
constructor(task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a task

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | () = & gt; void | Yes |
| needInterop | boolean | Yes |

## constructor

```TypeScript
constructor(name: string, task: () => void, needInterop: boolean = false)
```

Constructs a new EAWorker instance with a name and task

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| task | () = & gt; void | Yes |
| needInterop | boolean | Yes |

## current

```TypeScript
static current(): EAWorker | undefined
```

Returns the current worker instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [EAWorker](arkts-arkts-eaworker-c.md) \| undefined |

## getName

```TypeScript
getName(): string
```

Returns the name of the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPriority

```TypeScript
getPriority(): WorkerPriority
```

Returns the priority of the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) |

## getUncaughtExceptionHandler

```TypeScript
getUncaughtExceptionHandler(): ((error: Error) => void) | undefined
```

Returns the uncaught exception handler for the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [function](arkts-arkts-taskpool-task-c.md) \| undefined |

## getWorkerId

```TypeScript
getWorkerId(): int | undefined
```

Returns the worker ID

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## isAlive

```TypeScript
isAlive(): boolean
```

Checks whether the worker is alive

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## join

```TypeScript
join(): Job<void>
```

Waits for the worker to finish execution

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;void&gt; |

## main

```TypeScript
static main(): EAWorker
```

Returns the main worker instance

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [EAWorker](arkts-arkts-eaworker-c.md) |

## postTask

```TypeScript
postTask(task: () => void): void
```

Posts a task to the worker for execution

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | () = & gt; void | Yes |

## postToMain

```TypeScript
static postToMain<R>(coroFun: Function, ...args: FixedArray<Any>): Job<R>
```

Posts a task to the main worker and returns a Job with the result

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coroFun | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; |

## quit

```TypeScript
quit(): void
```

Terminates the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## run

```TypeScript
run<R>(task: Function, ...args: FixedArray<Any>): Job<R>
```

Runs a task on the worker and returns a Job with the result

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Job](arkts-arkts-job-c.md)&lt;R&gt; |

## setPriority

```TypeScript
setPriority(priority: WorkerPriority): void
```

Sets the priority of the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| priority | [WorkerPriority](arkts-arkts-eaworker-workerpriority-e.md) | Yes |

## setUncaughtExceptionHandler

```TypeScript
setUncaughtExceptionHandler(handler: (error: Error) => void): void
```

Sets the uncaught exception handler for the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | (error: Error) = & gt; void | Yes |

## start

```TypeScript
start(): void
```

Starts the worker

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
