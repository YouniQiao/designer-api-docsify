# stopBluetoothDiscovery

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## stopBluetoothDiscovery

```TypeScript
function stopBluetoothDiscovery(): boolean
```

Stops Bluetooth device scanning.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.stopBluetoothDiscovery

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function stopBluetoothDiscovery(): boolean--><!--Device-bluetooth-function stopBluetoothDiscovery(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let result : boolean = bluetooth.stopBluetoothDiscovery();
```
