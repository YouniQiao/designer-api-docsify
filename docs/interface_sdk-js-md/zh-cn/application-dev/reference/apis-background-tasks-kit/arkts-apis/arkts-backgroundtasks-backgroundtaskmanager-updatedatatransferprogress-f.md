# updateDataTransferProgress

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## updateDataTransferProgress

```TypeScript
function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void
```

更新通知。仅支持数据传输类型长时任务。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| progressInfo | [DataTransferProgress](arkts-backgroundtasks-backgroundtaskmanager-datatransferprogress-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-长时任务通知信息校验失败) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-长时任务信息存储失败) |
