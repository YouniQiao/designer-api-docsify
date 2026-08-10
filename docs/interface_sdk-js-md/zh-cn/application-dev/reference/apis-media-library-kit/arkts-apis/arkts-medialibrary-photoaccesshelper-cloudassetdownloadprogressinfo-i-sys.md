# CloudAssetDownloadProgressInfo（系统接口）

Describes the progress information about a batch download.

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface CloudAssetDownloadProgressInfo--><!--Device-photoAccessHelper-interface CloudAssetDownloadProgressInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## autoPauseReason

```TypeScript
readonly autoPauseReason: int
```

Reason for automatic pause.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

<!--Device-CloudAssetDownloadProgressInfo-readonly autoPauseReason: int--><!--Device-CloudAssetDownloadProgressInfo-readonly autoPauseReason: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## downloadEventType

```TypeScript
readonly downloadEventType: CloudAssetDownloadNotifyType
```

Type of event that triggers this update.

**类型：** [CloudAssetDownloadNotifyType](arkts-medialibrary-photoaccesshelper-cloudassetdownloadnotifytype-e-sys.md)

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

<!--Device-CloudAssetDownloadProgressInfo-readonly downloadEventType: CloudAssetDownloadNotifyType--><!--Device-CloudAssetDownloadProgressInfo-readonly downloadEventType: CloudAssetDownloadNotifyType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## fileId

```TypeScript
readonly fileId: int
```

ID of the file being downloaded.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

<!--Device-CloudAssetDownloadProgressInfo-readonly fileId: int--><!--Device-CloudAssetDownloadProgressInfo-readonly fileId: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## percent

```TypeScript
readonly percent: int
```

Download completion percentage.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

<!--Device-CloudAssetDownloadProgressInfo-readonly percent: int--><!--Device-CloudAssetDownloadProgressInfo-readonly percent: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

