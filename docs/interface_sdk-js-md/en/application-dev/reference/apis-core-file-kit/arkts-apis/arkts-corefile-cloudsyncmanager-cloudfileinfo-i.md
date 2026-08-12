# CloudFileInfo

Represents the number and size of local and cloud files of an application.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cloudSyncManager-interface CloudFileInfo--><!--Device-cloudSyncManager-interface CloudFileInfo-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## bothFileCount

```TypeScript
bothFileCount: int
```

Total number of local files that have been uploaded to the cloud. The value range is [0, INT32_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-bothFileCount: int--><!--Device-CloudFileInfo-bothFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## bothFileTotalSize

```TypeScript
bothFileTotalSize: long
```

Total size of local files that have been uploaded to the cloud, in bytes. The value range is [0, INT64_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-bothFileTotalSize: long--><!--Device-CloudFileInfo-bothFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## cloudFileCount

```TypeScript
cloudFileCount: int
```

Total number of cloud files that are not downloaded locally. The value range is [0, INT32_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-cloudFileCount: int--><!--Device-CloudFileInfo-cloudFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## cloudFileTotalSize

```TypeScript
cloudFileTotalSize: long
```

Total size of cloud files that are not downloaded locally, in bytes. The value range is [0, INT64_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-cloudFileTotalSize: long--><!--Device-CloudFileInfo-cloudFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## localFileCount

```TypeScript
localFileCount: int
```

Total number of local files that are not uploaded to the cloud. The value range is [0, INT32_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-localFileCount: int--><!--Device-CloudFileInfo-localFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## localFileTotalSize

```TypeScript
localFileTotalSize: long
```

Total size of local files that are not uploaded to the cloud, in bytes. The value range is [0, INT64_MAX].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-localFileTotalSize: long--><!--Device-CloudFileInfo-localFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

