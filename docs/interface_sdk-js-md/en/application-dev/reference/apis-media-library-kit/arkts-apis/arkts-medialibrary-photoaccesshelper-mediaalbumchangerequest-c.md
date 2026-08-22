# MediaAlbumChangeRequest

Provides APIs for managing the media album change request.

**Inheritance/Implementation:** MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md)

**Since:** 23

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

<!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-addAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assets | Array&lt;PhotoAsset&gt; | Yes | Array of assets to add. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |
| 14000016 | Operation Not Support |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('addAssetsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    // Ensure that user albums and photos exist in Gallery.
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.addAssets([asset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('addAssets successfully');
  } catch (err) {
    console.error(`addAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('addAssetsDemoCallback');
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('addAssetsDemoCallback asset is undefined');
      return;
    }
    album.addAssets([asset], (err) => {
      if (err === undefined) {
        console.info('album addAssets successfully');
      } else {
        console.error(`album addAssets failed with error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`addAssetsDemoCallback failed with error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('addAssetsDemoPromise');
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('addAssetsDemoPromise asset is undefined');
      return;
    }
    album.addAssets([asset]).then(() => {
      console.info('album addAssets successfully');
    }).catch((err: BusinessError) => {
      console.error(`album addAssets failed with error: ${err.code}, ${err.message}`);
    });
  } catch (err) {
    console.error(`addAssetsDemoPromise failed with error: ${err.code}, ${err.message}`);
  }
}
```

## constructor

```TypeScript
constructor(album: Album)
```

Constructor used to initialize a new object.

**Since:** 23

<!--Device-MediaAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| album | Album | Yes | Album to change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |

**Examples**

```TypeScript
let assetEditData: photoAccessHelper.MediaAssetEditData = new photoAccessHelper.MediaAssetEditData('system', '1.0');
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('MediaAssetsChangeRequest constructorDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
  let assetsChangeRequest: photoAccessHelper.MediaAssetsChangeRequest = new photoAccessHelper.MediaAssetsChangeRequest(photoAssetList);
}
```

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('HighlightAlbum constructorDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(
    photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, fetchOption);
  let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
  let highlightAlbum: photoAccessHelper.HighlightAlbum = new photoAccessHelper.HighlightAlbum(album);
  albumFetchResult.close();
}
```

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('MediaAnalysisAlbumChangeRequest constructorDemo');
  let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let albumFetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: new dataSharePredicates.DataSharePredicates()
  };
  let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
    await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, albumFetchOption);
  if (albumFetchResult.getCount() === 0) {
    console.error('No album');
    return;
  }
  let highlightAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
  albumFetchResult.close();
  let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
    new photoAccessHelper.MediaAnalysisAlbumChangeRequest(highlightAlbum);
}
```

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('MediaHighlightAlbumChangeRequest constructorDemo');
  let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let albumFetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: new dataSharePredicates.DataSharePredicates()
  };
  let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
    await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, albumFetchOption);
  if (albumFetchResult.getCount() === 0) {
    console.error('No album');
    return;
  }
  let highlightAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
  albumFetchResult.close();
  let changeRequest: photoAccessHelper.MediaHighlightAlbumChangeRequest =
    new photoAccessHelper.MediaHighlightAlbumChangeRequest(highlightAlbum);
}
```

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('AnalysisAlbum constructorDemo');
  let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let albumFetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: new dataSharePredicates.DataSharePredicates()
  };
  let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = 
    await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, albumFetchOption);
  if (albumFetchResult.getCount() === 0) {
    console.error('No album');
    return;
  }
  let highlightAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
  albumFetchResult.close();
  let analysisAlbum: photoAccessHelper.AnalysisAlbum = new photoAccessHelper.AnalysisAlbum(highlightAlbum);
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('MediaAlbumChangeRequest constructorDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
  let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
  let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('MediaAssetChangeRequest constructorDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
}
```

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

| Type | Description |
| --- | --- |
| Album | Album obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAlbumDemo');
  try {
    // Ensure that the user album exists in the gallery.
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    let changeRequestAlbum: photoAccessHelper.Album = albumChangeRequest.getAlbum();
    console.info('change request album uri: ' + changeRequestAlbum.albumUri);
  } catch (err) {
    console.error(`getAlbumDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getAlbum

```TypeScript
getAlbum(): Album | null
```

Obtains the album in the current album change request.

**Since:** 23

<!--Device-MediaAlbumChangeRequest-getAlbum(): Album | null--><!--Device-MediaAlbumChangeRequest-getAlbum(): Album | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| Album \| null | Returns the album, if the operation fails, returns null |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |

**Examples**

See [getAlbum](#getalbum)

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>): void
```

Removes assets from the album.

**Since:** 23

<!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-removeAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assets | Array&lt;PhotoAsset&gt; | Yes | Array of assets to remove. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |
| 14000016 | Operation Not Support |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('removeAssetsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.removeAssets([asset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('removeAssets successfully');
  } catch (err) {
    console.error(`removeAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('removeAssetsDemoCallback');
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('removeAssetsDemoCallback asset is undefined');
      return;
    }
    album.removeAssets([asset], (err) => {
      if (err === undefined) {
        console.info('album removeAssets successfully');
      } else {
        console.error(`album removeAssets failed with error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`removeAssetsDemoCallback failed with error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('removeAssetsDemoPromise');
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (album === undefined) {
      console.error('removeAssetsPromise albums is undefined');
      return;
    }
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOption);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('removeAssetsPromise asset is undefined');
      return;
    }
    album.removeAssets([asset]).then(() => {
      console.info('album removeAssets successfully');
    }).catch((err: BusinessError) => {
      console.error(`album removeAssets failed with error: ${err.code}, ${err.message}`);
    });
  } catch (err) {
    console.error(`removeAssetsDemoPromise failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setAlbumName

```TypeScript
setAlbumName(name: string): void
```

Sets the album name.

The album name must meet the following requirements:

- The total length of the album name must be between 1 and 255 characters. - It must not contain any invalid characters, which are:

. \ / : ? " ' ` &lt; &gt; | { } [ ]

- It is case-insensitive. - Duplicate album names are not allowed.

**Since:** 23

<!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void--><!--Device-MediaAlbumChangeRequest-setAlbumName(name: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Album name to set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | System inner fail |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('setAlbumNameDemo');
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    let newAlbumName: string = 'newAlbumName' + new Date().getTime();
    albumChangeRequest.setAlbumName(newAlbumName);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('setAlbumName successfully');
  } catch (err) {
    console.error(`setAlbumNameDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

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

