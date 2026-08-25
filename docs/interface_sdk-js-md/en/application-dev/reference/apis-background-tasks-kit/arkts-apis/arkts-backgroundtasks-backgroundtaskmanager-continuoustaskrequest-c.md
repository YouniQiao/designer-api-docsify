# ContinuousTaskRequest

Specifies details of the continuous task being requested or updated. It is typically used as input for the [startBackgroundRunning()](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md) and [updateBackgroundRunning()](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md) APIs. Note that:
1. When requesting a continuous task via  
[startBackgroundRunning()](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md), notifications will be combined if the main type and subtype of the continuous task to be requested are the same as those of the existing continuous task in the current application, and the **combinedTaskNotification** value is **true** for both tasks. Otherwise, notifications will not be combined.
2. Notifications will not be combined if the continuous task has no notification.
For details about whether notifications are sent for the continuous task, see [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md).
3. Notifications cannot be combined if the continuous task includes data transmission.
4. Notifications that have been combined cannot be canceled.
If notifications have been combined, they cannot be updated to uncombined.
5. After notifications are combined, tapping the notification will redirect to the UIAbility
corresponding to the first requested continuous task. If the update API is called, the redirection will target the UIAbility corresponding to the last updated continuous task.
6. When the [updateBackgroundRunning()](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md)
API is called to update a continuous task, the input **continuousTaskId** must exist. Otherwise, the update fails.
7. Continuous tasks of the [MODE_SPECIAL_SCENARIO_PROCESSING](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md) type
are supported since API version 22. This task type must be used independently and notifications cannot be combined. Specifically, when you request or update a continuous task, it must be of the **MODE_SPECIAL_SCENARIO_PROCESSING** type. Otherwise, an error is returned.

**Since:** 21

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## checkSpecialScenarioAuth

```TypeScript
checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>
```

Checks whether the user has authorized tasks to run continuously in the background. This API uses a promise to return the result. An exception will be thrown if unauthorized.

**Since:** 22

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;UserAuthResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |

## checkSpecialScenarioAuthResult

```TypeScript
checkSpecialScenarioAuthResult(context: Context): Promise<UserAuthResult>
```

Check whether the application can request MODE_SPECIAL_SCENARIO_PROCESSING. No exception will be thrown whether authorized or not.

**Since:** 26.0.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;UserAuthResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |

## isModeSupported

```TypeScript
isModeSupported(): boolean
```

Checks whether **BackgroundTaskMode** specified in [ContinuousTaskRequest](#continuoustaskrequest) is supported. For details, see [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md).

**Since:** 21

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |

## requestAuthFromUser

```TypeScript
requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void
```

Requests user authorization to run tasks continuously in the background. This API uses an asynchronous callback to return the result. If the API call is successful, a banner notification with a sound is sent. This API is applicable only to continuous tasks of the [MODE_SPECIAL_SCENARIO_PROCESSING](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md) type.

**Since:** 22

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserAuthResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |

## requestAuthFromUserByDialog

```TypeScript
requestAuthFromUserByDialog(context: Context, callback: Callback<UserAuthResult>): void
```

Requesting MODE_SPECIAL_SCENARIO_PROCESSING authorization from users, a dialog box will be displayed.

**Since:** 26.0.0

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UserAuthResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-continuous-task-verification-failure) |

## backgroundTaskModes

```TypeScript
set backgroundTaskModes(value: BackgroundTaskMode[])
```

Main type of a continuous task.Note: The main type must match the subtype.

**Type:** [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md)[]

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## backgroundTaskSubmodes

```TypeScript
set backgroundTaskSubmodes(value: BackgroundTaskSubmode[])
```

Subtype of a continuous task.Note: The main type must match the subtype.

**Type:** [BackgroundTaskSubmode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtasksubmode-e.md)[]

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## combinedTaskNotification

```TypeScript
combinedTaskNotification?: boolean
```

Whether to combine notifications. The value **true** means to combine notifications, and the value **false** (default) means the opposite.Note: This property does not take effect in [updateBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md) API. If notifications need to be combined for an existing task, request the task again and set the value to **true**.

**Type:** boolean

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## continuousTaskId

```TypeScript
continuousTaskId?: number
```

Continuous task ID. The default value is **-1**.Note: If **combinedTaskNotification** is set to true, this property is mandatory and the corresponding ID must exist.Additionally, this property is mandatory (with the corresponding ID required) when used as an input parameter for the [updateBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md) API.You can call the [getAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-getallcontinuoustasks-f.md) API to view information about all continuous tasks.

**Type:** number

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## progressInfo

```TypeScript
progressInfo?: ProgressInfo
```

Notify progress data.

**Type:** ProgressInfo

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## wantAgent

```TypeScript
set wantAgent(value: WantAgent)
```

Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked.

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md)

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
