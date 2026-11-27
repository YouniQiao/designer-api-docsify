# finishTask

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## finishTask

```TypeScript
function finishTask(taskInfo: TaskInfo): void
```

Finish background load task.

**Since:** 26.1.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| taskInfo | [TaskInfo](arkts-backgroundtasks-backgroundloader-taskinfo-i.md) | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 9710001 | Memory operation failed. |
| 9710002 | Parcel operation failed. |
| 9710003 | Background loader service operation failed. |
| 9710004 | Parameter error. |
| 9710005 | Background load failed. |
