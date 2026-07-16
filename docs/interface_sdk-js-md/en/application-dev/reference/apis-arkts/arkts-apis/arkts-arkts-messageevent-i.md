# MessageEvent

Holds the data transferred between worker threads.

**Inheritance/Implementation:** MessageEvent extends [Event](arkts-arkts-event-i.md)

**Since:** 7

<!--Device-unnamed-export interface MessageEvent<T> extends Event--><!--Device-unnamed-export interface MessageEvent<T> extends Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from '@kit.ArkTS';
```

## data

```TypeScript
readonly data: T
```

Data transferred when an exception occurs.

**Type:** T

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MessageEvent-readonly data: T--><!--Device-MessageEvent-readonly data: T-End-->

**System capability:** SystemCapability.Utils.Lang

