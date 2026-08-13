# getActiveNotifications

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getActiveNotifications

```TypeScript
function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void
```

Obtains the active notifications of this application. This API uses an asynchronous callback to return the result. This API is used to query the detailed information list of all stored notifications of the current application in the notification center, including the ID, tag, content, and creation time of each notification.

**Since:** 23

**Deprecated since:** -1

<!--Device-notificationManager-function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void--><!--Device-notificationManager-function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

setBadgeNumber sets the notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;NotificationRequest&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationsCallback = (err: BusinessError, data: Array<notificationManager.NotificationRequest>): void => {
  if (err) {
    console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
  }
}
notificationManager.getActiveNotifications(getActiveNotificationsCallback);
```


## getActiveNotifications

```TypeScript
function getActiveNotifications(): Promise<Array<NotificationRequest>>
```

Obtains the active notifications of this application. This API uses a promise to return the result. This API is used to query the detailed information list of all stored notifications of the current application in the notification center, including the ID, tag, content, and creation time of each notification.

**Since:** 23

**Deprecated since:** -1

<!--Device-notificationManager-function getActiveNotifications(): Promise<Array<NotificationRequest>>--><!--Device-notificationManager-function getActiveNotifications(): Promise<Array<NotificationRequest>>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

setBadgeNumber sets the notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;NotificationRequest & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotifications().then((data: Array<notificationManager.NotificationRequest>) => {
  console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
});
```
