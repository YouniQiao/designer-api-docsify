# getAllValidReminders

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## getAllValidReminders

```TypeScript
function getAllValidReminders(): Promise<Array<ReminderInfo>>
```

获取当前应用设置的所有[有效（未过期）的代理提醒](../../../task-management/agent-powered-reminder.md#约束与限制)。使用Promise异步回调。 该接口调用需要申请ohos.permission.PUBLISH_AGENT_REMINDER权限。

**起始版本：** 12

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ReminderInfo](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
