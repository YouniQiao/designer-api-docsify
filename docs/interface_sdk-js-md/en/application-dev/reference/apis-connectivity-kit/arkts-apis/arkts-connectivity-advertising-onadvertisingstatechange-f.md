# onAdvertisingStateChange

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.ConnectivityKit';
```

## onAdvertisingStateChange

```TypeScript
function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void
```

订阅广播状态变化事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的系统应用程序才能访问此事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void--><!--Device-advertising-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | Yes | 用于监听广播状态的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |

