# stopOptimizeSpace (System API)

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## stopOptimizeSpace

```TypeScript
function stopOptimizeSpace(): void
```

Synchronously stops optimizing cloud resource space. This method is used with **startOptimizeSpace**.

**Since:** 17

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function stopOptimizeSpace(): void--><!--Device-cloudSync-function stopOptimizeSpace(): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let para:cloudSync.OptimizeSpaceParam = {totalSize: 1073741824, agingDays: 30};
let callback = (data:cloudSync.OptimizeSpaceProgress) => {
  if (data.state == cloudSync.OptimizeState.FAILED) {
    console.info("optimize space failed");
  } else if (data.state == cloudSync.OptimizeState.RUNNING) {
    console.info("optimize space progress: " + data.progress);
  }
}
cloudSync.startOptimizeSpace(para, callback);
cloudSync.stopOptimizeSpace();   // Stop space optimization.
```
