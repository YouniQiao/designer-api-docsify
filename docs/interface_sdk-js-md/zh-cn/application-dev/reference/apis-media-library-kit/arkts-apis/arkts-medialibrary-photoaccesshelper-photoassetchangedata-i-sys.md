# PhotoAssetChangeData

Describes the change data of a media asset.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface PhotoAssetChangeData--><!--Device-photoAccessHelper-interface PhotoAssetChangeData-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## thumbnailChangeStatus

```TypeScript
thumbnailChangeStatus: ThumbnailChangeStatus
```

Change status of the thumbnail (image/video).

**类型：** [ThumbnailChangeStatus](arkts-medialibrary-photoaccesshelper-thumbnailchangestatus-e-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-thumbnailChangeStatus: ThumbnailChangeStatus--><!--Device-PhotoAssetChangeData-thumbnailChangeStatus: ThumbnailChangeStatus-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## version

```TypeScript
version: long
```

Version number of the media asset notification, which is used to determine the order of notifications.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-version: long--><!--Device-PhotoAssetChangeData-version: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

