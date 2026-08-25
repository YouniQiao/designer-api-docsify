# getExtBundleStats (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getExtBundleStats

```TypeScript
function getExtBundleStats(userId: number, businessName: string): Promise<ExtBundleStats>
```

Obtains the space usage of a specified user, system application bundle name, or system service name. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.STORAGE_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| [businessName](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13600010 |
| 13600012 |
