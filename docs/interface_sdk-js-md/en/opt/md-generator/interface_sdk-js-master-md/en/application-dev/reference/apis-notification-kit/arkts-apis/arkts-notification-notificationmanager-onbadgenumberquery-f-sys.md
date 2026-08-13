# onBadgeNumberQuery (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## onBadgeNumberQuery

```TypeScript
function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<number>): void
```

Registers a callback for querying the number of application badges.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void--><!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (bundle: BundleOption) = & gt; Promise & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
try{
    notificationManager.onBadgeNumberQuery(
        async (bundleOption: notificationManager.BundleOption) => {
            return 1;
        }
    );
} catch (err) {
    console.error(`OnBadgeNumberQuery failed, code is ${err.code}, message is ${err.message}`);
}
```
