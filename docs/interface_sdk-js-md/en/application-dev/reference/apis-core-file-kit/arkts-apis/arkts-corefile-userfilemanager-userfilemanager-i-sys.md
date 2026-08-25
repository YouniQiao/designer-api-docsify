# UserFileManager (System API)

Defines the UserFileManager class and provides functions to access the data in user file storage.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [PhotoAccessHelper](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## createAlbum

```TypeScript
createAlbum(name: string, callback: AsyncCallback<Album>): void
```

Creates an album. This API uses an asynchronous callback to return the result.The album name must meet the following requirements:  
- The album name is a string of 1 to 255 characters.  
- The album name cannot contain any of the following characters:  
. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- The album name is case-insensitive.  
- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [createAlbumRequest](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Album&gt; | Yes |

## createAlbum

```TypeScript
createAlbum(name: string): Promise<Album>
```

Creates an album. This API uses a promise to return the result.The album name must meet the following requirements:  
- The album name is a string of 1 to 255 characters.  
- The album name cannot contain any of the following characters:  
. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- The album name is case-insensitive.  
- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [createAlbumRequest](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Album & gt; |

## createAudioAsset

```TypeScript
createAudioAsset(displayName: string, callback: AsyncCallback<FileAsset>): void
```

Creates an audio asset. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## createAudioAsset

```TypeScript
createAudioAsset(displayName: string): Promise<FileAsset>
```

Creates an audio asset. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, albumUri: string, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name and URI. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| albumUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, albumUri?: string): Promise<FileAsset>
```

Creates an image or video asset with the specified file name and album URI. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| albumUri | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, createOption: PhotoCreateOptions): Promise<FileAsset>
```

Creates an image or video asset with the specified file name and options. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| createOption | [PhotoCreateOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, createOption: PhotoCreateOptions, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name and options. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| createOption | [PhotoCreateOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<void>): void
```

Deletes a media file. This API uses an asynchronous callback to return the result. The deleted file is moved to the recycle bin. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [deleteAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## delete

```TypeScript
delete(uri: string): Promise<void>
```

Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [deleteAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

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

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void
```

Deletes user albums. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [deleteAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>): Promise<void>
```

Deletes user albums. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [deleteAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## getActivePeers

```TypeScript
getActivePeers(callback: AsyncCallback<Array<PeerInfo>>): void
```

Obtains information about online peer devices. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PeerInfo&gt;&gt; | Yes |

## getActivePeers

```TypeScript
getActivePeers(): Promise<Array<PeerInfo>>
```

Obtains the information about online peer devices. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;PeerInfo & gt; & gt; |

## getAlbums

```TypeScript
getAlbums(
      type: AlbumType,
      subType: AlbumSubType,
      options: FetchOptions,
      callback: AsyncCallback<FetchResult<Album>>
    ): void
```

Obtains albums based on the specified options and album type. This API uses an asynchronous callback to return the result.This API cannot be used to obtain hidden albums. Use [getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums) to obtain hidden albums.Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** getAlbums

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subType: AlbumSubType, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains albums by type. This API uses an asynchronous callback to return the result.This API cannot be used to obtain hidden albums. Use [getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums) to obtain hidden albums.Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** getAlbums

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subType: AlbumSubType, options?: FetchOptions): Promise<FetchResult<Album>>
```

Obtains albums based on the specified options and album type. This API uses a promise to return the result.This API cannot be used to obtain hidden albums. Use [getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums) to obtain hidden albums.Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** getAlbums

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getAllPeers

```TypeScript
getAllPeers(callback: AsyncCallback<Array<PeerInfo>>): void
```

Obtains information about all peer devices. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PeerInfo&gt;&gt; | Yes |

## getAllPeers

```TypeScript
getAllPeers(): Promise<Array<PeerInfo>>
```

Obtains the information about all peer devices. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;PeerInfo & gt; & gt; |

## getAudioAssets

```TypeScript
getAudioAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains audio assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.READ_AUDIO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getAudioAssets

```TypeScript
getAudioAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains an audio asset. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.READ_AUDIO

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

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options: AlbumFetchOptions, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains image and video albums. This API uses an asynchronous callback to return the result.This API cannot be used to obtain hidden albums. Use [getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums) to obtain hidden albums.This API will be deprecated. Use [getAlbums](#getalbums) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AlbumFetchOptions](arkts-corefile-userfilemanager-albumfetchoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options: AlbumFetchOptions): Promise<FetchResult<Album>>
```

Obtains albums. This API uses a promise to return the result.This API cannot be used to obtain hidden albums. Use [getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums) to obtain hidden albums.This API will be deprecated. Use [getAlbums](#getalbums) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AlbumFetchOptions](arkts-corefile-userfilemanager-albumfetchoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; | Yes |

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

**Substitutes:** [getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

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

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void
```

Obtains the index of an image or video in an album. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getPhotoIndex](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#getphotoindex)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoUri | string | Yes |
| albumUri | string | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>
```

Obtains the index of an image or video in an album. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [getPhotoIndex](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#getphotoindex)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoUri | string | Yes |
| albumUri | string | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getPrivateAlbum

```TypeScript
getPrivateAlbum(type: PrivateAlbumType, callback: AsyncCallback<FetchResult<PrivateAlbum>>): void
```

Obtains the system album. This API uses an asynchronous callback to return the result.This API will be deprecated. Use [getAlbums](#getalbums) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** getAlbums

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [PrivateAlbumType](arkts-corefile-userfilemanager-privatealbumtype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;[PrivateAlbum](arkts-corefile-userfilemanager-privatealbum-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## getPrivateAlbum

```TypeScript
getPrivateAlbum(type: PrivateAlbumType): Promise<FetchResult<PrivateAlbum>>
```

Obtains the private album. This API uses a promise to return the result.This API will be deprecated. Use [getAlbums](#getalbums) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** getAlbums

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [PrivateAlbumType](arkts-corefile-userfilemanager-privatealbumtype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;[PrivateAlbum](arkts-corefile-userfilemanager-privatealbum-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## off

```TypeScript
off(type: ChangeEvent, callback?: Callback<void>): void
```

Unsubscribes from changes of the file management library. This API uses a callback to return the result.This API will be deprecated. Use off instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [off](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#offmedialibraryavailability)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ChangeEvent](arkts-corefile-userfilemanager-changeevent-t-sys.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off

```TypeScript
off(uri: string, callback?: Callback<ChangeData>): void
```

Unregisters the listener for the specified URI. Multiple callbacks can be registered for a URI for listening. You can use this API to unregister the specified callbacks or all callbacks.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** unregisterChange

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## on

```TypeScript
on(type: ChangeEvent, callback: Callback<void>): void
```

Subscribes to changes of the file management library. This API uses a callback to return the result.This API will be deprecated. Use on instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [on](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#onmedialibraryavailability)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ChangeEvent](arkts-corefile-userfilemanager-changeevent-t-sys.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on

```TypeScript
on(uri: string, forSubUri: boolean, callback: Callback<ChangeData>): void
```

Registers a listener for the specified URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [registerChange](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#registerchange)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| forSubUri | boolean | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this **UserFileManager** instance. This API uses an asynchronous callback to return the result.Call this API when the APIs in the **UserFileManager** instance are no longer used.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [release](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#release)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this **UserFileManager** instance. This API uses a promise to return the result.Call this API when the APIs in the **UserFileManager** instance are no longer used.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [release](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#release)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
