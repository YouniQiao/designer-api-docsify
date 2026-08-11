# RestrictedWorker (System API)

The RestrictedWorker class contains all Worker functions.

**Inheritance/Implementation:** RestrictedWorker extends [ThreadWorker](arkts-arkts-worker-threadworker-c.md)

**Since:** 11

<!--Device-worker-class RestrictedWorker extends ThreadWorker--><!--Device-worker-class RestrictedWorker extends ThreadWorker-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

Creates a worker instance

**Since:** 11

<!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)--><!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scriptURL | string | Yes |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200007](../errorcode-utils.md#10200007-abnormal-worker-file-path) |
