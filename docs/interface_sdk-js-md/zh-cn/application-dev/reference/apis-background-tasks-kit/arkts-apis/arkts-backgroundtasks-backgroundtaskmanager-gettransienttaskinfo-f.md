# getTransientTaskInfo

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getTransientTaskInfo

```TypeScript
function getTransientTaskInfo(): Promise<TransientTaskInfo>
```

获取所有短时任务信息，如当日剩余总配额等，使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**返回值：**

| 类型 |
| --- |
| Promise&lt;[TransientTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-transienttaskinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9900001](../errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9900003](../errorcode-backgroundTaskMgr.md#9900003-parcel读写操作失败) |
| [9900004](../errorcode-backgroundTaskMgr.md#9900004-系统服务失败) |
