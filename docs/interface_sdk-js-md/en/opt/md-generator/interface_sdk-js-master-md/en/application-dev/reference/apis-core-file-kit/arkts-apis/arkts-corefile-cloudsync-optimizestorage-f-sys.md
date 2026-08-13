# optimizeStorage (System API)

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## optimizeStorage

```TypeScript
function optimizeStorage():Promise<void>
```

Optimizes the resources that have been synced to the cloud from the local Gallery and executes the automatic aging policy according to the remaining local space. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function optimizeStorage():Promise<void>--><!--Device-cloudSync-function optimizeStorage():Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

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
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudSync.optimizeStorage().then(() => {
  console.info("optimize storage successfully");   // The foreground UX waits for blocking operations to complete.
}).catch((err: BusinessError) => {
  console.error("optimize storage failed with error message: " + err.message + ", error code: " + err.code);
});
```
