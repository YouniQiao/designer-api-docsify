# publish (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { notificationSubscribe } from '@kit.NotificationKit';
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, userId: number, callback: AsyncCallback<void>): void
```

Publishes a notification to a specified user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [publish](arkts-notification-notificationmanager-publish-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function publish(request: NotificationRequest, userId: number, callback: AsyncCallback<void>): void--><!--Device-notification-function publish(request: NotificationRequest, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes | Content and related configuration of the notification to publish. |
| userId | number | Yes | User ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |


## publish

```TypeScript
function publish(request: NotificationRequest, userId: number): Promise<void>
```

Publishes a notification to a specified user. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [publish](arkts-notification-notificationmanager-publish-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function publish(request: NotificationRequest, userId: number): Promise<void>--><!--Device-notification-function publish(request: NotificationRequest, userId: number): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes | Content and related configuration of the notification to publish. |
| userId | number | Yes | User ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

