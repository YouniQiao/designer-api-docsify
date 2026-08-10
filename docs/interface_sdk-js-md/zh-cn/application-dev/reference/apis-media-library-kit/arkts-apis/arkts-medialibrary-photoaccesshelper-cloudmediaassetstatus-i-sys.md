# CloudMediaAssetStatus（系统接口）

Describes the details of a cloud media asset download task. It is the return value of the API used by applications to obtain the cloud asset download task status.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface CloudMediaAssetStatus--><!--Device-photoAccessHelper-interface CloudMediaAssetStatus-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## errorCode

```TypeScript
readonly errorCode: CloudMediaTaskPauseCause
```

Reason why the download task is suspended.

**类型：** [CloudMediaTaskPauseCause](arkts-medialibrary-photoaccesshelper-cloudmediataskpausecause-e-sys.md)

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-CloudMediaAssetStatus-readonly errorCode: CloudMediaTaskPauseCause--><!--Device-CloudMediaAssetStatus-readonly errorCode: CloudMediaTaskPauseCause-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## taskInfo

```TypeScript
readonly taskInfo: string
```

Total number of and size (measured in bytes) of the assets that have been downloaded, and the total number and size (also measured in bytes) of the assets remaining to be downloaded.

**类型：** string

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-CloudMediaAssetStatus-readonly taskInfo: string--><!--Device-CloudMediaAssetStatus-readonly taskInfo: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## taskStatus

```TypeScript
readonly taskStatus: CloudMediaAssetTaskStatus
```

Status of the download task.

**类型：** [CloudMediaAssetTaskStatus](arkts-medialibrary-photoaccesshelper-cloudmediaassettaskstatus-e-sys.md)

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-CloudMediaAssetStatus-readonly taskStatus: CloudMediaAssetTaskStatus--><!--Device-CloudMediaAssetStatus-readonly taskStatus: CloudMediaAssetTaskStatus-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

