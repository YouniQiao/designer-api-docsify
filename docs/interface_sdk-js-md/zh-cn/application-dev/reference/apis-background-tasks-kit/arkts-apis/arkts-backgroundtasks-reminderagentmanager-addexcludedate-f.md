# addExcludeDate

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## addExcludeDate

```TypeScript
function addExcludeDate(reminderId: number, date: Date): Promise<void>
```

为指定id的周期性的日历提醒，添加不提醒日期（如每天提醒的日历，设置周二不提醒）。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reminderId | number | 是 |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700003](../errorcode-reminderAgentManager.md#1700003-提醒不存在) |
