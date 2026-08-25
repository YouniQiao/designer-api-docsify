# PrivateAlbum (System API)

Provides APIs for managing the system albums.This API will be deprecated. Use [Album](arkts-corefile-userfilemanager-album-i-sys.md) instead.

**Inheritance/Implementation:** PrivateAlbum extends [AbsAlbum](arkts-corefile-userfilemanager-absalbum-i-sys.md)

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [Album](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-album-i.md)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<void>): void
```

Deletes a file from the system album. Only the files in the trash can be deleted. This API uses an asynchronous callback to return the result.This API will be deprecated. Use [Album.deletePhotoAssets](arkts-corefile-userfilemanager-album-i-sys.md#deletephotoassets) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** deleteAlbumsWithUri

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## delete

```TypeScript
delete(uri: string): Promise<void>
```

Deletes a file from the system album. Only the files in the trash can be deleted. This API uses a promise to return the result.This API will be deprecated. Use [Album.deletePhotoAssets](arkts-corefile-userfilemanager-album-i-sys.md#deletephotoassets) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** deleteAlbumsWithUri

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## recover

```TypeScript
recover(uri: string, callback: AsyncCallback<void>): void
```

Recovers a file in the system album. Only the files in the trash can be recovered. This API uses an asynchronous callback to return the result.This API will be deprecated. Use [Album.recoverPhotoAssets](arkts-corefile-userfilemanager-album-i-sys.md#recoverphotoassets) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** recoverAssetsWithUri

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## recover

```TypeScript
recover(uri: string): Promise<void>
```

Recovers a file in the system album. Only the files in the trash can be recovered. This API uses a promise to return the result.This API will be deprecated. Use [Album.recoverPhotoAssets](arkts-corefile-userfilemanager-album-i-sys.md#recoverphotoassets) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** recoverAssetsWithUri

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
