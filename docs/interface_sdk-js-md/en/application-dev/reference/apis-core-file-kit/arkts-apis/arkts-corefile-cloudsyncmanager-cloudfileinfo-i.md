# CloudFileInfo

应用本地和云端文件个数以及大小信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cloudSyncManager-interface CloudFileInfo--><!--Device-cloudSyncManager-interface CloudFileInfo-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Modules to Import

```TypeScript
import { cloudSyncManager } from 'kits/@kit.CoreFileKit';
```

## bothFileCount

```TypeScript
bothFileCount: int
```

本地已上传云端的文件总个数，取值范围[0, INT32_MAX]，单位：个。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-bothFileCount: int--><!--Device-CloudFileInfo-bothFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## bothFileTotalSize

```TypeScript
bothFileTotalSize: long
```

本地已上传云端的文件总大小，取值范围[0, INT64_MAX]，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-bothFileTotalSize: long--><!--Device-CloudFileInfo-bothFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## cloudFileCount

```TypeScript
cloudFileCount: int
```

本地未下载的云端文件总个数，取值范围[0, INT32_MAX]，单位：个。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-cloudFileCount: int--><!--Device-CloudFileInfo-cloudFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## cloudFileTotalSize

```TypeScript
cloudFileTotalSize: long
```

本地未下载的云端文件总大小，取值范围[0, INT64_MAX]，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-cloudFileTotalSize: long--><!--Device-CloudFileInfo-cloudFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## localFileCount

```TypeScript
localFileCount: int
```

本地未上传云端的文件总个数，取值范围[0, INT32_MAX]，单位：个。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-localFileCount: int--><!--Device-CloudFileInfo-localFileCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## localFileTotalSize

```TypeScript
localFileTotalSize: long
```

本地未上传云端的文件总大小，取值范围[0, INT64_MAX]，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CloudFileInfo-localFileTotalSize: long--><!--Device-CloudFileInfo-localFileTotalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

