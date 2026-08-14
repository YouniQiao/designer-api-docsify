# WorkerGlobalScope

Specifies the worker thread running environment, which is isolated from the host thread environment.

**Inheritance/Implementation:** WorkerGlobalScope extends [EventTarget](arkts-arkts-worker-eventtarget-i.md#EventTarget)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [GlobalScope](arkts-arkts-worker-globalscope-i.md#GlobalScope)

<!--Device-unnamed-declare interface WorkerGlobalScope--><!--Device-unnamed-declare interface WorkerGlobalScope-End-->

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

## name

```TypeScript
readonly name: string
```

Worker name specified when there is a new worker.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** name

<!--Device-WorkerGlobalScope-readonly name: string--><!--Device-WorkerGlobalScope-readonly name: string-End-->

**System capability:** SystemCapability.Utils.Lang

## onerror

```TypeScript
onerror?: (ev: ErrorEvent) => void
```

The onerror attribute of parentPort specifies the event handler to be called when an exception occurs during worker execution. The event handler is executed in the worker thread.

**Type:** (ev: ErrorEvent) =&gt; void

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** onerror

<!--Device-WorkerGlobalScope-onerror?: (ev: ErrorEvent) => void--><!--Device-WorkerGlobalScope-onerror?: (ev: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

## self

```TypeScript
readonly self: WorkerGlobalScope & typeof globalThis
```

Specify the type attribute for self.

**Type:** [WorkerGlobalScope](arkts-arkts-worker-workerglobalscope-i.md) & typeof globalThis

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** self

<!--Device-WorkerGlobalScope-readonly self: WorkerGlobalScope & typeof globalThis--><!--Device-WorkerGlobalScope-readonly self: WorkerGlobalScope & typeof globalThis-End-->

**System capability:** SystemCapability.Utils.Lang

