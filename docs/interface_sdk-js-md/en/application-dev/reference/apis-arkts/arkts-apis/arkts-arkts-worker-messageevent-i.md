# MessageEvent

Holds the data transferred between worker threads.

**Inheritance/Implementation:** MessageEvent extends [Event](arkts-arkts-worker-event-i.md#event)

**Since:** 7

<!--Device-unnamed-export interface MessageEvent--><!--Device-unnamed-export interface MessageEvent-End-->

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

