# publishReminder

## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void
```

发布后台代理提醒。使用callback异步回调。 > **说明：** > > 该接口需要申请通知弹窗权限 > [notificationManager.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) > 后调用。 >

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgentManager-function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<int>): void--><!--Device-reminderAgentManager-function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700001](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700001-通知使能未开启) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1700002](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700002-提醒数量超出限制) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("callback, reminderId = " + reminderId);
  }
});
```


## publishReminder

```TypeScript
function publishReminder(reminderReq: ReminderRequest): Promise<number>
```

发布后台代理提醒。使用Promise异步回调。 > **说明：** > > 该接口需要申请通知弹窗权限 > [notificationManager.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) > 后调用。 >

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgentManager-function publishReminder(reminderReq: ReminderRequest): Promise<int>--><!--Device-reminderAgentManager-function publishReminder(reminderReq: ReminderRequest): Promise<int>-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700001](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700001-通知使能未开启) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1700002](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700002-提醒数量超出限制) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let timer: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgentManager.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
