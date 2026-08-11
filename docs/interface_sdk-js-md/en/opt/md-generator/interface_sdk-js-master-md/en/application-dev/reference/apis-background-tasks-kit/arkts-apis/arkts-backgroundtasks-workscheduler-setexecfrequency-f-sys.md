# setExecFrequency (System API)

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## setExecFrequency

```TypeScript
function setExecFrequency(info: FrequencyInfo): void
```

Set the execution frequency.

**Since:** 26.1.0

**Required permissions:** ohos.permission.SET_WORK_SCHEDULER_PROPERTY

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function setExecFrequency(info: FrequencyInfo): void--><!--Device-workScheduler-function setExecFrequency(info: FrequencyInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [FrequencyInfo](arkts-backgroundtasks-workscheduler-frequencyinfo-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 9700006 |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
