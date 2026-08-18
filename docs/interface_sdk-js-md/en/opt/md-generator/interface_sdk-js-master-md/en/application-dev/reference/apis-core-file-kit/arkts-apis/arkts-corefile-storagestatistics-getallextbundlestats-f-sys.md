# getAllExtBundleStats (System API)

## Modules to Import

```TypeScript
```

## getAllExtBundleStats

```TypeScript
function getAllExtBundleStats(userId: number): Promise<Array<ExtBundleStats>>
```

Obtains the space usage of all system applications or system services of a specified user. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.STORAGE_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>--><!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600013 |
| 13600010 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

**Examples**

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
storageStatistics.getAllExtBundleStats(userId).then((bundleStatsList: storageStatistics.ExtBundleStats[]) => {
  console.info("getAllExtBundleStats successfully");
}).catch((err: BusinessError) => {
  console.error(`getAllExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
