# onPrinterChange

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## onPrinterChange

```TypeScript
function onPrinterChange(callback: PrinterChangeCallback): void
```

Register event callback for the change of printer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void--><!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Yes | The callback function for change of printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | the application does not have permission to call this function. |

