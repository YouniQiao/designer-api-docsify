# obtainAllContinuousTasks (System API)

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'backgroundTaskManager';
```

## obtainAllContinuousTasks

```TypeScript
function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>
```

Obtains all continuous task information, including the task ID and type. This API uses a promise to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BACKGROUND_TASK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundTaskManager-function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>--><!--Device-backgroundTaskManager-function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md)[]&gt; | Promise that returns all continuous task information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) | System service operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    // If no continuous task is requested, an empty array is obtained.
    backgroundTaskManager.obtainAllContinuousTasks().then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
        console.info(`Operation obtainAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
    }).catch((error: BusinessError) => {
        console.error(`Operation obtainAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
    });
} catch (error) {
    console.error(`Operation obtainAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

