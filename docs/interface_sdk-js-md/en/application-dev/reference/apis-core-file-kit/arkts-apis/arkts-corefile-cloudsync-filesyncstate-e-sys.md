# FileSyncState (System API)

端云文件同步状态，为枚举类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudSync-enum FileSyncState--><!--Device-cloudSync-enum FileSyncState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## UPLOADING

```TypeScript
UPLOADING = 0
```

上行同步中。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FileSyncState-UPLOADING = 0--><!--Device-FileSyncState-UPLOADING = 0-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## DOWNLOADING

```TypeScript
DOWNLOADING = 1
```

下行同步中。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FileSyncState-DOWNLOADING = 1--><!--Device-FileSyncState-DOWNLOADING = 1-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## COMPLETED

```TypeScript
COMPLETED = 2
```

同步成功。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FileSyncState-COMPLETED = 2--><!--Device-FileSyncState-COMPLETED = 2-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## STOPPED

```TypeScript
STOPPED = 3
```

同步已停止。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FileSyncState-STOPPED = 3--><!--Device-FileSyncState-STOPPED = 3-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## TO_BE_UPLOADED

```TypeScript
TO_BE_UPLOADED = 4
```

正在等待上行。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FileSyncState-TO_BE_UPLOADED = 4--><!--Device-FileSyncState-TO_BE_UPLOADED = 4-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## UPLOAD_SUCCESS

```TypeScript
UPLOAD_SUCCESS = 5
```

文件已成功上行。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FileSyncState-UPLOAD_SUCCESS = 5--><!--Device-FileSyncState-UPLOAD_SUCCESS = 5-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## UPLOAD_FAILURE

```TypeScript
UPLOAD_FAILURE = 6
```

文件上行失败。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FileSyncState-UPLOAD_FAILURE = 6--><!--Device-FileSyncState-UPLOAD_FAILURE = 6-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

