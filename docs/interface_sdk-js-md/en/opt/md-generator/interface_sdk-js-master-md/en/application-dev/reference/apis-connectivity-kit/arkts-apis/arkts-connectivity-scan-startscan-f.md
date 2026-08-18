# startScan

## Modules to Import

```TypeScript
```

## startScan

```TypeScript
function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>
```

Starts scanning for specified NearLink devices with filters. It is allowed to set filter parameter to {@code null} if you do not want to use filter.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>--><!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>-End-->

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100042 |
| 36100040 |
| 36100041 |
