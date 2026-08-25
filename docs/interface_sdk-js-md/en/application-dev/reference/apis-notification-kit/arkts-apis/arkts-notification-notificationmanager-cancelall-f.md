# cancelAll

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancelAll

```TypeScript
function cancelAll(callback: AsyncCallback<void>): void
```

Cancels all notifications of this application. This API uses an asynchronous callback to return the result.After cancellation, all notifications of the current application will be removed from the notification center, status bar, and other locations, and will no longer be visible to the user. This is suitable for scenarios such as application exit or when the user manually clears all notifications.

**Since:** 9

**System capability:** SystemCapability.Notification.Notification

**See also:**

publish publishes a notification.

cancel cancels a published notification based

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |


## cancelAll

```TypeScript
function cancelAll(): Promise<void>
```

Cancels all notifications of this application. This API uses a promise to return the result.After cancellation, all notifications of the current application will be removed from the notification center, status bar, and other locations, and will no longer be visible to the user. This is suitable for scenarios such as application exit or when the user manually clears all notifications.

**Since:** 9

**System capability:** SystemCapability.Notification.Notification

**See also:**

publish publishes a notification.

cancel cancels a notification with the specified ID.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
