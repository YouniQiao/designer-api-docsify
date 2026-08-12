# WorkerEventListener

事件监听类。

**起始版本：** 9

<!--Device-unnamed-export interface WorkerEventListener--><!--Device-unnamed-export interface WorkerEventListener-End-->

**系统能力：** SystemCapability.Utils.Lang

## [[Call]]

```TypeScript
(event: Event): void | Promise<void>
```

指定要调用的回调函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WorkerEventListener-(event: Event): void | Promise<void>--><!--Device-WorkerEventListener-(event: Event): void | Promise<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200005-worker不支持某api) |
| [10200004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkts/errorcode-utils.md#10200004-worker处于非运行状态) |

## 示例

```TypeScript
// Index.ets
import { worker, Event } from "@kit.ArkTS"

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", (event: Event) => {
  console.info("event type is: ", JSON.stringify(event.type));
});

const eventToDispatch : Event = { type: "alert", timeStamp: 0 }; // timeStamp暂未支持
workerInstance.dispatchEvent(eventToDispatch);
```
