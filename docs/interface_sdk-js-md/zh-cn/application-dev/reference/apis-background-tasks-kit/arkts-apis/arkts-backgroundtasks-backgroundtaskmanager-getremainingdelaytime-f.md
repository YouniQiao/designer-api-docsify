# getRemainingDelayTime

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void
```

获取本次短时任务的剩余时间，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9900001](../errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9900002](../errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) |


## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number): Promise<number>
```

获取本次短时任务的剩余时间，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9900001](../errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9900002](../errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) |
