# getTaskInfo

## Modules to Import

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## getTaskInfo

```TypeScript
function getTaskInfo(taskId: int): Promise<TaskInfo>
```

获取后台预取任务信息。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>--><!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| taskId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 后台加载任务id。 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TaskInfo&gt; | Promise对象， 返回任务信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9700004 | Check on taskId failed. |
| 9700003 | System service operation failed. |
| 201 | Permission denied. |

