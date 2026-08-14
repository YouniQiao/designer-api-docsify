# getNotificationSwitch (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'notificationManager';
```

## getNotificationSwitch

```TypeScript
function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>
```

Obtains the notification switch state. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>--><!--Device-notificationManager-function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| switchName | string | Yes | Name of the notification switch. The value can be **DEAL** (aggregated switch for transaction notifications) or **LOGISTICS** (aggregated switch for logistics notifications). |
| userId | int | Yes | User ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[SwitchState](arkts-notification-notificationmanager-switchstate-e-sys.md)&gt; | Promise used to return the notification switch state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1600008](../errorcode-notification.md#1600008-user-not-found) | The user does not exist. |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../errorcode-notification.md#1600001-internal-error) | Internal error. Database operation failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

