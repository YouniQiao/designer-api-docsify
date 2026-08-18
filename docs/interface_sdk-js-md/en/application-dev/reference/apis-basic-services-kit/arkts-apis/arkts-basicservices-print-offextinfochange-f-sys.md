# offExtInfoChange (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## offExtInfoChange

```TypeScript
function offExtInfoChange(callback?: Callback<boolean>): void
```

Unregister event callback for the information change of print extension.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function offExtInfoChange(callback?: Callback<boolean>): void--><!--Device-print-function offExtInfoChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | The callback function for state change of printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

