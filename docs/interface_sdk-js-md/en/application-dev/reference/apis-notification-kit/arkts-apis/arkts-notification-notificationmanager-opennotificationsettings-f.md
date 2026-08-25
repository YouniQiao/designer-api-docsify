# openNotificationSettings

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## openNotificationSettings

```TypeScript
function openNotificationSettings(context: UIAbilityContext): Promise<void>
```

Opens the notification settings page of the application, which is displayed in semi-modal mode and can be used to set the notification enabling and notification mode. This API uses a promise to return the result.This is suitable for scenarios where users need to manually modify notification settings, such as a secondary request after a user denies authorization, or when the notification reminder method (vibration, ringtone, etc.) needs to be modified. When the requestEnableNotification dialog box is denied by the user, you can call this API to guide the user to the notification settings page to manually enable it.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.NotificationSettings

**See also:**

requestEnableNotification requests notification

isNotificationEnabled checks whether notification is

getNotificationSetting obtains the notification settings

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600018](../errorcode-notification.md#1600018-notification-settings-page-already-displayed) |
