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

## albumChangeInfos

```TypeScript
albumChangeInfos?: AlbumChangeInfo[] | null
```

Smart album change information.

**类型：** AlbumChangeInfo[] \| null

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAssetChangeInfo-albumChangeInfos?: AlbumChangeInfo[] | null--><!--Device-PhotoAssetChangeInfo-albumChangeInfos?: AlbumChangeInfo[] | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## assetSourceType

```TypeScript
assetSourceType?: AssetSourceType
```

The asset source type.Default value: 0.

**类型：** [AssetSourceType](arkts-medialibrary-photoaccesshelper-assetsourcetype-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAssetChangeInfo-assetSourceType?: AssetSourceType--><!--Device-PhotoAssetChangeInfo-assetSourceType?: AssetSourceType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## dateAddedMs

```TypeScript
dateAddedMs: long
```

Unix timestamp when the media asset was created, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-dateAddedMs: long--><!--Device-PhotoAssetChangeInfo-dateAddedMs: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## dateDay

```TypeScript
dateDay: string
```

Date when the media asset was created.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-dateDay: string--><!--Device-PhotoAssetChangeInfo-dateDay: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## dateModifiedMs

```TypeScript
dateModifiedMs?: long
```

The modified time of asset.&lt;br&gt;Unit:milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAssetChangeInfo-dateModifiedMs?: long--><!--Device-PhotoAssetChangeInfo-dateModifiedMs?: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## dateTakenMs

```TypeScript
dateTakenMs: long
```

Unix timestamp when the media asset was captured, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-dateTakenMs: long--><!--Device-PhotoAssetChangeInfo-dateTakenMs: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## dateTrashedMs

```TypeScript
dateTrashedMs: long
```

Unix timestamp when the media asset was deleted, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-dateTrashedMs: long--><!--Device-PhotoAssetChangeInfo-dateTrashedMs: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## displayName

```TypeScript
displayName?: string
```

Display name of the media asset.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-PhotoAssetChangeInfo-displayName?: string--><!--Device-PhotoAssetChangeInfo-displayName?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## fileId

```TypeScript
fileId: int
```

ID of the media asset.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-fileId: int--><!--Device-PhotoAssetChangeInfo-fileId: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## hiddenTime

```TypeScript
hiddenTime?: long
```

The hidden time of asset.&lt;br&gt;Unit:milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAssetChangeInfo-hiddenTime?: long--><!--Device-PhotoAssetChangeInfo-hiddenTime?: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## isHidden

```TypeScript
isHidden: boolean
```

Whether the media asset is hidden. **true** if hidden, **false** otherwise.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-isHidden: boolean--><!--Device-PhotoAssetChangeInfo-isHidden: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## position

```TypeScript
position?: PositionType
```

Position of the media asset.

**类型：** [PositionType](arkts-medialibrary-photoaccesshelper-positiontype-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-PhotoAssetChangeInfo-position?: PositionType--><!--Device-PhotoAssetChangeInfo-position?: PositionType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## size

```TypeScript
size?: long
```

File size of the media asset, in bytes. The size of a moving photo includes the total size of the image and video.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-PhotoAssetChangeInfo-size?: long--><!--Device-PhotoAssetChangeInfo-size?: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## strongAssociation

```TypeScript
strongAssociation: StrongAssociationType
```

Strong association type of the media asset.

**类型：** [StrongAssociationType](arkts-medialibrary-photoaccesshelper-strongassociationtype-e-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-strongAssociation: StrongAssociationType--><!--Device-PhotoAssetChangeInfo-strongAssociation: StrongAssociationType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## thumbnailVisible

```TypeScript
thumbnailVisible: ThumbnailVisibility
```

Accessibility status of the thumbnail.

**类型：** [ThumbnailVisibility](arkts-medialibrary-sendablephotoaccesshelper-thumbnailvisibility-e-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PhotoAssetChangeInfo-thumbnailVisible: ThumbnailVisibility--><!--Device-PhotoAssetChangeInfo-thumbnailVisible: ThumbnailVisibility-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

