# onPrinterChange

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## onPrinterChange

```TypeScript
function onPrinterChange(callback: PrinterChangeCallback): void
```

Register event callback for the change of printer.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void--><!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
