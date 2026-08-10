# offContinuousTaskSuspend

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## offContinuousTaskSuspend

```TypeScript
function offContinuousTaskSuspend(callback?: Callback<ContinuousTaskSuspendInfo>): void
```

取消长时任务暂停的监听，使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function offContinuousTaskSuspend(callback?: Callback<ContinuousTaskSuspendInfo>): void--><!--Device-backgroundTaskManager-function offContinuousTaskSuspend(callback?: Callback<ContinuousTaskSuspendInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuousTaskSuspendInfo&gt; | No | the callback of continuous task suspend. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9800005 | Continuous task verification failed. |
| 201 | Permission denied. |

