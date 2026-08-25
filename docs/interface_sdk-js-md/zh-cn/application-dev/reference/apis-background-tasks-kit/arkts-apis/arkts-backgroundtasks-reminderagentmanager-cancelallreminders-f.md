# cancelAllReminders

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## cancelAllReminders

```TypeScript
function cancelAllReminders(callback: AsyncCallback<void>): void
```

取消当前应用设置的所有代理提醒。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700004](../errorcode-reminderAgentManager.md#1700004-包名不存在) |


## cancelAllReminders

```TypeScript
function cancelAllReminders(): Promise<void>
```

取消当前应用设置的所有代理提醒。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700004](../errorcode-reminderAgentManager.md#1700004-包名不存在) |
