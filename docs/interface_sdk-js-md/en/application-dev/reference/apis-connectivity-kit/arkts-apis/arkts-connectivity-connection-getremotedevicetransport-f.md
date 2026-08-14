# getRemoteDeviceTransport

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## getRemoteDeviceTransport

```TypeScript
function getRemoteDeviceTransport(deviceId: string): BluetoothTransport
```

Get the transport of the bluetooth device.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getRemoteDeviceTransport(deviceId: string): BluetoothTransport--><!--Device-connection-function getRemoteDeviceTransport(deviceId: string): BluetoothTransport-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID. For example, "11:22:33:AA:BB:FF". |

**Return value:**

| Type | Description |
| --- | --- |
| BluetoothTransport | The transport of bluetooth device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Get transport failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let transport: connection.BluetoothTransport = connection.getRemoteDeviceTransport('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

