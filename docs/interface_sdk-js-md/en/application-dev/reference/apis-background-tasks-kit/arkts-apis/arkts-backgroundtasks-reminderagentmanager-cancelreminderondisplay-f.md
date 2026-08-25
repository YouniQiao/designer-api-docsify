# cancelReminderOnDisplay

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## cancelReminderOnDisplay

```TypeScript
function cancelReminderOnDisplay(reminderId: number): Promise<void>
```

Cancels the notification card displayed in the notification center with the agent reminder data retained. For example, for a daily repeating reminder, calling this API removes the card from the notification center, but the reminder will be triggered again the next day according to its schedule.

**Since:** 23

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reminderId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1700003](../errorcode-reminderAgentManager.md#1700003-nonexistent-reminder) |
| [1700007](../errorcode-reminderAgentManager.md#1700007-invalid-parameter) |
