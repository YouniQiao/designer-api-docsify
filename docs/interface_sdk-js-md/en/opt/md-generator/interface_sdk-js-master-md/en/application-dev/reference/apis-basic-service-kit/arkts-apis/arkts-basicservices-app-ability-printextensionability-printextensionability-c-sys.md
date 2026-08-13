# PrintExtensionAbility (System API)

class of print extension ability.

**Since:** 23

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobInfo | print.PrintJob | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onRequestPreview

```TypeScript
onRequestPreview(jobInfo: print.PrintJob): string
```

Called once to request preview and send result to Print SA.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string--><!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobInfo | print.PrintJob | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
public onRequestPrinterCapability(printerId: number): print.PrinterCapability
```

Called once to request the printer's capabilities.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability--><!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| print.PrinterCapability |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onStartPrintJob

```TypeScript
public onStartPrintJob(jobInfo: print.PrintJob): void
```

Called once to start print job.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobInfo | print.PrintJob | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
