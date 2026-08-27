# setCurrentFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## setCurrentFunctions

```TypeScript
function setCurrentFunctions(funcs: FunctionType): Promise<void>
```

Sets the current USB function list in Device mode. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md)(funcs: FunctionType)

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | FunctionType | Yes | USB function list in numeric mask format. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types. |
| [14400002](../errorcode-usb.md#14400002-hdc-disabled) | Permission denied. The HDC is disabled by the system. |

**Examples**

```TypeScript
import {BusinessError} from '@kit.BasicServicesKit';
let funcs: number = usbManager.FunctionType.HDC;
usbManager.setCurrentFunctions(funcs).then(() => {
    console.info('usb setCurrentFunctions successfully.');
}).catch((err: BusinessError) => {
    console.error('usb setCurrentFunctions failed: ' + err.code + ' message: ' + err.message);
});
```
