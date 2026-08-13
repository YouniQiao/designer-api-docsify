# getTransientTaskInfo

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## getTransientTaskInfo

```TypeScript
function getTransientTaskInfo(): Promise<TransientTaskInfo>
```

Obtains all transient task information, including the remaining quota of the current day. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-backgroundTaskManager-function getTransientTaskInfo(): Promise<TransientTaskInfo>--><!--Device-backgroundTaskManager-function getTransientTaskInfo(): Promise<TransientTaskInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TransientTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-transienttaskinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9900004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900004-system-service-failure) |
| [9900003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900003-parcel-operation-failure) |
| [9900001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-caller-information-verification-failure-for-a-transient-task) |

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
