# cancel

## Modules to Import

```TypeScript
```

## cancel

```TypeScript
function cancel(id: number, callback: AsyncCallback<void>): void
```

Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result. After cancellation, the corresponding notification will be removed from the notification center, status bar, etc., and will no longer be visible to the user. Compared with notificationManager.cancel(id, label, callback), which includes the label parameter, this API does not pass in a label and will cancel the notification matching the specified ID. When a notification is published with a non-empty label, the `notificationManager.cancel(id, label, callback)` API must be used to cancel it.

**Since:** 23

<!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

publish publishes a notification.

cancelAll cancels all notifications of this application.

cancelGroup cancels notifications

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  }
}
notificationManager.cancel(0, cancelCallback);
```


## cancel

```TypeScript
function cancel(id: number, label: string, callback: AsyncCallback<void>): void
```

Cancels a published notification based on the notification ID and label. This API uses an asynchronous callback to return the result. After cancellation, the corresponding notification will be removed from the notification center, status bar, and other locations, and will no longer be visible to the user. This is suitable for scenarios where a specific notification with a particular tag needs to be precisely canceled. Compared with notificationManager.cancel(id, callback), which requires only the notification ID, this API additionally has the **label** parameter, allowing precise cancellation of notifications with the same ID but different labels.

**Since:** 23

<!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

publish publishes a notification.

cancelAll cancels all notifications of this application.

cancelGroup cancels

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| label | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  } 
}
notificationManager.cancel(0, "label", cancelCallback);
```


## cancel

```TypeScript
function cancel(id: number, label?: string): Promise<void>
```

Cancels a published notification based on the notification ID and label. This API uses a promise to return the result. After cancellation, the corresponding notification will be removed from the notification center, status bar, and other locations, and will no longer be visible to the user.

**Since:** 23

<!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>--><!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

publish publishes a notification.

cancelAll cancels all notifications of this application.

cancelGroup cancels notifications

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| label | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancel(0).then(() => {
  console.info(`Succeeded in canceling notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
});
```
