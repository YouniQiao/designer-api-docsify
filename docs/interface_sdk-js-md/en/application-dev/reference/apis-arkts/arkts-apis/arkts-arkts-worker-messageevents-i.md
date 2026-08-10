# MessageEvents

消息类，持有Worker线程间传递的数据。

**Inheritance/Implementation:** MessageEvents extends [Event](arkts-arkts-worker-event-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export interface MessageEvents extends Event--><!--Device-unnamed-export interface MessageEvents extends Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## data

```TypeScript
readonly data: any
```

异常发生时传递的数据。

**Type:** any

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MessageEvents-readonly data: any--><!--Device-MessageEvents-readonly data: any-End-->

**System capability:** SystemCapability.Utils.Lang

