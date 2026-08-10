# PhotoAssetChangeInfo

Describes the information about a media asset.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface PhotoAssetChangeInfo--><!--Device-photoAccessHelper-interface PhotoAssetChangeInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## albumUri

```TypeScript
albumUri: string
```

URI of the album that the media asset belongs to.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-albumUri: string--><!--Device-PhotoAssetChangeInfo-albumUri: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isFavorite

```TypeScript
isFavorite: boolean
```

Whether the media asset is marked as a favorite. **true** if marked, **false** otherwise.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-isFavorite: boolean--><!--Device-PhotoAssetChangeInfo-isFavorite: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mediaType

```TypeScript
mediaType: PhotoType
```

Type of the media asset (image or video).

**类型：** [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-mediaType: PhotoType--><!--Device-PhotoAssetChangeInfo-mediaType: PhotoType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
uri: string
```

URI of the media asset.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-uri: string--><!--Device-PhotoAssetChangeInfo-uri: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

