# onScanDeviceDel (System API)

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## onScanDeviceDel

```TypeScript
function onScanDeviceDel(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device delete (system API).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceDel(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceDel(callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | Yes | Callback for device delete event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

