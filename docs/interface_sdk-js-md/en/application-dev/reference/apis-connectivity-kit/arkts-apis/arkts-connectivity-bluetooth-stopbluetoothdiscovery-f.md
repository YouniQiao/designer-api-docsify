# stopBluetoothDiscovery

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## stopBluetoothDiscovery

```TypeScript
function stopBluetoothDiscovery(): boolean
```

Stops Bluetooth device scanning.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [stopBluetoothDiscovery](ohos.bluetoothManager/bluetoothManager.stopBluetoothDiscovery)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function stopBluetoothDiscovery(): boolean--><!--Device-bluetooth-function stopBluetoothDiscovery(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let result : boolean = bluetooth.stopBluetoothDiscovery();
```

