# getBackgroundTaskState (System API)

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getBackgroundTaskState

```TypeScript
function getBackgroundTaskState(stateInfo: BackgroundTaskStateInfo): UserAuthResult
```

获取长时任务授权信息。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Required permissions:** ohos.permission.SET_BACKGROUND_TASK_STATE

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundTaskManager-function getBackgroundTaskState(stateInfo: BackgroundTaskStateInfo): UserAuthResult--><!--Device-backgroundTaskManager-function getBackgroundTaskState(stateInfo: BackgroundTaskStateInfo): UserAuthResult-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stateInfo | [BackgroundTaskStateInfo](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskstateinfo-i-sys.md) | Yes | 授权的必要信息，包括用户ID、应用包名、应用分身ID等。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UserAuthResult](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-userauthresult-i.md) | 授权结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9800005 | Continuous task verification failed. |
| 9800004 | System service operation failed. |
| 201 | Permission denied. |
| 202 | Not System App. |

## Examples

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Update the parameters based on the actual situation.
    let backgroundTaskStateInfo: backgroundTaskManager.BackgroundTaskStateInfo = {
        userId: 100,
        bundleName: 'com.example.continuoustask',
        appIndex: 0
    };
    let auth = backgroundTaskManager.getBackgroundTaskState(backgroundTaskStateInfo);
    console.info('Operation getBackgroundTaskState succeeded. data: ' + JSON.stringify(auth));
} catch (error) {
    console.error(`Operation getBackgroundTaskState failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

