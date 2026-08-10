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

## assetAfterChange

```TypeScript
assetAfterChange: PhotoAssetChangeInfo | null
```

Data of the media asset after change. In the case of asset deletion, **assetAfterChange** is null.

**类型：** [PhotoAssetChangeInfo](arkts-medialibrary-photoaccesshelper-photoassetchangeinfo-i.md) \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-assetAfterChange: PhotoAssetChangeInfo | null--><!--Device-PhotoAssetChangeData-assetAfterChange: PhotoAssetChangeInfo | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## assetBeforeChange

```TypeScript
assetBeforeChange: PhotoAssetChangeInfo | null
```

Data of the media asset before change. In the case of asset addition, **assetBeforeChange** is null.

**类型：** [PhotoAssetChangeInfo](arkts-medialibrary-photoaccesshelper-photoassetchangeinfo-i.md) \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-assetBeforeChange: PhotoAssetChangeInfo | null--><!--Device-PhotoAssetChangeData-assetBeforeChange: PhotoAssetChangeInfo | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isContentChanged

```TypeScript
isContentChanged: boolean
```

Whether the content of the media asset is changed. **true** if changed, **false** otherwise.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-isContentChanged: boolean--><!--Device-PhotoAssetChangeData-isContentChanged: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isDeleted

```TypeScript
isDeleted: boolean
```

Whether the media asset is deleted. **true** if deleted, **false** otherwise.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeData-isDeleted: boolean--><!--Device-PhotoAssetChangeData-isDeleted: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

