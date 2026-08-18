# offPrinterChange

## Modules to Import

```TypeScript
```

## offPrinterChange

```TypeScript
function offPrinterChange(callback?: PrinterChangeCallback): void
```

Unregister event callback for the change of printer.

**Since:** 23

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void--><!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
