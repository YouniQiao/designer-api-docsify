# startScan

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## startScan

```TypeScript
function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>
```

Starts NearLink scanning. This API uses a promise to return the result. You need to call [scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md) to subscribe to the scanning results. After this API initiates scanning, the scanned device information is reported through the [scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md) callback. After the scanning is complete, you can call [scan.stopScan](arkts-connectivity-scan-stopscan-f.md) to stop scanning.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filters | [ScanFilters](arkts-connectivity-scan-scanfilters-i.md)[] \| null | Yes |
| options | [ScanOptions](arkts-connectivity-bluetoothmanager-scanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100040 |
| 36100041 |
| 36100042 |
| 36100099 |
