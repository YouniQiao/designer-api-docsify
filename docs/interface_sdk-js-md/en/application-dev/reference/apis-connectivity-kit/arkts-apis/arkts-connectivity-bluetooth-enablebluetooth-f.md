# enableBluetooth

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## enableBluetooth

```TypeScript
function enableBluetooth(): boolean
```

Enables Bluetooth on a device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [enableBluetooth](arkts-connectivity-bluetoothmanager-enablebluetooth-f.md#enableBluetooth)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function enableBluetooth(): boolean--><!--Device-bluetooth-function enableBluetooth(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let enable : boolean = bluetooth.enableBluetooth();
```

