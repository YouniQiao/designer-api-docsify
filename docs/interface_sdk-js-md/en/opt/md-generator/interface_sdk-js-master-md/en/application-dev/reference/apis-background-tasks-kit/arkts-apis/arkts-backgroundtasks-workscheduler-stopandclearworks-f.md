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

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function stopAndClearWorks(): void--><!--Device-workScheduler-function stopAndClearWorks(): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) |

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
