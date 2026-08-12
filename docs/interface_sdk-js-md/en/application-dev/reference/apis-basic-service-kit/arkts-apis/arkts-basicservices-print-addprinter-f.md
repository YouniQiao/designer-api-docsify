# addPrinter

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## addPrinter

```TypeScript
function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>
```

Add a printer to system.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINTER_DRIVER

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>--><!--Device-print-function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerName | string | Yes | Indicates the printer name. &lt;br&gt;Name of the printer to be added. |
| uri | string | Yes | Indicates the printer uri. &lt;br&gt;Uri of the printer to be added. |
| ppdName | string | No | Indicates the ppd name. &lt;br&gt;Ppd name of the printer to be added. |
| options | string | No | Indicates the options. &lt;br&gt;Optional parameters when adding a printer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-print.md#13100003-print-service-error) | Add the printer to system failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

