# stopAndClearWorks

## Modules to Import

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## stopAndClearWorks

```TypeScript
function stopAndClearWorks(): void
```

Stops and clears all the deferred tasks.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function stopAndClearWorks(): void--><!--Device-workScheduler-function stopAndClearWorks(): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [9700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-memory-operation-failure) | Memory operation failed. |
| [9700002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel-operation-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| [9700003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) | System service operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  try{
    workScheduler.stopAndClearWorks();
    console.info(`workschedulerLog stopAndClearWorks success`);
  } catch (error) {
    console.error(`workschedulerLog stopAndClearWorks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
  }
```

