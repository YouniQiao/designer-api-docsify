# setSilentReminderEnabled (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setSilentReminderEnabled

```TypeScript
function setSilentReminderEnabled(bundle: BundleOption, enabled: boolean): Promise<void>
```

Sets the enabling status of the silent reminder. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setSilentReminderEnabled(bundle: BundleOption, enabled: boolean): Promise<void>--><!--Device-notificationManager-function setSilentReminderEnabled(bundle: BundleOption, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundle: notificationManager.BundleOption = {
    bundle: "bundleName",
};
notificationManager.setSilentReminderEnabled(bundle, true).then(() => {
    hilog.info(0x0000, 'testTag', '%{public}s', `setSilentReminderEnabled success.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `setSilentReminderEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```
