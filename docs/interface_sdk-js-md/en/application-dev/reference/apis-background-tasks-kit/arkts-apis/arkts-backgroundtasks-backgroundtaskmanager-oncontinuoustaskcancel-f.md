# onContinuousTaskCancel

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## onContinuousTaskCancel

```TypeScript
function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void
```

Register continuous task cancel callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuousTaskCancelInfo&gt; | Yes | the callback of continuous task cancel. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

