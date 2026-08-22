# onContinuousTaskActive

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## onContinuousTaskActive

```TypeScript
function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void
```

Register continuous task active callback.

**Since:** 23

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md)&gt; | Yes | the callback of continuous task active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) | Continuous task verification failed. |

