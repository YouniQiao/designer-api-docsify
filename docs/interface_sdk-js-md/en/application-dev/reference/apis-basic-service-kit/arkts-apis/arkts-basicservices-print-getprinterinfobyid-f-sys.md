# getPrinterInfoById (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## getPrinterInfoById

```TypeScript
function getPrinterInfoById(printerId: string): Promise<PrinterInfo>
```

Obtains printer information based on the printer ID. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>--><!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | string | Yes | Printer ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PrinterInfo](arkts-basicservices-print-printerinfo-i-sys.md)&gt; | Promise used to return the printer information. |

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
print.getPrinterInfoById(printerId).then((printerInfo : print.PrinterInfo) => {
    console.info('getPrinterInfoById data : ' + JSON.stringify(printerInfo));
}).catch((error: BusinessError) => {
    console.error('getPrinterInfoById error : ' + JSON.stringify(error));
})
```

