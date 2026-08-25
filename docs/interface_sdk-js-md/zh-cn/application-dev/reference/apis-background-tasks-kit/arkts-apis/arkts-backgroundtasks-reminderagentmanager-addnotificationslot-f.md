# addNotificationSlot

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## addNotificationSlot

```TypeScript
function addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void
```

添加通知渠道。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [slot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## addNotificationSlot

```TypeScript
function addNotificationSlot(slot: NotificationSlot): Promise<void>
```

添加通知渠道。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [slot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
