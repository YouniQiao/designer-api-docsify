# updateBackgroundRunning

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## updateBackgroundRunning

```TypeScript
function updateBackgroundRunning(context: Context, bgModes: string[]): Promise<ContinuousTaskNotification>
```

Updates continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task is successfully updated, there will be a notification message without prompt tone.Before updating a continuous task, you can call [getAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-getallcontinuoustasks-f.md) to retrieve information about all existing continuous tasks. If there are no continuous tasks, the update will fail.This API can only be used to update continuous tasks that were requested via the following APIs:  
[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback&lt;void&gt;): void](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)  
[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise&lt;void&gt;](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)  
[startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise&lt;ContinuousTaskNotification&gt;][startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**Since:** 12

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgModes | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ContinuousTaskNotification](arkts-backgroundtasks-backgroundtaskmanager-continuoustasknotification-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-notification-verification-failure-for-a-continuous-task) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-continuous-task-storage-failure) |


## updateBackgroundRunning

```TypeScript
function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>
```

Updates a continuous task. This API uses a promise to return the result. After a continuous task is successfully updated, there will be a notification message without prompt tone.The following restrictions apply when updating a continuous task:
1. This API can only update continuous tasks requested via  
[startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md).
2. If the main type and subtype of the background tasks are the same,
only the wants information (such as **abilityName**) in **ContinuousTaskRequest.wantAgent** can be updated. If the types are different, the update fails.
3. If the continuous task to be updated or the specified update type contains the data transmission type,
a failure message is returned.

**Since:** 21

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| request | [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ContinuousTaskNotification](arkts-backgroundtasks-backgroundtaskmanager-continuoustasknotification-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-notification-verification-failure-for-a-continuous-task) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-continuous-task-storage-failure) |
