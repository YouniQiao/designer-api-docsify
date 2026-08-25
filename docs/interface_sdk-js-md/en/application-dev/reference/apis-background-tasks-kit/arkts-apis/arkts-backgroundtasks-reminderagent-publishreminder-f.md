# publishReminder

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void
```

Publishes a reminder through the reminder agent. This API uses an asynchronous callback to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** publishReminder

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest): Promise<number>
```

Publishes a reminder through the reminder agent. This API uses a promise to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** publishReminder

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
