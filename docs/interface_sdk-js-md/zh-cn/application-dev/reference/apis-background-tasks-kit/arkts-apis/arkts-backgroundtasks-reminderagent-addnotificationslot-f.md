# addNotificationSlot

## 导入模块

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## addNotificationSlot

```TypeScript
function addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void
```

添加一个NotificationSlot，使用回调的方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** addNotificationSlot

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [slot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## addNotificationSlot

```TypeScript
function addNotificationSlot(slot: NotificationSlot): Promise<void>
```

添加一个NotificationSlot，使用Promise方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** addNotificationSlot

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [slot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [NotificationSlot](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
