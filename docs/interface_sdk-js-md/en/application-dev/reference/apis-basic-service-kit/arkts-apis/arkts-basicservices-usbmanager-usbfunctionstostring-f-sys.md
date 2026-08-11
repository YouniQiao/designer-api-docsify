# usbFunctionsToString (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## usbFunctionsToString

```TypeScript
function usbFunctionsToString(funcs: FunctionType): string
```

Converts the USB function list in the numeric mask format to a string in Device mode.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [usbManager.getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getstringfromfunctions)(funcs:

<!--Device-usbManager-function usbFunctionsToString(funcs: FunctionType): string--><!--Device-usbManager-function usbFunctionsToString(funcs: FunctionType): string-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Yes | USB function list in numeric mask format. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Function list in string format after conversion. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |

