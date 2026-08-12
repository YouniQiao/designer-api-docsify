# getSlot

## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void
```

获取一个指定类型的通知通道（callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getSlot](ohos.notificationManager/notificationManager#getSlot)

<!--Device-notification-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void--><!--Device-notification-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt; | 是 |


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot>
```

获取一个指定类型的通知通道（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getSlot](ohos.notificationManager/notificationManager#getSlot)

<!--Device-notification-function getSlot(slotType: SlotType): Promise<NotificationSlot>--><!--Device-notification-function getSlot(slotType: SlotType): Promise<NotificationSlot>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt; |
