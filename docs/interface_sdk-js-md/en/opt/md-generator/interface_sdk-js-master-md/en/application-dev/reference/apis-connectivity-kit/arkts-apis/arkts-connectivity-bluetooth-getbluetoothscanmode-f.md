# getBluetoothScanMode

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getBluetoothScanMode

```TypeScript
function getBluetoothScanMode(): ScanMode
```

Obtains the Bluetooth scanning mode of a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getBluetoothScanMode

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getBluetoothScanMode(): ScanMode--><!--Device-bluetooth-function getBluetoothScanMode(): ScanMode-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ScanMode](arkts-connectivity-connection-scanmode-e.md) |

## Examples

```TypeScript
let scanMode : bluetooth.ScanMode = bluetooth.getBluetoothScanMode();
```
