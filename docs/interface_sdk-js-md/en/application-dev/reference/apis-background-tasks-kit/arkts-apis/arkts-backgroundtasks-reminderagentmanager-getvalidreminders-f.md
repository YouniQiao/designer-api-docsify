# getValidReminders

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## getValidReminders

```TypeScript
function getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void
```

Obtains all [valid (not yet expired) reminders](../../../task-management/agent-powered-reminder.md#constraints) set by the current application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ReminderRequest&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1700004](../errorcode-reminderAgentManager.md#1700004-nonexistent-bundle-name) |


## getValidReminders

```TypeScript
function getValidReminders(): Promise<Array<ReminderRequest>>
```

Obtains all [valid (not yet expired) reminders](../../../task-management/agent-powered-reminder.md#constraints) set by the current application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ReminderRequest & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1700004](../errorcode-reminderAgentManager.md#1700004-nonexistent-bundle-name) |
