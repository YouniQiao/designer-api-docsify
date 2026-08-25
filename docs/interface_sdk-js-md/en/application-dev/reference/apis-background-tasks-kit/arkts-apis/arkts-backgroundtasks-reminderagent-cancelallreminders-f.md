# cancelAllReminders

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## cancelAllReminders

```TypeScript
function cancelAllReminders(callback: AsyncCallback<void>): void
```

Cancels all reminders set by the current application. This API uses an asynchronous callback to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** cancelAllReminders

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## cancelAllReminders

```TypeScript
function cancelAllReminders(): Promise<void>
```

Cancels all reminders set by the current application. This API uses a promise to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** cancelAllReminders

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
