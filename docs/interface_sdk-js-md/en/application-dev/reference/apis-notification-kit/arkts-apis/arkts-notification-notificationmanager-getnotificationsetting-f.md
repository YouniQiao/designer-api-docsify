# getNotificationSetting

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationSetting

```TypeScript
function getNotificationSetting(): Promise<NotificationSetting>
```

Obtains the notification settings of the application, including the switch statuses for lock screen notifications, banner notifications, desktop badges, vibration, and ringtone. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Notification.Notification

**See also:**

openNotificationSettings opens the notification

isNotificationEnabled Checks whether notification is enabled for the

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
