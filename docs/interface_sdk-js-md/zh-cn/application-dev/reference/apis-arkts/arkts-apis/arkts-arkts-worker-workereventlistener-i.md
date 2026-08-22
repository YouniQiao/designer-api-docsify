# WorkerEventListener

事件监听类。

**起始版本：** 9

<!--Device-unnamed-export interface WorkerEventListener--><!--Device-unnamed-export interface WorkerEventListener-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from '@kit.ArkTS';
```

## constructor

```TypeScript
(event: Event): void | Promise<void>
```

指定要调用的回调函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WorkerEventListener-(event: Event): void | Promise<void>--><!--Device-WorkerEventListener-(event: Event): void | Promise<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | 是 | 回调的事件类。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) | The Worker instance is not running. |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) | The called API is not supported in the worker thread. |

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

