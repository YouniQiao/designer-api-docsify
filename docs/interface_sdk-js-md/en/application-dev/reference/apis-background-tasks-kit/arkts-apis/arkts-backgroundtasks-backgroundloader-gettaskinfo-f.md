# getTaskInfo

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## getTaskInfo

```TypeScript
function getTaskInfo(taskId: int): Promise<TaskInfo>
```

Obtains the information of a background load task. This API returns the result via a promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>--><!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| taskId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Id of the background load task. &lt;br&gt;The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TaskInfo&gt; | Promise used to return the TaskInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9700004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) | Check on taskInfo failed. |
| [9700003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) | System service operation failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | No permission. |

