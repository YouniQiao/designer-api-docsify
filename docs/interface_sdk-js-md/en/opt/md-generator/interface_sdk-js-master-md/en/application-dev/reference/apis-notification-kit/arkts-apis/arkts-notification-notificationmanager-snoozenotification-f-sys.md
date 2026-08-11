# snoozeNotification (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## snoozeNotification

```TypeScript
function snoozeNotification(hashCode: string, delayTime: number): Promise<void>
```

Snoozes a notification. The notification will be reminded again after the specified time. Each setting will trigger only one reminder, and the reminder mode will be the same as that of the notification.&lt;br&gt;The notification will be deleted after the setting.

**Since:** 26.0.0

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function snoozeNotification(hashCode: string, delayTime: long): Promise<void>--><!--Device-notificationManager-function snoozeNotification(hashCode: string, delayTime: long): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hashCode | string | Yes |
| delayTime | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600028](../errorcode-notification.md#1600028-current-notification-does-not-support-this-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Replace it with the unique ID of the notification to be snoozed.
let hashCode: string = "hashCode";
let delayTime: number = 60;
notificationManager.snoozeNotification(hashCode, delayTime).then(() => {
  console.info("snoozeNotification success.")
}).catch((err: BusinessError):void => {
  console.error(`snoozeNotification failed, code is ${err.code}, message is ${err.message}`);
});
```
