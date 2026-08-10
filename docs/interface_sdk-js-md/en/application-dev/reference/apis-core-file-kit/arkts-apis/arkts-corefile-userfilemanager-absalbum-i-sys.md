# AbsAlbum (System API)

Defines the AbsAlbum.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md)

<!--Device-userFileManager-interface AbsAlbum--><!--Device-userFileManager-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes | Retrieval options. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;FileAsset&gt;&gt; | Yes | Callback used to return the image and video assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | if type options is not FetchOptions |

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FetchResult&lt;FileAsset&gt;&gt; | Promise that returns the image and video assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
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

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumName](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumname)

<!--Device-AbsAlbum-albumName: string--><!--Device-AbsAlbum-albumName: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## albumSubType

```TypeScript
readonly albumSubType: AlbumSubType
```

Subtype of the album.

**Type:** [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumSubType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumsubtype)

<!--Device-AbsAlbum-readonly albumSubType: AlbumSubType--><!--Device-AbsAlbum-readonly albumSubType: AlbumSubType-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## albumType

```TypeScript
readonly albumType: AlbumType
```

Type of the album to obtain.

**Type:** [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-sendablephotoaccesshelper-albumtype-e-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumtype)

<!--Device-AbsAlbum-readonly albumType: AlbumType--><!--Device-AbsAlbum-readonly albumType: AlbumType-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## albumUri

```TypeScript
readonly albumUri: string
```

URI of the album.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.albumUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumuri)

<!--Device-AbsAlbum-readonly albumUri: string--><!--Device-AbsAlbum-readonly albumUri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## count

```TypeScript
readonly count: number
```

Number of files in the album.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.count](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#count)

<!--Device-AbsAlbum-readonly count: number--><!--Device-AbsAlbum-readonly count: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## coverUri

```TypeScript
coverUri: string
```

URI of the cover file of the album.

> **NOTE：**
> 
> The user album is writable, but the system album is not writable.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.AbsAlbum.coverUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md/arkts-medialibrary-photoaccesshelper-absalbum-i.md#coveruri)

<!--Device-AbsAlbum-coverUri: string--><!--Device-AbsAlbum-coverUri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## dateModified

```TypeScript
readonly dateModified: number
```

Time when the album was modified.Unit: ms, The value must be an integer greater than or equal to 0.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.Album.dateModified](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-album-i-sys.md/arkts-medialibrary-photoaccesshelper-album-i-sys.md#datemodified)

<!--Device-AbsAlbum-readonly dateModified: number--><!--Device-AbsAlbum-readonly dateModified: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

