# startWork

## Modules to Import

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## startWork

```TypeScript
function startWork(work: WorkInfo): void
```

Requests a deferred task. Upon successful request, the deferred task is added to the execution queue and will be executed by the system once the trigger conditions are met.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function startWork(work: WorkInfo): void--><!--Device-workScheduler-function startWork(work: WorkInfo): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9700004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo-verification-failure) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9700005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700005-startwork-call-failure) |
| [9700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |

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
    workScheduler.startWork(workInfo);
    console.info('workschedulerLog startWork success');
  } catch (error) {
    console.error(`workschedulerLog startwork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```
