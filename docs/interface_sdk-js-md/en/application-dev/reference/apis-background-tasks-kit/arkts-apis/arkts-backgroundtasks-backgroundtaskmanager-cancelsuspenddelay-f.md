# cancelSuspendDelay

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'backgroundTaskManager';
```

## cancelSuspendDelay

```TypeScript
function cancelSuspendDelay(requestId: int): void
```

Cancels a transient task.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: int): void--><!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: int): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| requestId | int | Yes | Request ID of the transient task. It is obtained by calling the [requestSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-requestsuspenddelay-f.md#requestSuspendDelay) API. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br> 2. Incorrect parameters types; 3. Parameter verification failed. |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) | System service operation failed. |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) | Memory operation failed. |
| [9900002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-transient-task-verification-failure) | Transient task verification failed. |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc-failure) | Internal transaction failed. |
| [9900001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-caller-information-verification-failure-for-a-transient-task) | Caller information verification failed for a transient task. |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; <br> 2. Failed to apply for memory. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
try {
  backgroundTaskManager.cancelSuspendDelay(id);
} catch (error) {
  console.error(`cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

