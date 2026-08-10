# DedicatedWorkerGlobalScope

Worker线程自身的运行环境，与宿主线程环境隔离。

**Inheritance/Implementation:** DedicatedWorkerGlobalScope extends [WorkerGlobalScope](arkts-arkts-worker-workerglobalscope-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

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

销毁Worker线程，终止Worker接收消息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

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

onmessage属性用于指定当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用的事件处理程序，该事件处理程序在Worker线程中执行。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.onmessage

<!--Device-DedicatedWorkerGlobalScope-onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void--><!--Device-DedicatedWorkerGlobalScope-onmessage?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | [DedicatedWorkerGlobalScope](arkts-arkts-worker-dedicatedworkerglobalscope-i.md) | Yes |  |
| ev | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |  |

## onmessageerror

```TypeScript
onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void
```

onmessage属性用于指定当Worker线程收到一条无法被反序列化的消息时被调用的事件处理程序，该事件处理程序在Worker线程中执行。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.onmessageerror

<!--Device-DedicatedWorkerGlobalScope-onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void--><!--Device-DedicatedWorkerGlobalScope-onmessageerror?: (this: DedicatedWorkerGlobalScope, ev: MessageEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | [DedicatedWorkerGlobalScope](arkts-arkts-worker-dedicatedworkerglobalscope-i.md) | Yes |  |
| ev | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |  |

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: Transferable[]): void
```

Worker线程向宿主线程发送消息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: Transferable[]): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: Transferable[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| messageObject | Object | Yes | messageObject 发送至宿主线程的数据。 |
| transfer | Transferable[] | Yes | transfer 数组不可包含null。 |

## postMessage

```TypeScript
postMessage(messageObject: Object, options?: PostMessageOptions): void
```

Worker线程向宿主线程发送消息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| messageObject | Object | Yes | messageObject 发送至宿主线程的数据。 |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No | 可为postMessage设置的选项。 |

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

Worker线程向宿主线程发送消息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** ohos.worker.ThreadWorkerGlobalScope.postMessage

<!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void--><!--Device-DedicatedWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| messageObject | Object | Yes | messageObject 发送至宿主线程的数据。 |
| transfer | ArrayBuffer[] | Yes | transfer 数组不可包含null。 |

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

