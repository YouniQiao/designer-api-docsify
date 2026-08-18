# EventListener

Implements event listening.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md#workereventlistener)

<!--Device-unnamed-export interface EventListener--><!--Device-unnamed-export interface EventListener-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
(evt: Event): void | Promise<void>
```

Specifies the callback to invoke.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.WorkerEventListener.(event: Event)

<!--Device-EventListener-(evt: Event): void | Promise<void>--><!--Device-EventListener-(evt: Event): void | Promise<void>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| evt | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Examples**

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", ()=>{
    console.info("alert listener callback");
})
```
