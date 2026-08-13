# unsubscribe（系统接口）

## unsubscribe

```TypeScript
function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void
```

取消订阅（callbcak形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unsubscribe](arkts-notification-notificationsubscribe-unsubscribe-f-sys.md#unsubscribe（系统接口）)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void--><!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## unsubscribe

```TypeScript
function unsubscribe(subscriber: NotificationSubscriber): Promise<void>
```

取消订阅（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unsubscribe](arkts-notification-notificationsubscribe-unsubscribe-f-sys.md#unsubscribe（系统接口）)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber): Promise<void>--><!--Device-notification-function unsubscribe(subscriber: NotificationSubscriber): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
