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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function onCheckNotification(callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void--><!--Device-notificationManager-function onCheckNotification(callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (checkInfo: NotificationCheckInfo) =&gt; NotificationCheckResult | Yes | callback - The callback of check notifications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600001](../errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |


## onCheckNotification

```TypeScript
function onCheckNotification(checkRequest: NotificationCheckRequest,
    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void
```

Subscribe the callback for check notifications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function onCheckNotification(checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void--><!--Device-notificationManager-function onCheckNotification(checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| checkRequest | NotificationCheckRequest | Yes | Check Request for filter notification request. |
| callback | (checkInfo: NotificationCheckInfo) =&gt; Promise&lt;[NotificationCheckResult](arkts-notification-notificationmanager-notificationcheckresult-i-sys.md)&gt; | Yes | callback - The callback of check notifications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

