# getNotificationStatisticsByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getNotificationStatisticsByBundle

```TypeScript
function getNotificationStatisticsByBundle(bundles: BundleOption[]): Promise<BundleNotificationStatistics[]>
```

Obtains notification statistics of a specified list of applications in batches.This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getNotificationStatisticsByBundle(bundles: BundleOption[]): Promise<BundleNotificationStatistics[]>--><!--Device-notificationManager-function getNotificationStatisticsByBundle(bundles: BundleOption[]): Promise<BundleNotificationStatistics[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundles | BundleOption[] | Yes | List of application bundle information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BundleNotificationStatistics](arkts-notification-notificationmanager-bundlenotificationstatistics-i-sys.md)[]&gt; | Promise used to return the notification statistics of a specified list of applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

