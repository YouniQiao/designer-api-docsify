# onScanDeviceAdd (System API)

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## onScanDeviceAdd

```TypeScript
function onScanDeviceAdd(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device add (system API).

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceAdd(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceAdd(callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | Yes | Callback for device add event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

