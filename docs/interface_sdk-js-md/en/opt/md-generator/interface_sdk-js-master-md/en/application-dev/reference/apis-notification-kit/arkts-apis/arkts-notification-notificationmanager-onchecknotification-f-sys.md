# onCheckNotification (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## onCheckNotification

```TypeScript
function onCheckNotification(callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void
```

Subscribe the callback for check notifications.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function onCheckNotification(callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void--><!--Device-notificationManager-function onCheckNotification(callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (checkInfo: NotificationCheckInfo) = & gt; NotificationCheckResult | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## onCheckNotification

```TypeScript
function onCheckNotification(checkRequest: NotificationCheckRequest,
    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void
```

Subscribe the callback for check notifications.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function onCheckNotification(checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void--><!--Device-notificationManager-function onCheckNotification(checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| checkRequest | [NotificationCheckRequest](arkts-notification-notificationrequest-notificationcheckrequest-i-sys.md) | Yes |
| callback | (checkInfo: NotificationCheckInfo) =&gt; Promise&lt;[NotificationCheckResult](arkts-notification-notificationmanager-notificationcheckresult-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
