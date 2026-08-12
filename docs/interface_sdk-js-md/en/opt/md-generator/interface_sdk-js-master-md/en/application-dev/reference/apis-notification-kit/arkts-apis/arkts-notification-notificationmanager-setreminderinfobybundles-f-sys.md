# setReminderInfoByBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setReminderInfoByBundles

```TypeScript
function setReminderInfoByBundles(reminderInfos: Array<NotificationReminderInfo>) : Promise<void>
```

Batch sets reminders for specified applications. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setReminderInfoByBundles(reminderInfos: Array<NotificationReminderInfo>) : Promise<void>--><!--Device-notificationManager-function setReminderInfoByBundles(reminderInfos: Array<NotificationReminderInfo>) : Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reminderInfos | Array&lt;[NotificationReminderInfo](arkts-notification-notificationmanager-notificationreminderinfo-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
    bundle: "bundleName",
};
let reminderInfos: Array<notificationManager.NotificationReminderInfo> = [
    {
        bundle: bundle,
        reminderFlags: 59,
        silentReminderEnabled: false
    }
];
notificationManager.setReminderInfoByBundles(reminderInfos).then(() => {
    console.info('SetReminderInfoByBundles success.');
}).catch((err: BusinessError) => {
    console.error(`SetReminderInfoByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```
