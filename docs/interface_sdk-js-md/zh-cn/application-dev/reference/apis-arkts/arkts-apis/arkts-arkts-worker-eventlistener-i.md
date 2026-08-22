# EventListener

事件监听类用于处理事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md)

<!--Device-unnamed-export interface EventListener--><!--Device-unnamed-export interface EventListener-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from '@kit.ArkTS';
```

## constructor

```TypeScript
(evt: Event): void | Promise<void>
```

指定要调用的回调函数。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.worker.WorkerEventListener.(event: Event)

<!--Device-EventListener-(evt: Event): void | Promise<void>--><!--Device-EventListener-(evt: Event): void | Promise<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| evt | [Event](arkts-arkts-worker-event-i.md) | 是 | evt evt 回调的事件类。 |

**示例**

以下示例展示了在Stage模型的entry模块Index.ets文件中加载Worker线程文件的方法，使用Library加载Worker线程文件的场景参考[文件路径注意事项](../../../arkts-utils/worker-introduction.md#文件路径注意事项)。

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// worker文件所在路径："entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

此处以在Stage模型的entry模块Index.ets文件中加载Worker线程文件为例，使用Library加载Worker线程文件的场景参考[文件路径注意事项](../../../arkts-utils/worker-introduction.md#文件路径注意事项)。

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// worker文件所在路径："entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.Worker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

