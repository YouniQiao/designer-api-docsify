# getReminderInfoByBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getReminderInfoByBundles

```TypeScript
function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>
```

Batch obtains reminders of specified applications. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>--><!--Device-notificationManager-function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundles | Array & lt;BundleOption & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[NotificationReminderInfo](arkts-notification-notificationmanager-notificationreminderinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundles: Array<notificationManager.BundleOption> = [
    {
        bundle: 'bundleName',
    },
    {
        bundle: 'bundleName1',
    }
];
notificationManager.getReminderInfoByBundles(bundles).then((data: Array<notificationManager.NotificationReminderInfo>) => {
    console.info(`Reminder data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`GetReminderInfoByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```
