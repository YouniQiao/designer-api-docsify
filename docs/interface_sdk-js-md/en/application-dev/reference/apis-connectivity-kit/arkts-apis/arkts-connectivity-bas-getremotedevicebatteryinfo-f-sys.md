# getRemoteDeviceBatteryInfo (System API)

## Modules to Import

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## getRemoteDeviceBatteryInfo

```TypeScript
function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>
```

Get remote device battery information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>--><!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | [BluetoothAddress](arkts-connectivity-ble-bluetoothaddress-t.md) | Yes | Indicates address of peer device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;BatteryInfo&gt; | Returns the battery info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Only can be called on phone, tablet, and 2in1 devices. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 2901003 | Connection not established. |
| 2900004 | Remote device profile not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

