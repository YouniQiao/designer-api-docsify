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

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
