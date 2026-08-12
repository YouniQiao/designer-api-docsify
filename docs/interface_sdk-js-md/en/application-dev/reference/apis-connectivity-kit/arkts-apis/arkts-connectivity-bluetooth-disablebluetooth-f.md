# disableBluetooth

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## disableBluetooth

```TypeScript
function disableBluetooth(): boolean
```

Disables Bluetooth on a device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [disableBluetooth](ohos.bluetoothManager/bluetoothManager.disableBluetooth)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function disableBluetooth(): boolean--><!--Device-bluetooth-function disableBluetooth(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let disable : boolean = bluetooth.disableBluetooth();
```

