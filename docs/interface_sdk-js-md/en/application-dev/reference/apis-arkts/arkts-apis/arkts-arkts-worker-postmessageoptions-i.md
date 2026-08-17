# PostMessageOptions

Defines the object for which the ownership is to be transferred during data transfer. The object must be an ArrayBuffer instance. After the ownership is transferred, the object becomes unavailable in the sender and can be used only in the receiver.

**Since:** 7

<!--Device-unnamed-export interface PostMessageOptions--><!--Device-unnamed-export interface PostMessageOptions-End-->

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

## transfer

```TypeScript
transfer?: Object[]
```

ArrayBuffer array used to transfer the ownership. The array cannot be null.

**Type:** Object[]

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PostMessageOptions-transfer?: Object[]--><!--Device-PostMessageOptions-transfer?: Object[]-End-->

**System capability:** SystemCapability.Utils.Lang

