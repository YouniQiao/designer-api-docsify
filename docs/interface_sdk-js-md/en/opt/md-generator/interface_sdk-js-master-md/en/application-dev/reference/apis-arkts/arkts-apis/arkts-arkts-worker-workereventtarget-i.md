# WorkerEventTarget

Processes worker listening events.

**Since:** 9

<!--Device-unnamed-export interface WorkerEventTarget--><!--Device-unnamed-export interface WorkerEventTarget-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: WorkerEventListener): void
```

Adds an event listener for the Worker thread. This API provides the same functionality as on9+.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventTarget-addEventListener(type: string, listener: WorkerEventListener): void--><!--Device-WorkerEventTarget-addEventListener(type: string, listener: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  })
};
```

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

Dispatches the event defined for the Worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventTarget-dispatchEvent(event: Event): boolean--><!--Device-WorkerEventTarget-dispatchEvent(event: Event): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
};
```

## removeAllListener

```TypeScript
removeAllListener(): void
```

Removes all event listeners for the Worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventTarget-removeAllListener(): void--><!--Device-WorkerEventTarget-removeAllListener(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeAllListener();
};
```

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: WorkerEventListener): void
```

Removes an event listener for the Worker thread. This API provides the same functionality as off9+.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventTarget-removeEventListener(type: string, callback?: WorkerEventListener): void--><!--Device-WorkerEventTarget-removeEventListener(type: string, callback?: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| callback | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeEventListener("alert");
};
```
