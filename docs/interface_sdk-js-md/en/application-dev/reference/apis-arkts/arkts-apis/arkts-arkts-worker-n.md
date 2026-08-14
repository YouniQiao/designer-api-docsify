# worker

JS cross-thread communication tool

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace worker--><!--Device-unnamed-declare namespace worker-End-->

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

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ThreadWorker](arkts-arkts-worker-threadworker-c.md) | Before using the following APIs, you must create a ThreadWorker instance. The ThreadWorker class inherits from WorkerEventTarget. |
| [Worker](arkts-arkts-worker-worker-c.md) | The Worker class contains all Worker functions. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [RestrictedWorker](arkts-arkts-worker-restrictedworker-c-sys.md) | The RestrictedWorker class contains all Worker functions. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [parentPort](arkts-arkts-worker-con.md#parentPort) | The object used by the worker thread to communicate with the host thread. |
| [workerPort](arkts-arkts-worker-con.md#workerPort) | The object used by the worker thread to communicate with the host thread. |

