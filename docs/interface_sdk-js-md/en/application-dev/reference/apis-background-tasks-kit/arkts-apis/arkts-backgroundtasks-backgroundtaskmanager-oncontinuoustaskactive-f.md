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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md)&gt; | Yes | the callback of continuous task active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9800005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) | Continuous task verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

