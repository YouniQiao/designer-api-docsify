# AbsAlbum

Defines the abstract interface of albums.

**Since:** 10

<!--Device-photoAccessHelper-interface AbsAlbum--><!--Device-photoAccessHelper-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getAssets

```TypeScript
getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void--><!--Device-AbsAlbum-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;PhotoAsset&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## getAssets

```TypeScript
getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbsAlbum-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-AbsAlbum-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;PhotoAsset&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## albumName

```TypeScript
albumName: string
```

Name of the album. System albums are not writable, whereas user albums can be written to.

**Type:** string

**Since:** 10

<!--Device-AbsAlbum-albumName: string--><!--Device-AbsAlbum-albumName: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumSubtype

```TypeScript
readonly albumSubtype: AlbumSubtype
```

Subtype of the album.

**Type:** [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md)

**Since:** 10

<!--Device-AbsAlbum-readonly albumSubtype: AlbumSubtype--><!--Device-AbsAlbum-readonly albumSubtype: AlbumSubtype-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumType

```TypeScript
readonly albumType: AlbumType
```

Type of the album.

**Type:** [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md)

**Since:** 10

<!--Device-AbsAlbum-readonly albumType: AlbumType--><!--Device-AbsAlbum-readonly albumType: AlbumType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumUri

```TypeScript
readonly albumUri: string
```

URI of the album.

**Type:** string

**Since:** 10

<!--Device-AbsAlbum-readonly albumUri: string--><!--Device-AbsAlbum-readonly albumUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## changeTime

```TypeScript
readonly changeTime?: number
```

Time when the album is changed.Unit: second, The value must be greater than or equal to 0.

**Type:** number

**Since:** 23

<!--Device-AbsAlbum-readonly changeTime?: long--><!--Device-AbsAlbum-readonly changeTime?: long-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## count

```TypeScript
readonly count: number
```

Number of files in the album.

**Type:** number

**Since:** 10

<!--Device-AbsAlbum-readonly count: int--><!--Device-AbsAlbum-readonly count: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## coverUri

```TypeScript
readonly coverUri: string
```

URI of the cover file of the album.

**Type:** string

**Since:** 10

<!--Device-AbsAlbum-readonly coverUri: string--><!--Device-AbsAlbum-readonly coverUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## lpath

```TypeScript
readonly lpath?: string
```

Virtual path of the album.

Albums and their virtual path values:

- Camera application album: '/DCIM/Camera'  
- Screenshot application album: '/Pictures/Screenshots'  
- Screen recording application album: '/Pictures/Screenrecords'  
- User-created album: '/Pictures/Users/{Custom album name}'

**Type:** string

**Since:** 23

<!--Device-AbsAlbum-readonly lpath?: string--><!--Device-AbsAlbum-readonly lpath?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
