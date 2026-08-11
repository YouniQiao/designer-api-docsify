# usbFunctionsFromString (System API)

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## usbFunctionsFromString

```TypeScript
function usbFunctionsFromString(funcs: string): number
```

Converts the USB function list in the string format to a numeric mask in Device mode.

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring)

<!--Device-usb-function usbFunctionsFromString(funcs: string): number--><!--Device-usb-function usbFunctionsFromString(funcs: string): number-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| funcs | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let funcs = "acm";
let ret = usb.usbFunctionsFromString(funcs);
```
