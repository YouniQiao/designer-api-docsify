# EventListener

Implements event listening.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md#WorkerEventListener)

<!--Device-unnamed-export interface EventListener--><!--Device-unnamed-export interface EventListener-End-->

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
(evt: Event): void | Promise<void>
```

Specifies the callback to invoke.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.WorkerEventListener.(event: Event)

<!--Device-EventListener-(evt: Event): void | Promise<void>--><!--Device-EventListener-(evt: Event): void | Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| evt | [Event](arkts-arkts-worker-event-i.md) | Yes | evt evt Event class for the callback to invoke. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", ()=>{
    console.info("alert listener callback");
})
```

