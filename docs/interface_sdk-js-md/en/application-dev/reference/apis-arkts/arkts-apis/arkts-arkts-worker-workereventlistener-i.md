# WorkerEventListener

Implements event listening.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-unnamed-export interface WorkerEventListener--><!--Device-unnamed-export interface WorkerEventListener-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { DedicatedWorkerGlobalScope } from 'DedicatedWorkerGlobalScope';
import { ErrorEvent } from 'ErrorEvent';
import { Event } from 'Event';
import { EventListener } from 'EventListener';
import { EventTarget } from 'EventTarget';
import { MessageEvent } from 'MessageEvent';
import { MessageEvents } from 'MessageEvents';
import { PostMessageOptions } from 'PostMessageOptions';
import { ThreadWorkerGlobalScope } from 'ThreadWorkerGlobalScope';
import { WorkerEventListener } from 'WorkerEventListener';
import { WorkerEventTarget } from 'WorkerEventTarget';
import { WorkerOptions } from 'WorkerOptions';
import { ThreadWorkerPriority } from 'ThreadWorkerPriority';
import { Priority } from 'Priority';
```

## constructor

```TypeScript
(event: Event): void | Promise<void>
```

Specifies the callback function to be invoked.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventListener-(event: Event): void | Promise<void>--><!--Device-WorkerEventListener-(event: Event): void | Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes | Event class for the callback to invoke. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) | The called API is not supported in the worker thread. |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker, Event } from "@kit.ArkTS"

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", (event: Event) => {
  console.info("event type is: ", JSON.stringify(event.type));
});

const eventToDispatch : Event = { type: "alert", timeStamp: 0 }; // timeStamp is not supported.
workerInstance.dispatchEvent(eventToDispatch);
```

