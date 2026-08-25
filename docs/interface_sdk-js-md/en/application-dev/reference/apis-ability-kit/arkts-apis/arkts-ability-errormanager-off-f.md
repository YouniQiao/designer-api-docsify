# off

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## off('error')

```TypeScript
function off(type: 'error', observerId: number, callback: AsyncCallback<void>): void
```

Unregisters an error observer. This API uses an asynchronous callback to return the result.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| observerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |


## off('error')

```TypeScript
function off(type: 'error', observerId: number): Promise<void>
```

Unregisters an error observer. This API uses a promise to return the result.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| observerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |


## off('loopObserver')

```TypeScript
function off(type: 'loopObserver', observer?: LoopObserver): void
```

Unregisters an observer for the message processing duration of the main thread.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loopObserver' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## off('unhandledRejection')

```TypeScript
function off(type: 'unhandledRejection', observer?: UnhandledRejectionObserver): void
```

Unregisters an observer for the promise rejection.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'unhandledRejection' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |


## off('globalUnhandledRejectionDetected')

```TypeScript
function off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void
```

Unregisters a rejected promise observer. After the deregistration, promise exceptions in the process cannot be listened for.If the observer passed in is not in the observer queue registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalUnhandledRejectionDetected' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |


## off('freeze')

```TypeScript
function off(type: 'freeze', observer?: FreezeObserver): void
```

Unregisters an observer for the main thread freeze event of the application.This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.If the observer passed in does not match the observer registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'freeze' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |


## off('globalErrorOccurred')

```TypeScript
function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void
```

Unregisters a global error observer. Once unregistered, global listening cannot be implemented.If the observer passed in is not in the observer queue registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |
