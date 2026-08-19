# offScanDeviceAdd (System API)

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## offScanDeviceAdd

```TypeScript
function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void
```

Unregister event callback for scanner device add (system API).

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void--><!--Device-scan-function offScanDeviceAdd(callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | No | Optional callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

