# disableBluetooth

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## disableBluetooth

```TypeScript
function disableBluetooth(): boolean
```

Disables Bluetooth on a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.disableBluetooth

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function disableBluetooth(): boolean--><!--Device-bluetooth-function disableBluetooth(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let disable : boolean = bluetooth.disableBluetooth();
```
