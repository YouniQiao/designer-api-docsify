# onScanDeviceFound

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## onScanDeviceFound

```TypeScript
function onScanDeviceFound(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device found.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | Yes | Callback for device found event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

