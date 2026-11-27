# stopBLEScan

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## stopBLEScan

```TypeScript
function stopBLEScan(): void
```

Stops BLE scanning.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [stopBLEScan](arkts-connectivity-bluetoothmanager-ble-stopblescan-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-BLE-function stopBLEScan(): void--><!--Device-BLE-function stopBLEScan(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Examples**

```TypeScript
bluetooth.BLE.stopBLEScan();
```
