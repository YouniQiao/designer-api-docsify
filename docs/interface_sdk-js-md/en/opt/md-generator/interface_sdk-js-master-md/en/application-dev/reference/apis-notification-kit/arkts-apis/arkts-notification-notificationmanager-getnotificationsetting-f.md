# getNotificationSetting

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getNotificationSetting

```TypeScript
function getNotificationSetting(): Promise<NotificationSetting>
```

Obtains the notification settings of the application, including the switch statuses for lock screen notifications, banner notifications, desktop badges, vibration, and ringtone.This API uses a promise to return the result.

**Since:** 20

<!--Device-notificationManager-function getNotificationSetting(): Promise<NotificationSetting>--><!--Device-notificationManager-function getNotificationSetting(): Promise<NotificationSetting>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[openNotificationSettings](notificationManager.openNotificationSettings(context: UIAbilityContext): Promise<void>) opens the notification

[isNotificationEnabled](notificationManager.isNotificationEnabled(): Promise<boolean>) Checks whether notification is enabled for the

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
    console.info(`getNotificationSetting success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNotificationSetting failed, code is ${err.code}, message is ${err.message}`);
});
```
