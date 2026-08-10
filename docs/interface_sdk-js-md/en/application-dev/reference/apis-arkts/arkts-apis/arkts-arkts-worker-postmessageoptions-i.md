# PostMessageOptions

明确数据传递过程中需要转移所有权的对象，这些对象必须是ArrayBuffer，在发送方的上下文中将变为不可用，仅在接收方可用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export interface PostMessageOptions--><!--Device-unnamed-export interface PostMessageOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## transfer

```TypeScript
transfer?: Object[]
```

ArrayBuffer数组，用于传递所有权。该数组中不可传入null。

**Type:** Object[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PostMessageOptions-transfer?: Object[]--><!--Device-PostMessageOptions-transfer?: Object[]-End-->

**System capability:** SystemCapability.Utils.Lang

