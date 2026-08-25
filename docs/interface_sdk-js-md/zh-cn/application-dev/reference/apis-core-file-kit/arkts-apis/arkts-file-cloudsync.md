# @ohos.file.cloudSync

该模块向应用提供端云同步能力，包括启动/停止端云同步以及启动/停止原图下载功能。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## 导入模块

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getCoreFileSyncState](arkts-corefile-cloudsync-getcorefilesyncstate-f.md) |
| [registerChange](arkts-corefile-cloudsync-registerchange-f.md) |
| [unregisterChange](arkts-corefile-cloudsync-unregisterchange-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getFileSyncState](arkts-corefile-cloudsync-getfilesyncstate-f-sys.md) |
| [getFileSyncState](arkts-corefile-cloudsync-getfilesyncstate-f-sys.md) |
| [getFileSyncState](arkts-corefile-cloudsync-getfilesyncstate-f-sys.md) |
| [optimizeStorage](arkts-corefile-cloudsync-optimizestorage-f-sys.md) |
| [startOptimizeSpace](arkts-corefile-cloudsync-startoptimizespace-f-sys.md) |
| [stopOptimizeSpace](arkts-corefile-cloudsync-stopoptimizespace-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [CloudFileCache](arkts-corefile-cloudsync-cloudfilecache-c.md) |
| [FileSync](arkts-corefile-cloudsync-filesync-c.md) |
| [FileVersion](arkts-corefile-cloudsync-fileversion-c.md) |
| [MultiDownloadProgress](arkts-corefile-cloudsync-multidownloadprogress-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [CloudFileCache](arkts-corefile-cloudsync-cloudfilecache-c-sys.md) |
| [Download](arkts-corefile-cloudsync-download-c-sys.md) |
| [FileSync](arkts-corefile-cloudsync-filesync-c-sys.md) |
| [GallerySync](arkts-corefile-cloudsync-gallerysync-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [ChangeData](arkts-corefile-cloudsync-changedata-i.md) |
| [DownloadProgress](arkts-corefile-cloudsync-downloadprogress-i.md) |
| [FailedFileInfo](arkts-corefile-cloudsync-failedfileinfo-i.md) |
| [HistoryVersion](arkts-corefile-cloudsync-historyversion-i.md) |
| [SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md) |
| [VersionDownloadProgress](arkts-corefile-cloudsync-versiondownloadprogress-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [OptimizeSpaceParam](arkts-corefile-cloudsync-optimizespaceparam-i-sys.md) |
| [OptimizeSpaceProgress](arkts-corefile-cloudsync-optimizespaceprogress-i-sys.md) |
| [UploadProgress](arkts-corefile-cloudsync-uploadprogress-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md) |
| [DownloadFileType](arkts-corefile-cloudsync-downloadfiletype-e.md) |
| [ErrorType](arkts-corefile-cloudsync-errortype-e.md) |
| [FileState](arkts-corefile-cloudsync-filestate-e.md) |
| [NotifyType](arkts-corefile-cloudsync-notifytype-e.md) |
| [State](arkts-corefile-cloudsync-state-e.md) |
| [SyncState](arkts-corefile-cloudsync-syncstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ErrorType](arkts-corefile-cloudsync-errortype-e-sys.md) |
| [FileSyncState](arkts-corefile-cloudsync-filesyncstate-e-sys.md) |
| [OptimizeState](arkts-corefile-cloudsync-optimizestate-e-sys.md) |
| [State](arkts-corefile-cloudsync-state-e-sys.md) |
| [UploadState](arkts-corefile-cloudsync-uploadstate-e-sys.md) |
<!--DelEnd-->
