# GlobalScope

Worker线程自身的运行环境，GlobalScope类继承WorkerEventTarget。

**Inheritance/Implementation:** GlobalScope extends [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare interface GlobalScope extends WorkerEventTarget--><!--Device-unnamed-declare interface GlobalScope extends WorkerEventTarget-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## onerror

```TypeScript
onerror?: (ev: ErrorEvent) => void
```

Worker在执行过程中发生异常被调用的回调函数，该回调函数在Worker线程中执行。其中ev类型为ErrorEvent，表示收到的异常数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GlobalScope-onerror?: (ev: ErrorEvent) => void--><!--Device-GlobalScope-onerror?: (ev: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ev | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |  |

## name

```TypeScript
readonly name: string
```

Worker的名字，new Worker时指定。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GlobalScope-readonly name: string--><!--Device-GlobalScope-readonly name: string-End-->

**System capability:** SystemCapability.Utils.Lang

## self

```TypeScript
readonly self: GlobalScope & typeof globalThis
```

GlobalScope本身。

**Type:** [GlobalScope](arkts-arkts-worker-globalscope-i.md) & typeof globalThis

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GlobalScope-readonly self: GlobalScope & typeof globalThis--><!--Device-GlobalScope-readonly self: GlobalScope & typeof globalThis-End-->

**System capability:** SystemCapability.Utils.Lang

