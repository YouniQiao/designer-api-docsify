# DownloadProgress

全量下载任务的进度信息。

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

已下载数据大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-downloadedSize: long--><!--Device-DownloadProgress-downloadedSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## failedCount

```TypeScript
failedCount: int
```

下载失败的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-failedCount: int--><!--Device-DownloadProgress-failedCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## state

```TypeScript
state: DownloadState
```

下载任务的状态。

**Type:** [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-state: DownloadState--><!--Device-DownloadProgress-state: DownloadState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## stopReason

```TypeScript
stopReason: DownloadStopReason
```

下载停止的原因。

**Type:** [DownloadStopReason](arkts-corefile-cloudsyncmanager-downloadstopreason-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-stopReason: DownloadStopReason--><!--Device-DownloadProgress-stopReason: DownloadStopReason-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## successfulCount

```TypeScript
successfulCount: int
```

已下载的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-successfulCount: int--><!--Device-DownloadProgress-successfulCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## totalCount

```TypeScript
totalCount: int
```

待下载文件总个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-totalCount: int--><!--Device-DownloadProgress-totalCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## totalSize

```TypeScript
totalSize: long
```

需要下载文件的总大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-totalSize: long--><!--Device-DownloadProgress-totalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

