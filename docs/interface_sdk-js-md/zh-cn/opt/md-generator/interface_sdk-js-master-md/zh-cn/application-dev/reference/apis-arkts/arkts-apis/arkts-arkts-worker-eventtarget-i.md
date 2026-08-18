# EventTarget

用于管理Worker的监听事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md#workereventtarget)

<!--Device-unnamed-export interface EventTarget--><!--Device-unnamed-export interface EventTarget-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: EventListener): void
```

向Worker添加一个事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** addEventListener

<!--Device-EventTarget-addEventListener(type: string, listener: EventListener): void--><!--Device-EventTarget-addEventListener(type: string, listener: EventListener): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | 是 |

**示例**

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})
```

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

分发Worker实例上已注册的事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** dispatchEvent

<!--Device-EventTarget-dispatchEvent(event: Event): boolean--><!--Device-EventTarget-dispatchEvent(event: Event): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.dispatchEvent({type: 'alert_add', timeStamp: 0}); // timeStamp暂未支持
```

分发事件（dispatchEvent）可与监听接口（addEventListener）搭配使用，示例如下：

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}
```

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", ()=>{
  console.info("alert listener callback");
})

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.dispatchEvent({type:"alert", timeStamp:0}); // timeStamp暂未支持
}
```

## removeAllListener

```TypeScript
removeAllListener(): void
```

移除Worker所有的事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeAllListener

<!--Device-EventTarget-removeAllListener(): void--><!--Device-EventTarget-removeAllListener(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**示例**

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert_add", ()=>{
  console.info("alert listener callback");
})

workerPort.removeAllListener();
```

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: EventListener): void
```

移除Worker的事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeEventListener

<!--Device-EventTarget-removeEventListener(type: string, callback?: EventListener): void--><!--Device-EventTarget-removeEventListener(type: string, callback?: EventListener): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| callback | [EventListener](arkts-arkts-worker-eventlistener-i.md) | 否 |

**示例**

```TypeScript
// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerPort.removeEventListener('alert');
```
