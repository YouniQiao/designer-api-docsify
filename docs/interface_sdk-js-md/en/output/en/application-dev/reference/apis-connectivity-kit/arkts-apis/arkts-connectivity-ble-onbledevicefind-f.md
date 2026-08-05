# onBLEDeviceFind

## onBLEDeviceFind

```TypeScript
function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void
```

Subscribe BLE scan result. If the application has ohos.permission.GET\_BLUETOOTH\_PEERS\_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void--><!--Device-ble-function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;ScanResult&gt;&gt; | Yes | Callback used to listen for the scan result event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 2900099 | Operation failed. |

