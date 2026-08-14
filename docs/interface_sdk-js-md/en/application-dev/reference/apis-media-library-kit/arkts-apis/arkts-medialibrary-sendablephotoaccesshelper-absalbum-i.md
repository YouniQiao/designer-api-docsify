# AbsAlbum

Defines the abstract interface of albums.

**Inheritance/Implementation:** AbsAlbum extends lang.ISendable

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-sendablePhotoAccessHelper-interface AbsAlbum--><!--Device-sendablePhotoAccessHelper-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { sendablePhotoAccessHelper } from 'sendablePhotoAccessHelper';
```

## getAssets

```TypeScript
getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>
```

Obtains media assets. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-AbsAlbum-getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-AbsAlbum-getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | photoAccessHelper.FetchOptions | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FetchResult&lt;PhotoAsset&gt;&gt; | Promise used to return the media assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 14000011 | Internal system error |

## albumName

```TypeScript
albumName: string
```

Album name.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-albumName: string--><!--Device-AbsAlbum-albumName: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumSubtype

```TypeScript
readonly albumSubtype: AlbumSubtype
```

Album subtype

**Type:** AlbumSubtype

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-readonly albumSubtype: AlbumSubtype--><!--Device-AbsAlbum-readonly albumSubtype: AlbumSubtype-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumType

```TypeScript
readonly albumType: AlbumType
```

Album type

**Type:** AlbumType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-readonly albumType: AlbumType--><!--Device-AbsAlbum-readonly albumType: AlbumType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumUri

```TypeScript
readonly albumUri: string
```

Album uri.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-readonly albumUri: string--><!--Device-AbsAlbum-readonly albumUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## count

```TypeScript
readonly count: number
```

Number of assets in the album

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-readonly count: number--><!--Device-AbsAlbum-readonly count: number-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## coverUri

```TypeScript
readonly coverUri: string
```

Cover uri for the album

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-AbsAlbum-readonly coverUri: string--><!--Device-AbsAlbum-readonly coverUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

