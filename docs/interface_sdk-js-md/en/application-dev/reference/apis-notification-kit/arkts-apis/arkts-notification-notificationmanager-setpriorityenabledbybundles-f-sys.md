# setPriorityEnabledByBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setPriorityEnabledByBundles

```TypeScript
function setPriorityEnabledByBundles(switches: Map<BundleOption, boolean>): Promise<void>
```

批量设置应用通知优先级开关状态。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function setPriorityEnabledByBundles(switches: Map<BundleOption, boolean>): Promise<void>--><!--Device-notificationManager-function setPriorityEnabledByBundles(switches: Map<BundleOption, boolean>): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| switches | Map&lt;BundleOption, boolean&gt; | Yes | 应用通知优先级开关状态的键值对集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600012 | No memory space. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const bundleOption : notificationManager.BundleOption = { bundle: 'bundleName', uid: 1000 };
let switches: Map<notificationManager.BundleOption, boolean> = new Map([[bundleOption, false]]);
notificationManager.setPriorityEnabledByBundles(switches).then(() => {
  hilog.info(0x0000, 'testTag', `setPriorityEnabledByBundles success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `setPriorityEnabledByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```

