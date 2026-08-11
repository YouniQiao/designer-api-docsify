# obtainAllContinuousTasks (System API)

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## obtainAllContinuousTasks

```TypeScript
function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>
```

Obtains all continuous task information, including the task ID and type. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_BACKGROUND_TASK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundTaskManager-function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>--><!--Device-backgroundTaskManager-function obtainAllContinuousTasks(): Promise<ContinuousTaskInfo[]>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ContinuousTaskInfo[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
