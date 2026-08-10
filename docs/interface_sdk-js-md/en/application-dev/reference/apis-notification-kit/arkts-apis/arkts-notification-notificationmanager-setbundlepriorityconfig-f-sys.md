# setBundlePriorityConfig (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBundlePriorityConfig

```TypeScript
function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>
```

设置应用的优先功能配置。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>--><!--Device-notificationManager-function setBundlePriorityConfig(bundle: BundleOption, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes | 指定应用的包信息。 |
| value | string | Yes | 应用的优先功能配置。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found. |

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

