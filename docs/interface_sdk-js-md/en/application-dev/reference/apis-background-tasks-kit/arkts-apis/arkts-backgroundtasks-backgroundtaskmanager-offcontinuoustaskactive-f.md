# offContinuousTaskActive

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'backgroundTaskManager';
```

## offContinuousTaskActive

```TypeScript
function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void
```

Unregister continuous task active callback.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md)&gt; | No | the callback of continuous task active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) | Continuous task verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

