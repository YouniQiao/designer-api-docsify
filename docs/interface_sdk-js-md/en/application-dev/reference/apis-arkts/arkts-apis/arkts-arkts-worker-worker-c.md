# Worker

The Worker class contains all Worker functions.

**Inheritance/Implementation:** Worker implements [EventTarget](arkts-arkts-worker-eventtarget-i.md)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ThreadWorker](arkts-arkts-worker-threadworker-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

Creates a worker instance

**Since:** 7

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scriptURL | string | Yes |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No |

## off

```TypeScript
off(type: string, listener?: EventListener): void
```

Removes an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** off

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | No |

## on

```TypeScript
on(type: string, listener: EventListener): void
```

Adds an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** on

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes |

## once

```TypeScript
once(type: string, listener: EventListener): void
```

Adds an event listener to the worker and removes the event listener automatically after it is invoked once.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** once

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes |

## onerror

```TypeScript
onerror?: (err: ErrorEvent) => void
```

The onerror attribute of the worker specifies the event handler to be called when an exception occurs during worker execution. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onerror

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |

## onexit

```TypeScript
onexit?: (code: number) => void
```

Called when the Worker thread exits. The event handler is executed in the host thread. In the callback function, the code value is of the number type, where the value 1 indicates abnormal exit and 0 indicates normal exit.The default value is undefined.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onexit

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

## onmessage

```TypeScript
onmessage?: (event: MessageEvent) => void
```

The onmessage attribute of the worker specifies the event handler to be called then the host thread receives a message created by itself and sent by the worker through the parentPort.postMessage. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onmessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |

## onmessageerror

```TypeScript
onmessageerror?: (event: MessageEvent) => void
```

The onmessage attribute of the worker specifies the event handler when the worker receives a message that cannot be serialized. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onmessageerror

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |

## postMessage

```TypeScript
postMessage(message: Object, transfer: ArrayBuffer[]): void
```

Sends a message to the worker thread. The data is transferred using the structured clone algorithm.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** postMessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | Yes |

## postMessage

```TypeScript
postMessage(message: Object, options?: PostMessageOptions): void
```

Sends a message to the worker thread. The data is transferred using the structured clone algorithm.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** postMessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No |

## terminate

```TypeScript
terminate(): void
```

Terminates the worker thread to stop the worker from receiving messages

**Since:** 7

**Deprecated since:** 9

**Substitutes:** terminate

**System capability:** SystemCapability.Utils.Lang
