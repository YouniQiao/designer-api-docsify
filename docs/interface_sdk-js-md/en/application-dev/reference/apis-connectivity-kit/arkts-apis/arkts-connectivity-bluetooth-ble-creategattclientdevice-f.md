# createGattClientDevice

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## createGattClientDevice

```TypeScript
function createGattClientDevice(deviceId: string): GattClientDevice
```

create a JavaScript Gatt client device instance.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createGattClientDevice](arkts-connectivity-bluetoothmanager-ble-creategattclientdevice-f.md)

<!--Device-BLE-function createGattClientDevice(deviceId: string): GattClientDevice--><!--Device-BLE-function createGattClientDevice(deviceId: string): GattClientDevice-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | The address of the remote device. |

**Return value:**

| Type | Description |
| --- | --- |
| GattClientDevice | Returns a JavaScript Gatt client device instance `GattClientDevice`. |

**Examples**

```TypeScript
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
```
