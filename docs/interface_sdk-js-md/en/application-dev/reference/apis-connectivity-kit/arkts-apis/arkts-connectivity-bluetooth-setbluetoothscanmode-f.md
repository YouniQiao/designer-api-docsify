# setBluetoothScanMode

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## setBluetoothScanMode

```TypeScript
function setBluetoothScanMode(mode: ScanMode, duration: number): boolean
```

Sets the Bluetooth scan mode for a device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [setBluetoothScanMode](ohos.bluetoothManager/bluetoothManager.setBluetoothScanMode)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function setBluetoothScanMode(mode: ScanMode, duration: number): boolean--><!--Device-bluetooth-function setBluetoothScanMode(mode: ScanMode, duration: number): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | ScanMode | Yes | Indicates the Bluetooth scan mode to set, [ScanMode](arkts-connectivity-bluetooth-scanmode-e.md#ScanMode). |
| duration | number | Yes | Indicates the duration in seconds, in which the host is discoverable. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
// The device can be discovered and connected only when the discoverable and connectable mode is used.
let result : boolean = bluetooth.setBluetoothScanMode(bluetooth.ScanMode
    .SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
```

