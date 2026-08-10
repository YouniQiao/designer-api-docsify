# RestrictedWorker (System API)

RestrictedWorker类继承[ThreadWorker](arkts-arkts-worker-threadworker-c.md)，具有ThreadWorker中所有的方法。RestrictedWorker主要用于提供受限的Worker线程运行环境，该线程运行环境中只允许导入Worker模块，不允许导入其他API。

**Inheritance/Implementation:** RestrictedWorker extends [ThreadWorker](arkts-arkts-worker-threadworker-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

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

RestrictedWorker构造函数。使用其他方法前，均需先构造RestrictedWorker实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)--><!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scriptURL | string | Yes | Worker线程文件的路径，路径规则详细参考文件路径注意事项。 |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No | 构造RestrictedWorker时的选项。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200003 | Worker initialization failure. |
| 10200007 | The worker file path is invalid. |

