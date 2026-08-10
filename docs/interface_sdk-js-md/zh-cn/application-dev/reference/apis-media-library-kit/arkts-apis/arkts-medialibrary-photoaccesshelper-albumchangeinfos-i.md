# AlbumChangeInfos

Describes the notification information about the change of an album.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface AlbumChangeInfos--><!--Device-photoAccessHelper-interface AlbumChangeInfos-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## albumChangeDatas

```TypeScript
albumChangeDatas: AlbumChangeData[] | null
```

Array of changed albums. If all albums need to be queried again, **albumChangeDatas** is null.

**类型：** AlbumChangeData[] \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfos-albumChangeDatas: AlbumChangeData[] | null--><!--Device-AlbumChangeInfos-albumChangeDatas: AlbumChangeData[] | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isForRecheck

```TypeScript
isForRecheck: boolean
```

Whether the application should query all media assets again. **true** if the application should query all assets again, **false** otherwise.

**NOTE：**

In scenarios involving bulk asset operations or abnormal notifications, **isForRecheck** will be **true**. In this case, the application should query all assets again.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfos-isForRecheck: boolean--><!--Device-AlbumChangeInfos-isForRecheck: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## type

```TypeScript
type: NotifyChangeType
```

Type of the album change.

**类型：** [NotifyChangeType](arkts-medialibrary-photoaccesshelper-notifychangetype-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfos-type: NotifyChangeType--><!--Device-AlbumChangeInfos-type: NotifyChangeType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

