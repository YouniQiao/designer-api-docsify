# enableBluetooth

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## enableBluetooth

```TypeScript
function enableBluetooth(): boolean
```

Enables Bluetooth on a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [enableBluetooth](arkts-connectivity-bluetoothmanager-enablebluetooth-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
let enable : boolean = bluetooth.enableBluetooth();
```
