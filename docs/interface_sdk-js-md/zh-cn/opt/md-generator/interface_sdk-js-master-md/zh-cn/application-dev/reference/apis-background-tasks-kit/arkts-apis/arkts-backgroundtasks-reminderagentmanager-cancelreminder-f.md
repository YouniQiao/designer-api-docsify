# cancelReminder

## cancelReminder

```TypeScript
function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void
```

取消指定id的代理提醒。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-reminderAgentManager-function cancelReminder(reminderId: int, callback: AsyncCallback<void>): void--><!--Device-reminderAgentManager-function cancelReminder(reminderId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reminderId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700003](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-提醒不存在) |
| [1700004](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700004-包名不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId, (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("cancelReminder callback");
  }
});
```


## cancelReminder

```TypeScript
function cancelReminder(reminderId: number): Promise<void>
```

取消指定id的代理提醒。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-reminderAgentManager-function cancelReminder(reminderId: int): Promise<void>--><!--Device-reminderAgentManager-function cancelReminder(reminderId: int): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1700003](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700003-提醒不存在) |
| [1700004](../../apis-backgroundtasks-kit/errorcode-reminderAgentManager.md#1700004-包名不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.cancelReminder(reminderId).then(() => {
  console.info("cancelReminder promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
