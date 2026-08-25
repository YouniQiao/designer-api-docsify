# getTransientTaskInfo

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## getTransientTaskInfo

```TypeScript
function getTransientTaskInfo(): Promise<TransientTaskInfo>
```

Obtains all transient task information, including the remaining quota of the current day. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TransientTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-transienttaskinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9900001](../errorcode-backgroundTaskMgr.md#9900001-caller-information-verification-failure-for-a-transient-task) |
| [9900003](../errorcode-backgroundTaskMgr.md#9900003-parcel-operation-failure) |
| [9900004](../errorcode-backgroundTaskMgr.md#9900004-system-service-failure) |
