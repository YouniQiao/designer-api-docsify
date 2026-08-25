# startOptimizeSpace (System API)

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## startOptimizeSpace

```TypeScript
function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>
```

Optimizes local resources that have been synced to the cloud and optimizes local images and videos that have not been accessed before the aging period expires. This API uses a promise to return the result. The callback returns the optimization progress.startOptimizeSpace is used together with **stopOptimizeSpace**. If **startOptimizeSpace** is called repeatedly, the error code 22400006 will be returned, indicating that other tasks are being executed.

**Since:** 17

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optimizePara | [OptimizeSpaceParam](arkts-corefile-cloudsync-optimizespaceparam-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OptimizeSpaceProgress](arkts-corefile-cloudsync-optimizespaceprogress-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 22400005 |
| 22400006 |
