# getWorkStatus

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## getWorkStatus

```TypeScript
function getWorkStatus(workId: number, callback: AsyncCallback<WorkInfo>): void
```

Obtains the information a deferred task. This API uses an asynchronous callback to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function getWorkStatus(workId: int, callback: AsyncCallback<WorkInfo>): void--><!--Device-workScheduler-function getWorkStatus(workId: int, callback: AsyncCallback<WorkInfo>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| workId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WorkInfo&gt; | Yes |

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

  workScheduler.getWorkStatus(50, (error: BusinessError, res: workScheduler.WorkInfo) => {
    if (error) {
      console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
    } else {
      console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
    }
  });
```


## getWorkStatus

```TypeScript
function getWorkStatus(workId: number): Promise<WorkInfo>
```

Obtains the information a deferred task. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function getWorkStatus(workId: int): Promise<WorkInfo>--><!--Device-workScheduler-function getWorkStatus(workId: int): Promise<WorkInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| workId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;WorkInfo&gt; |

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

  workScheduler.getWorkStatus(50).then((res: workScheduler.WorkInfo) => {
    console.info(`workschedulerLog getWorkStatus success, ${JSON.stringify(res)}`);
  }).catch((error: BusinessError) => {
    console.error(`workschedulerLog getWorkStatus failed. code is ${error.code} message is ${error.message}`);
  })
```
