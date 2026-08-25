# getAllContinuousTasks

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getAllContinuousTasks

```TypeScript
function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>
```

获取所有长时任务信息，如长时任务ID、长时任务类型等，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |


## getAllContinuousTasks

```TypeScript
function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>
```

获取所有长时任务信息，如长时任务ID、长时任务类型等。可选择是否获取暂停的长时任务信息，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| includeSuspended | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
