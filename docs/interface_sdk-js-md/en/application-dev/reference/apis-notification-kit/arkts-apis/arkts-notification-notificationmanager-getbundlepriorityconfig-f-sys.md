# getBundlePriorityConfig (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getBundlePriorityConfig

```TypeScript
function getBundlePriorityConfig(bundle: BundleOption): Promise<string>
```

获取应用的优先功能配置。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getBundlePriorityConfig(bundle: BundleOption): Promise<string>--><!--Device-notificationManager-function getBundlePriorityConfig(bundle: BundleOption): Promise<string>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes | 指定应用的包信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回包含应用优先功能配置的Promise对象。 |

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
notificationManager.getBundlePriorityConfig(bundleOption).then((value: string) => {
  hilog.info(0x0000, 'testTag', `getBundlePriorityConfig value is ${value}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `getBundlePriorityConfig failed, code is ${err.code}, message is ${err.message}`);
});
```

