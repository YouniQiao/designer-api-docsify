# addSlots（系统接口）

## addSlots

```TypeScript
function addSlots(slots: Array<NotificationSlot>, callback: AsyncCallback<void>): void
```

创建多个通知通道（callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addSlots](ohos.notificationManager/notificationManager#addSlots)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function addSlots(slots: Array<NotificationSlot>, callback: AsyncCallback<void>): void--><!--Device-notification-function addSlots(slots: Array<NotificationSlot>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slots | Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## addSlots

```TypeScript
function addSlots(slots: Array<NotificationSlot>): Promise<void>
```

创建多个通知通道（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [addSlots](ohos.notificationManager/notificationManager#addSlots)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function addSlots(slots: Array<NotificationSlot>): Promise<void>--><!--Device-notification-function addSlots(slots: Array<NotificationSlot>): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slots | Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
