# setBadgeNumberByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBadgeNumberByBundle

```TypeScript
function setBadgeNumberByBundle(bundle: BundleOption, badgeNumber: number): Promise<void>
```

Sets the badge count for other applications. This API uses a promise to return the result.The current application must have a proxy relationship with another application, or the **ohos.permission.NOTIFICATION_AGENT_CONTROLLER** permission is granted to the current application.This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 12

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes |
| badgeNumber | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600017](../errorcode-notification.md#1600017-no-configured-proxy-relationship) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
