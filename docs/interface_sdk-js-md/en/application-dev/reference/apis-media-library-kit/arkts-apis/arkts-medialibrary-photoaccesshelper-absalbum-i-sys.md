# AbsAlbum

Defines the abstract interface of albums.

**Since:** 23

<!--Device-photoAccessHelper-interface AbsAlbum--><!--Device-photoAccessHelper-interface AbsAlbum-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getSharedPhotoAssets

```TypeScript
getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>
```

Fetch shared photo assets in an album.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

<!--Device-AbsAlbum-getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>--><!--Device-AbsAlbum-getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | FetchOptions | Yes | Fetch options. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;SharedPhotoAsset&gt; | Returns the shared photo assets |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| 14000011 | Internal system error |

**Examples**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  try {
    console.info('getSharedPhotoAssets test start');
    phAccessHelper.getSharedPhotoAssets(fetchOptions);
    console.info('getSharedPhotoAssets test end');
  } catch (err) {
    console.error(`getSharedPhotoAssets failed, error: ${err.code}, ${err.message}`);
  }
}
```

## coverUriSource

```TypeScript
readonly coverUriSource?: CoverUriSource
```

Source URI of the album cover.

**Type:** [CoverUriSource](arkts-medialibrary-photoaccesshelper-coverurisource-e-sys.md)

**Since:** 23

<!--Device-AbsAlbum-readonly coverUriSource?: CoverUriSource--><!--Device-AbsAlbum-readonly coverUriSource?: CoverUriSource-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## hidden

```TypeScript
readonly hidden?: boolean
```

Whether the album is hidden. **true** if hidden, **false** otherwise.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbsAlbum-readonly hidden?: boolean--><!--Device-AbsAlbum-readonly hidden?: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## lpath

```TypeScript
readonly lpath?: string
```

Virtual path of the album.Albums and their virtual path values:  
- Camera application album: '/DCIM/Camera'- Screenshot application album: '/Pictures/Screenshots'- Screen recording application album: '/Pictures/Screenrecords'- User-created album: '/Pictures/Users/{Custom album name}'

**Type:** string

**Since:** 23

<!--Device-AbsAlbum-readonly lpath?: string--><!--Device-AbsAlbum-readonly lpath?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## uploadStatus

```TypeScript
readonly uploadStatus: boolean
```

Whether the album can be synced to cloud storage or family storage. **true** if it can be synced, **false** otherwise.

**Type:** boolean

**Since:** 26.0.0

<!--Device-AbsAlbum-readonly uploadStatus: boolean--><!--Device-AbsAlbum-readonly uploadStatus: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

