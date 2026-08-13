# onAdvertisingStateChange

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## onAdvertisingStateChange

```TypeScript
function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void
```

Subscribing to advertising state change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void--><!--Device-ble-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | Yes | Callback used to listen for the advertising state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

