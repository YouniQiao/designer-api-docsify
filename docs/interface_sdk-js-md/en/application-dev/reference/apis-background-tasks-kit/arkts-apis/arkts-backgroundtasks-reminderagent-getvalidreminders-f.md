# getValidReminders

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## getValidReminders

```TypeScript
function getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void
```

Obtains all valid (not yet expired) reminders set by the current application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getValidReminders

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ReminderRequest&gt;&gt; | Yes |


## getValidReminders

```TypeScript
function getValidReminders(): Promise<Array<ReminderRequest>>
```

Obtains all valid (not yet expired) reminders set by the current application. This API uses a promise to return the reminders.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getValidReminders

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ReminderRequest & gt; & gt; |
