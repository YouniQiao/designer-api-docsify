# deleteExcludeDates

## deleteExcludeDates

```TypeScript
function deleteExcludeDates(reminderId: number): Promise<void>
```

为指定id的周期性的日历提醒，删除设置的所有不提醒日期。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>--><!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>-End-->

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1700003](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-提醒不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
  console.info("deleteExcludeDates promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
