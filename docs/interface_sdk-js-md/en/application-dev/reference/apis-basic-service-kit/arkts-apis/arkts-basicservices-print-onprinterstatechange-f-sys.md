# onPrinterStateChange (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## onPrinterStateChange

```TypeScript
function onPrinterStateChange(callback: PrinterStateChangeCallback): void
```

Register event callback for the state change of printer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void--><!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) | Yes | The callback function for state change of printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

