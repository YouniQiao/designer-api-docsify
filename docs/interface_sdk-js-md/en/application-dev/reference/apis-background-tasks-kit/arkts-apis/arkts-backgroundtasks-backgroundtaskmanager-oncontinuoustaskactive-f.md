# onContinuousTaskActive

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## onContinuousTaskActive

```TypeScript
function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void
```

注册长时任务激活的监听，使用callback异步回调。应用回前台激活暂停的长时任务。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuousTaskActiveInfo&gt; | Yes | the callback of continuous task active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9800005 | Continuous task verification failed. |
| 201 | Permission denied. |

