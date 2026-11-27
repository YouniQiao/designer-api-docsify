# createGattServer

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## createGattServer

```TypeScript
function createGattServer(): GattServer
```

create a Gatt server instance.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ble-function createGattServer(): GattServer--><!--Device-ble-function createGattServer(): GattServer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [GattServer](arkts-connectivity-ble-gattserver-i.md) | Returns a Gatt server instance `GattServer`. |

**Examples**

```TypeScript
let gattServer: ble.GattServer = ble.createGattServer();
console.info('gatt success');
```
