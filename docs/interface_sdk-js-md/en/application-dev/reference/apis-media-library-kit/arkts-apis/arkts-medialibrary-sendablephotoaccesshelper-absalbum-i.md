# AbsAlbum

Defines the abstract interface of albums.

**Inheritance/Implementation:** AbsAlbum extends lang.ISendable

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { sendablePhotoAccessHelper } from '@kit.MediaLibraryKit';
```

## getAssets

```TypeScript
getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>
```

Obtains media assets. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes | Retrieval options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FetchResult&lt;PhotoAsset&gt;&gt; | Promise used to return the media assets obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 14000011 | Internal system error |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in sendablePhotoAccessHelper.getPhotoAccessHelper.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
    }
  } catch (err) {
    console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
  }
}
```

For details about how to create a phAccessHelper instance, see the example provided in sendablePhotoAccessHelper.getPhotoAccessHelper.

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('albumGetAssetsDemoPromise');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption).then((albumFetchResult) => {
    console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
  });
}
```

## albumName

```TypeScript
albumName: string
```

Album name.

**Type:** string

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumSubtype

```TypeScript
readonly albumSubtype: AlbumSubtype
```

Album subtype

**Type:** AlbumSubtype

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumType

```TypeScript
readonly albumType: AlbumType
```

Album type

**Type:** AlbumType

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumUri

```TypeScript
readonly albumUri: string
```

Album uri.

**Type:** string

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## count

```TypeScript
readonly count: number
```

Number of assets in the album

**Type:** number

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## coverUri

```TypeScript
readonly coverUri: string
```

Cover uri for the album

**Type:** string

**Since:** 12

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
