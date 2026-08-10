# obtainAllWorks

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>
```

获取当前应用所有的延迟任务，使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [workScheduler.obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks)(callback:

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>--><!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，获取成功时，err为undefined，否则为错误对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;WorkInfo&gt; | 延迟任务列表，如果已添加延迟任务到执行队列，则返回当前应用所有的延迟任务列表；否则返回空列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |


## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void
```

获取当前应用所有的延迟任务，使用Callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void--><!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;WorkInfo&gt;&gt; | Yes | 回调函数，获取成功时，返回当前应用所有的延迟任务列表，否则抛出异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.obtainAllWorks((error: BusinessError, res: Array<workScheduler.WorkInfo>) =>{
    if (error) {
      console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
    } else {
      console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
    }
  });
```


## obtainAllWorks

```TypeScript
function obtainAllWorks(): Promise<Array<WorkInfo>>
```

获取当前应用所有的延迟任务，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function obtainAllWorks(): Promise<Array<WorkInfo>>--><!--Device-workScheduler-function obtainAllWorks(): Promise<Array<WorkInfo>>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;WorkInfo&gt;&gt; | Promise对象，返回当前应用所有的延迟任务。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9700001 | Memory operation failed. |
| 9700002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9700003 | System service operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { workScheduler } from '@kit.BackgroundTasksKit';

  workScheduler.obtainAllWorks().then((res: Array<workScheduler.WorkInfo>) => {
    console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
  }).catch((error: BusinessError) => {
    console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
  })
```

