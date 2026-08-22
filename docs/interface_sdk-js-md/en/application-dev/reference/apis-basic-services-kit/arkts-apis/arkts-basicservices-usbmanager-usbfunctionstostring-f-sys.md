# usbFunctionsToString (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## usbFunctionsToString

```TypeScript
function usbFunctionsToString(funcs: FunctionType): string
```

Converts the USB function list in the numeric mask format to a string in Device mode.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md)(funcs: FunctionType)

<!--Device-usbManager-function usbFunctionsToString(funcs: FunctionType): string--><!--Device-usbManager-function usbFunctionsToString(funcs: FunctionType): string-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | FunctionType | Yes | USB function list in numeric mask format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Function list in string format after conversion. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |

**Examples**

```TypeScript
let funcs: number = usbManager.FunctionType.ACM | usb.FunctionType.ECM;
let ret: string = usbManager.usbFunctionsToString(funcs);
```

