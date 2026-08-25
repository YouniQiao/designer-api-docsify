# EventTarget

用于管理Worker的监听事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md)

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: EventListener): void
```

向Worker添加一个事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** addEventListener

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | 是 |

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

分发Worker实例上已注册的事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** dispatchEvent

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## removeAllListener

```TypeScript
removeAllListener(): void
```

移除Worker所有的事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeAllListener

**系统能力：** SystemCapability.Utils.Lang

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: EventListener): void
```

移除Worker的事件监听。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeEventListener

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| callback | [EventListener](arkts-arkts-worker-eventlistener-i.md) | 否 |
