# onScanDeviceSync

## Modules to Import

```TypeScript
```

## onScanDeviceSync

```TypeScript
function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void
```

Register event callback for scanner device sync.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void--><!--Device-scan-function onScanDeviceSync(callback: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
