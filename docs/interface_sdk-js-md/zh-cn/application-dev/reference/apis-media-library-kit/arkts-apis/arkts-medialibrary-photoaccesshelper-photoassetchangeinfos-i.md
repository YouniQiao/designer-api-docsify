# PhotoAssetChangeInfos

Describes the notification information about the change of a media asset.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface PhotoAssetChangeInfos--><!--Device-photoAccessHelper-interface PhotoAssetChangeInfos-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## assetChangeDatas

```TypeScript
assetChangeDatas: PhotoAssetChangeData[] | null
```

Array of changed media assets. If all media assets need to be queried again, **assetChangeDatas** is null.

**类型：** PhotoAssetChangeData[] \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfos-assetChangeDatas: PhotoAssetChangeData[] | null--><!--Device-PhotoAssetChangeInfos-assetChangeDatas: PhotoAssetChangeData[] | null-End-->

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

<!--Device-PhotoAssetChangeInfos-isForRecheck: boolean--><!--Device-PhotoAssetChangeInfos-isForRecheck: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## type

```TypeScript
type: NotifyChangeType
```

Type of the media asset change.

**类型：** [NotifyChangeType](arkts-medialibrary-photoaccesshelper-notifychangetype-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfos-type: NotifyChangeType--><!--Device-PhotoAssetChangeInfos-type: NotifyChangeType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

