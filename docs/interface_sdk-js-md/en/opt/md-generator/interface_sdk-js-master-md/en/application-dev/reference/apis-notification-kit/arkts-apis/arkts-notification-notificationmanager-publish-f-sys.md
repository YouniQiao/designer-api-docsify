# publish (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, userId: number, callback: AsyncCallback<void>): void
```

Publishes a notification to a specified user. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 18+: ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API version 9 - 17: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600025](../errorcode-notification.md#1600025-geofencing-disabled) |
| [1600026](../errorcode-notification.md#1600026-location-disabled) |
| [1600027](../errorcode-notification.md#1600027-awareness-suggestions-switch-of-the-location-service-disabled) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [1600029](../errorcode-notification.md#1600029-failed-to-find-the-extensionability-for-the-custom-extension-area-of-the-live-view-widget) |
| [1600016](../errorcode-notification.md#1600016-updated-notification-version-outdated) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600020](../errorcode-notification.md#1600020-applications-in-the-permission-control-list-are-not-allowed-to-publish-notifications) |
| [1600008](../errorcode-notification.md#1600008-user-not-found) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600009](../errorcode-notification.md#1600009-notification-sending-limit-reached) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600014](../errorcode-notification.md#1600014-no-related-permission) |
| [1600015](../errorcode-notification.md#1600015-duplicate-configurations-not-allowed-for-the-current-notification-status) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../errorcode-notification.md#1600004-notification-disabled) |
| [1600005](../errorcode-notification.md#1600005-notification-slot-disabled) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish callback
let publishCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("publish success");
    }
}
// Use the actual user ID when calling the API.
let userId: number = 1;
// NotificationRequest object
let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: "test_title",
            text: "test_text",
            additionalText: "test_additionalText"
        }
    }
};
notificationManager.publish(notificationRequest, userId, publishCallback);
```


## publish

```TypeScript
function publish(request: NotificationRequest, userId: number): Promise<void>
```

Publishes a notification to a specified user. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 18+: ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API version 9 - 17: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600025](../errorcode-notification.md#1600025-geofencing-disabled) |
| [1600026](../errorcode-notification.md#1600026-location-disabled) |
| [1600027](../errorcode-notification.md#1600027-awareness-suggestions-switch-of-the-location-service-disabled) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-failed-to-connect-to-the-server) |
| [1600029](../errorcode-notification.md#1600029-failed-to-find-the-extensionability-for-the-custom-extension-area-of-the-live-view-widget) |
| [1600016](../errorcode-notification.md#1600016-updated-notification-version-outdated) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600020](../errorcode-notification.md#1600020-applications-in-the-permission-control-list-are-not-allowed-to-publish-notifications) |
| [1600008](../errorcode-notification.md#1600008-user-not-found) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1600009](../errorcode-notification.md#1600009-notification-sending-limit-reached) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600014](../errorcode-notification.md#1600014-no-related-permission) |
| [1600015](../errorcode-notification.md#1600015-duplicate-configurations-not-allowed-for-the-current-notification-status) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../errorcode-notification.md#1600004-notification-disabled) |
| [1600005](../errorcode-notification.md#1600005-notification-slot-disabled) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: "test_title",
            text: "test_text",
            additionalText: "test_additionalText"
        }
    }
};

// Use the actual user ID when calling the API.
let userId: number = 1;

notificationManager.publish(notificationRequest, userId).then(() => {
    console.info("publish success");
}).catch((err: BusinessError) => {
    console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
});
```
