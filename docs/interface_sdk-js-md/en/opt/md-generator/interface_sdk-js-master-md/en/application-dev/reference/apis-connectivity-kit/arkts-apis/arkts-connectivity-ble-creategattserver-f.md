# createGattServer

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

create a JavaScript Gatt server instance.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ohos.bluetooth.ble/ble#createGattServer

<!--Device-BLE-function createGattServer(): GattServer--><!--Device-BLE-function createGattServer(): GattServer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GattServer](arkts-connectivity-bluetooth-gattserver-i.md) |

## Examples

```TypeScript
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```
