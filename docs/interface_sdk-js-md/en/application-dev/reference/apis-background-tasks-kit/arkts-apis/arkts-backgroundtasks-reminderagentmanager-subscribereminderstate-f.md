# subscribeReminderState

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## subscribeReminderState

```TypeScript
function subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>
```

Subscribes to agent-powered reminder state changes. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[ReminderState](arkts-backgroundtasks-reminderagentmanager-reminderstate-i.md)&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1700007](../errorcode-reminderAgentManager.md#1700007-invalid-parameter) |
