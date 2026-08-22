# clearInterval

## Modules to Import

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from '@kit.ArkTS';
```

## clearInterval

```TypeScript
function clearInterval(timerId?: int | null): void
```

Cancel the specified timer.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function clearInterval(timerId?: int | null): void--><!--Device-unnamed-function clearInterval(timerId?: int | null): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timerId | int \| null | No | The id of the timer returned from setInterval, if pass empty or null or undefined will do nothing. |

