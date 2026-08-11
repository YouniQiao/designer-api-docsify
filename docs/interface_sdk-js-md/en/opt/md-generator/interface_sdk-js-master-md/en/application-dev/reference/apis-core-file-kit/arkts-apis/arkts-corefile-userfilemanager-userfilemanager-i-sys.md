# UserFileManager (System API)

Defines the UserFileManager class and provides functions to access the data in user file storage.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md)

<!--Device-userFileManager-interface UserFileManager--><!--Device-userFileManager-interface UserFileManager-End-->

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

Creates an album. This API uses an asynchronous callback to return the result.

The album name must meet the following requirements:

- The album name is a string of 1 to 255 characters.  
- The album name cannot contain any of the following characters:

. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

- The album name is case-insensitive.  
- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAlbumChangeRequest.createAlbumRequest](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createAlbum(name: string, callback: AsyncCallback<Album>): void--><!--Device-UserFileManager-createAlbum(name: string, callback: AsyncCallback<Album>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Album&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createAlbumDemo');
  let albumName: string = 'newAlbumName' + new Date().getTime();
  mgr.createAlbum(albumName, (err, album) => {
    if (err) {
      console.error('createAlbumCallback failed with err: ' + err);
      return;
    }
    console.info('createAlbumCallback successfully, album: ' + album.albumName + ' album uri: ' + album.albumUri);
  });
}
```

## createAlbum

```TypeScript
createAlbum(name: string): Promise<Album>
```

Creates an album. This API uses a promise to return the result.

The album name must meet the following requirements:

- The album name is a string of 1 to 255 characters.  
- The album name cannot contain any of the following characters:

. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

- The album name is case-insensitive.  
- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAlbumChangeRequest.createAlbumRequest](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createAlbum(name: string): Promise<Album>--><!--Device-UserFileManager-createAlbum(name: string): Promise<Album>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Album&gt; |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('createAlbumDemo');
  let albumName: string  = 'newAlbumName' + new Date().getTime();
  mgr.createAlbum(albumName).then((album) => {
    console.info('createAlbumPromise successfully, album: ' + album.albumName + ' album uri: ' + album.albumUri);
  }).catch((err: BusinessError) => {
    console.error('createAlbumPromise failed with err: ' + err);
  });
}
```

## createAudioAsset

```TypeScript
createAudioAsset(displayName: string, callback: AsyncCallback<FileAsset>): void
```

Creates an audio asset. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_AUDIO

<!--Device-UserFileManager-createAudioAsset(displayName: string, callback: AsyncCallback<FileAsset>): void--><!--Device-UserFileManager-createAudioAsset(displayName: string, callback: AsyncCallback<FileAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createAudioAssetDemo');
  let testFileName: string = 'testFile' + Date.now() + '.mp3';
  mgr.createAudioAsset(testFileName, (err, fileAsset) => {
    if (fileAsset != undefined) {
      console.info('createAudioAsset file displayName' + fileAsset.displayName);
      console.info('createAudioAsset successfully');
    } else {
      console.error('createAudioAsset failed, message = ', err);
    }
  });
}
```

## createAudioAsset

```TypeScript
createAudioAsset(displayName: string): Promise<FileAsset>
```

Creates an audio asset. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_AUDIO

<!--Device-UserFileManager-createAudioAsset(displayName: string): Promise<FileAsset>--><!--Device-UserFileManager-createAudioAsset(displayName: string): Promise<FileAsset>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FileAsset&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createAudioAssetDemo');
  try {
    let testFileName: string = 'testFile' + Date.now() + '.mp3';
    let fileAsset: userFileManager.FileAsset = await mgr.createAudioAsset(testFileName);
    console.info('createAudioAsset file displayName' + fileAsset.displayName);
    console.info('createAudioAsset successfully');
  } catch (err) {
    console.error('createAudioAsset failed, message = ', err);
  }
}
```

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, albumUri: string, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name and URI. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createPhotoAsset(displayName: string, albumUri: string, callback: AsyncCallback<FileAsset>): void--><!--Device-UserFileManager-createPhotoAsset(displayName: string, albumUri: string, callback: AsyncCallback<FileAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| albumUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('createPhotoAssetDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.AlbumFetchOptions = {
    predicates: predicates
  };
  let albums: userFileManager.FetchResult<userFileManager.Album> = await mgr.getPhotoAlbums(fetchOptions);
  let album: userFileManager.Album = await albums.getFirstObject();
  let testFileName: string = 'testFile' + Date.now() + '.jpg';
  mgr.createPhotoAsset(testFileName, album.albumUri, (err, fileAsset) => {
    if (fileAsset != undefined) {
      console.info('createPhotoAsset file displayName' + fileAsset.displayName);
      console.info('createPhotoAsset successfully');
    } else {
      console.error('createPhotoAsset failed, message = ', err);
    }
  });
}
```

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createPhotoAsset(displayName: string, callback: AsyncCallback<FileAsset>): void--><!--Device-UserFileManager-createPhotoAsset(displayName: string, callback: AsyncCallback<FileAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createPhotoAssetDemo');
  let testFileName: string = 'testFile' + Date.now() + '.jpg';
  mgr.createPhotoAsset(testFileName, (err, fileAsset) => {
    if (fileAsset != undefined) {
      console.info('createPhotoAsset file displayName' + fileAsset.displayName);
      console.info('createPhotoAsset successfully');
    } else {
      console.error('createPhotoAsset failed, message = ', err);
    }
  });
}
```

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, albumUri?: string): Promise<FileAsset>
```

Creates an image or video asset with the specified file name and album URI. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createPhotoAsset(displayName: string, albumUri?: string): Promise<FileAsset>--><!--Device-UserFileManager-createPhotoAsset(displayName: string, albumUri?: string): Promise<FileAsset>-End-->

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
| Promise&lt;FileAsset&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createPhotoAssetDemo');
  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let fileAsset: userFileManager.FileAsset = await mgr.createPhotoAsset(testFileName);
    console.info('createPhotoAsset file displayName' + fileAsset.displayName);
    console.info('createPhotoAsset successfully');
  } catch (err) {
    console.error('createPhotoAsset failed, message = ', err);
  }
}
```

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, createOption: PhotoCreateOptions): Promise<FileAsset>
```

Creates an image or video asset with the specified file name and options. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createPhotoAsset(displayName: string, createOption: PhotoCreateOptions): Promise<FileAsset>--><!--Device-UserFileManager-createPhotoAsset(displayName: string, createOption: PhotoCreateOptions): Promise<FileAsset>-End-->

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
| Promise&lt;FileAsset&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createPhotoAssetDemo');
  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let createOption: userFileManager.PhotoCreateOptions = {
      subType: userFileManager.PhotoSubType.DEFAULT
    }
    let fileAsset: userFileManager.FileAsset = await mgr.createPhotoAsset(testFileName, createOption);
    console.info('createPhotoAsset file displayName' + fileAsset.displayName);
    console.info('createPhotoAsset successfully');
  } catch (err) {
    console.error('createPhotoAsset failed, message = ', err);
  }
}
```

## createPhotoAsset

```TypeScript
createPhotoAsset(displayName: string, createOption: PhotoCreateOptions, callback: AsyncCallback<FileAsset>): void
```

Creates an image or video asset with the specified file name and options. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.createAsset](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#createasset)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-createPhotoAsset(displayName: string, createOption: PhotoCreateOptions, callback: AsyncCallback<FileAsset>): void--><!--Device-UserFileManager-createPhotoAsset(displayName: string, createOption: PhotoCreateOptions, callback: AsyncCallback<FileAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| createOption | [PhotoCreateOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000001 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('createPhotoAssetDemo');
  let testFileName: string = 'testFile' + Date.now() + '.jpg';
  let createOption: userFileManager.PhotoCreateOptions = {
    subType: userFileManager.PhotoSubType.DEFAULT
  }
  mgr.createPhotoAsset(testFileName, createOption, (err, fileAsset) => {
    if (fileAsset != undefined) {
      console.info('createPhotoAsset file displayName' + fileAsset.displayName);
      console.info('createPhotoAsset successfully');
    } else {
      console.error('createPhotoAsset failed, message = ', err);
    }
  });
}
```

## delete

```TypeScript
delete(uri: string, callback: AsyncCallback<void>): void
```

Deletes a media file. This API uses an asynchronous callback to return the result. The deleted file is moved to the recycle bin. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAssetChangeRequest.deleteAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

<!--Device-UserFileManager-delete(uri: string, callback: AsyncCallback<void>): void--><!--Device-UserFileManager-delete(uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('deleteAssetDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    const fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getPhotoAssets(fetchOptions);
    let asset: userFileManager.FileAsset = await fetchResult.getFirstObject();


    if (asset == undefined) {
      console.error('asset not exist');
      return;
    }
    mgr.delete(asset.uri, (err) => {
      if (err == undefined) {
        console.info('delete successfully');
      } else {
        console.error('delete failed with error: ' + err);
      }
    });
  } catch (err) {
    console.error('fetch failed, message =', err);
  }
}
```

## delete

```TypeScript
delete(uri: string): Promise<void>
```

Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAssetChangeRequest.deleteAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md/arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.WRITE_IMAGEVIDEO or ohos.permission.READ_AUDIO and ohos.permission.WRITE_AUDIO

<!--Device-UserFileManager-delete(uri: string): Promise<void>--><!--Device-UserFileManager-delete(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('deleteDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    const fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getPhotoAssets(fetchOptions);
    let asset: userFileManager.FileAsset = await fetchResult.getFirstObject();
    if (asset == undefined) {
      console.error('asset not exist');
      return;
    }
    await mgr.delete(asset.uri);
    console.info('delete successfully');
  } catch (err) {
    console.error('delete failed with error: ' + err);
  }
}
```

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void
```

Deletes user albums. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAlbumChangeRequest.deleteAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void--><!--Device-UserFileManager-deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array&lt;Album&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  // Delete the album named newAlbumName.
  console.info('deleteAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: userFileManager.FetchResult<userFileManager.Album> = await mgr.getAlbums(userFileManager.AlbumType.USER, userFileManager.AlbumSubType.USER_GENERIC, fetchOptions);
  let album: userFileManager.Album = await fetchResult.getFirstObject();
  mgr.deleteAlbums([album], (err) => {
    if (err) {
      console.error('deletePhotoAlbumsCallback failed with err: ' + err);
      return;
    }
    console.info('deletePhotoAlbumsCallback successfully');
  });
  fetchResult.close();
}
```

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>): Promise<void>
```

Deletes user albums. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.MediaAlbumChangeRequest.deleteAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md/arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-UserFileManager-deleteAlbums(albums: Array<Album>): Promise<void>--><!--Device-UserFileManager-deleteAlbums(albums: Array<Album>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array&lt;Album&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(mgr: userFileManager.UserFileManager) {
  // Delete the album named newAlbumName.
  console.info('deleteAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: userFileManager.FetchResult<userFileManager.Album> = await mgr.getAlbums(userFileManager.AlbumType.USER, userFileManager.AlbumSubType.USER_GENERIC, fetchOptions);
  let album: userFileManager.Album = await fetchResult.getFirstObject();
  mgr.deleteAlbums([album]).then(() => {
    console.info('deletePhotoAlbumsPromise successfully');
      fetchResult.close();
    }).catch((err: BusinessError) => {
      console.error('deletePhotoAlbumsPromise failed with err: ' + err);
      fetchResult.close();
  });
}
```

## getActivePeers

```TypeScript
getActivePeers(callback: AsyncCallback<Array<PeerInfo>>): void
```

Obtains information about online peer devices. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

<!--Device-UserFileManager-getActivePeers(callback: AsyncCallback<Array<PeerInfo>>): void--><!--Device-UserFileManager-getActivePeers(callback: AsyncCallback<Array<PeerInfo>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PeerInfo&gt;&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getActivePeersDemo');
  mgr.getActivePeers((err, devicesInfo) => {
    if (devicesInfo != undefined) {
      console.info('getActivePeers succeed.');
      for (let i = 0; i < devicesInfo.length; i++) {
        console.info('get distributed info ' + devicesInfo[i].deviceName + devicesInfo[i].networkId);
      }
    } else {
      console.error('getActivePeers failed. message = ', err);
    }
  });
}
```

## getActivePeers

```TypeScript
getActivePeers(): Promise<Array<PeerInfo>>
```

Obtains the information about online peer devices. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

<!--Device-UserFileManager-getActivePeers(): Promise<Array<PeerInfo>>--><!--Device-UserFileManager-getActivePeers(): Promise<Array<PeerInfo>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;PeerInfo&gt;&gt; |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getActivePeersDemo');
  try {
    let devicesInfo: Array<userFileManager.PeerInfo> = await mgr.getActivePeers();
    if (devicesInfo != undefined) {
      console.info('getActivePeers succeed.');
      for (let i = 0; i < devicesInfo.length; i++) {
        console.info('get distributed info ' + devicesInfo[i].deviceName + devicesInfo[i].networkId);
      }
    } else {
      console.error('get distributed fail');
    }
  } catch (err) {
    console.error('getActivePeers failed. message = ', err);
  }
}
```

## getAlbums

```TypeScript
getAlbums(
      type: AlbumType,
      subType: AlbumSubType,
      options: FetchOptions,
      callback: AsyncCallback<FetchResult<Album>>
    ): void
```

Obtains albums based on the specified options and album type. This API uses an asynchronous callback to return the result.

This API cannot be used to obtain hidden albums. Use   
[getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums)to obtain hidden albums.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.photoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getAlbums(      type: AlbumType,      subType: AlbumSubType,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void--><!--Device-UserFileManager-getAlbums(      type: AlbumType,      subType: AlbumSubType,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e-sys.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  // Obtain the album named newAlbumName.
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  mgr.getAlbums(userFileManager.AlbumType.USER, userFileManager.AlbumSubType.USER_GENERIC, fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error('getAlbumsCallback failed with err: ' + err);
      return;
    }
    if (fetchResult == undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album: userFileManager.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumName: ' + album.albumName);
    fetchResult.close();
  });
}
```

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subType: AlbumSubType, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains albums by type. This API uses an asynchronous callback to return the result.

This API cannot be used to obtain hidden albums. Use   
[getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums)to obtain hidden albums.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.photoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getAlbums(type: AlbumType, subType: AlbumSubType, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-UserFileManager-getAlbums(type: AlbumType, subType: AlbumSubType, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e-sys.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  // Obtain the system album VIDEO, which is preset by default.
  console.info('getAlbumsDemo');
  mgr.getAlbums(userFileManager.AlbumType.SYSTEM, userFileManager.AlbumSubType.VIDEO, async (err, fetchResult) => {
    if (err) {
      console.error('getAlbumsCallback failed with err: ' + err);
      return;
    }
    if (fetchResult == undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album: userFileManager.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumUri: ' + album.albumUri);
    fetchResult.close();
  });
}
```

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subType: AlbumSubType, options?: FetchOptions): Promise<FetchResult<Album>>
```

Obtains albums based on the specified options and album type. This API uses a promise to return the result.

This API cannot be used to obtain hidden albums. Use   
[getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums)to obtain hidden albums.

Before the operation, ensure that the albums to obtain exist.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.photoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getAlbums(type: AlbumType, subType: AlbumSubType, options?: FetchOptions): Promise<FetchResult<Album>>--><!--Device-UserFileManager-getAlbums(type: AlbumType, subType: AlbumSubType, options?: FetchOptions): Promise<FetchResult<Album>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AlbumType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-albumtype-e-sys.md) | Yes |
| subType | [AlbumSubType](arkts-corefile-userfilemanager-albumsubtype-e-sys.md) | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;Album&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(mgr: userFileManager.UserFileManager) {
  // Obtain the album named newAlbumName.
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  mgr.getAlbums(userFileManager.AlbumType.USER, userFileManager.AlbumSubType.USER_GENERIC, fetchOptions).then( async (fetchResult) => {
    if (fetchResult == undefined) {
      console.error('getAlbumsPromise fetchResult is undefined');
      return;
    }
    let album: userFileManager.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error('getAlbumsPromise failed with err: ' + err);
  });
}
```

## getAllPeers

```TypeScript
getAllPeers(callback: AsyncCallback<Array<PeerInfo>>): void
```

Obtains information about all peer devices. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

<!--Device-UserFileManager-getAllPeers(callback: AsyncCallback<Array<PeerInfo>>): void--><!--Device-UserFileManager-getAllPeers(callback: AsyncCallback<Array<PeerInfo>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PeerInfo&gt;&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getAllPeersDemo');
  mgr.getAllPeers((err, devicesInfo) => {
    if (devicesInfo != undefined) {
      console.info('getAllPeers succeed.');
      for (let i = 0; i < devicesInfo.length; i++) {
        console.info('get distributed info ' + devicesInfo[i].deviceName + devicesInfo[i].networkId);
      }
    } else {
      console.error('getAllPeers failed. message = ', err);
    }
  });
}
```

## getAllPeers

```TypeScript
getAllPeers(): Promise<Array<PeerInfo>>
```

Obtains the information about all peer devices. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

<!--Device-UserFileManager-getAllPeers(): Promise<Array<PeerInfo>>--><!--Device-UserFileManager-getAllPeers(): Promise<Array<PeerInfo>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.DistributedCore

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;PeerInfo&gt;&gt; |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getAllPeersDemo');
  try {
    let devicesInfo: Array<userFileManager.PeerInfo> = await mgr.getAllPeers();

    if (devicesInfo != undefined) {
      console.info('getAllPeers succeed.');
      for (let i = 0; i < devicesInfo.length; i++) {
        console.info('get distributed info ' + devicesInfo[i].deviceName + devicesInfo[i].networkId);
      }
    } else {
      console.error('get distributed fail');
    }
  } catch (err) {
    console.error('getAllPeers failed. message = ', err);
  }
}
```

## getAudioAssets

```TypeScript
getAudioAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains audio assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.READ_AUDIO

<!--Device-UserFileManager-getAudioAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void--><!--Device-UserFileManager-getAudioAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;FileAsset&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getAudioAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  mgr.getAudioAssets(fetchOptions, async (err, fetchResult) => {
    if (fetchResult != undefined) {
      console.info('fetchFileResult success');
      let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
      if (fileAsset != undefined) {
        console.info('fileAsset.displayName :' + fileAsset.displayName);
      }
    } else {
      console.error('fetchFileResult fail' + err);
    }
  });
}
```

## getAudioAssets

```TypeScript
getAudioAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains an audio asset. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Required permissions:** ohos.permission.READ_AUDIO

<!--Device-UserFileManager-getAudioAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>--><!--Device-UserFileManager-getAudioAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;FileAsset&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getAudioAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getAudioAssets(fetchOptions);
    if (fetchResult != undefined) {
      console.info('fetchFileResult success');
      let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
      if (fileAsset != undefined) {
        console.info('fileAsset.displayName :' + fileAsset.displayName);
      }
    }
  } catch (err) {
    console.error('getAudioAssets failed, message = ', err);
  }
}
```

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options: AlbumFetchOptions, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains image and video albums. This API uses an asynchronous callback to return the result.

This API cannot be used to obtain hidden albums. Use   
[getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums)to obtain hidden albums.

This API will be deprecated. Use   
[getAlbums](arkts-corefile-userfilemanager-userfilemanager-i-sys.md#getalbums)instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoAlbums(options: AlbumFetchOptions, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-UserFileManager-getPhotoAlbums(options: AlbumFetchOptions, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AlbumFetchOptions](arkts-corefile-userfilemanager-albumfetchoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPhotoAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: userFileManager.AlbumFetchOptions = {
    predicates: predicates
  };

  mgr.getPhotoAlbums(albumFetchOptions, (err, fetchResult) => {
    if (fetchResult != undefined) {
      console.info('albums.count = ' + fetchResult.getCount());
      fetchResult.getFirstObject((err, album) => {
        if (album != undefined) {
          console.info('first album.albumName = ' + album.albumName);
        } else {
          console.error('album is undefined, err = ', err);
        }
      });
    } else {
      console.error('getPhotoAlbums fail, message = ', err);
    }
  });
}
```

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options: AlbumFetchOptions): Promise<FetchResult<Album>>
```

Obtains albums. This API uses a promise to return the result.

This API cannot be used to obtain hidden albums. Use   
[getHiddenAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#gethiddenalbums)to obtain hidden albums.

This API will be deprecated. Use   
[getAlbums](arkts-corefile-userfilemanager-userfilemanager-i-sys.md#getalbums)instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoAlbums(options: AlbumFetchOptions): Promise<FetchResult<Album>>--><!--Device-UserFileManager-getPhotoAlbums(options: AlbumFetchOptions): Promise<FetchResult<Album>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AlbumFetchOptions](arkts-corefile-userfilemanager-albumfetchoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;Album&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPhotoAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: userFileManager.AlbumFetchOptions = {
    predicates: predicates
  };
  try {
    let fetchResult: userFileManager.FetchResult<userFileManager.Album> = await mgr.getPhotoAlbums(albumFetchOptions);
    console.info('album.count = ' + fetchResult.getCount());
    const album: userFileManager.Album = await fetchResult.getFirstObject();
    console.info('first album.albumName = ' + album.albumName);
  } catch (err) {
    console.error('getPhotoAlbums fail, message = ' + err);
  }
}
```

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void
```

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void--><!--Device-UserFileManager-getPhotoAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<FileAsset>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;FileAsset&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPhotoAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  mgr.getPhotoAssets(fetchOptions, async (err, fetchResult) => {
    if (fetchResult != undefined) {
      console.info('fetchResult success');
      let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
      if (fileAsset != undefined) {
        console.info('fileAsset.displayName : ' + fileAsset.displayName);
      }
    } else {
      console.error('fetchResult fail' + err);
    }
  });
}
```

## getPhotoAssets

```TypeScript
getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>
```

Obtains image and video assets. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>--><!--Device-UserFileManager-getPhotoAssets(options: FetchOptions): Promise<FetchResult<FileAsset>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;FileAsset&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPhotoAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getPhotoAssets(fetchOptions);
    if (fetchResult != undefined) {
      console.info('fetchResult success');
      let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
      if (fileAsset != undefined) {
        console.info('fileAsset.displayName :' + fileAsset.displayName);
      }
    }
  } catch (err) {
    console.error('getPhotoAssets failed, message = ', err);
  }
}
```

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void
```

Obtains the index of an image or video in an album. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getPhotoIndex](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#getphotoindex)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void--><!--Device-UserFileManager-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoUri | string | Yes |
| albumUri | string | Yes |
| options | [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  try {
    console.info('getPhotoIndexDemo');
    let predicatesForGetAsset: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOp: userFileManager.FetchOptions = {
      fetchColumns: [],
      predicates: predicatesForGetAsset
    };
    // Obtain the album URI.
    let albumFetchResult: userFileManager.FetchResult<userFileManager.Album> = await mgr.getAlbums(userFileManager.AlbumType.SYSTEM, userFileManager.AlbumSubType.FAVORITE, fetchOp);
    let album: userFileManager.Album = await albumFetchResult.getFirstObject();
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc(userFileManager.ImageVideoKey.DATE_MODIFIED.toString());
    let fetchOptions: userFileManager.FetchOptions = {
      fetchColumns: [userFileManager.ImageVideoKey.DATE_MODIFIED.toString()],
      predicates: predicates
    };
    let photoFetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await album.getPhotoAssets(fetchOptions);
    let expectIndex = 1;
    // Obtain the URI of the second file.
    let photoAsset: userFileManager.FileAsset = await photoFetchResult.getPositionObject(expectIndex);
    mgr.getPhotoIndex(photoAsset.uri, album.albumUri, fetchOptions, (err, index) => {
      if (err == undefined) {
        console.info(`getPhotoIndex successfully and index is : ${index}`);
      } else {
        console.error(`getPhotoIndex failed;`);
      }
    });
  } catch (error) {
    console.error(`getPhotoIndex failed; error: ${error}`);
  }
}
```

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>
```

Obtains the index of an image or video in an album. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getPhotoIndex](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#getphotoindex)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>--><!--Device-UserFileManager-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>-End-->

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
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(mgr: userFileManager.UserFileManager) {
  try {
    console.info('getPhotoIndexDemo');
    let predicatesForGetAsset: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOp: userFileManager.FetchOptions = {
      fetchColumns: [],
      predicates: predicatesForGetAsset
    };
    // Obtain the album URI.
    let albumFetchResult: userFileManager.FetchResult<userFileManager.Album> = await mgr.getAlbums(userFileManager.AlbumType.SYSTEM, userFileManager.AlbumSubType.FAVORITE, fetchOp);
    let album: userFileManager.Album = await albumFetchResult.getFirstObject();
    if (album === undefined) {
      console.error('getPhotoIndexPromise albums is undefined');
      return;
    }
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc(userFileManager.ImageVideoKey.DATE_MODIFIED.toString());
    let fetchOptions: userFileManager.FetchOptions = {
      fetchColumns: [userFileManager.ImageVideoKey.DATE_MODIFIED.toString()],
      predicates: predicates
    };
    let photoFetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await album.getPhotoAssets(fetchOptions);
    let expectIndex = 1;
    // Obtain the URI of the second file.
    let photoAsset: userFileManager.FileAsset = await photoFetchResult.getPositionObject(expectIndex);
    mgr.getPhotoIndex(photoAsset.uri, album.albumUri, fetchOptions).then((index) => {
      console.info(`getPhotoIndex successfully and index is : ${index}`);
    }).catch((err: BusinessError) => {
      console.error(`getPhotoIndex failed; error: ${err}`);
    });
  } catch (error) {
    console.error(`getPhotoIndex failed; error: ${error}`);
  }
}
```

## getPrivateAlbum

```TypeScript
getPrivateAlbum(type: PrivateAlbumType, callback: AsyncCallback<FetchResult<PrivateAlbum>>): void
```

Obtains the system album. This API uses an asynchronous callback to return the result.

This API will be deprecated. Use   
[getAlbums](arkts-corefile-userfilemanager-userfilemanager-i-sys.md#getalbums)instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.photoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPrivateAlbum(type: PrivateAlbumType, callback: AsyncCallback<FetchResult<PrivateAlbum>>): void--><!--Device-UserFileManager-getPrivateAlbum(type: PrivateAlbumType, callback: AsyncCallback<FetchResult<PrivateAlbum>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [PrivateAlbumType](arkts-corefile-userfilemanager-privatealbumtype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;PrivateAlbum&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPrivateAlbumDemo');
  mgr.getPrivateAlbum(userFileManager.PrivateAlbumType.TYPE_TRASH, async (err, fetchResult) => {
    if (fetchResult != undefined) {
      let trashAlbum: userFileManager.PrivateAlbum = await fetchResult.getFirstObject();
      console.info('first album.albumName = ' + trashAlbum.albumName);
    } else {
      console.error('getPrivateAlbum failed. message = ', err);
    }
  });
}
```

## getPrivateAlbum

```TypeScript
getPrivateAlbum(type: PrivateAlbumType): Promise<FetchResult<PrivateAlbum>>
```

Obtains the private album. This API uses a promise to return the result.

This API will be deprecated. Use   
[getAlbums](arkts-corefile-userfilemanager-userfilemanager-i-sys.md#getalbums)instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.photoAccessHelper.getAlbums](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getalbums)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-UserFileManager-getPrivateAlbum(type: PrivateAlbumType): Promise<FetchResult<PrivateAlbum>>--><!--Device-UserFileManager-getPrivateAlbum(type: PrivateAlbumType): Promise<FetchResult<PrivateAlbum>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [PrivateAlbumType](arkts-corefile-userfilemanager-privatealbumtype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;PrivateAlbum&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('getPrivateAlbumDemo');
  try {
    let fetchResult: userFileManager.FetchResult<userFileManager.PrivateAlbum> = await mgr.getPrivateAlbum(userFileManager.PrivateAlbumType.TYPE_TRASH);
    let trashAlbum: userFileManager.PrivateAlbum = await fetchResult.getFirstObject();
    console.info('first album.albumName = ' + trashAlbum.albumName);
  } catch (err) {
    console.error('getPrivateAlbum failed. message = ', err);
  }
}
```

## off

```TypeScript
off(type: ChangeEvent, callback?: Callback<void>): void
```

Unsubscribes from changes of the file management library. This API uses a callback to return the result.

This API will be deprecated. Use   
[off](userFileManager.UserFileManager.off(uri: string, callback?: Callback&lt;ChangeData&gt;)) instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.off

<!--Device-UserFileManager-off(type: ChangeEvent, callback?: Callback<void>): void--><!--Device-UserFileManager-off(type: ChangeEvent, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ChangeEvent](arkts-corefile-userfilemanager-changeevent-t-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('offDemo');
  let count = 0;
  mgr.on('imageChange', () => {
    count++;
    // The image file has been changed. Go to the next step.
  });

  mgr.off('imageChange', () => {
    // The listening is stopped successfully.
  });

  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let fileAsset: userFileManager.FileAsset = await mgr.createPhotoAsset(testFileName);
    console.info('createPhotoAsset file displayName' + fileAsset.displayName);
    console.info('createPhotoAsset successfully');
  } catch (err) {
    console.error('createPhotoAsset failed, message = ' + err);
  }
  // Sleep for 1s.
  if (count == 0) {
    console.info('offDemo success');
  } else {
    console.error('offDemo fail');
  }
}
```

## off

```TypeScript
off(uri: string, callback?: Callback<ChangeData>): void
```

Unregisters the listener for the specified URI. Multiple callbacks can be registered for a URI for listening. You can use this API to unregister the specified callbacks or all callbacks.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.unregisterChange](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#unregisterchange)

<!--Device-UserFileManager-off(uri: string, callback?: Callback<ChangeData>): void--><!--Device-UserFileManager-off(uri: string, callback?: Callback<ChangeData>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('offDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getPhotoAssets(fetchOptions);
  let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
  if (fileAsset != undefined) {
    console.info('fileAsset.displayName : ' + fileAsset.displayName);
  }
  let onCallback1 = (changeData: userFileManager.ChangeData) => {
    console.info('onCallback1 on');
  }
  let onCallback2 = (changeData: userFileManager.ChangeData) => {
    console.info('onCallback2 on');
  }
  if (fileAsset.uri !== undefined) {
    // Register onCallback1.
    mgr.on(fileAsset.uri, false, onCallback1);
    // Register onCallback2.
    mgr.on(fileAsset.uri, false, onCallback2);
    // Unregister the listening of onCallback1.
    mgr.off(fileAsset.uri, onCallback1);  
  }
  fileAsset.favorite(true, (err) => {
    if (err == undefined) {
      console.info('favorite successfully');
    } else {
      console.error('favorite failed with error:' + err);
    }
  });
}
```

## on

```TypeScript
on(type: ChangeEvent, callback: Callback<void>): void
```

Subscribes to changes of the file management library. This API uses a callback to return the result.

This API will be deprecated. Use   
[on](userFileManager.UserFileManager.on(uri: string, forSubUri: boolean, callback: Callback&lt;ChangeData&gt;))instead.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.on

<!--Device-UserFileManager-on(type: ChangeEvent, callback: Callback<void>): void--><!--Device-UserFileManager-on(type: ChangeEvent, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ChangeEvent](arkts-corefile-userfilemanager-changeevent-t-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('onDemo');
  let count = 0;
  mgr.on('imageChange', () => {
    count++;
    // The image file has been changed. Go to the next step.
  });
  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let fileAsset: userFileManager.FileAsset = await mgr.createPhotoAsset(testFileName);
    console.info('createPhotoAsset file displayName' + fileAsset.displayName);
    console.info('createPhotoAsset successfully');
  } catch (err) {
    console.error('createPhotoAsset failed, message = ' + err);
  }
  // Sleep for 1s.
  if (count > 0) {
    console.info('onDemo success');
  } else {
    console.error('onDemo fail');
  }
  mgr.off('imageChange', () => {
    // The listening is stopped successfully.
  });
}
```

## on

```TypeScript
on(uri: string, forSubUri: boolean, callback: Callback<ChangeData>): void
```

Registers a listener for the specified URI. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.registerChange](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#registerchange)

<!--Device-UserFileManager-on(uri: string, forSubUri: boolean, callback: Callback<ChangeData>): void--><!--Device-UserFileManager-on(uri: string, forSubUri: boolean, callback: Callback<ChangeData>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| forSubUri | boolean | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('onDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await mgr.getPhotoAssets(fetchOptions);
  let fileAsset: userFileManager.FileAsset = await fetchResult.getFirstObject();
  if (fileAsset != undefined) {
    console.info('fileAsset.displayName : ' + fileAsset.displayName);
  }
  let onCallback1 = (changeData: userFileManager.ChangeData) => {
      console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
    // The image file has been changed. Go to the next step.
  }
  let onCallback2 = (changeData: userFileManager.ChangeData) => {
      console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
    // The image file has been changed. Go to the next step.
  }
  // Register onCallback1.
  mgr.on(fileAsset.uri, false, onCallback1);
  // Register onCallback2.
  mgr.on(fileAsset.uri, false, onCallback2);

  fileAsset.favorite(true, (err) => {
    if (err == undefined) {
      console.info('favorite successfully');
    } else {
      console.error('favorite failed with error:' + err);
    }
  });
}
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this **UserFileManager** instance. This API uses an asynchronous callback to return the result.

Call this API when the APIs in the **UserFileManager** instance are no longer used.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.release](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#release)

<!--Device-UserFileManager-release(callback: AsyncCallback<void>): void--><!--Device-UserFileManager-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('releaseDemo');
  mgr.release((err) => {
    if (err != undefined) {
      console.error('release failed. message = ', err);
    } else {
      console.info('release ok.');
    }
  });
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases this **UserFileManager** instance. This API uses a promise to return the result.

Call this API when the APIs in the **UserFileManager** instance are no longer used.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.release](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#release)

<!--Device-UserFileManager-release(): Promise<void>--><!--Device-UserFileManager-release(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

For details about how to create a userFileManager instance, see the example in [userFileManager.getUserFileMgr](#userfilemanagergetuserfilemgr).

```TypeScript
async function example(mgr: userFileManager.UserFileManager) {
  console.info('releaseDemo');
  try {
    await mgr.release();
    console.info('release ok.');
  } catch (err) {
    console.error('release failed. message = ', err);
  }
}
```
