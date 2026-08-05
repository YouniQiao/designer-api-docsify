# offScanDeviceSync

## offScanDeviceSync

```TypeScript
function offScanDeviceSync(callback?: Callback<ScannerSyncDevice>): void
```

Unregister event callback for scanner device sync.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function offScanDeviceSync(callback?: Callback<ScannerSyncDevice>): void--><!--Device-scan-function offScanDeviceSync(callback?: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ScannerSyncDevice&gt; | No | Optional callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

