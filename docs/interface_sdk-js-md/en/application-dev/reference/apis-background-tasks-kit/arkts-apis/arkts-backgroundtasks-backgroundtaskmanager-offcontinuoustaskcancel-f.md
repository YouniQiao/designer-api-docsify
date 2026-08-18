# offContinuousTaskCancel

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## offContinuousTaskCancel

```TypeScript
function offContinuousTaskCancel(callback?: Callback<ContinuousTaskCancelInfo>): void
```

Unregister continuous task cancel callback.

**Since:** 23

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function offContinuousTaskCancel(callback?: Callback<ContinuousTaskCancelInfo>): void--><!--Device-backgroundTaskManager-function offContinuousTaskCancel(callback?: Callback<ContinuousTaskCancelInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskCancelInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskcancelinfo-i.md)&gt; | No | the callback of continuous task cancel. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

