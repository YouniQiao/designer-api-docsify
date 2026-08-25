# OptimizeSpaceParam (System API)

Sets the total optimization space and aging days.

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## agingDays

```TypeScript
agingDays: int
```

Aging days. The system optimizes the local images and videos that have been uploaded to the cloud but not viewed for more than the aging days.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## totalSize

```TypeScript
totalSize:long
```

Total size of the optimization space. You can obtain the total size of all files to be aged through the media library API. The size is transferred by the application and is in bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.
