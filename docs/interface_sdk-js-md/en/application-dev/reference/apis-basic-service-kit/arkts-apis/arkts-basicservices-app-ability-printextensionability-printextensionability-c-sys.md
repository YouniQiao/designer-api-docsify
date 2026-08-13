# PrintExtensionAbility (System API)

class of print extension ability.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class PrintExtensionAbility--><!--Device-unnamed-declare class PrintExtensionAbility-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
```

## onCancelPrintJob

```TypeScript
public onCancelPrintJob(jobInfo: print.PrintJob): void
```

Called once to remove the print job has been started.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobInfo | print.PrintJob | Yes | Indicates the information of print job. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

## onRequestPreview

```TypeScript
onRequestPreview(jobInfo: print.PrintJob): string
```

Called once to request preview and send result to Print SA.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string--><!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobInfo | print.PrintJob | Yes | Indicates the information of job. |

**Return value:**

| Type | Description |
| --- | --- |
| string | preview result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

## Examples

```TypeScript
import { print, PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onRequestPreview(jobInfo: print.PrintJob): string {
        console.info('onRequestPreview enter');
        // ...
        let tmp : string = '';
        return tmp;
    }
}
```

## onRequestPrinterCapability

```TypeScript
public onRequestPrinterCapability(printerId: int): print.PrinterCapability
```

Called once to request the printer's capabilities.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability--><!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | int | Yes | Indicates the information of printer. |

**Return value:**

| Type | Description |
| --- | --- |
| print.PrinterCapability | printer capability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

## onStartPrintJob

```TypeScript
public onStartPrintJob(jobInfo: print.PrintJob): void
```

Called once to start print job.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobInfo | print.PrintJob | Yes | Indicates the information of print job. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

