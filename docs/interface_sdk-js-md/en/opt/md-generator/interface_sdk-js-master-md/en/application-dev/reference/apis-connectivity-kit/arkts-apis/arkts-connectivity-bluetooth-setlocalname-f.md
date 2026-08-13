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

**Deprecated since:** 9

**Substitutes:** [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md#setLocalName)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function setLocalName(name: string): boolean--><!--Device-bluetooth-function setLocalName(name: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let ret : boolean = bluetooth.setLocalName('device_name');
```
