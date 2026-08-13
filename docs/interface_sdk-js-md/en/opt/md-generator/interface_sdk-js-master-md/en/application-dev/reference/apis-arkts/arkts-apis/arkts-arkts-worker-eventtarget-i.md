# EventTarget

Specific event features.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md#WorkerEventTarget)

<!--Device-unnamed-export interface EventTarget--><!--Device-unnamed-export interface EventTarget-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from '@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: EventListener): void
```

Adds an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** addEventListener

<!--Device-EventTarget-addEventListener(type: string, listener: EventListener): void--><!--Device-EventTarget-addEventListener(type: string, listener: EventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes |

## Examples

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})
```

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

Dispatches the event defined for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** dispatchEvent

<!--Device-EventTarget-dispatchEvent(event: Event): boolean--><!--Device-EventTarget-dispatchEvent(event: Event): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.dispatchEvent({type: 'alert_add', timeStamp: 0}); // timeStamp is not supported yet.
```

The dispatchEvent API can be used together with the addEventListener API. The sample code is as follows:

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
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", ()=>{
  console.info("alert listener callback");
})

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.dispatchEvent({type:"alert", timeStamp:0}); // timeStamp is not supported yet.
}
```

## removeAllListener

```TypeScript
removeAllListener(): void
```

Removes all event listeners for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** removeAllListener

<!--Device-EventTarget-removeAllListener(): void--><!--Device-EventTarget-removeAllListener(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.removeAllListener();
```

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: EventListener): void
```

Removes an event defined for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** removeEventListener

<!--Device-EventTarget-removeEventListener(type: string, callback?: EventListener): void--><!--Device-EventTarget-removeEventListener(type: string, callback?: EventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| callback | [EventListener](arkts-arkts-worker-eventlistener-i.md) | No |

## Examples

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerPort.removeEventListener('alert');
```
