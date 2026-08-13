# MediaAlbumChangeRequest

Provides APIs for managing the media album change request.

**Inheritance/Implementation:** MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md#MediaChangeRequest)

**Since:** 23

**Deprecated since:** -1

<!--Device-photoAccessHelper-class MediaAlbumChangeRequest--><!--Device-photoAccessHelper-class MediaAlbumChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## addAssets

```TypeScript
addAssets(assets: Array<PhotoAsset>): void
```

Add assets to the album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| 14000011 |

## constructor

```TypeScript
constructor(album: Album)
```

Constructor used to initialize a new object.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## getAlbum

```TypeScript
getAlbum(): Album
```

Obtains the album in the current album change request. > **NOTE：**> > For the change request for creating an album, this API returns **null** before > [applyChanges](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#applyChanges) is called > to apply the changes.

**Since:** 11

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-getAlbum(): Album--><!--Device-MediaAlbumChangeRequest-getAlbum(): Album-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## getAlbum

```TypeScript
getAlbum(): Album | null
```

Obtains the album in the current album change request.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-getAlbum(): Album | null--><!--Device-MediaAlbumChangeRequest-getAlbum(): Album | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>): void
```

Removes assets from the album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| 14000011 |

## setAlbumName

```TypeScript
setAlbumName(name: string): void
```

Sets the album name. The album name must meet the following requirements: - The total length of the album name must be between 1 and 255 characters. - It must not contain any invalid characters, which are: . \ / : * ? " ' ` &lt; &gt; | { } [ ] - It is case-insensitive. - Duplicate album names are not allowed.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void--><!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## comment

```TypeScript
readonly comment: string
```

A readonly member for type checking.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAlbumChangeRequest-readonly comment: string--><!--Device-MediaAlbumChangeRequest-readonly comment: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
