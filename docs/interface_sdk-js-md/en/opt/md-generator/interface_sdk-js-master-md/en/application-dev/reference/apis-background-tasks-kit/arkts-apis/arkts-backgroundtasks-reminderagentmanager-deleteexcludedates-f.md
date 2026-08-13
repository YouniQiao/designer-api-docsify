# deleteExcludeDates

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## deleteExcludeDates

```TypeScript
function deleteExcludeDates(reminderId: number): Promise<void>
```

Deletes all non-reminder dates for a recurring calendar reminder with a specific ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>--><!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>-End-->

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1700003](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-nonexistent-reminder) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
  console.info("deleteExcludeDates promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
