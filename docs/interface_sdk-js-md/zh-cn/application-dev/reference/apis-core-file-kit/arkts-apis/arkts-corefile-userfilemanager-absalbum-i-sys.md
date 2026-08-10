# AbsAlbum（系统接口）

Defines the AbsAlbum.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md)

<!--Device-userFileManager-interface AbsAlbum--><!--Device-userFileManager-interface AbsAlbum-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 | Retrieval options. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;FileAsset&gt;&gt; | 是 | Callback used to return the image and video assets obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | if type options is not FetchOptions |

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 | Retrieval options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;FetchResult&lt;FileAsset&gt;&gt; | Promise that returns the image and video assets obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | if type options is not FetchOptions |

## albumName

```TypeScript
albumName: string
```

Name of the album.

> **NOTE：**
> 
> The user album is writable, but the system album is not writable.

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumName](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumname)

<!--Device-AbsAlbum-albumName: string--><!--Device-AbsAlbum-albumName: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## albumSubType

```TypeScript
readonly albumSubType: AlbumSubType
```

Subtype of the album.

**类型：** [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumSubType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumsubtype)

<!--Device-AbsAlbum-readonly albumSubType: AlbumSubType--><!--Device-AbsAlbum-readonly albumSubType: AlbumSubType-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## albumType

```TypeScript
readonly albumType: AlbumType
```

Type of the album to obtain.

**类型：** [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-sendablephotoaccesshelper-albumtype-e-sys.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumtype)

<!--Device-AbsAlbum-readonly albumType: AlbumType--><!--Device-AbsAlbum-readonly albumType: AlbumType-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## albumUri

```TypeScript
readonly albumUri: string
```

URI of the album.

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumuri)

<!--Device-AbsAlbum-readonly albumUri: string--><!--Device-AbsAlbum-readonly albumUri: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## count

```TypeScript
readonly count: number
```

Number of files in the album.

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.count](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#count)

<!--Device-AbsAlbum-readonly count: number--><!--Device-AbsAlbum-readonly count: number-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## coverUri

```TypeScript
coverUri: string
```

URI of the cover file of the album.

> **NOTE：**
> 
> The user album is writable, but the system album is not writable.

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.coverUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#coveruri)

<!--Device-AbsAlbum-coverUri: string--><!--Device-AbsAlbum-coverUri: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## dateModified

```TypeScript
readonly dateModified: number
```

Time when the album was modified.Unit: ms, The value must be an integer greater than or equal to 0.

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.Album.dateModified](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-album-i-sys.md/arkts-medialibrary-photoaccesshelper-album-i-sys.md#datemodified)

<!--Device-AbsAlbum-readonly dateModified: number--><!--Device-AbsAlbum-readonly dateModified: number-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

