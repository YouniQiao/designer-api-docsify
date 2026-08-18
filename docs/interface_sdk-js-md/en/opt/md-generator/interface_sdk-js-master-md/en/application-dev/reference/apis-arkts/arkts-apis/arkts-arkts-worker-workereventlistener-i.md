# WorkerEventListener

Implements event listening.

**Since:** 9

<!--Device-unnamed-export interface WorkerEventListener--><!--Device-unnamed-export interface WorkerEventListener-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
(event: Event): void | Promise<void>
```

Specifies the callback function to be invoked.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WorkerEventListener-(event: Event): void | Promise<void>--><!--Device-WorkerEventListener-(event: Event): void | Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

**Examples**

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
