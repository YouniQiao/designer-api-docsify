# setBadgeDisplayStatusByBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBadgeDisplayStatusByBundles

```TypeScript
function setBadgeDisplayStatusByBundles(badges: Map<BundleOption, boolean>) : Promise<void>
```

批量设置指定应用是否显示角标。使用Promise异步回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setBadgeDisplayStatusByBundles(badges: Map<BundleOption, boolean>) : Promise<void>--><!--Device-notificationManager-function setBadgeDisplayStatusByBundles(badges: Map<BundleOption, boolean>) : Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| badges | Map&lt;BundleOption, boolean&gt; | Yes | 应用包名信息和角标显示状态的列表。 |

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
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let badges = new Map<notificationManager.BundleOption, boolean>();
let bundle: notificationManager.BundleOption = {
    bundle: 'bundleName',
};
badges.set(bundle, true);

notificationManager.setBadgeDisplayStatusByBundles(badges).then(() => {
    console.info('SetBadgeDisplayStatusByBundles success.');
}).catch((err: BusinessError) => {
    console.error(`SetBadgeDisplayStatusByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```

