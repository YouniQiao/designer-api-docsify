# AbsAlbum (System API)

Defines the AbsAlbum.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [AbsAlbum](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#absalbum)

<!--Device-userFileManager-interface AbsAlbum--><!--Device-userFileManager-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>--><!--Device-AbsAlbum-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## albumName

```TypeScript
albumName: string
```

Name of the album. > **NOTE：**> > The user album is writable, but the system album is not writable.

**Type:** string

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [albumName](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumname)

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

**Deprecated since:** 26.0.0

**Substitutes:** albumSubType

<!--Device-AbsAlbum-readonly albumSubType: AlbumSubType--><!--Device-AbsAlbum-readonly albumSubType: AlbumSubType-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## albumType

```TypeScript
readonly albumType: AlbumType
```

Type of the album to obtain.

**Type:** AlbumType

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [albumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumtype)

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

**Deprecated since:** 26.0.0

**Substitutes:** [albumUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumuri)

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

**Deprecated since:** 26.0.0

**Substitutes:** [count](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#count)

<!--Device-AbsAlbum-readonly count: number--><!--Device-AbsAlbum-readonly count: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## coverUri

```TypeScript
coverUri: string
```

URI of the cover file of the album. > **NOTE：**> > The user album is writable, but the system album is not writable.

**Type:** string

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [coverUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#coveruri)

<!--Device-AbsAlbum-coverUri: string--><!--Device-AbsAlbum-coverUri: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## dateModified

```TypeScript
readonly dateModified: number
```

Time when the album was modified. Unit: ms, The value must be an integer greater than or equal to 0.

**Type:** number

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [dateModified](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-album-i-sys.md#datemodified)

<!--Device-AbsAlbum-readonly dateModified: number--><!--Device-AbsAlbum-readonly dateModified: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.
