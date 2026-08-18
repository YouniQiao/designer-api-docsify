# onPrinterStateChange (System API)

## Modules to Import

```TypeScript
```

## onPrinterStateChange

```TypeScript
function onPrinterStateChange(callback: PrinterStateChangeCallback): void
```

Register event callback for the state change of printer.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void--><!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
