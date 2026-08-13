# onContinuousTaskSuspend

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## onContinuousTaskSuspend

```TypeScript
function onContinuousTaskSuspend(callback: Callback<ContinuousTaskSuspendInfo>): void
```

Register continuous task suspend callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskSuspend(callback: Callback<ContinuousTaskSuspendInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskSuspend(callback: Callback<ContinuousTaskSuspendInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskSuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustasksuspendinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
