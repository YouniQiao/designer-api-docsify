# getTaskInfo

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## getTaskInfo

```TypeScript
function getTaskInfo(taskId: number): Promise<TaskInfo>
```

Obtains the information of a background load task. This API returns the result via a promise.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>--><!--Device-backgroundLoader-function getTaskInfo(taskId: int): Promise<TaskInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;TaskInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
