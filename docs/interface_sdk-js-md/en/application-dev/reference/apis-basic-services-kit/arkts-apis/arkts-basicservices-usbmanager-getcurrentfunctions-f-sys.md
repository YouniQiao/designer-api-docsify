# getCurrentFunctions (System API)

## Modules to Import

```TypeScript
import usbManager from '@kit.BasicServicesKit';
import serialManager from '@kit.BasicServicesKit.serial';
```

## getCurrentFunctions

```TypeScript
function getCurrentFunctions(): FunctionType
```

Obtains the numeric mask combination for the USB function list in Device mode. When the developer mode is disabled, **undefined** may be returned if no device is connected. Check whether the return value of the API is empty.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md)()

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Numeric mask combination for the USB function list. |

**Examples**

```TypeScript
let ret: number = usbManager.getCurrentFunctions();
```
