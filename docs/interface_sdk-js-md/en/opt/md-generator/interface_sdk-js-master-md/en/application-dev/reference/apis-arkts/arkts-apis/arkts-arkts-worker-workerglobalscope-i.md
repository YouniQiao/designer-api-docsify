# WorkerGlobalScope

Specifies the worker thread running environment, which is isolated from the host thread environment.

**Inheritance/Implementation:** WorkerGlobalScope extends [EventTarget](arkts-arkts-worker-eventtarget-i.md#EventTarget)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [GlobalScope](arkts-arkts-worker-globalscope-i.md#GlobalScope)

<!--Device-unnamed-declare interface WorkerGlobalScope extends EventTarget--><!--Device-unnamed-declare interface WorkerGlobalScope extends EventTarget-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from '@kit.ArkTS';
```

## onerror

```TypeScript
onerror?: (ev: ErrorEvent) => void
```

The onerror attribute of parentPort specifies the event handler to be called when an exception occurs during worker execution.The event handler is executed in the worker thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [onerror](ohos.worker.GlobalScope.onerror)

<!--Device-WorkerGlobalScope-onerror?: (ev: ErrorEvent) => void--><!--Device-WorkerGlobalScope-onerror?: (ev: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ev | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |

## name

```TypeScript
readonly name: string
```

Worker name specified when there is a new worker.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [name](ohos.worker.GlobalScope.name)

<!--Device-WorkerGlobalScope-readonly name: string--><!--Device-WorkerGlobalScope-readonly name: string-End-->

**System capability:** SystemCapability.Utils.Lang

## self

```TypeScript
readonly self: WorkerGlobalScope & typeof globalThis
```

Specify the type attribute for self.

**Type:** [WorkerGlobalScope](arkts-arkts-worker-workerglobalscope-i.md) & typeof globalThis

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [self](ohos.worker.GlobalScope.self)

<!--Device-WorkerGlobalScope-readonly self: WorkerGlobalScope & typeof globalThis--><!--Device-WorkerGlobalScope-readonly self: WorkerGlobalScope & typeof globalThis-End-->

**System capability:** SystemCapability.Utils.Lang
