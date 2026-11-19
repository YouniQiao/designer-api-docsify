# startPairOutOfBand (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## startPairOutOfBand

```TypeScript
function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,
    p256Data?: OobData): Promise<void>
```

Starts pairing with the specific remote Bluetooth device using the Out Of Band mechanism. This function is asynchronous, and the pairing status is obtained by listening to the bondStateChange event. If both p192Data and p256Data are not used, the function call will fail. If both p192Data and p256Data are used simultaneously, p256Data takes effect.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,    p256Data?: OobData): Promise<void>--><!--Device-connection-function startPairOutOfBand(deviceId: string, transport: BluetoothTransport, p192Data?: OobData,    p256Data?: OobData): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID. For example, "11:22:33:AA:BB:FF". |
| transport | [BluetoothTransport](arkts-connectivity-connection-bluetoothtransport-e.md) | Yes | Indicates the transport of a remote Bluetooth device. |
| p192Data | [OobData](arkts-connectivity-connection-oobdata-i-sys.md) | No | The out-of-band data (P192). |
| p256Data | [OobData](arkts-connectivity-connection-oobdata-i-sys.md) | No | The out-of-band data (P256). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
