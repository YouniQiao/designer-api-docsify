# EventTarget

Specific event features.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: EventListener): void
```

Adds an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** addEventListener

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes |

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

Dispatches the event defined for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** dispatchEvent

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## removeAllListener

```TypeScript
removeAllListener(): void
```

Removes all event listeners for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** removeAllListener

**System capability:** SystemCapability.Utils.Lang

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: EventListener): void
```

Removes an event defined for the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** removeEventListener

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| callback | [EventListener](arkts-arkts-worker-eventlistener-i.md) | No |
