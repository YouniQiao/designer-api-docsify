# updateDataTransferProgress

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## updateDataTransferProgress

```TypeScript
function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void
```

Update notification. Only data transfer ContinuousTasks are supported.

**Since:** 26.1.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundTaskManager-function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void--><!--Device-backgroundTaskManager-function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| progressInfo | [DataTransferProgress](arkts-backgroundtasks-backgroundtaskmanager-datatransferprogress-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9800005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [9800004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800007-continuous-task-storage-failure) |
| [9800006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800006-notification-verification-failure-for-a-continuous-task) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
