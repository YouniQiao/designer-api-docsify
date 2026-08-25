# startBackgroundRunning

## Modules to Import

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void
```

Requests a continuous task from the system. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [startBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| request | [NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>
```

Requests a continuous task from the system. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [startBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| request | [NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
