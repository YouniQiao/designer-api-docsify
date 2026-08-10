# MessageEvent

消息类，持有Worker线程间传递的数据，MessageEvent类继承Event。

**Inheritance/Implementation:** MessageEvent extends [Event](arkts-arkts-worker-event-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export interface MessageEvent<T> extends Event--><!--Device-unnamed-export interface MessageEvent<T> extends Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## data

```TypeScript
readonly data: T
```

异常发生时传递的数据。

**Type:** T

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MessageEvent-readonly data: T--><!--Device-MessageEvent-readonly data: T-End-->

**System capability:** SystemCapability.Utils.Lang

