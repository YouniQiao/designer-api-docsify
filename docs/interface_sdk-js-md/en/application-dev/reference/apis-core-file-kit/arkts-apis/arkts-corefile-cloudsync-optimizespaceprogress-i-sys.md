# OptimizeSpaceProgress (System API)

Represents the space optimization states and optimization progress.

**Since:** 23

<!--Device-cloudSync-interface OptimizeSpaceProgress--><!--Device-cloudSync-interface OptimizeSpaceProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## progress

```TypeScript
progress: int
```

Optimization progress percentage. The value range is [0, 100].

**Type:** int

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-OptimizeSpaceProgress-progress: int--><!--Device-OptimizeSpaceProgress-progress: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## state

```TypeScript
state: OptimizeState
```

Enumerates the space optimization states.

**Type:** [OptimizeState](arkts-corefile-cloudsync-optimizestate-e-sys.md)

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-OptimizeSpaceProgress-state: OptimizeState--><!--Device-OptimizeSpaceProgress-state: OptimizeState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

