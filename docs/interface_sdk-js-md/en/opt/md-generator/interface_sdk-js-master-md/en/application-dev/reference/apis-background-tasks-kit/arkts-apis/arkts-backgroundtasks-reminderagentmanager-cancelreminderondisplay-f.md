# cancelReminderOnDisplay

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## cancelReminderOnDisplay

```TypeScript
function cancelReminderOnDisplay(reminderId: number): Promise<void>
```

Cancels the notification card displayed in the notification center with the agent reminder data retained. For example, for a daily repeating reminder, calling this API removes the card from the notification center, but the reminder will be triggered again the next day according to its schedule.

**Since:** 23

<!--Device-reminderAgentManager-function cancelReminderOnDisplay(reminderId: int): Promise<void>--><!--Device-reminderAgentManager-function cancelReminderOnDisplay(reminderId: int): Promise<void>-End-->

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
| [1700003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-nonexistent-reminder) |
| [1700007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700007-invalid-parameter) |

## Examples

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminderOnDisplay(reminderId).then(() => {
  console.info("cancel display reminder  succeed");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
