# createGattServer

## Modules to Import

```TypeScript
import { bluetoothManager } from 'bluetoothManager';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

create a JavaScript Gatt server instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [createGattServer](#createGattServer)

<!--Device-BLE-function createGattServer(): GattServer--><!--Device-BLE-function createGattServer(): GattServer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| GattServer | Returns a JavaScript Gatt server instance { |

## Examples

```TypeScript
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```

