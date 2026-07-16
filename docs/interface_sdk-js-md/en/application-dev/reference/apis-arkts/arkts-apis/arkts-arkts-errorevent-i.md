# ErrorEvent

Provides detailed information about the exception that occurs during worker execution. The ErrorEvent class inherits from Event.

**Inheritance/Implementation:** ErrorEvent extends [Event](arkts-arkts-event-i.md)

**Since:** 7

<!--Device-unnamed-export interface ErrorEvent extends Event--><!--Device-unnamed-export interface ErrorEvent extends Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from '@kit.ArkTS';
```

## colno

```TypeScript
readonly colno: number
```

Serial number of the column where the exception is located.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly colno: number--><!--Device-ErrorEvent-readonly colno: number-End-->

**System capability:** SystemCapability.Utils.Lang

## error

```TypeScript
readonly error: Object
```

Type of the exception.

**Type:** Object

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly error: Object--><!--Device-ErrorEvent-readonly error: Object-End-->

**System capability:** SystemCapability.Utils.Lang

## filename

```TypeScript
readonly filename: string
```

File where the exception is located.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly filename: string--><!--Device-ErrorEvent-readonly filename: string-End-->

**System capability:** SystemCapability.Utils.Lang

## lineno

```TypeScript
readonly lineno: number
```

Serial number of the line where the exception is located.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly lineno: number--><!--Device-ErrorEvent-readonly lineno: number-End-->

**System capability:** SystemCapability.Utils.Lang

## message

```TypeScript
readonly message: string
```

Information about the exception.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorEvent-readonly message: string--><!--Device-ErrorEvent-readonly message: string-End-->

**System capability:** SystemCapability.Utils.Lang

