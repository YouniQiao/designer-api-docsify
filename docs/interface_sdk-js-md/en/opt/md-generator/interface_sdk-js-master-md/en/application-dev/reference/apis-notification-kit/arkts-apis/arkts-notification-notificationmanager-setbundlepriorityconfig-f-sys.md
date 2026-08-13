# setBundlePriorityConfig (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setBundlePriorityConfig

```TypeScript
function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>
```

Sets the priority configuration of an application.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>--><!--Device-notificationManager-function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const bundleOption : notificationManager.BundleOption = { bundle: 'bundleName', uid: 0 };
notificationManager.setBundlePriorityConfig(bundleOption, 'keyword\nkeyword1').then(() => {
  hilog.info(0x0000, 'testTag', `setBundlePriorityConfig success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `setBundlePriorityConfig failed, code is ${err.code}, message is ${err.message}`);
});
```
