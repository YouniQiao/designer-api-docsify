# getRemoteDeviceTransport

## Modules to Import

```TypeScript
```

## getRemoteDeviceTransport

```TypeScript
function getRemoteDeviceTransport(deviceId: string): BluetoothTransport
```

Get the transport of the bluetooth device.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getRemoteDeviceTransport(deviceId: string): BluetoothTransport--><!--Device-connection-function getRemoteDeviceTransport(deviceId: string): BluetoothTransport-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BluetoothTransport](arkts-connectivity-ble-bluetoothtransport-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900003 |
| 2900099 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let transport: connection.BluetoothTransport = connection.getRemoteDeviceTransport('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
