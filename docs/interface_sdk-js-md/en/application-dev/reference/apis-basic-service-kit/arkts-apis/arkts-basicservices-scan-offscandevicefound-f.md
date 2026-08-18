# offScanDeviceFound

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## offScanDeviceFound

```TypeScript
function offScanDeviceFound(callback?: Callback<ScannerDevice>): void
```

Unregister event callback for scanner device found.

**Since:** 23

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function offScanDeviceFound(callback?: Callback<ScannerDevice>): void--><!--Device-scan-function offScanDeviceFound(callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | No | Optional callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

