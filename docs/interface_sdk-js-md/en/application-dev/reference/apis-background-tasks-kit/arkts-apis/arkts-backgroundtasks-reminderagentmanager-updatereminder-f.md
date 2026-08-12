# updateReminder

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## updateReminder

```TypeScript
function updateReminder(reminderId: int, reminderReq: ReminderRequest): Promise<void>
```

Updates the agent-powered reminder with the specified ID. This API uses a promise to return the result. Only   
[valid (not yet expired) reminders](../../../task-management/agent-powered-reminder.md#constraints) that are not displayed in the notification panel can be updated.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgentManager-function updateReminder(reminderId: int, reminderReq: ReminderRequest): Promise<void>--><!--Device-reminderAgentManager-function updateReminder(reminderId: int, reminderReq: ReminderRequest): Promise<void>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reminderId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the agent-powered reminder to be updated. The reminder ID is returned when the [publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishReminder) API is called. |
| reminderReq | ReminderRequest | Yes | Request instance used to set detailed information such as the reminder type and ringing duration. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1700003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-nonexistent-reminder) | The reminder does not exist. |
| [1700007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700007-invalid-parameter) | If the input parameter is not valid parameter. |

## Examples

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

let reminderId: number = 1;
reminderAgentManager.updateReminder(reminderId, timer).then(() => {
  console.info("update reminder succeed");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

