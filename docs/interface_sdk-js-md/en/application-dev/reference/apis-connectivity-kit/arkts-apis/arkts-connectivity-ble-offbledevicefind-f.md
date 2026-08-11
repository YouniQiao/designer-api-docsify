# offBLEDeviceFind

## Modules to Import

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## offBLEDeviceFind

```TypeScript
function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void
```

Unsubscribe BLE scan result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void--><!--Device-ble-function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | No | Callback used to listen for the scan result event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

