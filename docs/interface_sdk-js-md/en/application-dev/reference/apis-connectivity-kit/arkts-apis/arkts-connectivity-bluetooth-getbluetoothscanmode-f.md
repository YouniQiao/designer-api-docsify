# getBluetoothScanMode

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getBluetoothScanMode

```TypeScript
function getBluetoothScanMode(): ScanMode
```

Obtains the Bluetooth scanning mode of a device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getBluetoothScanMode](ohos.bluetoothManager/bluetoothManager.getBluetoothScanMode)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getBluetoothScanMode(): ScanMode--><!--Device-bluetooth-function getBluetoothScanMode(): ScanMode-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| ScanMode | Returns the Bluetooth scanning mode, { |

## Examples

```TypeScript
let scanMode : bluetooth.ScanMode = bluetooth.getBluetoothScanMode();
```

