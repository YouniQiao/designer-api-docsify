# MediaAlbumChangeRequest

Provides APIs for managing the media album change request.

**Inheritance/Implementation:** MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md)

**Since:** 11

<!--Device-photoAccessHelper-class MediaAlbumChangeRequest implements MediaChangeRequest--><!--Device-photoAccessHelper-class MediaAlbumChangeRequest implements MediaChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## addAssets

```TypeScript
addAssets(assets: Array<PhotoAsset>): void
```

Add assets to the album.

**Since:** 11

<!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array&lt;PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000016 |
| 14000011 |

## constructor

```TypeScript
constructor(album: Album)
```

Constructor used to initialize a new object.

**Since:** 11

<!--Device-MediaAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## getAlbum

```TypeScript
getAlbum(): Album
```

Obtains the album in the current album change request.

> **NOTE：**
> 
> For the change request for creating an album, this API returns **null** before
> [applyChanges](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#applychanges) is called
> to apply the changes.

**Since:** 11

<!--Device-MediaAlbumChangeRequest-getAlbum(): Album--><!--Device-MediaAlbumChangeRequest-getAlbum(): Album-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>): void
```

Removes assets from the album.

**Since:** 11

<!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array&lt;PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000016 |
| 14000011 |

## setAlbumName

```TypeScript
setAlbumName(name: string): void
```

Sets the album name.

The album name must meet the following requirements:

- The total length of the album name must be between 1 and 255 characters.  
- It must not contain any invalid characters, which are:

. \ / : * ? " ' ` &lt; &gt; | { } [ ]

- It is case-insensitive.  
- Duplicate album names are not allowed.

**Since:** 11

<!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void--><!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000011 |

## comment

```TypeScript
readonly comment: string
```

A readonly member for type checking.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAlbumChangeRequest-readonly comment: string--><!--Device-MediaAlbumChangeRequest-readonly comment: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
