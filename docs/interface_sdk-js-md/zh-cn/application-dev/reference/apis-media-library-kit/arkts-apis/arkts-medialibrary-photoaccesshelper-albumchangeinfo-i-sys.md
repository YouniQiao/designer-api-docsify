# AlbumChangeInfo

Describes the information about an album.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface AlbumChangeInfo--><!--Device-photoAccessHelper-interface AlbumChangeInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## albumOrder

```TypeScript
albumOrder?: int
```

Sorting value of the album.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-AlbumChangeInfo-albumOrder?: int--><!--Device-AlbumChangeInfo-albumOrder?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## coverInfo

```TypeScript
coverInfo?: PhotoAssetChangeInfo
```

Information of the album cover asset.

**类型：** [PhotoAssetChangeInfo](arkts-medialibrary-photoaccesshelper-photoassetchangeinfo-i-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-coverInfo?: PhotoAssetChangeInfo--><!--Device-AlbumChangeInfo-coverInfo?: PhotoAssetChangeInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## hidden

```TypeScript
hidden?: boolean
```

Whether the album is hidden. **true** if hidden, **false** otherwise.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumChangeInfo-hidden?: boolean--><!--Device-AlbumChangeInfo-hidden?: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## hiddenCount

```TypeScript
hiddenCount: int
```

Number of hidden assets in the album.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-hiddenCount: int--><!--Device-AlbumChangeInfo-hiddenCount: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## hiddenCoverInfo

```TypeScript
hiddenCoverInfo?: PhotoAssetChangeInfo
```

Information of the hidden album cover asset.

**类型：** [PhotoAssetChangeInfo](arkts-medialibrary-photoaccesshelper-photoassetchangeinfo-i-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-hiddenCoverInfo?: PhotoAssetChangeInfo--><!--Device-AlbumChangeInfo-hiddenCoverInfo?: PhotoAssetChangeInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## hiddenCoverUri

```TypeScript
hiddenCoverUri: string
```

URI of the hidden cover asset in the album.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-hiddenCoverUri: string--><!--Device-AlbumChangeInfo-hiddenCoverUri: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## isCoverChanged

```TypeScript
isCoverChanged: boolean
```

Whether the file content of the album cover has changed. **true** if changed, **false** otherwise.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-isCoverChanged: boolean--><!--Device-AlbumChangeInfo-isCoverChanged: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## isHiddenCoverChanged

```TypeScript
isHiddenCoverChanged: boolean
```

Whether the file content of the hidden album cover has changed. **true** if changed, **false** otherwise.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeInfo-isHiddenCoverChanged: boolean--><!--Device-AlbumChangeInfo-isHiddenCoverChanged: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## lpath

```TypeScript
lpath?: string
```

The virtual path of album.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumChangeInfo-lpath?: string--><!--Device-AlbumChangeInfo-lpath?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## orderSection

```TypeScript
orderSection?: int
```

Section that defines the order of the album, specifying where the album is displayed in the Gallery.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-AlbumChangeInfo-orderSection?: int--><!--Device-AlbumChangeInfo-orderSection?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

