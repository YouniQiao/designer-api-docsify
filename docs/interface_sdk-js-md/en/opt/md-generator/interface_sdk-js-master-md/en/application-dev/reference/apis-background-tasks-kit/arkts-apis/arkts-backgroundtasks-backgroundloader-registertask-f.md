# registerTask

## Modules to Import

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## registerTask

```TypeScript
function registerTask(taskInfo: TaskInfo): void
```

Register background load task.

**Since:** 26.0.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function registerTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function registerTask(taskInfo: TaskInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskInfo | [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
