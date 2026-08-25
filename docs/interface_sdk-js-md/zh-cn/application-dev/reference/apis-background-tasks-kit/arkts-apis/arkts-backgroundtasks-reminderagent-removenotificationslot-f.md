# removeNotificationSlot

## 导入模块

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## removeNotificationSlot

```TypeScript
function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void
```

删除目标NotificationSlot，使用callback方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeNotificationSlot

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | notification.SlotType | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## removeNotificationSlot

```TypeScript
function removeNotificationSlot(slotType: notification.SlotType): Promise<void>
```

删除目标NotificationSlot，使用Promise方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** removeNotificationSlot

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | notification.SlotType | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
