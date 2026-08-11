# PrintExtensionAbility

class of print extension ability.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class PrintExtensionAbility--><!--Device-unnamed-declare class PrintExtensionAbility-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { PrintExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onCancelPrintJob

```TypeScript
public onCancelPrintJob(jobInfo: print.PrintJob): void
```

Called once to remove the print job has been started.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onCancelPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobInfo | print.PrintJob | Yes | Indicates the information of print job. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

## onConnectPrinter

ArkTS-Dyn:
```TypeScript
onConnectPrinter(printerId: number): void
```

ArkTS-Sta:
```TypeScript
onConnectPrinter(printerId: int): void
```

Called once to connect to the specific printer.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onConnectPrinter(printerId: int): void--><!--Device-PrintExtensionAbility-onConnectPrinter(printerId: int): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | connect the printerId. |

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onConnectPrinter(printerId: number): void {
        console.info('onConnectPrinter enter');
        // ...
    }
}
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called once to initialize the extensionAbility.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onCreate(want: Want): void--><!--Device-PrintExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | call print page want params. |

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onCreate(want: Want): void {
        console.info('onCreate');
        // ...
    }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called once to finalize the extensionAbility.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onDestroy(): void--><!--Device-PrintExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onDestroy(): void {
        console.info('onDestroy');
    }
}
```

## onDisconnectPrinter

ArkTS-Dyn:
```TypeScript
onDisconnectPrinter(printerId: number): void
```

ArkTS-Sta:
```TypeScript
onDisconnectPrinter(printerId: int): void
```

Called once to disconnect to the specific printer.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onDisconnectPrinter(printerId: int): void--><!--Device-PrintExtensionAbility-onDisconnectPrinter(printerId: int): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | connect the printerId. |

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onDisconnectPrinter(printerId: number): void {
        console.info('onDisconnectPrinter enter');
        // ...
    }
}
```

## onRequestPreview

```TypeScript
onRequestPreview(jobInfo: print.PrintJob): string
```

Called once to request preview and send result to Print SA.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string--><!--Device-PrintExtensionAbility-onRequestPreview(jobInfo: print.PrintJob): string-End-->

**System capability:** SystemCapability.Print.PrintFramework

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

ArkTS-Dyn:
```TypeScript
public onRequestPrinterCapability(printerId: number): print.PrinterCapability
```

ArkTS-Sta:
```TypeScript
public onRequestPrinterCapability(printerId: int): print.PrinterCapability
```

Called once to request the printer's capabilities.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability--><!--Device-PrintExtensionAbility-public onRequestPrinterCapability(printerId: int): print.PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the information of printer. |

**Return value:**

| Type | Description |
| --- | --- |
| print.PrinterCapability | printer capability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

## onStartDiscoverPrinter

```TypeScript
onStartDiscoverPrinter(): void
```

Called once to start to discover the printers connected with the device.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onStartDiscoverPrinter(): void--><!--Device-PrintExtensionAbility-onStartDiscoverPrinter(): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onStartDiscoverPrinter(): void {
        console.info('onStartDiscoverPrinter enter');
        // ...
    }
}
```

## onStartPrintJob

```TypeScript
public onStartPrintJob(jobInfo: print.PrintJob): void
```

Called once to start print job.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void--><!--Device-PrintExtensionAbility-public onStartPrintJob(jobInfo: print.PrintJob): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobInfo | print.PrintJob | Yes | Indicates the information of print job. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application<br>**Applicable version:** 10 - 23 |

## onStopDiscoverPrinter

```TypeScript
onStopDiscoverPrinter(): void
```

Called once to stop discovering the printer.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-onStopDiscoverPrinter(): void--><!--Device-PrintExtensionAbility-onStopDiscoverPrinter(): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Examples

```TypeScript
import { PrintExtensionAbility } from '@kit.BasicServicesKit';

export default class HWPrintExtension extends PrintExtensionAbility {
    onStopDiscoverPrinter(): void {
        console.info('onStopDiscoverPrinter enter');
        // ...
    }
}
```

## context

```TypeScript
context: PrintExtensionContext
```

Indicates print service extension ability context.

**Type:** [PrintExtensionContext](arkts-basicservices-printextensioncontext-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintExtensionAbility-context: PrintExtensionContext--><!--Device-PrintExtensionAbility-context: PrintExtensionContext-End-->

**System capability:** SystemCapability.Print.PrintFramework

