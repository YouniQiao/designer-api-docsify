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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 10

**Substitutes:** [createGattServer](#creategattserver)

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GattServer](arkts-connectivity-bluetooth-gattserver-i.md) |

**Examples**

```TypeScript
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```
