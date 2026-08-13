# updateReminder

## updateReminder

```TypeScript
function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>
```

更新指定id的代理提醒，使用Promise异步回调。仅[有效（未过期）](../../../task-management/agent-powered-reminder.md#约束与限制)、未显示在通知中心的代理提醒支持更新。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PUBLISH_AGENT_REMINDER

<!--Device-reminderAgentManager-function updateReminder(reminderId: int, reminderReq: ReminderRequest): Promise<void>--><!--Device-reminderAgentManager-function updateReminder(reminderId: int, reminderReq: ReminderRequest): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reminderId | number | 是 |
| [reminderReq](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) | [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1700003](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-提醒不存在) |
| [1700007](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700007-参数错误) |

## 示例

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
