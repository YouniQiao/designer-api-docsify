# publishReminder

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void
```

Publishes a reminder. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API can be called only after the
> [notificationManager.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-requestenablenotification-f.md)
> permission is obtained.&gt;

**Since:** 9

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1700001](../errorcode-reminderAgentManager.md#1700001-notification-disabled) |
| [1700002](../errorcode-reminderAgentManager.md#1700002-too-many-reminders) |


## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest): Promise<number>
```

Publishes a reminder. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API can be called only after the
> [notificationManager.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-requestenablenotification-f.md)
> permission is obtained.&gt;

**Since:** 9

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1700001](../errorcode-reminderAgentManager.md#1700001-notification-disabled) |
| [1700002](../errorcode-reminderAgentManager.md#1700002-too-many-reminders) |
