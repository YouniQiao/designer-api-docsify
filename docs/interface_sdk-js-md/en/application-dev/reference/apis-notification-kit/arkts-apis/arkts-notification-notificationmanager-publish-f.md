# publish

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

Publishes a notification. This API uses an asynchronous callback to return the result.After a notification is published, it will be displayed as a notification widget in the device's notification center, status bar, etc. If the ID and tag of the newly published notification are the same as those of an already published notification, the new notification will replace the original one, achieving a notification update effect.

**Since:** 9

**System capability:** SystemCapability.Notification.Notification

**See also:**

isNotificationEnabled checks whether

cancel cancels a published

cancelAll cancels all

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../errorcode-notification.md#1600004-notification-disabled) |
| [1600005](../errorcode-notification.md#1600005-notification-slot-disabled) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [1600009](../errorcode-notification.md#1600009-notification-sending-limit-reached) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600014](../errorcode-notification.md#1600014-no-related-permission) |
| [1600015](../errorcode-notification.md#1600015-duplicate-configurations-not-allowed-for-the-current-notification-status) |
| [1600016](../errorcode-notification.md#1600016-updated-notification-version-outdated) |
| [1600020](../errorcode-notification.md#1600020-applications-in-the-permission-control-list-are-not-allowed-to-publish-notifications) |
| [1600029](../errorcode-notification.md#1600029-failed-to-find-the-extensionability-for-the-custom-extension-area-of-the-live-view-widget) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

Publishes a notification. This API uses a promise to return the result.After a notification is published, it will be displayed as a notification card in the device's notification center, status bar, and other locations. If the ID and tag of the newly published notification are the same as those of an already published notification, the new notification will replace the original one, achieving a notification update effect.

**Since:** 9

**System capability:** SystemCapability.Notification.Notification

**See also:**

isNotificationEnabled checks whether

cancel cancels a published

cancelAll cancels all notifications of

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../errorcode-notification.md#1600004-notification-disabled) |
| [1600005](../errorcode-notification.md#1600005-notification-slot-disabled) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |
| [1600009](../errorcode-notification.md#1600009-notification-sending-limit-reached) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600014](../errorcode-notification.md#1600014-no-related-permission) |
| [1600015](../errorcode-notification.md#1600015-duplicate-configurations-not-allowed-for-the-current-notification-status) |
| [1600016](../errorcode-notification.md#1600016-updated-notification-version-outdated) |
| [1600020](../errorcode-notification.md#1600020-applications-in-the-permission-control-list-are-not-allowed-to-publish-notifications) |
| [1600029](../errorcode-notification.md#1600029-failed-to-find-the-extensionability-for-the-custom-extension-area-of-the-live-view-widget) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
