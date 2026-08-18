# VersionDownloadProgress

Represents the download state and progress information of historical version files when the [downloadHistoryVersion](arkts-corefile-cloudsync-fileversion-c.md#downloadhistoryversion) method of the [FileVersion](arkts-corefile-cloudsync-fileversion-c.md#fileversion) class is called.

**Since:** 23

<!--Device-cloudSync-interface VersionDownloadProgress--><!--Device-cloudSync-interface VersionDownloadProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
import { cloudSync } from '@kit.CoreFileKit';
import { cloudSyncManager } from '@kit.CoreFileKit';
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## errType

```TypeScript
errType: DownloadErrorType
```

Type of the error returned when the batch download fails.

**Type:** [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md)

**Since:** 23

<!--Device-VersionDownloadProgress-errType: DownloadErrorType--><!--Device-VersionDownloadProgress-errType: DownloadErrorType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## progress

```TypeScript
progress: int
```

Download progress, in percentage.

**Type:** int

**Since:** 23

<!--Device-VersionDownloadProgress-progress: int--><!--Device-VersionDownloadProgress-progress: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## state

```TypeScript
state: State
```

Download state of the cloud file of the selected version.

**Type:** State

**Since:** 23

<!--Device-VersionDownloadProgress-state: State--><!--Device-VersionDownloadProgress-state: State-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

