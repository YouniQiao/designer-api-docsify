# setLocalName

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## setLocalName

```TypeScript
function setLocalName(name: string): boolean
```

Sets the Bluetooth friendly name of a device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md#setLocalName)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function setLocalName(name: string): boolean--><!--Device-bluetooth-function setLocalName(name: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates a valid Bluetooth name. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
let ret : boolean = bluetooth.setLocalName('device_name');
```

