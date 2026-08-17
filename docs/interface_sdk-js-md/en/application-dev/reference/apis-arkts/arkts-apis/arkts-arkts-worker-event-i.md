# Event

Defines the event.

**Since:** 7

<!--Device-unnamed-export interface Event--><!--Device-unnamed-export interface Event-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { DedicatedWorkerGlobalScope } from 'DedicatedWorkerGlobalScope';
import { ErrorEvent } from 'ErrorEvent';
import { Event } from 'Event';
import { EventListener } from 'EventListener';
import { EventTarget } from 'EventTarget';
import { MessageEvent } from 'MessageEvent';
import { MessageEvents } from 'MessageEvents';
import { PostMessageOptions } from 'PostMessageOptions';
import { ThreadWorkerGlobalScope } from 'ThreadWorkerGlobalScope';
import { WorkerEventListener } from 'WorkerEventListener';
import { WorkerEventTarget } from 'WorkerEventTarget';
import { WorkerOptions } from 'WorkerOptions';
import { ThreadWorkerPriority } from 'ThreadWorkerPriority';
import { Priority } from 'Priority';
```

## timeStamp

```TypeScript
readonly timeStamp: number
```

Timestamp (accurate to millisecond) when the event is created. This parameter is not supported yet.

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-readonly timeStamp: number--><!--Device-Event-readonly timeStamp: number-End-->

**System capability:** SystemCapability.Utils.Lang

## type

```TypeScript
readonly type: string
```

Type of the Event.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-readonly type: string--><!--Device-Event-readonly type: string-End-->

**System capability:** SystemCapability.Utils.Lang

