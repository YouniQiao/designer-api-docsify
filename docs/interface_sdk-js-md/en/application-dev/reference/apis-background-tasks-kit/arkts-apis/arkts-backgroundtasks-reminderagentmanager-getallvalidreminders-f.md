# getAllValidReminders

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## getAllValidReminders

```TypeScript
function getAllValidReminders(): Promise<Array<ReminderInfo>>
```

Obtains all [valid (not yet expired) reminders](../../../task-management/agent-powered-reminder.md#constraints) set by the current application. This API uses a promise to return the result. To call this API, you need to request the ohos.permission.PUBLISH_AGENT_REMINDER permission.

**Since:** 12

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ReminderInfo](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
