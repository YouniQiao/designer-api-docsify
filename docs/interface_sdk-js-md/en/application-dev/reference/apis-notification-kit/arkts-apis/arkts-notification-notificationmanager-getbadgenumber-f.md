# getBadgeNumber

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getBadgeNumber

```TypeScript
function getBadgeNumber(): Promise<number>
```

Obtains the badge number of this application. This API uses a promise to return the result.This API is used to query the badge number displayed on the current application's desktop icon.

**Since:** 22

**System capability:** SystemCapability.Notification.Notification

**See also:**

setBadgeNumber sets the notification badge number.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
