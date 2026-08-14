# RestrictedWorker (System API)

The RestrictedWorker class contains all Worker functions.

**Inheritance/Implementation:** RestrictedWorker extends [ThreadWorker](arkts-arkts-worker-threadworker-c.md#ThreadWorker)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-worker-class RestrictedWorker--><!--Device-worker-class RestrictedWorker-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

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

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

Creates a worker instance

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)--><!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scriptURL | string | Yes | scriptURL URL of the script to be executed by the worker |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No | Options that can be set for the worker |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) | Worker initialization failure. |
| [10200007](../errorcode-utils.md#10200007-abnormal-worker-file-path) | The worker file patch is invalid path. |

