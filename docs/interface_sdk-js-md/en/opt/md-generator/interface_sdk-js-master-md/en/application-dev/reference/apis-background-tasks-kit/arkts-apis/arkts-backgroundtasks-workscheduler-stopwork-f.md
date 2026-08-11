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

<!--Device-workScheduler-function stopWork(work: WorkInfo, needCancel?: boolean): void--><!--Device-workScheduler-function stopWork(work: WorkInfo, needCancel?: boolean): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | Yes |
| needCancel | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  let workInfo: workScheduler.WorkInfo = {
      workId: 1,
      batteryStatus:workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
      isRepeat: false,
      isPersisted: true,
      bundleName: "com.example.myapplication",
      abilityName: "MyExtension",
      parameters: {
          mykey0: 1,
          mykey1: "string value",
          mykey2: true,
          mykey3: 1.5
      }
     }
  try{
    workScheduler.stopWork(workInfo, false);
    console.info('workschedulerLog stopWork success');
  } catch (error) {
    console.error(`workschedulerLog stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```
