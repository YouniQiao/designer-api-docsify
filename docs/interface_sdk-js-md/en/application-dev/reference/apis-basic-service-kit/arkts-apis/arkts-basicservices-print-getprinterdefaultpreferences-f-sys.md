# getPrinterDefaultPreferences (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## getPrinterDefaultPreferences

```TypeScript
function getPrinterDefaultPreferences(printerId: string): Promise<PrinterPreferences>
```

按打印机ID获取默认首选项。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function getPrinterDefaultPreferences(printerId: string): Promise<PrinterPreferences>--><!--Device-print-function getPrinterDefaultPreferences(printerId: string): Promise<PrinterPreferences>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | string | Yes | 打印机ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PrinterPreferences&gt; | Promise that resolves with the default preferences of the printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100005 | Can not find the printer or printer's ppd file in system. |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

