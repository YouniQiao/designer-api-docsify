# cancelReminder

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## cancelReminder

```TypeScript
function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void
```

Cancels the reminder with the specified ID. This API uses an asynchronous callback to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelreminder)

<!--Device-reminderAgent-function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void--><!--Device-reminderAgent-function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reminderId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelReminder(1, (err: BusinessError, data: void) => {
  console.info("cancelReminder callback");
});
```


## cancelReminder

```TypeScript
function cancelReminder(reminderId: number): Promise<void>
```

Cancels the reminder with the specified ID. This API uses a promise to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelreminder)

<!--Device-reminderAgent-function cancelReminder(reminderId: number): Promise<void>--><!--Device-reminderAgent-function cancelReminder(reminderId: number): Promise<void>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reminderId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelReminder(1).then(() => {
    console.info("cancelReminder promise");
});
```
