# on

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## on('error')

```TypeScript
function on(type: 'error', observer: ErrorObserver): number
```

Registers an error observer. Once registered, it can capture JavaScript crashes occurring within the application, which are a type of application crash. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [ErrorObserver](arkts-ability-errormanager-errorobserver-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |


## on('loopObserver')

```TypeScript
function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void
```

Registers an observer for the message processing duration of the main thread. After the registration, the execution time of a message processed by the main thread of the application can be captured.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loopObserver' | Yes |
| timeout | number | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('unhandledRejection')

```TypeScript
function on(type: 'unhandledRejection', observer: UnhandledRejectionObserver): void
```

Registers an observer for the promise rejection. After the registration, a rejected promise that is not captured in the current thread of the application can be captured.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'unhandledRejection' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |


## on('globalUnhandledRejectionDetected')

```TypeScript
function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void
```

Registers a rejected promise observer with any thread in the process. Once registered, it can capture a rejected promise that is not captured in the current thread of the application.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalUnhandledRejectionDetected' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |


## on('freeze')

```TypeScript
function on(type: 'freeze', observer: FreezeObserver): void
```

Registers an observer for the main thread freeze event of the application. If the observer is registered multiple times, only the last one takes effect.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

> **NOTE：**&gt;
> If the callback function runs for more than 1 second, the
> [AppRecovery](arkts-app-ability-apprecovery.md) feature may not work. The execution duration can
> be calculated by parsing the time difference between **begin** and **Freeze callback execution completed** in
> HiLogs. If the execution duration exceeds 1 second, you can optimize the callback logic by using methods such as
> asynchronous processing, reducing operations that block other tasks, and optimizing the data structures to reduce
> the execution duration.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'freeze' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('globalErrorOccurred')

```TypeScript
function on(type: 'globalErrorOccurred', observer: GlobalObserver): void
```

Registers a global error observer via the **errorManager.on** API within any thread of a process. Once registered, it can capture exceptions occurring in any thread across the entire process. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
