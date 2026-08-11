# DownloadProgress

Describes the full download progress.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cloudSyncManager-class DownloadProgress--><!--Device-cloudSyncManager-class DownloadProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Modules to Import

```TypeScript
import { cloudSyncManager } from 'kits/@kit.CoreFileKit';
```

## downloadedSize

```TypeScript
downloadedSize: long
```

Size of the downloaded data, in bytes. The value range is  
[0, INT64_MAX). If the progress is abnormal, **INT64_MAX** is returned.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-downloadedSize: long--><!--Device-DownloadProgress-downloadedSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## failedCount

```TypeScript
failedCount: int
```

Number of files that fail to be downloaded. The value range is [0, INT32_MAX]. If the progress is abnormal,  
**-1** is returned.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-failedCount: int--><!--Device-DownloadProgress-failedCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## state

```TypeScript
state: DownloadState
```

Download state.

**Type:** [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-state: DownloadState--><!--Device-DownloadProgress-state: DownloadState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## stopReason

```TypeScript
stopReason: DownloadStopReason
```

Reason why the download stops.

**Type:** [DownloadStopReason](arkts-corefile-cloudsyncmanager-downloadstopreason-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-stopReason: DownloadStopReason--><!--Device-DownloadProgress-stopReason: DownloadStopReason-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## successfulCount

```TypeScript
successfulCount: int
```

Number of downloaded files. The value range is [0, INT32_MAX]. If the progress is abnormal, **-1** is returned.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-successfulCount: int--><!--Device-DownloadProgress-successfulCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## totalCount

```TypeScript
totalCount: int
```

Total number of files to be downloaded. The value range is [0, INT32_MAX]. If the progress is abnormal, **-1** is returned.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-totalCount: int--><!--Device-DownloadProgress-totalCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## totalSize

```TypeScript
totalSize: long
```

Total size of the files to be downloaded, in bytes. The value range is  
[0, INT64_MAX). If the progress is abnormal, **INT64_MAX** is returned.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-totalSize: long--><!--Device-DownloadProgress-totalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

