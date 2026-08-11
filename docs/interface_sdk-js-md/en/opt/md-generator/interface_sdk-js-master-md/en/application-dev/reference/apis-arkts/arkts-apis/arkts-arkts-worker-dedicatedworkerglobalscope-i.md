# DedicatedWorkerGlobalScope

Specifies the worker thread running environment, which is isolated from the host thread environment

**Inheritance/Implementation:** DedicatedWorkerGlobalScope extends [WorkerGlobalScope](arkts-arkts-worker-workerglobalscope-i.md)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope

<!--Device-unnamed-export interface DedicatedWorkerGlobalScope extends WorkerGlobalScope--><!--Device-unnamed-export interface DedicatedWorkerGlobalScope extends WorkerGlobalScope-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## close

```TypeScript
close(): void
```

Close the worker thread to stop the worker from receiving messages

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.close

<!--Device-DedicatedWorkerGlobalScope-close(): void--><!--Device-DedicatedWorkerGlobalScope-close(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
```

```TypeScript
// worker.ets
import { worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (): void => {
    parentPort.close()
}
```

## onmessage

```TypeScript
onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void
```

The onmessage attribute of parentPort specifies the event handler to be called then the worker thread receives a message sent by the host thread through worker postMessage.The event handler is executed in the worker thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.onmessage

<!--Device-DedicatedWorkerGlobalScope-onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void--><!--Device-DedicatedWorkerGlobalScope-onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [DedicatedWorkerGlobalScope](arkts-arkts-worker-dedicatedworkerglobalscope-i.md) | Yes |
| ev | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |

## onmessageerror

```TypeScript
onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void
```

The onmessage attribute of parentPort specifies the event handler to be called then the worker receives a message that cannot be deserialized.The event handler is executed in the worker thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.onmessageerror

<!--Device-DedicatedWorkerGlobalScope-onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void--><!--Device-DedicatedWorkerGlobalScope-onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [DedicatedWorkerGlobalScope](arkts-arkts-worker-dedicatedworkerglobalscope-i.md) | Yes |
| ev | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: Transferable[]): void
```

Send a message to be host thread from the worker

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: Transferable[]): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: Transferable[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| transfer | Transferable[] | Yes |

## postMessage

```TypeScript
postMessage(messageObject: Object, options?: PostMessageOptions): void
```

Send a message to be host thread from the worker

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}
```

```TypeScript
// worker.ets
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (e: MessageEvents) => {
  parentPort.postMessage("receive data from main thread");
}
```

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: ArrayBuffer[]): void
```

Send a message to host thread from the worker

**Since:** 9

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| transfer | ArrayBuffer[] | Yes |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    // let data = e.data;
    console.info("receive data from worker.ets");
}
```

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.onmessage = (): void => {
    // let data = e.data;
    let buffer = new ArrayBuffer(5)
    workerPort.postMessage(buffer, [buffer]);
}
```
