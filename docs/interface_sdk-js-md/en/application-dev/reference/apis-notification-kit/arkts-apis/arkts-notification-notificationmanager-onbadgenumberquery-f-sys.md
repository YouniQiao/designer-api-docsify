# onBadgeNumberQuery (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## onBadgeNumberQuery

```TypeScript
function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void
```

注册应用角标数量查询回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void--><!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: (bundle: BundleOption) =&gt; Promise&lt;number&gt;  <br>ArkTS-Sta：(bundle: BundleOption) =&gt; Promise&lt;long&gt; | Yes | 应用角标数量查询函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

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

