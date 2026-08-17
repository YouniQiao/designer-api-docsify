# OptimizeSpaceParam (System API)

Sets the total optimization space and aging days.

**Since:** 23

<!--Device-cloudSync-interface OptimizeSpaceParam--><!--Device-cloudSync-interface OptimizeSpaceParam-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from 'cloudSync';
```

## agingDays

```TypeScript
agingDays: int
```

Aging days. The system optimizes the local images and videos that have been uploaded to the cloud but not viewed for more than the aging days.

**Type:** int

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-OptimizeSpaceParam-agingDays: int--><!--Device-OptimizeSpaceParam-agingDays: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## totalSize

```TypeScript
totalSize:long
```

Total size of the optimization space. You can obtain the total size of all files to be aged through the media library API. The size is transferred by the application and is in bytes.

**Type:** long

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-OptimizeSpaceParam-totalSize:long--><!--Device-OptimizeSpaceParam-totalSize:long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

