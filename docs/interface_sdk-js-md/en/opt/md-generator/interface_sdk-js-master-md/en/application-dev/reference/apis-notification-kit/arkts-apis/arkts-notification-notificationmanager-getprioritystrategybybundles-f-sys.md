# getPriorityStrategyByBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getPriorityStrategyByBundles

```TypeScript
function getPriorityStrategyByBundles(bundles: Array<BundleOption>): Promise<Map<BundleOption, number>>
```

Obtains the application priority notification strategies in batches. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function getPriorityStrategyByBundles(bundles: Array<BundleOption>): Promise<Map<BundleOption, long>>--><!--Device-notificationManager-function getPriorityStrategyByBundles(bundles: Array<BundleOption>): Promise<Map<BundleOption, long>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundles | Array & lt;BundleOption & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;BundleOption, number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [17700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const bundleOption : notificationManager.BundleOption = { bundle: 'bundleName', uid: 1000 };
let bundles: Array<notificationManager.BundleOption> = new Array(bundleOption);
notificationManager.getPriorityStrategyByBundles(bundles).then((strategies: Map<notificationManager.BundleOption, number>) => {
  strategies.forEach((value, key) => {
    hilog.info(0x0000, 'testTag', `getPriorityStrategyByBundles strategies: ${key.bundle} ${key.uid}, ${value}`);
  })
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `getPriorityStrategyByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```
