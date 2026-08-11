# getCurrentFunctions (System API)

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## getCurrentFunctions

```TypeScript
function getCurrentFunctions(): FunctionType
```

Obtains the numeric mask combination for the USB function list in Device mode.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md#getcurrentfunctions)

<!--Device-usb-function getCurrentFunctions(): FunctionType--><!--Device-usb-function getCurrentFunctions(): FunctionType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Numeric mask combination for the USB function list. |

## Examples

```TypeScript
let ret = usb.getCurrentFunctions();
```

