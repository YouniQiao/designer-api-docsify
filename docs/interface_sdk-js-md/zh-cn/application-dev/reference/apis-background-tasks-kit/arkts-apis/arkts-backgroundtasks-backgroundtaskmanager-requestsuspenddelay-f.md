# requestSuspendDelay

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## requestSuspendDelay

```TypeScript
function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo
```

申请短时任务。

> **说明：**&gt;
> 短时任务的申请和使用过程中的约束与限制请参考[指南](../../../task-management/transient-task.md#约束与限制)。

**起始版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md) |

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
