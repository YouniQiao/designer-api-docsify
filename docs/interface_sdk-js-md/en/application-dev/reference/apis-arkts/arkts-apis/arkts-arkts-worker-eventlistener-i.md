# EventListener

Implements event listening.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## [[Call]]

```TypeScript
(evt: Event): void | Promise<void>
```

Specifies the callback to invoke.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.worker.WorkerEventListener.(event: Event)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| evt | [Event](arkts-arkts-worker-event-i.md) | Yes |
