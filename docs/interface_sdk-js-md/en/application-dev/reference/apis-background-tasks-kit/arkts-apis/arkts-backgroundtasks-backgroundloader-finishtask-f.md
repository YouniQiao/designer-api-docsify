# finishTask

## Modules to Import

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## finishTask

```TypeScript
function finishTask(taskInfo: TaskInfo): void
```

结束后台加载任务。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| taskInfo | [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md) | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9700004 | Check on taskInfo failed. |
| 9700003 | System service operation failed. |
| 201 | 后台加载任务信息。 |

