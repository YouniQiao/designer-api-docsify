# createGattServer

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

create a JavaScript Gatt server instance.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [createGattServer](arkts-connectivity-ble-creategattserver-f.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| GattServer | Returns a JavaScript Gatt server instance { |

**Examples**

```TypeScript
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```
