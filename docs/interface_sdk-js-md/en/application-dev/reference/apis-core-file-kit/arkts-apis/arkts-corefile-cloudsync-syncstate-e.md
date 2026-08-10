# SyncState

端云同步状态，为枚举类型。

> **说明：**
> 
> 以下同步状态发生变更时，如果应用注册了同步过程事件监听，则通过回调通知应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cloudSync-enum SyncState--><!--Device-cloudSync-enum SyncState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## UPLOADING

```TypeScript
UPLOADING = 0
```

上行同步中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-UPLOADING = 0--><!--Device-SyncState-UPLOADING = 0-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## UPLOAD_FAILED

```TypeScript
UPLOAD_FAILED = 1
```

上行同步失败。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-UPLOAD_FAILED = 1--><!--Device-SyncState-UPLOAD_FAILED = 1-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## DOWNLOADING

```TypeScript
DOWNLOADING = 2
```

下行同步中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-DOWNLOADING = 2--><!--Device-SyncState-DOWNLOADING = 2-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## DOWNLOAD_FAILED

```TypeScript
DOWNLOAD_FAILED = 3
```

下行同步失败。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-DOWNLOAD_FAILED = 3--><!--Device-SyncState-DOWNLOAD_FAILED = 3-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## COMPLETED

```TypeScript
COMPLETED = 4
```

同步成功。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-COMPLETED = 4--><!--Device-SyncState-COMPLETED = 4-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## STOPPED

```TypeScript
STOPPED = 5
```

同步已停止。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SyncState-STOPPED = 5--><!--Device-SyncState-STOPPED = 5-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

