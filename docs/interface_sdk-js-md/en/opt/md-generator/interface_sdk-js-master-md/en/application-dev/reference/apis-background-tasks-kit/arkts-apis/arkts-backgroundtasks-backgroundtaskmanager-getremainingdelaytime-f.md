# getRemainingDelayTime

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void
```

Obtains the remaining time of a transient task. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int, callback: AsyncCallback<int>): void--><!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9900002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-transient-task-verification-failure) |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9900001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-caller-information-verification-failure-for-a-transient-task) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id, (error: BusinessError, res: number) => {
  if(error) {
    console.error(`callback => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
  } else {
    console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
  }
})
```


## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number): Promise<number>
```

Obtains the remaining time of a transient task. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int): Promise<int>--><!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int): Promise<int>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9900002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-transient-task-verification-failure) |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9900001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-caller-information-verification-failure-for-a-transient-task) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
  console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
}).catch((error: BusinessError) => {
  console.error(`promise => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
})
```
