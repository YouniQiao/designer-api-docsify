# setExtBundleStats (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## setExtBundleStats

```TypeScript
function setExtBundleStats(userId: number, stats: ExtBundleStats): Promise<void>
```

Reports the space usage of system applications or system services. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the value of **flag** in **stats** is **false**, the value of **businessName** must be the bundle name of an
> application.

**Since:** 23

**Required permissions:** ohos.permission.STORAGE_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| stats | [ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13600010 |
| 13600011 |
