# WorkerEventListener

Implements event listening.

**Since:** 9

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## [[Call]]

```TypeScript
(event: Event): void | Promise<void>
```

Specifies the callback function to be invoked.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |
