# getCurrentFunctions (System API)

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## getCurrentFunctions

```TypeScript
function getCurrentFunctions(): FunctionType
```

Obtains the numeric mask combination for the USB function list in Device mode.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 9

**Substitutes:** [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md)

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |

**Examples**

```TypeScript
let ret = usb.getCurrentFunctions();
```
