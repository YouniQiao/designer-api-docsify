# CloudMediaAssetStatus (System API)

Describes the details of a cloud media asset download task. It is the return value of the API used by applications to obtain the cloud asset download task status.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface CloudMediaAssetStatus--><!--Device-photoAccessHelper-interface CloudMediaAssetStatus-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## errorCode

```TypeScript
readonly errorCode: CloudMediaTaskPauseCause
```

Reason why the download task is suspended.

**Type:** CloudMediaTaskPauseCause

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-CloudMediaAssetStatus-readonly errorCode: CloudMediaTaskPauseCause--><!--Device-CloudMediaAssetStatus-readonly errorCode: CloudMediaTaskPauseCause-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## taskInfo

```TypeScript
readonly taskInfo: string
```

Total number of and size (measured in bytes) of the assets that have been downloaded, and the total number and size (also measured in bytes) of the assets remaining to be downloaded.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-CloudMediaAssetStatus-readonly taskInfo: string--><!--Device-CloudMediaAssetStatus-readonly taskInfo: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## taskStatus

```TypeScript
readonly taskStatus: CloudMediaAssetTaskStatus
```

Status of the download task.

**Type:** CloudMediaAssetTaskStatus

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-CloudMediaAssetStatus-readonly taskStatus: CloudMediaAssetTaskStatus--><!--Device-CloudMediaAssetStatus-readonly taskStatus: CloudMediaAssetTaskStatus-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

