# publish

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

Publishes a notification. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** publish

<!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void--><!--Device-notification-function publish(request: NotificationRequest, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-t.md) | Yes | Content and related configuration of the notification to publish. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-i.md)<void> | Yes | Callback used to return the result. |


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

Publishes a notification. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** publish

<!--Device-notification-function publish(request: NotificationRequest): Promise<void>--><!--Device-notification-function publish(request: NotificationRequest): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-t.md) | Yes | Content and related configuration of the notification to publish. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

