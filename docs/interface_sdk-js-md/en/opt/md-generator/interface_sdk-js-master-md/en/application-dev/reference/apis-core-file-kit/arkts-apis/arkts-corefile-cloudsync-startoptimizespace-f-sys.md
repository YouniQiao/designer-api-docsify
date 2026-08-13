# startOptimizeSpace (System API)

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## startOptimizeSpace

```TypeScript
function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>
```

Optimizes local resources that have been synced to the cloud and optimizes local images and videos that have not been accessed before the aging period expires. This API uses a promise to return the result. The callback returns the optimization progress. startOptimizeSpace is used together with **stopOptimizeSpace**. If **startOptimizeSpace** is called repeatedly, the error code 22400006 will be returned, indicating that other tasks are being executed.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>--><!--Device-cloudSync-function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optimizePara | [OptimizeSpaceParam](arkts-corefile-cloudsync-optimizespaceparam-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OptimizeSpaceProgress](arkts-corefile-cloudsync-optimizespaceprogress-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 22400006 |
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
  } else if (data.state == cloudSync.OptimizeState.COMPLETED && data.progress == 100) {
    console.info("optimize space successfully");
  } else if (data.state == cloudSync.OptimizeState.RUNNING) {
    console.info("optimize space progress: " + data.progress);
  }
}
cloudSync.startOptimizeSpace(para, callback).then(() => {
  console.info("start optimize space");
}).catch((err: BusinessError) => {
  console.error("start optimize space failed with error message: " + err.message + ", error code: " + err.code);
});
```
