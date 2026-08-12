# offScanDeviceSync

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

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
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md)&gt; | No | Optional callback to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

