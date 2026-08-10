# publishReminder

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void
```

发布一个后台代理提醒，使用回调的方式实现异步调用，该方法需要申请通知弹窗权限  
[Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification)后才能调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishreminder)

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgent-function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void--><!--Device-reminderAgent-function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | Yes | 需要发布的提醒实例。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步回调，返回当前发布的提醒的id。 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import reminderAgent from '@ohos.reminderAgent';

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  console.info("callback, reminderId = " + reminderId);
});
```


## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest): Promise<number>
```

发布一个后台代理提醒，使用Promise方式实现异步调用，该方法需要申请通知弹窗权限  
[Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification)后才能调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishreminder)

**Required permissions:** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgent-function publishReminder(reminderReq: ReminderRequest): Promise<number>--><!--Device-reminderAgent-function publishReminder(reminderReq: ReminderRequest): Promise<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | Yes | Indicates the reminder instance to publish. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | reminder id. |

## Examples

```TypeScript
import reminderAgent from '@ohos.reminderAgent';

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
});
```

