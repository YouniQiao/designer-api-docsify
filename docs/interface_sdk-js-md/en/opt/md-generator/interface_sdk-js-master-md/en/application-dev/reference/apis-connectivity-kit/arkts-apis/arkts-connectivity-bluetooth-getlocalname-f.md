# getLocalName

## Modules to Import

```TypeScript
```

## getLocalName

```TypeScript
function getLocalName(): string
```

Obtains the Bluetooth local name of a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getLocalName](arkts-connectivity-bluetoothmanager-getlocalname-f.md#getlocalname)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getLocalName(): string--><!--Device-bluetooth-function getLocalName(): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let localName : string = bluetooth.getLocalName();
```
