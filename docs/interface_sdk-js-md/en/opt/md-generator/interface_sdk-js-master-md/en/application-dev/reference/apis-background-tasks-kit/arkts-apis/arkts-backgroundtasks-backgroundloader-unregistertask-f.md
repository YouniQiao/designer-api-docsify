# unregisterTask

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## unregisterTask

```TypeScript
function unregisterTask(taskInfo: TaskInfo): void
```

Unregister background load task.

**Since:** 26.0.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function unregisterTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function unregisterTask(taskInfo: TaskInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [taskInfo](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-cloudmediaassetstatus-i-sys.md) | [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9700004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
| [9700003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
