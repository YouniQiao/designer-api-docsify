# onJobStateChange (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## onJobStateChange

```TypeScript
function onJobStateChange(callback: PrintJobStateChangeCallback): void
```

Register event callback for the state change of print job.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onJobStateChange(callback: PrintJobStateChangeCallback): void--><!--Device-print-function onJobStateChange(callback: PrintJobStateChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PrintJobStateChangeCallback](arkts-basicservices-print-printjobstatechangecallback-t-sys.md) | Yes | The callback function for state change of printer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

