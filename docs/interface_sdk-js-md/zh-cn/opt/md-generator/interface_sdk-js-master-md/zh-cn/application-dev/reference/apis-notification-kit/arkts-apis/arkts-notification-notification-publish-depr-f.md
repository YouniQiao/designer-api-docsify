# publish

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

发布通知（callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [publish](arkts-notification-notificationmanager-publish-f.md#publish)

<!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void--><!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

发布通知（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [publish](arkts-notification-notificationmanager-publish-f.md#publish)

<!--Device-notification-function publish(request: NotificationRequest): Promise<void>--><!--Device-notification-function publish(request: NotificationRequest): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
