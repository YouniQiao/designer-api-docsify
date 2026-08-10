# ErrorEvent

错误事件类用于表示Worker执行过程中出现异常的详细信息，ErrorEvent类继承Event。

**Inheritance/Implementation:** ErrorEvent extends [Event](arkts-arkts-worker-event-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export interface ErrorEvent extends Event--><!--Device-unnamed-export interface ErrorEvent extends Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## colno

```TypeScript
readonly colno: number
```

异常所在的列数。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly colno: number--><!--Device-ErrorEvent-readonly colno: number-End-->

**System capability:** SystemCapability.Utils.Lang

## error

```TypeScript
readonly error: Object
```

异常类型。

**Type:** Object

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly error: Object--><!--Device-ErrorEvent-readonly error: Object-End-->

**System capability:** SystemCapability.Utils.Lang

## filename

```TypeScript
readonly filename: string
```

出现异常所在的文件。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly filename: string--><!--Device-ErrorEvent-readonly filename: string-End-->

**System capability:** SystemCapability.Utils.Lang

## lineno

```TypeScript
readonly lineno: number
```

异常所在的行数。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly lineno: number--><!--Device-ErrorEvent-readonly lineno: number-End-->

**System capability:** SystemCapability.Utils.Lang

## message

```TypeScript
readonly message: string
```

异常发生的错误信息。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly message: string--><!--Device-ErrorEvent-readonly message: string-End-->

**System capability:** SystemCapability.Utils.Lang

