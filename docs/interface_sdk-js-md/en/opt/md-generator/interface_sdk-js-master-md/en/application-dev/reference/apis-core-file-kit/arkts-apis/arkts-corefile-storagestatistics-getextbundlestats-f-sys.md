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

<!--Device-storageStatistics-function getExtBundleStats(userId: int, businessName: string): Promise<ExtBundleStats>--><!--Device-storageStatistics-function getExtBundleStats(userId: int, businessName: string): Promise<ExtBundleStats>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| businessName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ExtBundleStats&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600012 |
| 13600010 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
let businessName: string = 'com.example.storagedemo';
storageStatistics.getExtBundleStats(userId, businessName).then((bundleStats: storageStatistics.ExtBundleStats) => {
  console.info("getExtBundleStats successfully.");
}).catch((err: BusinessError) => {
  console.error(`getExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
