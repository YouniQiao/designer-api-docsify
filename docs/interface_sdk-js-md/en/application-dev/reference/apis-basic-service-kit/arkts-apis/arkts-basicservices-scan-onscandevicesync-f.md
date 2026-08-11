# onScanDeviceSync

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## onScanDeviceSync

```TypeScript
function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void
```

Register event callback for scanner device sync.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void--><!--Device-scan-function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerSyncDevice&gt; | Yes | Callback for device sync event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

