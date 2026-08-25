# getActiveNotifications

## 导入模块

```TypeScript
```

## getActiveNotifications

```TypeScript
function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void
```

获取当前应用未删除的通知列表（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)&gt;&gt; | 是 |


## getActiveNotifications

```TypeScript
function getActiveNotifications(): Promise<Array<NotificationRequest>>
```

获取当前应用未删除的通知列表（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md)

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)&gt;&gt; |
