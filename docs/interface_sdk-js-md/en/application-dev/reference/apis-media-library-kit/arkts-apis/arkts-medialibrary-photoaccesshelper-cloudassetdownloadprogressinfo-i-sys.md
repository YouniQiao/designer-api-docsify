# CloudAssetDownloadProgressInfo (System API)

Describes the progress information about a batch download.

**Since:** 23

<!--Device-photoAccessHelper-interface CloudAssetDownloadProgressInfo--><!--Device-photoAccessHelper-interface CloudAssetDownloadProgressInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'photoAccessHelper';
```

## autoPauseReason

```TypeScript
readonly autoPauseReason: int
```

Reason for automatic pause.

**Type:** int

**Since:** 23

<!--Device-CloudAssetDownloadProgressInfo-readonly autoPauseReason: int--><!--Device-CloudAssetDownloadProgressInfo-readonly autoPauseReason: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## downloadEventType

```TypeScript
readonly downloadEventType: CloudAssetDownloadNotifyType
```

Type of event that triggers this update.

**Type:** [CloudAssetDownloadNotifyType](arkts-medialibrary-photoaccesshelper-cloudassetdownloadnotifytype-e-sys.md)

**Since:** 23

<!--Device-CloudAssetDownloadProgressInfo-readonly downloadEventType: CloudAssetDownloadNotifyType--><!--Device-CloudAssetDownloadProgressInfo-readonly downloadEventType: CloudAssetDownloadNotifyType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## fileId

```TypeScript
readonly fileId: int
```

ID of the file being downloaded.

**Type:** int

**Since:** 23

<!--Device-CloudAssetDownloadProgressInfo-readonly fileId: int--><!--Device-CloudAssetDownloadProgressInfo-readonly fileId: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## percent

```TypeScript
readonly percent: int
```

Download completion percentage.

**Type:** int

**Since:** 23

<!--Device-CloudAssetDownloadProgressInfo-readonly percent: int--><!--Device-CloudAssetDownloadProgressInfo-readonly percent: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

