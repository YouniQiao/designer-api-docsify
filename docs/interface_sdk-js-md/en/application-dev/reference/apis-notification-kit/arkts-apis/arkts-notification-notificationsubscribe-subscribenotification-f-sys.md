# subscribeNotification (System API)

## Modules to Import

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## subscribeNotification

```TypeScript
function subscribeNotification(subscriber: NotificationSubscriber): Promise<void>
```

Subscribes to notifications. After the subscription, the new message is received through the callback in the subscriber. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_SYSTEM_SUBSCRIBER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationSubscribe-function subscribeNotification(subscriber: NotificationSubscriber): Promise<void>--><!--Device-notificationSubscribe-function subscribeNotification(subscriber: NotificationSubscriber): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriber | NotificationSubscriber | Yes | Notification subscriber. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../errorcode-notification.md#1600001-internal-error) | Internal error. Possible cause: 1.IPC communication failed. 2.Memory operation error. 3.The user does not exist. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |


## subscribeNotification

```TypeScript
function subscribeNotification(subscriber: NotificationSubscriber, info: NotificationSubscribeInfo): Promise<void>
```

Subscribes to notifications. After the subscription, the new message is received through the callback in the subscriber. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_SYSTEM_SUBSCRIBER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationSubscribe-function subscribeNotification(subscriber: NotificationSubscriber, info: NotificationSubscribeInfo): Promise<void>--><!--Device-notificationSubscribe-function subscribeNotification(subscriber: NotificationSubscriber, info: NotificationSubscribeInfo): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriber | NotificationSubscriber | Yes | Notification subscriber. |
| info | NotificationSubscribeInfo | Yes | Notification subscription information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../errorcode-notification.md#1600001-internal-error) | Internal error. Possible cause: 1.IPC communication failed. 2.Memory operation error. 3.The user does not exist. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

