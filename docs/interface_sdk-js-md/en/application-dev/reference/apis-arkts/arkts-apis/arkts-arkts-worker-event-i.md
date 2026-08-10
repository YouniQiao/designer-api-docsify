# Event

事件类。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export interface Event--><!--Device-unnamed-export interface Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## timeStamp

```TypeScript
readonly timeStamp: number
```

事件创建时的时间戳（精度为毫秒），目前不支持。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-readonly timeStamp: number--><!--Device-Event-readonly timeStamp: number-End-->

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
readonly type: string
```

指定事件的类型。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-readonly type: string--><!--Device-Event-readonly type: string-End-->

**System capability:** SystemCapability.Utils.Lang

