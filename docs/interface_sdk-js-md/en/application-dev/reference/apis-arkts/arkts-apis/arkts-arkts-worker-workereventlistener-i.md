# WorkerEventListener

Implements event listening.

**Since:** 9

<!--Device-unnamed-export interface WorkerEventListener--><!--Device-unnamed-export interface WorkerEventListener-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from '@kit.ArkTS';
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes | Event class for the callback to invoke. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) | The Worker instance is not running. |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) | The called API is not supported in the worker thread. |

**Examples**

The following uses the Index.ets file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](../../../arkts-utils/worker-introduction.md#precautions-for-file-urls).

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

The following uses the Index.ets file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](../../../arkts-utils/worker-introduction.md#precautions-for-file-urls).

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.Worker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

