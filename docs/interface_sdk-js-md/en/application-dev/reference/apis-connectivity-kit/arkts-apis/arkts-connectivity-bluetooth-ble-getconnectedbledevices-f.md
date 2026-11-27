# getConnectedBLEDevices

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getConnectedBLEDevices

```TypeScript
function getConnectedBLEDevices(): Array<string>
```

Obtains the list of devices in the connected status.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getConnectedBLEDevices](arkts-connectivity-bluetoothmanager-ble-getconnectedbledevices-f.md)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-BLE-function getConnectedBLEDevices(): Array<string>--><!--Device-BLE-function getConnectedBLEDevices(): Array<string>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Returns the list of device address. |

**Examples**

```TypeScript
let result : Array<string> = bluetooth.BLE.getConnectedBLEDevices();
```
