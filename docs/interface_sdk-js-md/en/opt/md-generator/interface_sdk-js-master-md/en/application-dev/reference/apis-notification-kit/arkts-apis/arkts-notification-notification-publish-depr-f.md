# publish

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

Publishes a notification. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#publish

<!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void--><!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

Publishes a notification. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#publish

<!--Device-notification-function publish(request: NotificationRequest): Promise<void>--><!--Device-notification-function publish(request: NotificationRequest): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
