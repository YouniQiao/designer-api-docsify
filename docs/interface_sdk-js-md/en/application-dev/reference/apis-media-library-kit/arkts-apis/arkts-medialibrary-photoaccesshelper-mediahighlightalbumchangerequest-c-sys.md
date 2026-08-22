# MediaHighlightAlbumChangeRequest (System API)

Provides APIs for managing the media album change request. It inherits from [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md).

**Inheritance/Implementation:** MediaHighlightAlbumChangeRequest extends [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md)

**Since:** 26.0.0

<!--Device-photoAccessHelper-class MediaHighlightAlbumChangeRequest--><!--Device-photoAccessHelper-class MediaHighlightAlbumChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## constructor

```TypeScript
constructor(album: Album)
```

Constructor.

**Since:** 26.0.0

<!--Device-MediaHighlightAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaHighlightAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| album | Album | Yes | Highlights** album. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application. |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |

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

## setHighlightAttribute

```TypeScript
setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void
```

Sets the specified attribute value in the highlights album.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaHighlightAlbumChangeRequest-setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void--><!--Device-MediaHighlightAlbumChangeRequest-setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attribute | [HighlightAlbumChangeAttribute](arkts-medialibrary-photoaccesshelper-highlightalbumchangeattribute-e-sys.md) | Yes | Attribute to set. |
| value | string | Yes | Value to set for the attribute. <br>When **attribute** is **IS_VIEWED** or **IS_FAVORITE**, the value is **0** or **1**. When **attribute** is **NOTIFICATION_TIME**, the value is a numeric string of a maximum of 8 bytes, for example, **12345678**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Called by non-system application. |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error.It is recommended to retry and check the logs. Possible causes: <br>1. Database corrupted; <br>2. The file system is abnormal; <br>3. The IPC request timed out. |

**Examples**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  try {
    console.info('setHighlightAttribute');
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
    let highlightAlbumChangeAttribute: photoAccessHelper.HighlightAlbumChangeAttribute =
      photoAccessHelper.HighlightAlbumChangeAttribute.IS_VIEWED;
    let value: string = "1";
    let changeRequest: photoAccessHelper.MediaHighlightAlbumChangeRequest =
      new photoAccessHelper.MediaHighlightAlbumChangeRequest(highlightAlbum);
    changeRequest.setHighlightAttribute(highlightAlbumChangeAttribute, value);
    await helper.applyChanges(changeRequest);
    console.info(`setHighlightAttribute end`);
  } catch (err) {
    console.error(`setHighlightAttribute error: ${err}`);
  }
}
```

