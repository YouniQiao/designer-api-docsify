# cancelReminderOnDisplay

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## cancelReminderOnDisplay

```TypeScript
function cancelReminderOnDisplay(reminderId: number): Promise<void>
```

取消当前通知中心内显示的通知卡片，不取消代理提醒数据。例如：每天重复的提醒，该提醒正在通知中心内显示，该接口将通知从通知中心内取消，并且会按照设定的周期，在第二天再次提醒。

**起始版本：** 23

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reminderId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1700003](../errorcode-reminderAgentManager.md#1700003-提醒不存在) |
| [1700007](../errorcode-reminderAgentManager.md#1700007-参数错误) |
