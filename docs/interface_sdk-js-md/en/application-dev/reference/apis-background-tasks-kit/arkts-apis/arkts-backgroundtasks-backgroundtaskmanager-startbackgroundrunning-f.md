# startBackgroundRunning

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void
```

Requests a continuous task of a specific type. This API uses an asynchronous callback to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#startbackgroundrunning) added in API version 21.

**Since:** 9

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | Yes |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-notification-verification-failure-for-a-continuous-task) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-continuous-task-storage-failure) |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>
```

Requests a continuous task of a specific type. This API uses a promise to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#startbackgroundrunning) added in API version 21.

**Since:** 9

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | Yes |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-notification-verification-failure-for-a-continuous-task) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-continuous-task-storage-failure) |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>
```

Requests continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#startbackgroundrunning) added in API version 21.

**Since:** 12

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgModes | string[] | Yes |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |

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


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>
```

Requests a continuous task. This API allows a UIAbility (ServiceAbility in the FA model) to request multiple continuous tasks and uses a promise to return the result. When using this API to request a continuous task, its notification can be combined with that of an existing continuous task. For details, see [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md).A maximum of 10 continuous tasks can be created simultaneously. Upon successful creation of a continuous task, a notification will be sent without a prompt tone.If a continuous task requested via this API includes multiple task types (including data transmission tasks), two notifications will appear in the notification panel: one for the data transmission task and the other for the remaining tasks. Removing either notification will cancel the continuous task and remove the other notification. The continuous task notification ID returned by the API is the ID of the data transmission type, which is used to update the data transmission progress.

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
