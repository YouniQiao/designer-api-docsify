# onExtInfoChange (System API)

## Modules to Import

```TypeScript
import { print } from 'print';
```

## onExtInfoChange

```TypeScript
function onExtInfoChange(callback: ExtInfoChangeCallback): void
```

Register event callback for the information change of print extension.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void--><!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) | Yes | The callback function for information change of print extension. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

