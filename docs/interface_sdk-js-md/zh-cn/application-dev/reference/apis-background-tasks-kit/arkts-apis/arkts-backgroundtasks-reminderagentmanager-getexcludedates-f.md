# getExcludeDates

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## getExcludeDates

```TypeScript
function getExcludeDates(reminderId: number): Promise<Array<Date>>
```

为指定id的周期性的日历提醒，查询设置的所有不提醒日期。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reminderId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Date & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1700003](../errorcode-reminderAgentManager.md#1700003-提醒不存在) |
