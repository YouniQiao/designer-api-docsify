# getTransientTaskInfo

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getTransientTaskInfo

```TypeScript
function getTransientTaskInfo(): Promise<TransientTaskInfo>
```

获取所有短时任务信息，如当日剩余总配额等，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-function getTransientTaskInfo(): Promise<TransientTaskInfo>--><!--Device-backgroundTaskManager-function getTransientTaskInfo(): Promise<TransientTaskInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TransientTaskInfo&gt; | Promise对象，返回所有短时任务信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9900004 | System service operation failed. |
| 9900003 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |
| 9900001 | Caller information verification failed for a transient task. |

## Examples

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  backgroundTaskManager.getTransientTaskInfo().then((res: backgroundTaskManager.TransientTaskInfo) => {
    console.info(`Operation getTransientTaskInfo succeeded. data: ` + JSON.stringify(res));
  }).catch((error : BusinessError) => {
    console.error(`Operation getTransientTaskInfo failed. code is ${error.code} message is ${error.message}`);
  });
} catch (error) {
  console.error(`Operation getTransientTaskInfo failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

