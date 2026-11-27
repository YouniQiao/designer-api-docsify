# createGattServer

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

create a JavaScript Gatt server instance.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createGattServer](arkts-connectivity-bluetoothmanager-ble-creategattserver-f.md)

<!--Device-BLE-function createGattServer(): GattServer--><!--Device-BLE-function createGattServer(): GattServer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| GattServer | Returns a JavaScript Gatt server instance `GattServer`. |

**Examples**

```TypeScript
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
```
