# cancelPairedDevice (System API)

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## cancelPairedDevice

```TypeScript
function cancelPairedDevice(deviceId: string): boolean
```

Remove a paired remote device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [cancelPairedDevice](arkts-connectivity-bluetoothmanager-cancelpaireddevice-f-sys.md#cancelpaireddevice-system-api)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function cancelPairedDevice(deviceId: string): boolean--><!--Device-bluetooth-function cancelPairedDevice(deviceId: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | The address of the remote device to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
let result : boolean = bluetooth.cancelPairedDevice("XX:XX:XX:XX:XX:XX");
```

