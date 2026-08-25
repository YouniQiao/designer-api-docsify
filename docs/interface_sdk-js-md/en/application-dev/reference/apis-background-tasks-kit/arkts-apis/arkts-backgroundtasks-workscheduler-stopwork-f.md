# stopWork

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## stopWork

```TypeScript
function stopWork(work: WorkInfo, needCancel?: boolean): void
```

Stops a deferred task.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | Yes |
| needCancel | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../errorcode-workScheduler.md#9700003-system-service-failure) |
| [9700004](../errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
