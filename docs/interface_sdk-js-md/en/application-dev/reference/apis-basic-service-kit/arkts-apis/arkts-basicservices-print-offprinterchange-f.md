# offPrinterChange

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## offPrinterChange

```TypeScript
function offPrinterChange(callback?: PrinterChangeCallback): void
```

Unregister event callback for the change of printer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void--><!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | No | The callback function for change of printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

