# getLocalName

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getLocalName

```TypeScript
function getLocalName(): string
```

Obtains the Bluetooth local name of a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getLocalName

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getLocalName(): string--><!--Device-bluetooth-function getLocalName(): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let localName : string = bluetooth.getLocalName();
```
