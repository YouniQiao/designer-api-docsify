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

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskSuspend(callback: Callback<ContinuousTaskSuspendInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskSuspend(callback: Callback<ContinuousTaskSuspendInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ContinuousTaskSuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustasksuspendinfo-i.md)&gt; | Yes | the callback of continuous task suspend. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) | Continuous task verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

