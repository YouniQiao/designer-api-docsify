# AbsAlbum (System API)

Defines the AbsAlbum.

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [AbsAlbum](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md)

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userFileManager } from '@kit.CoreFileKit';
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

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | FetchOptions | Yes | Retrieval options. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; | Yes | Callback used to return the image and video assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | if type options is not FetchOptions |

**Examples**

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

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

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('albumGetFileAssetsDemoCallback');

  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: userFileManager.AlbumFetchOptions = {
    predicates: predicates
  };
  let fetchOption: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: userFileManager.FetchResult<userFileManager.Album> = await mgr.getPhotoAlbums(albumFetchOptions);
  let album: userFileManager.Album = await albumList.getFirstObject();
  album.getPhotoAssets(fetchOption, (err, albumFetchResult) => {
    if (albumFetchResult != undefined) {
      console.info('album getPhotoAssets successfully, getCount: ' + albumFetchResult.getCount());
    } else {
      console.error('album getPhotoAssets failed with error: ' + err);
    }
  });
}
```

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('privateAlbumGetFileAssetsDemoCallback');
  let albumList: userFileManager.FetchResult<userFileManager.PrivateAlbum> = await mgr.getPrivateAlbum(userFileManager.PrivateAlbumType.TYPE_TRASH);
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  const trashAlbum: userFileManager.PrivateAlbum = await albumList.getFirstObject();
  if (trashAlbum === undefined) {
    console.error('trashAlbum is undefined');
    return;
  }
  trashAlbum.getPhotoAssets(fetchOption, (err, fetchResult) => {
    if (fetchResult != undefined) {
      let count = fetchResult.getCount();
      console.info('fetchResult.count = ', count);
    } else {
      console.error('getFileAssets failed, message = ', err);
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

**Substitutes:** [getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#getassets)

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | FetchOptions | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FetchResult&lt;[FileAsset](arkts-corefile-userfilemanager-fileasset-i-sys.md)&gt;&gt; | Promise that returns the image and video assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | if type options is not FetchOptions |

**Examples**

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

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

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('albumGetFileAssetsDemoPromise');

  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: userFileManager.AlbumFetchOptions = {
    predicates: predicates
  };
  let fetchOption: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  const albumList: userFileManager.FetchResult<userFileManager.Album> = await mgr.getPhotoAlbums(albumFetchOptions);
  const album: userFileManager.Album = await albumList.getFirstObject();
  album.getPhotoAssets(fetchOption).then((albumFetchResult) => {
    console.info('album getFileAssets successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error('album getFileAssets failed with error: ' + err);
  });
}
```

For details about how to create a userFileManager instance, see the example in userFileManager.getUserFileMgr.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(mgr: userFileManager.UserFileManager) {
  console.info('privateAlbumGetFileAssetsDemoPromise');
  let albumList: userFileManager.FetchResult<userFileManager.PrivateAlbum> = await mgr.getPrivateAlbum(userFileManager.PrivateAlbumType.TYPE_TRASH);
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: userFileManager.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  const trashAlbum: userFileManager.PrivateAlbum = await albumList.getFirstObject();
  let fetchResult: userFileManager.FetchResult<userFileManager.FileAsset> = await trashAlbum.getPhotoAssets(fetchOption);
  let count = fetchResult.getCount();
  console.info('fetchResult.count = ', count);
}
```

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

**Deprecated since:** 26.0.0

**Substitutes:** [albumName](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#albumname)

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

**Deprecated since:** 26.0.0

**Substitutes:** [coverUri](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-absalbum-i.md#coveruri)

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

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.
