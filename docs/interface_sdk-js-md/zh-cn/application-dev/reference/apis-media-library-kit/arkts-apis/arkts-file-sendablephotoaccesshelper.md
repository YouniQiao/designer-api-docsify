# @ohos.file.sendablePhotoAccessHelper(Helper functions to access image and video assets)

The module provides APIs for album management, including creating an album and accessing and modifying media data in an album, based on a [Sendable](../../../arkts-utils/arkts-sendable.md) object.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-unnamed-declare namespace sendablePhotoAccessHelper--><!--Device-unnamed-declare namespace sendablePhotoAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { sendablePhotoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getPhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-getphotoaccesshelper-f.md#getphotoaccesshelper) | Obtains a PhotoAccessHelper instance, which can be used for accessing and modifying media files in an album. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getPhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-getphotoaccesshelper-f-sys.md#getphotoaccesshelper-1) | Obtains a PhotoAccessHelper instance for the specified user, letting you access and modify media files in an album. |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AbsAlbum](arkts-medialibrary-sendablephotoaccesshelper-absalbum-i.md) | Defines the abstract interface of albums. |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Provides APIs to manage albums. |
| [FetchResult](arkts-medialibrary-sendablephotoaccesshelper-fetchresult-i.md) | Provides APIs to manage the file retrieval result. |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i.md) | Helper functions to access photos and albums. |
| [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Provides APIs for encapsulating file asset attributes. |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AbsAlbum](arkts-medialibrary-sendablephotoaccesshelper-absalbum-i-sys.md) | Defines the abstract interface of albums. |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i-sys.md) | Provides APIs to manage albums. |
| [PhotoAccessHelper](arkts-medialibrary-sendablephotoaccesshelper-photoaccesshelper-i-sys.md) | Helper functions to access photos and albums. |
| [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i-sys.md) | Provides APIs for encapsulating file asset attributes. |
| [SharedPhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-sharedphotoasset-i-sys.md) | Defines the shared photo asset |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | Enumerate the album subtypes. |
| [AlbumType](arkts-medialibrary-sendablephotoaccesshelper-albumtype-e.md) | Enumerates the album types. |
| [DynamicRangeType](arkts-medialibrary-sendablephotoaccesshelper-dynamicrangetype-e.md) | Enumerates the dynamic range types of media assets. |
| [PhotoSubtype](arkts-medialibrary-sendablephotoaccesshelper-photosubtype-e.md) | Enumerates the [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) types. |
| [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | Enumerates media file types. |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e-sys.md) | Enumerate the album subtypes. |
| [AlbumType](arkts-medialibrary-sendablephotoaccesshelper-albumtype-e-sys.md) | Enumerates the album types. |
| [MovingPhotoEffectMode](arkts-medialibrary-sendablephotoaccesshelper-movingphotoeffectmode-e-sys.md) | Enumeration of moving photo effect mode. |
| [PhotoSubtype](arkts-medialibrary-sendablephotoaccesshelper-photosubtype-e-sys.md) | Enumerates the [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) types. |
| [PositionType](arkts-medialibrary-sendablephotoaccesshelper-positiontype-e-sys.md) | Photo asset position |
| [ThumbnailVisibility](arkts-medialibrary-sendablephotoaccesshelper-thumbnailvisibility-e-sys.md) | Ability to access thumbnail |
<!--DelEnd-->

