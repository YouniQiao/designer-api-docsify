# ThreadWorkerGlobalScope

Implements communication between the Worker thread and the host thread. The postMessage API is used to send messages to the host thread, and the close API is used to terminate the Worker thread. The ThreadWorkerGlobalScope class inherits from GlobalScope9+.

**Inheritance/Implementation:** ThreadWorkerGlobalScope extends [GlobalScope](arkts-arkts-worker-globalscope-i.md)

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## callGlobalCallObjectMethod

```TypeScript
callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object
```

Calls a method of an object registered with the host thread. This API is called by the Worker thread. The invoking is synchronous for the Worker thread and asynchronous for the host thread. The return value is transferred through serialization.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [instanceName](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-globalerror-i.md) | string | Yes |
| methodName | string | Yes |
| timeout | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200019](../errorcode-utils.md#10200019-failed-to-call-an-api-of-an-unregistered-object) |
| [10200020](../errorcode-utils.md#10200020-failed-to-call-an-api-of-a-registered-object) |
| [10200021](../errorcode-utils.md#10200021-waiting-for-a-global-call-times-out) |

## close

```TypeScript
close(): void
```

Terminates the Worker thread to stop it from receiving messages.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## onmessage

```TypeScript
onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

Called when the Worker thread receives a message sent by the host thread through postMessage. The event handler is executed in the Worker thread. In the callback function, this indicates the caller's ThreadWorkerGlobalScope, and the ev type is MessageEvents, indicating the received message data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | Yes |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |

## onmessageerror

```TypeScript
onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

Called when the Worker thread receives a message that cannot be deserialized. The event handler is executed in the Worker thread. In the callback function, this indicates the caller's ThreadWorkerGlobalScope, and the ev type is MessageEvents, indicating the received message data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | Yes |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the host thread by transferring object ownership.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## postMessage

```TypeScript
postMessage(messageObject: Object, options?: PostMessageOptions): void
```

Sends a message from the Worker thread to the host thread by transferring object ownership or copying data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## postMessageAtFront

```TypeScript
postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the main thread by transferring object ownership, and inserted into the head of the corresponding priority queue.Except for the worker thread to the main thread, this interface has the same function as postMessage.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| priority | [Priority](arkts-arkts-worker-priority-e.md) | Yes |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |

## postMessageWithSharedSendable

```TypeScript
postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the host thread. In the message, a sendable object is passed by reference, and a non-sendable object is passed by serialization.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
