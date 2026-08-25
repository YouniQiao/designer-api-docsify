# setBadgeNumber

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void
```

Sets the notification badge number. This API uses an asynchronous callback to return the result.A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be prompted on the desktop icon, such as the number of unread messages and to-do items.This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 10

**System capability:** SystemCapability.Notification.Notification

**See also:**

getActiveNotificationCount obtains the number of

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| badgeNumber | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |


## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number): Promise<void>
```

Sets the notification badge number. This API uses a promise to return the result.A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be prompted on the desktop icon, such as the number of unread messages and to-do items.This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 10

**System capability:** SystemCapability.Notification.Notification

**See also:**

getActiveNotificationCount obtains the number of

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| badgeNumber | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
