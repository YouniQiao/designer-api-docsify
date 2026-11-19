# getRemoteDeviceBatteryInfo (System API)

## Modules to Import

```TypeScript
import { bas } from '@kit.ConnectivityKit';
```

## getRemoteDeviceBatteryInfo

```TypeScript
function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>
```

Get remote device battery information.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>--><!--Device-bas-function getRemoteDeviceBatteryInfo(deviceId: BluetoothAddress): Promise<BatteryInfo>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | BluetoothAddress | Yes | Indicates address of peer device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BatteryInfo](arkts-connectivity-connection-batteryinfo-i.md)&gt; | Returns the battery info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Remote Device profile not supported. |
| 2900099 | Operation failed. |
| 2901003 | Connection not established. |
