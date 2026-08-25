# WorkerEventTarget

Processes worker listening events.

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: WorkerEventListener): void
```

Adds an event listener for the Worker thread. This API provides the same functionality as on9+.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

Dispatches the event defined for the Worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## removeAllListener

```TypeScript
removeAllListener(): void
```

Removes all event listeners for the Worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: WorkerEventListener): void
```

Removes an event listener for the Worker thread. This API provides the same functionality as off9+.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

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
