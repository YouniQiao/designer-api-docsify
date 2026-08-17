# MessageEvents

Holds the data transferred between Worker threads.

**Inheritance/Implementation:** MessageEvents extends [Event](arkts-arkts-worker-event-i.md#event)

**Since:** 9

<!--Device-unnamed-export interface MessageEvents--><!--Device-unnamed-export interface MessageEvents-End-->

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
readonly data: any
```

Data transferred when an exception occurs.

**Type:** any

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MessageEvents-readonly data: any--><!--Device-MessageEvents-readonly data: any-End-->

**System capability:** SystemCapability.Utils.Lang

