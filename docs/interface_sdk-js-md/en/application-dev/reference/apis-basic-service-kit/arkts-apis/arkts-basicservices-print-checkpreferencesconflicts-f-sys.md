# checkPreferencesConflicts (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## checkPreferencesConflicts

```TypeScript
function checkPreferencesConflicts(printerId: string, changedType: string, preferences: PrinterPreferences): Promise<string[]>
```

检查首选项冲突。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function checkPreferencesConflicts(printerId: string, changedType: string, preferences: PrinterPreferences): Promise<string[]>--><!--Device-print-function checkPreferencesConflicts(printerId: string, changedType: string, preferences: PrinterPreferences): Promise<string[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | string | Yes | 打印机ID。 |
| changedType | string | Yes | 在打印界面上修改的字段名称。 |
| preferences | [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) | Yes | 打印界面选择的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise that resolves with the conflicting field names. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100005 | Can not find the printer or printer's ppd file in system. |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

