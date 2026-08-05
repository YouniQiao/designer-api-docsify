# offScanDeviceAdd (System API)

## offScanDeviceAdd

```TypeScript
function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void
```

Unregister event callback for scanner device add (system API).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void--><!--Device-scan-function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ScannerDevice&gt; | No | Optional callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

