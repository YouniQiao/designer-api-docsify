# getFreeSizeSync (System API)

## Modules to Import

```TypeScript
```

## getFreeSizeSync

```TypeScript
function getFreeSizeSync(): number
```

Obtains the available space of the built-in storage, in bytes. This API returns the result synchronously.

**Since:** 23

**Required permissions:** 
- API version 10 - 14: ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getFreeSizeSync(): long--><!--Device-storageStatistics-function getFreeSizeSync(): long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getFreeSizeSync();
  console.info("getFreeSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFreeSizeSync failed with error:" + JSON.stringify(error));
}
```
