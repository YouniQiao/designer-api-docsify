# cancelAllReminders

## Modules to Import

```TypeScript
```

## cancelAllReminders

```TypeScript
function cancelAllReminders(callback: AsyncCallback<void>): void
```

Cancels all reminders set by the current application. This API uses an asynchronous callback to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** cancelAllReminders

<!--Device-reminderAgent-function cancelAllReminders(callback: AsyncCallback<void>): void--><!--Device-reminderAgent-function cancelAllReminders(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
  console.info("cancelAllReminders callback")
})
```


## cancelAllReminders

```TypeScript
function cancelAllReminders(): Promise<void>
```

Cancels all reminders set by the current application. This API uses a promise to return the cancellation result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** cancelAllReminders

<!--Device-reminderAgent-function cancelAllReminders(): Promise<void>--><!--Device-reminderAgent-function cancelAllReminders(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelAllReminders().then(() => {
    console.info("cancelAllReminders promise")
})
```
