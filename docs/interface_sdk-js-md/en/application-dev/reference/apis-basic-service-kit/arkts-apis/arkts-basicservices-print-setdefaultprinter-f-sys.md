# setDefaultPrinter (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## setDefaultPrinter

```TypeScript
function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>
```

Sets the default printer. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>--><!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | string | Yes | Printer ID. |
| type | [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) | Yes | Default printer type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = '1';
let type : print.DefaultPrinterType = print.DefaultPrinterType.DEFAULT_PRINTER_TYPE_SET_BY_USER;
print.setDefaultPrinter(printerId, type).then(() => {
    console.info('setDefaultPrinter success');
}).catch((error: BusinessError) => {
    console.error('setDefaultPrinter error : ' + JSON.stringify(error));
})
```

