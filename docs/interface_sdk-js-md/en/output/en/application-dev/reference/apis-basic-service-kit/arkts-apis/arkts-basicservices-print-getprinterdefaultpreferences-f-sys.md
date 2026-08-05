# getPrinterDefaultPreferences (System API)

## getPrinterDefaultPreferences

```TypeScript
function getPrinterDefaultPreferences(printerId: string): Promise<PrinterPreferences>
```

Get default preferences by printer ID.

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
| printerId | string | Yes | Indicates the printer ID.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Added printer ID in the system. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PrinterPreferences&gt; | - Promise that resolves with the default preferences of the printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |
| [13100005](../../apis-basic-services-kit/errorcode-print.md#13100005-invalid-printer) | Can not find the printer or printer's ppd file in system. |

