# resetExecFrequency (System API)

## Modules to Import

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## resetExecFrequency

```TypeScript
function resetExecFrequency(uid: number): void
```

Reset the execution frequency.

**Since:** 26.1.0

**Required permissions:** ohos.permission.SET_WORK_SCHEDULER_PROPERTY

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function resetExecFrequency(uid: number): void--><!--Device-workScheduler-function resetExecFrequency(uid: number): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 9700006 |
| [9700003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
