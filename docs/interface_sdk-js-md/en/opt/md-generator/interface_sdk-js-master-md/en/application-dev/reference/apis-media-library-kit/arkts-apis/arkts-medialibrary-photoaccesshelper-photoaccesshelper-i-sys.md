# PhotoAccessHelper

Helper functions to access photos and albums.

**Since:** 10

<!--Device-photoAccessHelper-interface PhotoAccessHelper--><!--Device-photoAccessHelper-interface PhotoAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## acquireDebugDatabase

```TypeScript
acquireDebugDatabase(betaIssueId: string, betaScenario: string): Promise<Map<string, string>>
```

Start medialibrary database backup and wait for returning with backup information which only works on beta device.

**Since:** 23

<!--Device-PhotoAccessHelper-acquireDebugDatabase(betaIssueId: string, betaScenario: string): Promise<Map<string, string>>--><!--Device-PhotoAccessHelper-acquireDebugDatabase(betaIssueId: string, betaScenario: string): Promise<Map<string, string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| betaIssueId | string | Yes |
| betaScenario | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800201-unsupported-operation-type) |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## batchGetPhotoAssetParams

```TypeScript
batchGetPhotoAssetParams(assets: PhotoAsset[], members: string[]): PhotoAssetParams
```

Obtains the values of specified properties for an array of   
[PhotoAsset](arkts-medialibrary-photoaccesshelper-photoasset-i.md#PhotoAsset) objects in batches.

**Since:** 21

<!--Device-PhotoAccessHelper-batchGetPhotoAssetParams(assets: PhotoAsset[], members: string[]): PhotoAssetParams--><!--Device-PhotoAccessHelper-batchGetPhotoAssetParams(assets: PhotoAsset[], members: string[]): PhotoAssetParams-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | [PhotoAsset[]](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| [members](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-cdsm-cdsminfo-i.md) | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PhotoAssetParams](arkts-medialibrary-photoaccesshelper-photoassetparams-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [23800104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800104-input-parameter-verification-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper} from '@kit.MediaLibraryKit';

async function example(context: Context) {
  console.info('batchGetPhotoAssetParams');
  type PhotoAsset = photoAccessHelper.PhotoAsset;
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  const FETCH_COLUMNS: string[] = [
    photoAccessHelper.PhotoKeys.SIZE,
    photoAccessHelper.PhotoKeys.DATE_ADDED,
    photoAccessHelper.PhotoKeys.DATE_MODIFIED,
    photoAccessHelper.PhotoKeys.PHOTO_TYPE,
    photoAccessHelper.PhotoKeys.TITLE,
    photoAccessHelper.PhotoKeys.DATE_MODIFIED_MS,
    photoAccessHelper.PhotoKeys.DURATION,
    photoAccessHelper.PhotoKeys.WIDTH,
    photoAccessHelper.PhotoKeys.HEIGHT,
    photoAccessHelper.PhotoKeys.DATE_TRASHED_MS,
    photoAccessHelper.PhotoKeys.POSITION,
    photoAccessHelper.PhotoKeys.DATE_TAKEN,
    'owner_album_id',
    'thumbnail_ready',
    'data',
  ];
  const keyToGet: string[] = [
    photoAccessHelper.PhotoKeys.URI,
    photoAccessHelper.PhotoKeys.DISPLAY_NAME,
    photoAccessHelper.PhotoKeys.DATE_ADDED,
    photoAccessHelper.PhotoKeys.SIZE,
    photoAccessHelper.PhotoKeys.DURATION,
    photoAccessHelper.PhotoKeys.WIDTH,
    photoAccessHelper.PhotoKeys.HEIGHT,
    'data',
    photoAccessHelper.PhotoKeys.THUMBNAIL_READY,];
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: FETCH_COLUMNS,
    predicates: predicates
  };
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: albumPredicates
  }
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.
  getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
  let photoAssetsFetchResult: photoAccessHelper.FetchResult<PhotoAsset> = await album.getAssets(fetchOptions);
  let photoAssets: PhotoAsset[] = await photoAssetsFetchResult.getAllObjects();
  const batchParamOfPhotoAssets: photoAccessHelper.PhotoAssetParams =
   phAccessHelper.batchGetPhotoAssetParams(photoAssets, keyToGet);
  console.info(`batchGetPhotoAssetParams success, the length is ${batchParamOfPhotoAssets.length}`);
}
```

## canPerformDeepOptimizeSpace

```TypeScript
canPerformDeepOptimizeSpace(): Promise<boolean>
```

Whether deep storage space optimization can be performed.

**Since:** 26.0.0

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-canPerformDeepOptimizeSpace(): Promise<boolean>--><!--Device-PhotoAccessHelper-canPerformDeepOptimizeSpace(): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let canPerform: boolean = await phAccessHelper.canPerformDeepOptimizeSpace();
    console.info(`canPerformDeepOptimizeSpace result: ${canPerform}`);
  } catch (err) {
    console.error(`canPerformDeepOptimizeSpace failed with error: ${err.code}, ${err.message}`);
  }
}
```

## cancelAnalysisTool

```TypeScript
cancelAnalysisTool(config: ToolCancelConfig): Promise<void>
```

Cancels the execution of an intelligent analysis tool.

**Since:** 26.1.0

**Required permissions:** ohos.permission.CONTROL_IMAGEVIDEO_ANALYSIS

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-cancelAnalysisTool(config: ToolCancelConfig): Promise<void>--><!--Device-PhotoAccessHelper-cancelAnalysisTool(config: ToolCancelConfig): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ToolCancelConfig](arkts-medialibrary-photoaccesshelper-toolcancelconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## cancelPhotoUriPermission

```TypeScript
cancelPhotoUriPermission(tokenId: number, uri: string, photoPermissionType: PhotoPermissionType): Promise<number>
```

Cancels the permission for accessing a URI from an application. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-cancelPhotoUriPermission(tokenId: long, uri: string, photoPermissionType: PhotoPermissionType): Promise<int>--><!--Device-PhotoAccessHelper-cancelPhotoUriPermission(tokenId: long, uri: string, photoPermissionType: PhotoPermissionType): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number | Yes |
| uri | string | Yes |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('cancelPhotoUriPermissionDemo');

  try {
    let tokenId = 502334412;
    let result = await phAccessHelper.cancelPhotoUriPermission(tokenId,
        'file://media/Photo/11/IMG_datetime_0001/displayName.jpg',
        photoAccessHelper.PhotoPermissionType.TEMPORARY_READ_IMAGEVIDEO);

    console.info('cancelPhotoUriPermission success, result=' + result);
  } catch (err) {
    console.error('cancelPhotoUriPermission failed, error=' + err);
  }
}
```

## cloneAssetsByPath

```TypeScript
cloneAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>
```

clone assets of filemanager to Album.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-cloneAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>--><!--Device-PhotoAccessHelper-cloneAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | string[] | Yes |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let assets: Array<string> = ['/Docs/Download/test.jpg'];
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let target: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let clonedUris: Array<string> = await phAccessHelper.cloneAssetsByPath(assets, target);
    console.info(`cloneAssetsByPath success, count: ${clonedUris.length}`);
  } catch (err) {
    console.error(`cloneAssetsByPath failed with error: ${err.code}, ${err.message}`);
  }
}
```

## cloneToAlbum

```TypeScript
cloneToAlbum(assets: PhotoAsset[], target: Album,option?: BatchOperationOptions): Promise<PhotoAsset[]>
```

clone assets to Album.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-cloneToAlbum(assets: PhotoAsset[], target: Album,option?: BatchOperationOptions): Promise<PhotoAsset[]>--><!--Device-PhotoAccessHelper-cloneToAlbum(assets: PhotoAsset[], target: Album,option?: BatchOperationOptions): Promise<PhotoAsset[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | [PhotoAsset[]](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | Yes |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoAsset[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let assetFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let assets: Array<photoAccessHelper.PhotoAsset> = await assetFetchResult.getAllObjects();
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let target: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let options: photoAccessHelper.BatchOperationOptions = {
      mode: 0
    };
    let clonedAssets: Array<photoAccessHelper.PhotoAsset> = await phAccessHelper.cloneToAlbum(assets, target, options);
    console.info(`cloneToAlbum success, count: ${clonedAssets.length}`);
  } catch (err) {
    console.error(`cloneToAlbum failed with error: ${err.code}, ${err.message}`);
  }
}
```

## cloneToDir

```TypeScript
cloneToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>
```

clone assets of medialibrary sandbox to directory of filemanager.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-cloneToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>--><!--Device-PhotoAccessHelper-cloneToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | string[] | Yes |
| target | string | Yes |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let assetFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let assets: Array<photoAccessHelper.PhotoAsset> = await assetFetchResult.getAllObjects();
    let assetUris: Array<string> = assets.map((item) => item.uri);
    let target: string = '/Docs/Download';
    let clonedPaths: Array<string> = await phAccessHelper.cloneToDir(assetUris, target);
    console.info(`cloneToDir success, count: ${clonedPaths.length}`);
  } catch (err) {
    console.error(`cloneToDir failed with error: ${err.code}, ${err.message}`);
  }
}
```

## convertAssetToCompatibleAsset

```TypeScript
convertAssetToCompatibleAsset(assets: Array<PhotoAsset>): Promise<Array<PhotoAsset>>
```

Convert Asset Attributes to Compatibility Attributes

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-convertAssetToCompatibleAsset(assets: Array<PhotoAsset>): Promise<Array<PhotoAsset>>--><!--Device-PhotoAccessHelper-convertAssetToCompatibleAsset(assets: Array<PhotoAsset>): Promise<Array<PhotoAsset>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;PhotoAsset & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## convertToAsset

```TypeScript
convertToAsset(path: string): Promise<PhotoAsset>
```

Convert to PhotoAsset from path of filemanagerr.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-convertToAsset(path: string): Promise<PhotoAsset>--><!--Device-PhotoAccessHelper-convertToAsset(path: string): Promise<PhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoAsset & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let path: string = '/Docs/Download/test.jpg';
    let photoAsset: photoAccessHelper.PhotoAsset = await phAccessHelper.convertToAsset(path);
    console.info(`convertToAsset success, asset uri: ${photoAsset.uri}`);
  } catch (err) {
    console.error(`convertToAsset failed with error: ${err.code}, ${err.message}`);
  }
}
```

## createAlbum

```TypeScript
createAlbum(name: string, callback: AsyncCallback<Album>): void
```

Creates an album. This API uses an asynchronous callback to return the result.

The album name must meet the following requirements:

- The total length of the album name must be between 1 and 255 characters.  
- It must not contain any invalid characters, which are:

. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [createAlbumRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createAlbumRequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAlbum(name: string, callback: AsyncCallback<Album>): void--><!--Device-PhotoAccessHelper-createAlbum(name: string, callback: AsyncCallback<Album>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Album&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900015 |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAlbumDemo');
  let albumName: string = 'newAlbumName' + new Date().getTime();
  phAccessHelper.createAlbum(albumName, (err, album) => {
    if (err) {
      console.error(`createAlbumCallback failed with err: ${err.code}, ${err.message}`);
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

- The total length of the album name must be between 1 and 255 characters.  
- It must not contain any invalid characters, which are:

. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

- Duplicate album names are not allowed.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [createAlbumRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createAlbumRequest)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAlbum(name: string): Promise<Album>--><!--Device-PhotoAccessHelper-createAlbum(name: string): Promise<Album>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Album & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900015 |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAlbumDemo');
  let albumName: string = 'newAlbumName' + new Date().getTime();
  phAccessHelper.createAlbum(albumName).then((album) => {
    console.info('createAlbumPromise successfully, album: ' + album.albumName + ' album uri: ' + album.albumUri);
  }).catch((err: BusinessError) => {
    console.error(`createAlbumPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

## createAsset

```TypeScript
createAsset(displayName: string, callback: AsyncCallback<PhotoAsset>): void
```

Creates an image or video asset with the specified file name. This API uses an asynchronous callback to return the result.

The file name must meet the following requirements:

- A valid file name must include a base name and a supported image or video extension.  
- The total length of the file name must be between 1 and 255 characters.  
- The base name must not contain any invalid characters.

Starting from API version 18, the following characters are considered invalid: \ / : * ? " &lt; &gt; | 

For API versions 10 to 17, the following characters are considered invalid: . .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string, callback: AsyncCallback<PhotoAsset>): void--><!--Device-PhotoAccessHelper-createAsset(displayName: string, callback: AsyncCallback<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let testFileName: string = 'testFile' + Date.now() + '.jpg';
  phAccessHelper.createAsset(testFileName, (err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('createAsset file displayName' + photoAsset.displayName);
      console.info('createAsset successfully');
    } else {
      console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
    }
  });
}
```

## createAsset

```TypeScript
createAsset(displayName: string): Promise<PhotoAsset>
```

Creates an image or video asset with the specified file name. This API uses a promise to return the result.

The file name must meet the following requirements:

- A valid file name must include a base name and a supported image or video extension.  
- The total length of the file name must be between 1 and 255 characters.  
- The base name must not contain any invalid characters.

Starting from API version 18, the following characters are considered invalid: \ / : * ? " &lt; &gt; | 

For API versions 10 to 17, the following characters are considered invalid: . .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string): Promise<PhotoAsset>--><!--Device-PhotoAccessHelper-createAsset(displayName: string): Promise<PhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoAsset & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let photoAsset: photoAccessHelper.PhotoAsset = await phAccessHelper.createAsset(testFileName);
    console.info('createAsset file displayName' + photoAsset.displayName);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
}
```

## createAsset

```TypeScript
createAsset(displayName: string, options: PhotoCreateOptions): Promise<PhotoAsset>
```

Creates an image or video asset with the specified file name and options. This API uses a promise to return the result.

The file name must meet the following requirements:

- A valid file name must include a base name and a supported image or video extension.  
- The total length of the file name must be between 1 and 255 characters.  
- The base name must not contain any invalid characters.

Starting from API version 18, the following characters are considered invalid: \ / : * ? " &lt; &gt; | 

For API versions 10 to 17, the following characters are considered invalid: . .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string, options: PhotoCreateOptions): Promise<PhotoAsset>--><!--Device-PhotoAccessHelper-createAsset(displayName: string, options: PhotoCreateOptions): Promise<PhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| options | [PhotoCreateOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-userfilemanager-photocreateoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoAsset & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let testFileName:string = 'testFile' + Date.now() + '.jpg';
    let createOption: photoAccessHelper.PhotoCreateOptions = {
      subtype: photoAccessHelper.PhotoSubtype.DEFAULT
    }
    let photoAsset: photoAccessHelper.PhotoAsset = await phAccessHelper.createAsset(testFileName, createOption);
    console.info('createAsset file displayName' + photoAsset.displayName);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
}
```

## createAsset

```TypeScript
createAsset(displayName: string, options: PhotoCreateOptions, callback: AsyncCallback<PhotoAsset>): void
```

Creates an image or video asset with the specified file name and options. This API uses an asynchronous callback to return the result.

The file name must meet the following requirements:

- A valid file name must include a base name and a supported image or video extension.  
- The total length of the file name must be between 1 and 255 characters.  
- The base name must not contain any invalid characters.

Starting from API version 18, the following characters are considered invalid: \ / : * ? " &lt; &gt; | 

For API versions 10 to 17, the following characters are considered invalid: . .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**Since:** 10

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string, options: PhotoCreateOptions, callback: AsyncCallback<PhotoAsset>): void--><!--Device-PhotoAccessHelper-createAsset(displayName: string, options: PhotoCreateOptions, callback: AsyncCallback<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayName | string | Yes |
| options | [PhotoCreateOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-userfilemanager-photocreateoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000001 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let testFileName: string = 'testFile' + Date.now() + '.jpg';
  let createOption: photoAccessHelper.PhotoCreateOptions = {
    subtype: photoAccessHelper.PhotoSubtype.DEFAULT
  }
  phAccessHelper.createAsset(testFileName, createOption, (err, photoAsset) => {
    if (photoAsset !== undefined) {
      console.info('createAsset file displayName' + photoAsset.displayName);
      console.info('createAsset successfully');
    } else {
      console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
    }
  });
}
```

## createAssetsForApp

```TypeScript
createAssetsForApp(bundleName: string, appName: string, tokenId: number, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

Creates media assets for an application with the specified token ID. The returned URIs have been granted with the permission for writing the media assets (images or videos).

**Since:** 19

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAssetsForApp(bundleName: string, appName: string, tokenId: long, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-createAssetsForApp(bundleName: string, appName: string, tokenId: long, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appName | string | Yes |
| tokenId | number | Yes |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetsForAppDemo.');

  try {
    let bundleName: string = 'testBundleName';
    let appName: string = 'testAppName';
    let tokenId: number = 537197950;
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
      {
        title: 'test',
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      }
    ];
    let desFileUris: Array<string> = await phAccessHelper.createAssetsForApp(bundleName, appName, tokenId, photoCreationConfigs);
    console.info('createAssetsForApp success, data is ' + desFileUris);
  } catch (err) {
    console.error(`createAssetsForApp failed with error: ${err.code}, ${err.message}`);
  }
}
```

## createAssetsForAppWithAlbum

```TypeScript
createAssetsForAppWithAlbum(source: PhotoCreationSource, albumUri: string, isAuthorized: boolean,
      photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

Creates assets for the current application or other applications in the specified source or user album. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAssetsForAppWithAlbum(source: PhotoCreationSource, albumUri: string, isAuthorized: boolean,      photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-createAssetsForAppWithAlbum(source: PhotoCreationSource, albumUri: string, isAuthorized: boolean,      photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [PhotoCreationSource](arkts-medialibrary-photoaccesshelper-photocreationsource-i-sys.md) | Yes |
| albumUri | string | Yes |
| isAuthorized | boolean | Yes |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetsForAppWithAlbumDemo.');

  try {
    let source: photoAccessHelper.PhotoCreationSource = {
      bundleName: 'testBundleName',
      appName: 'testAppName',
      appId: 'testAppId',
      tokenId: 537197950,
    }
    let albumUri: string = 'file://media/PhotoAlbum/10';
    let isAuthorized: boolean = true;
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
      {
        title: 'test',
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      }
    ];
    let desFileUris: Array<string> = await phAccessHelper.createAssetsForAppWithAlbum(source, albumUri, isAuthorized, photoCreationConfigs);
    console.info('createAssetsForAppWithAlbum success, data is ' + desFileUris);
  } catch (err) {
    console.error(`createAssetsForAppWithAlbum failed with error: ${err.code}, ${err.message}`);
  }
}
```

## createAssetsForAppWithMode

```TypeScript
createAssetsForAppWithMode(
      bundleName: string,
      appName: string,
      appId: string,
      tokenId: number,
      authorizationMode: AuthorizationMode,
      photoCreationConfigs: Array<PhotoCreationConfig>
    ): Promise<Array<string>>
```

Creates assets with a temporary permission. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAssetsForAppWithMode(      bundleName: string,      appName: string,      appId: string,      tokenId: long,      authorizationMode: AuthorizationMode,      photoCreationConfigs: Array<PhotoCreationConfig>    ): Promise<Array<string>>--><!--Device-PhotoAccessHelper-createAssetsForAppWithMode(      bundleName: string,      appName: string,      appId: string,      tokenId: long,      authorizationMode: AuthorizationMode,      photoCreationConfigs: Array<PhotoCreationConfig>    ): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appName | string | Yes |
| appId | string | Yes |
| tokenId | number | Yes |
| authorizationMode | [AuthorizationMode](arkts-medialibrary-photoaccesshelper-authorizationmode-e-sys.md) | Yes |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetsForAppWithModeDemo.');

  try {
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
      {
        title: '123456',
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      }
    ];
    let bundleName: string = 'testBundleName';
    let appName: string = 'testAppName';
    let appId: string = 'testAppId';
    let tokenId: number = 537197950;
    let authorizationMode: photoAccessHelper.AuthorizationMode = photoAccessHelper.AuthorizationMode.SHORT_TIME_AUTHORIZATION;
    let result: Array<string> = await phAccessHelper.createAssetsForAppWithMode(bundleName, appName, appId, tokenId, authorizationMode, photoCreationConfigs);
    console.info(`result: ${JSON.stringify(result)}`);
    console.info('Photo createAssetsForAppWithMode success.');
  } catch (err) {
    console.error(`createAssetsForAppWithMode failed with error: ${err.code}, ${err.message}`);
  }
}
```

## createAssetsWithAlbum

```TypeScript
createAssetsWithAlbum(
      creationSettings: CreationSetting[],
      isRealTimeThumb: boolean,
      albumUri?: string): Promise<string[]>
```

Batch create assets,which also support to choose whether specifying an album and whether generating thumbnails in real time.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-createAssetsWithAlbum(      creationSettings: CreationSetting[],      isRealTimeThumb: boolean,      albumUri?: string): Promise<string[]>--><!--Device-PhotoAccessHelper-createAssetsWithAlbum(      creationSettings: CreationSetting[],      isRealTimeThumb: boolean,      albumUri?: string): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| creationSettings | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md)[] | Yes |
| isRealTimeThumb | boolean | Yes |
| albumUri | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    // Construct creation parameters.
    let creationSettings: Array<photoAccessHelper.CreationSetting> = [
      {
        title: 'test',
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE
      }
    ];
    // Do not generate a thumbnail in real time when an asset is created.
    let isRealTimeThumb: boolean = false;
    // Specify the album URI.
    let albumUri: string = 'file://media/PhotoAlbum/10';
    // Call the API to create an asset.
    let result: Array<string> = await phAccessHelper.createAssetsWithAlbum(
      creationSettings,
      isRealTimeThumb,
      albumUri
    );
    console.info('Succeeded in creating assets with album, uri is ' + result);
  } catch (err) {
    console.error(`createAssetsWithAlbum failed with error: ${err.code}, ${err.message}`);
  }
}
```

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void
```

Deletes user albums. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [deleteAlbums](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deleteAlbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // Delete the album named newAlbumName.
  console.info('deleteAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
  let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
  phAccessHelper.deleteAlbums([album], (err) => {
    if (err) {
      console.error(`deletePhotoAlbumsCallback failed with err: ${err.code}, ${err.message}`);
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

**Deprecated since:** 11

**Substitutes:** [deleteAlbums](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deleteAlbums)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-deleteAlbums(albums: Array<Album>): Promise<void>--><!--Device-PhotoAccessHelper-deleteAlbums(albums: Array<Album>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // Delete the album named newAlbumName.
  console.info('deleteAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
  let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
  phAccessHelper.deleteAlbums([album]).then(() => {
    console.info('deletePhotoAlbumsPromise successfully');
    }).catch((err: BusinessError) => {
      console.error(`deletePhotoAlbumsPromise failed with err: ${err.code}, ${err.message}`);
  });
  fetchResult.close();
}
```

## deleteAssets

```TypeScript
deleteAssets(uriList: Array<string>, callback: AsyncCallback<void>): void
```

Deletes media assets. The deleted assets are moved to the trash. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteAssets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-deleteAssets(uriList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-deleteAssets(uriList: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000002 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('deleteAssetDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    phAccessHelper.deleteAssets([asset.uri], (err) => {
      if (err === undefined) {
        console.info('deleteAssets successfully');
      } else {
        console.error(`deleteAssets failed with error: ${err.code}, ${err.message}`);
      }
    });
  } catch (err) {
    console.error(`fetch failed, error: ${err.code}, ${err.message}`);
  }
}
```

## deleteAssets

```TypeScript
deleteAssets(uriList: Array<string>): Promise<void>
```

Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteAssets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-deleteAssets(uriList: Array<string>): Promise<void>--><!--Device-PhotoAccessHelper-deleteAssets(uriList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 14000002 |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('deleteDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    await phAccessHelper.deleteAssets([asset.uri]);
    console.info('deleteAssets successfully');
  } catch (err) {
    console.error(`deleteAssets failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getAlbumIdByBundleName

```TypeScript
getAlbumIdByBundleName(bundleName: string): Promise<number>
```

Get the corresponding albumId of a bundleName.

**Since:** 22

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getAlbumIdByBundleName(bundleName: string): Promise<int>--><!--Device-PhotoAccessHelper-getAlbumIdByBundleName(bundleName: string): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAlbumIdByBundleName');

  try {
      let albumId: number = await phAccessHelper.getAlbumIdByBundleName('test.bundleName');
      console.info('requestFile:: albumId: ', albumId);

      console.info('getAlbumIdByBundleName completed.');
      console.info(`albumId : ${albumId}`);
    } catch (err) {
      console.error(`getAlbumIdByBundleName failed: ${err.code}, ${err.message}`);
    }
}
```

## getAlbumsByIds

```TypeScript
getAlbumsByIds(albumIds: Array<number>): Promise<Map<number, Album>>
```

Obtains album information by album IDs. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbumsByIds(albumIds: Array<int>): Promise<Map<int, Album>>--><!--Device-PhotoAccessHelper-getAlbumsByIds(albumIds: Array<int>): Promise<Map<int, Album>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| albumIds | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;number, Album & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('startGetAlbumsByIdsDemo');

  try {
    // Obtain the sandbox URIs of the images or videos to be saved to the media library.
    let albumIds: Array<number> = [
      12 //Use the actual album ID.
    ];
    let map: Map<number, photoAccessHelper.Album> = await phAccessHelper.getAlbumsByIds(albumIds);
    console.info('getAlbumsByIds success, size is ' + map.size);
  } catch (err) {
    console.error('getAlbumsByIds failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
}
```

## getAssetCompatibleCapability

```TypeScript
getAssetCompatibleCapability(bundleName: string): Promise<AssetCompatibleCapability>
```

Obtains the asset compatibility capability based on the bundle name. When an application obtains a file, it can determine whether compatibility conversion is required.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getAssetCompatibleCapability(bundleName: string): Promise<AssetCompatibleCapability>--><!--Device-PhotoAccessHelper-getAssetCompatibleCapability(bundleName: string): Promise<AssetCompatibleCapability>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let bundleName = "com.test.example";
    let capability : photoAccessHelper.AssetCompatibleCapability = await phAccessHelper.getAssetCompatibleCapability(bundleName);
  } catch (error) {
    console.error('failed to getAssetCompatibleCapability err', error);
  }
}
```

## getAssetCompatibleUris

```TypeScript
getAssetCompatibleUris(bundleName: string, assets: Array<PhotoAsset>, compatibleFlag?: number): Promise<Array<string>>
```

Obtain the URI list to be transcoded based on bundleName, photoAsset list, and compatibleFlag.compatibleFlags description. Bit 0 indicates a large image, and bit 1 indicates a Heif image.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getAssetCompatibleUris(bundleName: string, assets: Array<PhotoAsset>, compatibleFlag?: int): Promise<Array<string>>--><!--Device-PhotoAccessHelper-getAssetCompatibleUris(bundleName: string, assets: Array<PhotoAsset>, compatibleFlag?: int): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| assets | Array & lt;PhotoAsset & gt; | Yes |
| compatibleFlag | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let bundleName: string = 'com.example.helloWorld';
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.URI, photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let assets: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
    // compatibleFlag: Bit 0 indicates the full image, and bit 1 indicates the HEIF image.
    let compatibleFlag: number = 0;
    let uris: Array<string> = await phAccessHelper.getAssetCompatibleUris(bundleName, assets, compatibleFlag);
    console.info(`getAssetCompatibleUris success, uri count: ${uris.length}`);
  } catch (err) {
    console.error(`getAssetCompatibleUris failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getClonedAlbumUris

```TypeScript
getClonedAlbumUris(oldUris: Array<string>): Promise<Map<string, string>>
```

Obtains the current URIs of cloned albums. This API uses a promise to return the result.

To control the size of the database table space, the system automatically deletes the previously stored clone data during each clone operation. As a result, this API only keeps the mapping between the user's new and old device URIs from the latest clone operation.

**Since:** 22

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getClonedAlbumUris(oldUris: Array<string>): Promise<Map<string, string>>--><!--Device-PhotoAccessHelper-getClonedAlbumUris(oldUris: Array<string>): Promise<Map<string, string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldUris | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
    console.info('getClonedAlbumUrisDemo');
    // The following is an array of URIs of media files.
    let uris: Array<string> = [
        'file://media/PhotoAlbum/1',
        'file://media/PhotoAlbum/2',
        'file://media/AnalysisAlbum/3'
    ];
    try {
        let albums: Map<string, string> = await phAccessHelper.getClonedAlbumUris(uris);
        console.info(`Albums: ${albums}`);
    } catch (error) {
        console.error(`Error thrown: ${error}`);
    }
}
```

## getClonedAssetUris

```TypeScript
getClonedAssetUris(oldUris: Array<string>): Promise<Map<string, string>>
```

Obtains the current URIs of cloned assets. This API uses a promise to return the result.

To control the size of the database table space, the system automatically deletes the previously stored clone data during each clone operation. As a result, this API only keeps the mapping between the user's new and old device URIs from the latest clone operation.

**Since:** 22

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getClonedAssetUris(oldUris: Array<string>): Promise<Map<string, string>>--><!--Device-PhotoAccessHelper-getClonedAssetUris(oldUris: Array<string>): Promise<Map<string, string>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldUris | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
    console.info('getClonedAssetUrisDemo');
    // The following is an array of URIs of media files.
    let uris: Array<string> = [
        'file://media/Photo/1/IMG_datetime_0001/displayName1.jpg',
        'file://media/Photo/2/IMG_datetime_0002/displayName2.jpg',
        'file://media/Photo/3/IMG_datetime_0003/displayName3.jpg'
    ];
    try {
        let assets: Map<string, string> = await phAccessHelper.getClonedAssetUris(uris);
        console.info(`Assets: ${assets}`);
    } catch (error) {
        console.error(`Error thrown: ${error}`);
    }
}
```

## getDataAnalysisProgress

```TypeScript
getDataAnalysisProgress(analysisType?: AnalysisType): Promise<string>
```

Obtains the asset analysis progress. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getDataAnalysisProgress(analysisType?: AnalysisType): Promise<string>--><!--Device-PhotoAccessHelper-getDataAnalysisProgress(analysisType?: AnalysisType): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| analysisType | [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('getDataAnalysisProgress test start');

    let result: string = await phAccessHelper.getDataAnalysisProgress();
    console.info('getDataAnalysisProgress:' + result);

  } catch (err) {
    console.error(`getDataAnalysisProgress failed, error: ${err.code}, ${err.message}`);
  }
}
```

## getDeepOptimizeSpace

```TypeScript
getDeepOptimizeSpace(): Promise<number>
```

Obtains the size of the deep storage space.&lt;br&gt;Unit:Byte{s}.

This API is time-consuming. Before using this API, you are advised to call [canPerformDeepOptimizeSpace()](#canPerformDeepOptimizeSpace) and call this API only when true is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getDeepOptimizeSpace(): Promise<long>--><!--Device-PhotoAccessHelper-getDeepOptimizeSpace(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let canPerform: boolean = await phAccessHelper.canPerformDeepOptimizeSpace();
    if (canPerform) {
      let size: number = await phAccessHelper.getDeepOptimizeSpace();
      console.info(`getDeepOptimizeSpace result: ${size}`);
    }
  } catch (err) {
    console.error(`getDeepOptimizeSpace failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains hidden albums based on the specified display mode and retrieval options. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

// Obtain the album newAlbumName that contains hidden files.
async function getHiddenAlbumsView(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getHiddenAlbumsViewDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getHiddenAlbums(photoAccessHelper.HiddenPhotosDisplayMode.ALBUMS_MODE, fetchOptions,
    async (err, fetchResult) => {
      if (err !== undefined) {
        console.error(`getHiddenAlbumsViewCallback failed with error: ${err.code}, ${err.message}`);
        return;
      }
      if (fetchResult === undefined) {
        console.error('getHiddenAlbumsViewCallback fetchResult is undefined');
        return;
      }
      let album = await fetchResult.getFirstObject();
      if (album === undefined) {
        console.error('getHiddenAlbumsViewCallback album is undefined');
        fetchResult.close();
        return;
      }
      console.info('getHiddenAlbumsViewCallback successfully, album name: ' + album.albumName);
      fetchResult.close();
  });
}
```

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, callback: AsyncCallback<FetchResult<Album>>): void
```

Obtains hidden albums based on the specified display mode. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

// Obtain the preset hidden album.
async function getSysHiddenAlbum(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getSysHiddenAlbumDemo');
  phAccessHelper.getHiddenAlbums(photoAccessHelper.HiddenPhotosDisplayMode.ASSETS_MODE, async (err, fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getSysHiddenAlbumCallback fetchResult is undefined');
      return;
    }
    let hiddenAlbum: photoAccessHelper.Album = await fetchResult.getFirstObject();
    if (hiddenAlbum === undefined) {
      console.error('getSysHiddenAlbumCallback hiddenAlbum is undefined');
      fetchResult.close();
      return;
    }
    console.info('getSysHiddenAlbumCallback successfully, albumUri: ' + hiddenAlbum.albumUri);
    fetchResult.close();
  });
}

// Obtain the hidden albums displayed by album, that is, the albums with hidden files. Such albums do not include the preset hidden album and the albums in the trash.
async function getHiddenAlbumsView(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getHiddenAlbumsViewDemo');
  phAccessHelper.getHiddenAlbums(photoAccessHelper.HiddenPhotosDisplayMode.ALBUMS_MODE, async (err, fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getHiddenAlbumsViewCallback fetchResult is undefined');
      return;
    }
    let albums: Array<photoAccessHelper.Album> = await fetchResult.getAllObjects();
    if (albums === undefined) {
      console.error('getHiddenAlbumsViewCallback albums is undefined');
      fetchResult.close();
      return;
    }
    console.info('getHiddenAlbumsViewCallback successfully, albums size: ' + albums.length);

    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    for (let i = 0; i < albums.length; i++) {
      // Obtain hidden files in the album.
      albums[i].getAssets(fetchOption, (err, assetFetchResult) => {
        if (assetFetchResult === undefined) {
          console.error('getHiddenAlbumsViewCallback assetFetchResult is undefined');
          return;
        }
        console.info('album get hidden assets successfully, getCount: ' + assetFetchResult.getCount());
      });
    }
    fetchResult.close();
  });
}
```

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, options?: FetchOptions): Promise<FetchResult<Album>>
```

Obtains hidden albums based on the specified display mode and retrieval options. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, options?: FetchOptions): Promise<FetchResult<Album>>--><!--Device-PhotoAccessHelper-getHiddenAlbums(mode: HiddenPhotosDisplayMode, options?: FetchOptions): Promise<FetchResult<Album>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the preset hidden album.
async function getSysHiddenAlbum(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getSysHiddenAlbumDemo');
  phAccessHelper.getHiddenAlbums(photoAccessHelper.HiddenPhotosDisplayMode.ASSETS_MODE)
    .then( async (fetchResult) => {
      if (fetchResult === undefined) {
        console.error('getSysHiddenAlbumPromise fetchResult is undefined');
        return;
      }
      let hiddenAlbum: photoAccessHelper.Album = await fetchResult.getFirstObject();
      console.info('getAlbumsPromise successfully, albumUri: ' + hiddenAlbum.albumUri);
      fetchResult.close();
    }).catch((err: BusinessError) => {
      console.error(`getSysHiddenAlbumPromise failed with err: ${err.code}, ${err.message}`);
    });
}

// Obtain the hidden albums displayed by album, that is, the albums with hidden files. Such albums do not include the preset hidden album and the albums in the trash.
async function getHiddenAlbumsView(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getHiddenAlbumsViewDemo');
  phAccessHelper.getHiddenAlbums(photoAccessHelper.HiddenPhotosDisplayMode.ALBUMS_MODE).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getHiddenAlbumsViewPromise fetchResult is undefined');
      return;
    }
    let albums: Array<photoAccessHelper.Album> = await fetchResult.getAllObjects();
    console.info('getHiddenAlbumsViewPromise successfully, albums size: ' + albums.length);

    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    for (let i = 0; i < albums.length; i++) {
      // Obtain hidden files in the album.
      albums[i].getAssets(fetchOption).then((assetFetchResult) => {
        console.info('album get hidden assets successfully, getCount: ' + assetFetchResult.getCount());
      }).catch((err: BusinessError) => {
        console.error(`album get hidden assets failed with error: ${err.code}, ${err.message}`);
      });
    }
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getHiddenAlbumsViewPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

## getIndexConstructProgress

```TypeScript
getIndexConstructProgress(): Promise<string>
```

Obtains the index construction progress. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getIndexConstructProgress(): Promise<string>--><!--Device-PhotoAccessHelper-getIndexConstructProgress(): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {

  class indexProgress {
    finishedImageCount: number = 0;
    totalImageCount: number = 0;
    finishedVideoCount: number = 0;
    totalVideoCount: number = 0;
  }

  try {
    console.info('getIndexConstructProgress test start');
    let result: string = await phAccessHelper.getIndexConstructProgress();
    console.info('getIndexProgress:' + result);

    let jsonObj: indexProgress = JSON.parse(result);
    //...Use the obtained index construction progress data.
  } catch (err) {
    console.error(`getIndexConstructProgress failed, error: ${err.code}, ${err.message}`);
  }
}
```

## getPhotoAlbumOrder

```TypeScript
getPhotoAlbumOrder(orderStyle: number, options?: FetchOptions): Promise<FetchResult<AlbumOrder>>
```

Obtains the sorting order for system, user, and source albums. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getPhotoAlbumOrder(orderStyle: int, options?: FetchOptions): Promise<FetchResult<AlbumOrder>>--><!--Device-PhotoAccessHelper-getPhotoAlbumOrder(orderStyle: int, options?: FetchOptions): Promise<FetchResult<AlbumOrder>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orderStyle | number | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FetchResult&lt;[AlbumOrder](arkts-medialibrary-photoaccesshelper-albumorder-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getPhotoAlbumOrderDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let orderStyle: number = 0;
  phAccessHelper.getPhotoAlbumOrder(orderStyle, fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getPhotoAlbumOrderPromise fetchResult is undefined');
      return;
    }
    let albumOrders: photoAccessHelper.AlbumOrder[] = await fetchResult.getAllObjects();
    console.info(`getPhotoAlbumOrderPromise successfully, albumOrders length: ${albumOrders.length}`);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getPhotoAlbumOrderPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options?: FetchOptions): Promise<FetchResult<Album>>
```

Obtains system, user, and source albums based on the specified options. This API uses a promise to return the result.

Before the operation, ensure that the albums to obtain exist.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getPhotoAlbums(options?: FetchOptions): Promise<FetchResult<Album>>--><!--Device-PhotoAccessHelper-getPhotoAlbums(options?: FetchOptions): Promise<FetchResult<Album>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getPhotoAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getPhotoAlbums(fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getPhotoAlbumsPromise fetchResult is undefined');
      return;
    }
    let albums: photoAccessHelper.Album[] = await fetchResult.getAllObjects();
    console.info(`getPhotoAlbumsPromise successfully, albums length: ${albums.length}`);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getPhotoAlbumsPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

## getPhotoAssets

```TypeScript
getPhotoAssets(assetsData: ValuesBucket[]): Promise<PhotoAsset[]>
```

Converts the **ValuesBucket** record to a **PhotoAsset** object.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getPhotoAssets(assetsData: ValuesBucket[]): Promise<PhotoAsset[]>--><!--Device-PhotoAccessHelper-getPhotoAssets(assetsData: ValuesBucket[]): Promise<PhotoAsset[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetsData | [ValuesBucket[]](../../apis-arkdata/arkts-apis/arkts-arkdata-rdb-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoAsset[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getPhotoAssets demo');
  let valuesArr: photoAccessHelper.ValuesBucket[] = [];
  let resultSet: photoAccessHelper.ResultSet | undefined = undefined;
  let photoAssetArr: photoAccessHelper.PhotoAsset[] = [];
  let QUERY_SQL = 'SELECT file_id,data,display_name,media_type,subtype from Photos limit 100';
  try {
    resultSet = await phAccessHelper.query(QUERY_SQL);
    let index: number = 0;
    while(resultSet && index < resultSet.rowCount){
      resultSet.goToRow(index);
      valuesArr.push(resultSet.getRow());
      index++;
    }
    photoAssetArr = await phAccessHelper.getPhotoAssets(valuesArr);
    console.info('getPhotoAssets successfully');
  } catch (err) {
    console.error(`valuesArr failed: ${err.code}, ${err.message}`);
  }
}
```

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void
```

Obtains the index of an image or video in an album. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<int>): void--><!--Device-PhotoAccessHelper-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoUri | string | Yes |
| albumUri | string | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('getPhotoIndexDemo');
    let predicatesForGetAsset: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOp: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicatesForGetAsset
    };
    // Obtain the uri of the album.
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE, fetchOp);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc(photoAccessHelper.PhotoKeys.DATE_MODIFIED);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.DATE_MODIFIED],
      predicates: predicates
    };
    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let expectIndex = 1;
    // Obtain the uri of the second file.
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getObjectByPosition(expectIndex);

    phAccessHelper.getPhotoIndex(photoAsset.uri, album.albumUri, fetchOptions, (err, index) => {
      if (err === undefined) {
        console.info(`getPhotoIndex successfully and index is : ${index}`);
      } else {
        console.error(`getPhotoIndex failed; error: ${err.code}, ${err.message}`);
      }
    });
  } catch (error) {
    console.error(`getPhotoIndex failed; error: ${error.code}, ${error.message}`);
  }
}
```

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>
```

Obtains the index of an image or video in an album. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<int>--><!--Device-PhotoAccessHelper-getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| photoUri | string | Yes |
| albumUri | string | Yes |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900012 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('getPhotoIndexDemo');
    let predicatesForGetAsset: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOp: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicatesForGetAsset
    };
    // Obtain the uri of the album.
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE, fetchOp);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.orderByAsc(photoAccessHelper.PhotoKeys.DATE_MODIFIED);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.DATE_MODIFIED],
      predicates: predicates
    };
    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let expectIndex = 1;
    // Obtain the uri of the second file.
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getObjectByPosition(expectIndex);
    phAccessHelper.getPhotoIndex(photoAsset.uri, album.albumUri, fetchOptions).then((index) => {
      console.info(`getPhotoIndex successfully and index is : ${index}`);
    }).catch((err: BusinessError) => {
      console.error(`getPhotoIndex failed; error: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    console.error(`getPhotoIndex failed; error: ${error.code}, ${error.message}`);
  }
}
```

## getPreferredCompatibleMode

```TypeScript
getPreferredCompatibleMode(bundleName: string): Promise<PreferredCompatibleMode>
```

Obtains the preferred compatible mode configured by the application based on bundleName.There are three types of applications. For details, see PreferredCompatibleMode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-getPreferredCompatibleMode(bundleName: string): Promise<PreferredCompatibleMode>--><!--Device-PhotoAccessHelper-getPreferredCompatibleMode(bundleName: string): Promise<PreferredCompatibleMode>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PreferredCompatibleMode](arkts-medialibrary-photoaccesshelper-preferredcompatiblemode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function getPreferredCompatibleMode(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper,
  bundleName: string
): Promise<photoAccessHelper.PreferredCompatibleMode> {
  console.info('getPreferredCompatibleModeDemo');
  let mode: photoAccessHelper.PreferredCompatibleMode = photoAccessHelper.PreferredCompatibleMode.DEFAULT;
  await phAccessHelper.getPreferredCompatibleMode(bundleName)
    .then((result: photoAccessHelper.PreferredCompatibleMode) => {
      mode = result;
      console.info('getPreferredCompatibleMode successfully');
    })
    .catch((err: BusinessError) => {
      console.error(`The getPreferredCompatibleMode call failed. error: ${err.code}, ${err.message}`);
    });
  return mode;
}
```

## getSharedPhotoAssets

```TypeScript
getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>
```

Obtains the shared photo assets.

**Since:** 13

**Required permissions:** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

<!--Device-PhotoAccessHelper-getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>--><!--Device-PhotoAccessHelper-getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;SharedPhotoAsset & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

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

## grantPhotoUriPermission

```TypeScript
grantPhotoUriPermission(
      tokenId: number,
      uri: string,
      photoPermissionType: PhotoPermissionType,
      hideSensitiveType: HideSensitiveType
    ): Promise<number>
```

Grants an application the permission to access a URI. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-grantPhotoUriPermission(      tokenId: long,      uri: string,      photoPermissionType: PhotoPermissionType,      hideSensitiveType: HideSensitiveType    ): Promise<int>--><!--Device-PhotoAccessHelper-grantPhotoUriPermission(      tokenId: long,      uri: string,      photoPermissionType: PhotoPermissionType,      hideSensitiveType: HideSensitiveType    ): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number | Yes |
| uri | string | Yes |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | Yes |
| hideSensitiveType | [HideSensitiveType](arkts-medialibrary-photoaccesshelper-hidesensitivetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('grantPhotoUriPermissionDemo');

  try {
    let tokenId = 502334412;
    let result = await phAccessHelper.grantPhotoUriPermission(tokenId,
        'file://media/Photo/1/IMG_datetime_0001/displayName.jpg',
        photoAccessHelper.PhotoPermissionType.TEMPORARY_READ_IMAGEVIDEO,
        photoAccessHelper.HideSensitiveType.HIDE_LOCATION_AND_SHOOTING_PARAM);

    console.info('grantPhotoUriPermission success, result=' + result);
  } catch (err) {
    console.error('grantPhotoUriPermission failed, error=' + err);
  }
}
```

## grantPhotoUrisPermission

```TypeScript
grantPhotoUrisPermission(
      tokenId: number,
      uriList: Array<string>,
      photoPermissionType: PhotoPermissionType,
      hideSensitiveType: HideSensitiveType
    ): Promise<number>
```

Grants an application the permission to access multiple URIs. This API uses a promise to return the result.

**Since:** 19

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-grantPhotoUrisPermission(      tokenId: long,      uriList: Array<string>,      photoPermissionType: PhotoPermissionType,      hideSensitiveType: HideSensitiveType    ): Promise<int>--><!--Device-PhotoAccessHelper-grantPhotoUrisPermission(      tokenId: long,      uriList: Array<string>,      photoPermissionType: PhotoPermissionType,      hideSensitiveType: HideSensitiveType    ): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number | Yes |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | Yes |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | Yes |
| hideSensitiveType | [HideSensitiveType](arkts-medialibrary-photoaccesshelper-hidesensitivetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('grantPhotoUrisPermissionDemo');

  try {
    // URIs of the media assets.
    let uris: Array<string> = [
      'file://media/Photo/11/IMG_datetime_0001/displayName1.jpg',
      'file://media/Photo/22/IMG_datetime_0002/displayName2.jpg'];
    let tokenId = 502334412;
    let result = await phAccessHelper.grantPhotoUrisPermission(tokenId, uris,
        photoAccessHelper.PhotoPermissionType.TEMPORARY_READ_IMAGEVIDEO,
        photoAccessHelper.HideSensitiveType.HIDE_LOCATION_AND_SHOOTING_PARAM);

    console.info('grantPhotoUrisPermission success, result=' + result);
  } catch (err) {
    console.error('grantPhotoUrisPermission failed, error=' + err);
  }
}
```

## invokeAnalysisTool

```TypeScript
invokeAnalysisTool(config: ToolInvokeConfig, callback: Callback<AnalysisToolResult>): Promise<string>
```

Triggers the execution of an analysis tool. This API uses an asynchronous callback to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.CONTROL_IMAGEVIDEO_ANALYSIS

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-invokeAnalysisTool(config: ToolInvokeConfig, callback: Callback<AnalysisToolResult>): Promise<string>--><!--Device-PhotoAccessHelper-invokeAnalysisTool(config: ToolInvokeConfig, callback: Callback<AnalysisToolResult>): Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ToolInvokeConfig](arkts-medialibrary-photoaccesshelper-toolinvokeconfig-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AnalysisToolResult](arkts-medialibrary-photoaccesshelper-analysistoolresult-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## isCompatibleDuplicateSupported

```TypeScript
isCompatibleDuplicateSupported(bundleName: string): Promise<boolean>
```

Checks whether a temporary JPEG copy should be created for an application. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-isCompatibleDuplicateSupported(bundleName: string): Promise<boolean>--><!--Device-PhotoAccessHelper-isCompatibleDuplicateSupported(bundleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('isCompatibleDuplicateSupportedPromiseDemo')
    let isSupport: boolean = await phAccessHelper.isCompatibleDuplicateSupported('com.example.helloworld');
    console.info(`isCompatibleDuplicateSupported: ${isSupport}`);
  } catch (err) {
    console.error(`isCompatibleDuplicateSupportedPromiseDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## isMediaDataReady

```TypeScript
isMediaDataReady(mediaDataKey: string): Promise<boolean>
```

Checks whether the specified media data is ready.

**Since:** 24

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-isMediaDataReady(mediaDataKey: string): Promise<boolean>--><!--Device-PhotoAccessHelper-isMediaDataReady(mediaDataKey: string): Promise<boolean>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaDataKey | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('isMediaDataReady demo');

  try {
    let ready: boolean = await phAccessHelper.isMediaDataReady('date_added_year');
    if (ready) {
      console.info('date_added_year media data is ready.');
    } else {
      console.info('date_added_year media data is not ready.');
    }
  } catch (err) {
    console.error(`isMediaDataReady failed: ${err.code}, ${err.message}`);
  }
}
```

## modifyAlbumDefaultCoverOrder

```TypeScript
modifyAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],
      disableModification: boolean,
      isAsyncRefreshAlbum: boolean): Promise<void>
```

modify the default cover order of album.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-modifyAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],      disableModification: boolean,      isAsyncRefreshAlbum: boolean): Promise<void>--><!--Device-PhotoAccessHelper-modifyAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],      disableModification: boolean,      isAsyncRefreshAlbum: boolean): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coverOrderInfos | [DefaultCoverOrderInfo](arkts-medialibrary-photoaccesshelper-defaultcoverorderinfo-c-sys.md)[] | Yes |
| disableModification | boolean | Yes |
| isAsyncRefreshAlbum | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function modifyAlbumDefaultCoverOrder(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let coverOrderInfos: Array<photoAccessHelper.DefaultCoverOrderInfo> = [];
    let coverOrderInfo: photoAccessHelper.DefaultCoverOrderInfo = {
      albumType: photoAccessHelper.AlbumType.USER,
      albumSubtype: photoAccessHelper.AlbumSubtype.USER_GENERIC,
      lpath: "/Pictures/Users/1",
      orderKey: photoAccessHelper.PhotoKeys.DATE_ADDED,
      orderSubKey: photoAccessHelper.PhotoKeys.DISPLAY_NAME,
      orderType: 1,
    }
    coverOrderInfos.push(coverOrderInfo);
    let disableModification: boolean = false;
    let isAsyncRefreshAlbum: boolean = false;
    await phAccessHelper.modifyAlbumDefaultCoverOrder(coverOrderInfos, disableModification, isAsyncRefreshAlbum);
    console.info(`Succeeded in modifying default cover order of user album 1`);
  } catch (err) {
    console.error(`modifyAlbumDefaultCoverOrder failed with error: ${err.code}, ${err.message}`);
  }
}
```

## modifyHiddenAlbumDefaultCoverOrder

```TypeScript
modifyHiddenAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],
      disableModification: boolean,
      isAsyncRefreshAlbum: boolean): Promise<void>
```

modify the default cover order of hidden album.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-modifyHiddenAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],      disableModification: boolean,      isAsyncRefreshAlbum: boolean): Promise<void>--><!--Device-PhotoAccessHelper-modifyHiddenAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[],      disableModification: boolean,      isAsyncRefreshAlbum: boolean): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coverOrderInfos | [DefaultCoverOrderInfo](arkts-medialibrary-photoaccesshelper-defaultcoverorderinfo-c-sys.md)[] | Yes |
| disableModification | boolean | Yes |
| isAsyncRefreshAlbum | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function modifyHiddenAlbumDefaultCoverOrder(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let coverOrderInfos: Array<photoAccessHelper.DefaultCoverOrderInfo> = [];
    let coverOrderInfo: photoAccessHelper.DefaultCoverOrderInfo = {
      albumType: photoAccessHelper.AlbumType.SYSTEM,
      albumSubtype: photoAccessHelper.AlbumSubtype.HIDDEN,
      orderKey: photoAccessHelper.PhotoKeys.DATE_ADDED,
      orderSubKey: photoAccessHelper.PhotoKeys.DISPLAY_NAME,
      orderType: 1,
    }
    coverOrderInfos.push(coverOrderInfo);
    let disableModification: boolean = false;
    let isAsyncRefreshAlbum: boolean = false;
    await phAccessHelper.modifyHiddenAlbumDefaultCoverOrder(coverOrderInfos, disableModification, isAsyncRefreshAlbum);
    console.info(`Succeeded in modifying default cover order of hidden album`);
  } catch (err) {
    console.error(`modifyHiddenAlbumDefaultCoverOrder failed with error: ${err.code}, ${err.message}`);
  }
}
```

## moveAssetsByPath

```TypeScript
moveAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>
```

move assets of filemanager to Album.

**Since:** 26.1.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-moveAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>--><!--Device-PhotoAccessHelper-moveAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | string[] | Yes |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let assets: Array<string> = ["/Docs/Download/test.jpg"];
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let target: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let moveUris: Array<string> = await phAccessHelper.moveAssetsByPath(assets, target);
    console.info(`moveAssetsByPath success, count: ${moveUris.length}`);
  } catch (err) {
    console.error(`moveAssetsByPath failed with error: ${err.code}, ${err.message}`);
  }
}
```

## moveAssetsToDir

```TypeScript
moveAssetsToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>
```

move assets of medialibrary sandbox to directory of filemanager.

**Since:** 26.1.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-moveAssetsToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>--><!--Device-PhotoAccessHelper-moveAssetsToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | string[] | Yes |
| target | string | Yes |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let assetFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let assets: Array<photoAccessHelper.PhotoAsset> = await assetFetchResult.getAllObjects();
    let assetUris: Array<string> = assets.map((item) => item.uri);
    let target: string = "/Docs/Download/";
    let movePaths: Array<string> = await phAccessHelper.moveAssetsToDir(assetUris, target);
    console.info(`moveAssetsToDir success, count: ${movePaths.length}`);
  } catch (err) {
    console.error(`moveAssetsToDir failed with error: ${err.code}, ${err.message}`);
  }
}
```

## off('hiddenPhotoChange')

```TypeScript
off(type: 'hiddenPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

Unregisters a listener for the **'hiddenPhotoChange'** event to stop monitoring hidden media asset changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-off(type: 'hiddenPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'hiddenPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hiddenPhotoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('offHiddenPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('hiddenPhotoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('hiddenPhotoChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('hiddenPhotoChange', onCallback1);
  } catch (error) {
    console.error('offHiddenPhotoChange failed, errCode is', error);
  }
}
```

## off('trashedPhotoChange')

```TypeScript
off(type: 'trashedPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

Unregisters a listener for the **'trashedPhotoChange'** event to stop monitoring media asset changes in the trash. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'trashedPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'trashedPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trashedPhotoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('offTrashedPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('trashedPhotoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('trashedPhotoChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('trashedPhotoChange', onCallback1);
  } catch (error) {
    console.error('offTrashedPhotoChangeDemo failed, errCode is', error);
  }
}
```

## off('hiddenAlbumChange')

```TypeScript
off(type: 'hiddenAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

Unregisters a listener for the **'hiddenAlbumChange'** event to stop monitoring hidden album changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-off(type: 'hiddenAlbumChange', callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'hiddenAlbumChange', callback?: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hiddenAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('onHiddenAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('hiddenAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('hiddenAlbumChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('hiddenAlbumChange', onCallback1);
  } catch (error) {
    console.error('onHiddenAlbumChangeDemo failed, errCode is', error);
  }
}
```

## off('trashedAlbumChange')

```TypeScript
off(type: 'trashedAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

Unregisters a listener for the **'trashedAlbumChange'** event to stop monitoring album changes in the trash. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'trashedAlbumChange', callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'trashedAlbumChange', callback?: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trashedAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onTrashedAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('trashedAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('trashedAlbumChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('trashedAlbumChange', onCallback1);
  } catch (error) {
    console.error('onTrashedAlbumChangeDemo failed, errCode is', error);
  }
}
```

## offAnalysisAlbumChange

```TypeScript
offAnalysisAlbumChange(callback?: Callback<AlbumChangeInfos>): void
```

Cancels the listener for the smart analysis album. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying   
**callback**. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-offAnalysisAlbumChange(callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-offAnalysisAlbumChange(callback?: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('offAnalysisAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.onAnalysisAlbumChange(onCallback1);
    // Register onCallback2.
    phAccessHelper.onAnalysisAlbumChange(onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.offAnalysisAlbumChange(onCallback1);
  } catch (error) {
    console.error('offAnalysisAlbumChangeDemo failed, errCode is', error);
  }
}
```

## offAnalysisPhotoChange

```TypeScript
offAnalysisPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void
```

Cancels the listening for the media asset changes related to the smart analysis album. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-offAnalysisPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-offAnalysisPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('offAnalysisPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.offAnalysisPhotoChange(onCallback1);
    // Register onCallback2.
    phAccessHelper.offAnalysisPhotoChange(onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.offAnalysisPhotoChange(onCallback1);
  } catch (error) {
    console.error('offAnalysisPhotoChangeDemo failed, errCode is', error);
  }
}
```

## on('hiddenPhotoChange')

```TypeScript
on(type: 'hiddenPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

Registers a listener for the **'hiddenPhotoChange'** event to monitor hidden media asset changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-on(type: 'hiddenPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'hiddenPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hiddenPhotoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('onHiddenPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('hiddenPhotoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('hiddenPhotoChange', onCallback2);
  } catch (error) {
    console.error('onHiddenPhotoChange failed, errCode is', error);
  }
}
```

## on('trashedPhotoChange')

```TypeScript
on(type: 'trashedPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

Registers a listener for the **'trashedPhotoChange'** event to monitor media asset changes in the trash. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'trashedPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'trashedPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trashedPhotoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onTrashedPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('trashedPhotoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('trashedPhotoChange', onCallback2);
  } catch (error) {
    console.error('onTrashedPhotoChangeDemo failed, errCode is', error);
  }
}
```

## on('hiddenAlbumChange')

```TypeScript
on(type: 'hiddenAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

Registers a listener for the **'hiddenAlbumChange'** event to monitor hidden album changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-on(type: 'hiddenAlbumChange', callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'hiddenAlbumChange', callback: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hiddenAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('onHiddenAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('hiddenAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('hiddenAlbumChange', onCallback2);
  } catch (error) {
    console.error('onHiddenAlbumChangeDemo failed, errCode is', error);
  }
}
```

## on('trashedAlbumChange')

```TypeScript
on(type: 'trashedAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

Registers a listener for the **'trashedAlbumChange'** event to monitor album changes in the trash. This API uses a callback to return the result, and it accepts multiple callbacks.

**Since:** 20

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'trashedAlbumChange', callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'trashedAlbumChange', callback: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trashedAlbumChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onTrashedAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('trashedAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('trashedAlbumChange', onCallback2);
  } catch (error) {
    console.error('onTrashedAlbumChangeDemo failed, errCode is', error);
  }
}
```

## onAnalysisAlbumChange

```TypeScript
onAnalysisAlbumChange(callback: Callback<AlbumChangeInfos>): void
```

Listens for the smart analysis album and returns the album change result using a callback. You can register multiple callbacks. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-onAnalysisAlbumChange(callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-onAnalysisAlbumChange(callback: Callback<AlbumChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper){
  console.info('onAnalysisAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.onAnalysisAlbumChange(onCallback1);
    // Register onCallback2.
    phAccessHelper.onAnalysisAlbumChange(onCallback2);
  } catch (error) {
    console.error('onAnalysisAlbumChangeDemo failed, errCode is', error);
  }
}
```

## onAnalysisPhotoChange

```TypeScript
onAnalysisPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void
```

Listens for the changes of media assets associated with the smart analysis album. The change carries the smart analysis album change information. The asset change notification is sent only when the asset change involves the smart analysis album information change. The asset change result is returned through the callback. Multiple callbacks can be registered. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-onAnalysisPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-onAnalysisPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onAnalysisPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.onAnalysisPhotoChange(onCallback1);
    // Register onCallback2.
    phAccessHelper.onAnalysisPhotoChange(onCallback2);
  } catch (error) {
    console.error('onAnalysisPhotoChangeDemo failed, errCode is', error);
  }
}
```

## query

```TypeScript
query(sql: string): Promise<ResultSet>
```

Queries data in the database using the specified SQL statement. This API does not support write operations or multi-level queries. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

<!--Device-PhotoAccessHelper-query(sql: string): Promise<ResultSet>--><!--Device-PhotoAccessHelper-query(sql: string): Promise<ResultSet>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('query');
  try {
    let ret: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    while (ret.goToNextRow()) {
      let row = ret.getRow();
      Object.entries(row).forEach((entry) => {
        const key = entry[0];
        const value = entry[1];
      });
    }
    ret.close();
  } catch (err) {
    console.error(`query failed with error: ${err.code}, ${err.message}`);
  }
}
```

## releaseDebugDatabase

```TypeScript
releaseDebugDatabase(betaIssueId: string, dbFd: number): Promise<void>
```

Release medialibrary database backup resources incluses closing backup database fd and deleting temporary backup database file which only works on beta device.

**Since:** 23

<!--Device-PhotoAccessHelper-releaseDebugDatabase(betaIssueId: string, dbFd: int): Promise<void>--><!--Device-PhotoAccessHelper-releaseDebugDatabase(betaIssueId: string, dbFd: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| betaIssueId | string | Yes |
| dbFd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800201-unsupported-operation-type) |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## removeFormInfo

```TypeScript
removeFormInfo(info: FormInfo, callback: AsyncCallback<void>): void
```

Removes the Gallery widget information bound to a single image from the database. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-removeFormInfo(info: FormInfo, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-removeFormInfo(info: FormInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('removeFormInfoDemo');
  let info: photoAccessHelper.FormInfo = {
    // formId is a string consisting of only digits. When removing a widget, leave uri empty.
    formId: "20230116123",
    uri: "",
  }

  phAccessHelper.removeFormInfo(info, async (err: BusinessError) => {
    if (err == undefined) {
      console.info('removeFormInfo success');
    } else {
      console.error(`removeFormInfo fail with error: ${err.code}, ${err.message}`);
    }
  });
}
```

## removeFormInfo

```TypeScript
removeFormInfo(info: FormInfo): Promise<void>
```

Removes the Gallery widget information bound to a single image from the database. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-removeFormInfo(info: FormInfo): Promise<void>--><!--Device-PhotoAccessHelper-removeFormInfo(info: FormInfo): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('removeFormInfoDemo');
  let info: photoAccessHelper.FormInfo = {
    // formId is a string consisting of only digits. When removing a widget, leave uri empty.
    formId: "20230116123",
    uri: "",
  }

  phAccessHelper.removeFormInfo(info).then(() => {
    console.info('removeFormInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`removeFormInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```

## removeGalleryFormInfo

```TypeScript
removeGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

Removes the Gallery widget information bound to a group of images from the database. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-removeGalleryFormInfo(info: GalleryFormInfo): Promise<void>--><!--Device-PhotoAccessHelper-removeGalleryFormInfo(info: GalleryFormInfo): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('removeGalleryFormInfoDemo');
  let info: photoAccessHelper.GalleryFormInfo = {
    // formId is a string consisting of only digits. When removing a widget, leave assertUris empty.
    formId: "20230116123"
  }

  phAccessHelper.removeGalleryFormInfo(info).then(() => {
    console.info('removeGalleryFormInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`removeGalleryFormInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```

## saveFormInfo

```TypeScript
saveFormInfo(info: FormInfo, callback: AsyncCallback<void>): void
```

Saves the Gallery widget information bound to a single image to the database. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-saveFormInfo(info: FormInfo, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-saveFormInfo(info: FormInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('saveFormInfoDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

  let info: photoAccessHelper.FormInfo = {
    // formId is a string consisting of only digits. uri indicates the URI of the image in Gallery. If there is no image in Gallery, uri must be an empty string.
    formId : "20230116123",
    uri: photoAsset.uri,
  }

  phAccessHelper.saveFormInfo(info, async (err: BusinessError) => {
    if (err == undefined) {
      console.info('saveFormInfo success');
    } else {
      console.error(`saveFormInfo fail with error: ${err.code}, ${err.message}`);
    }
  });
}
```

## saveFormInfo

```TypeScript
saveFormInfo(info: FormInfo): Promise<void>
```

Saves the Gallery widget information bound to a single image to the database. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-saveFormInfo(info: FormInfo): Promise<void>--><!--Device-PhotoAccessHelper-saveFormInfo(info: FormInfo): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('saveFormInfoDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

  let info: photoAccessHelper.FormInfo = {
    // formId is a string consisting of only digits. uri indicates the URI of the image in Gallery. If there is no image in Gallery, uri must be an empty string.
    formId: "20230116123",
    uri: photoAsset.uri,
  }

  phAccessHelper.saveFormInfo(info).then(() => {
    console.info('saveFormInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`saveFormInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```

## saveGalleryFormInfo

```TypeScript
saveGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

Saves the Gallery widget information bound to a group of images to the database. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-saveGalleryFormInfo(info: GalleryFormInfo): Promise<void>--><!--Device-PhotoAccessHelper-saveGalleryFormInfo(info: GalleryFormInfo): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('saveGalleryFormInfoDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  if (fetchResult === undefined) {
    console.error('fetchResult is undefined');
    return;
  }  
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset === undefined) {
    console.error('photoAsset is undefined');
    return;
  }
  let uriList: Array<string> = [
    photoAsset.uri,
  ];
  let info: photoAccessHelper.GalleryFormInfo = {
    // formId is a string consisting of only digits. assetUris indicates the URIs of the images or albums in Gallery.
    formId: "20230116123",
    assetUris: uriList,
  }

  phAccessHelper.saveGalleryFormInfo(info).then(() => {
    console.info('saveGalleryFormInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`saveGalleryFormInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```

## setAssetCompatibleCapability

```TypeScript
setAssetCompatibleCapability(bundleName: string, capability: AssetCompatibleCapability): Promise<void>
```

Sets the asset compatibility capability based on the bundle name. You can obtain the compatibility capability and determine whether to perform compatibility conversion based on the capability.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-setAssetCompatibleCapability(bundleName: string, capability: AssetCompatibleCapability): Promise<void>--><!--Device-PhotoAccessHelper-setAssetCompatibleCapability(bundleName: string, capability: AssetCompatibleCapability): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| capability | [AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let bundleName = "com.test.example";
    let capability : photoAccessHelper.AssetCompatibleCapability = {
        supportedHighResolution : true,
    };
    await phAccessHelper.setAssetCompatibleCapability(bundleName, capability);
  } catch (error) {
    console.error('failed to setAssetCompatibleCapability err', error);
  }
}
```

## setPhotoAlbumOrder

```TypeScript
setPhotoAlbumOrder(orderStyle: number, albumOrders: Array<AlbumOrder>): Promise<void>
```

Sets the sorting order for system, user, and source albums. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-setPhotoAlbumOrder(orderStyle: int, albumOrders: Array<AlbumOrder>): Promise<void>--><!--Device-PhotoAccessHelper-setPhotoAlbumOrder(orderStyle: int, albumOrders: Array<AlbumOrder>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orderStyle | number | Yes |
| albumOrders | Array&lt;[AlbumOrder](arkts-medialibrary-photoaccesshelper-albumorder-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('setPhotoAlbumOrderDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let orderStyle: number = 0;
  phAccessHelper.getPhotoAlbumOrder(orderStyle, fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getPhotoAlbumOrderPromise fetchResult is undefined');
      return;
    }
    let albumOrder: photoAccessHelper.AlbumOrder = await fetchResult.getFirstObject();
    albumOrder.albumOrder = 10;
    albumOrder.orderSection = 0;
    albumOrder.orderType = 1;
    albumOrder.orderStatus = 1;
    await phAccessHelper.setPhotoAlbumOrder(orderStyle, [albumOrder]);
    console.info('setPhotoAlbumOrderPromise successfully.');
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`setPhotoAlbumOrderPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

## setPreferredCompatibleMode

```TypeScript
setPreferredCompatibleMode(bundleName: string, compatibleMode: PreferredCompatibleMode): Promise<void>
```

Configure the preferred compatible mode configured by the application based on bundleName.There are three types of applications. For details, see PreferredCompatibleMode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-setPreferredCompatibleMode(bundleName: string, compatibleMode: PreferredCompatibleMode): Promise<void>--><!--Device-PhotoAccessHelper-setPreferredCompatibleMode(bundleName: string, compatibleMode: PreferredCompatibleMode): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| [compatibleMode](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | [PreferredCompatibleMode](arkts-medialibrary-photoaccesshelper-preferredcompatiblemode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function setPreferredCompatibleMode(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper,
  bundleName: string,
  preferredCompatibleMode: photoAccessHelper.PreferredCompatibleMode
): Promise<void> {
  console.info('setPreferredCompatibleModeDemo');
  phAccessHelper.setPreferredCompatibleMode(bundleName, preferredCompatibleMode)
    .then(() => {
      console.info('setPreferredCompatibleMode successfully');
    })
    .catch((err: BusinessError) => {
      console.error(`The setPreferredCompatibleMode call failed. error: ${err.code}, ${err.message}`);
    });
}
```

## startAssetAnalysis

```TypeScript
startAssetAnalysis(type: AnalysisType, assetUris?: Array<string>): Promise<number>
```

Starts asset analysis.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-startAssetAnalysis(type: AnalysisType, assetUris?: Array<string>): Promise<int>--><!--Device-PhotoAccessHelper-startAssetAnalysis(type: AnalysisType, assetUris?: Array<string>): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) | Yes |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(context: Context) {
  console.info('startAssetAnalysisDemo');
  try {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let uris = ["file://media/Photo/14/IMG_1729066473_013/IMG_20241016_122253.jpg",
                "file://media/Photo/68/IMG_1729033213_018/IMG_20241016_100082.jpg"];
    let taskId = await phAccessHelper.startAssetAnalysis(photoAccessHelper.AnalysisType.ANALYSIS_SEARCH_INDEX,
        uris);
    console.info('startAssetAnalysis success, taskId=' + taskId);
  } catch (err) {
    console.error('startAssetAnalysis failed, error=' + err);
  }
}
```

## startAssetAnalysisAsync

```TypeScript
startAssetAnalysisAsync(config: AnalysisConfig, callback: Callback<AnalysisResult>): Promise<number>
```

Starts asynchronous asset analysis. This API uses an asynchronous callback to return the result.

**Since:** 24

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-startAssetAnalysisAsync(config: AnalysisConfig, callback: Callback<AnalysisResult>): Promise<int>--><!--Device-PhotoAccessHelper-startAssetAnalysisAsync(config: AnalysisConfig, callback: Callback<AnalysisResult>): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AnalysisConfig](arkts-medialibrary-photoaccesshelper-analysisconfig-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AnalysisResult](arkts-medialibrary-photoaccesshelper-analysisresult-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
let callback = (result: photoAccessHelper.AnalysisResult) => {
  console.info('startAssetAnalysisAsync callback result: ' + JSON.stringify(result));
};

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('startAssetAnalysisAsyncDemo');
  let config: photoAccessHelper.AnalysisConfig = {
    types: [photoAccessHelper.AnalysisType.ANALYSIS_SEARCH_INDEX],
    uris: ['file://media/Photo/14/IMG_1729066473_013/IMG_20241016_122253.jpg'],
    extraInfos: '{"trigger":"manual"}'
  };

  try {
    let taskId = await phAccessHelper.startAssetAnalysisAsync(config, callback);
    console.info('startAssetAnalysisAsync success, taskId=' + taskId);
  } catch (err) {
    console.error(`startAssetAnalysisAsync failed with error: ${err.code}, ${err.message}`);
  }
}
```

## startDeepOptimizeSpace

```TypeScript
startDeepOptimizeSpace(callback?: Callback<DeepOptimizeSpaceProgress>): Promise<void>
```

Start deep optimize storage space.

Before using this API, you are advised to call [canPerformDeepOptimizeSpace()](#canPerformDeepOptimizeSpace) and call this API only when true is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-startDeepOptimizeSpace(callback?: Callback<DeepOptimizeSpaceProgress>): Promise<void>--><!--Device-PhotoAccessHelper-startDeepOptimizeSpace(callback?: Callback<DeepOptimizeSpaceProgress>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeepOptimizeSpaceProgress](arkts-medialibrary-photoaccesshelper-deepoptimizespaceprogress-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800201-unsupported-operation-type) |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    await phAccessHelper.startDeepOptimizeSpace((progress: photoAccessHelper.DeepOptimizeSpaceProgress) => {
      console.info(`startDeepOptimizeSpace progress: state=${progress.state}, progress=${progress.progress}`);
    });
    console.info('startDeepOptimizeSpace successfully');
  } catch (err) {
    console.error(`startDeepOptimizeSpace failed with error: ${err.code}, ${err.message}`);
  }
}
```

## startThumbnailCreationTask

```TypeScript
startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): number
```

Generates a thumbnail based on the specified rule.

**Since:** 13

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): int--><!--Device-PhotoAccessHelper-startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

function testCallBack() {

}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();

  try {
    console.info('startThumbnailCreationTask test start');
    phAccessHelper.startThumbnailCreationTask(predicates, testCallBack);
  } catch (err) {
    console.error(`startThumbnailCreationTask failed, error: ${err.code}, ${err.message}`);
  }
}
```

## startThumbnailCreationTask

```TypeScript
startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>, response: AsyncCallback<number>): number
```

Generates a thumbnail based on the specified rule. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>, response: AsyncCallback<int>): int--><!--Device-PhotoAccessHelper-startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>, response: AsyncCallback<int>): int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
| response | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData'

function testCallBack() {
  console.info(`startThumbnailCreationTask: First callback`);
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();

  try {
    console.info('startThumbnailCreationTask test start');
    phAccessHelper.startThumbnailCreationTask(predicates, testCallBack, (err, state) =>{
        if(err) {
          console.error("error message: " + err?.message)
          console.error("error code: " + err?.code)
          return
        }
        console.info(`startThumbnailCreationTask: response state ${state}`);
      });
  } catch (err) {
    console.error(`startThumbnailCreationTask failed, error: ${err.code}, ${err.message}`);
  }
}
```

## stopAssetAnalysis

```TypeScript
stopAssetAnalysis(config: AnalysisConfig): void
```

Stops asset analysis.

**Since:** 24

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-stopAssetAnalysis(config: AnalysisConfig): void--><!--Device-PhotoAccessHelper-stopAssetAnalysis(config: AnalysisConfig): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AnalysisConfig](arkts-medialibrary-photoaccesshelper-analysisconfig-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('stopAssetAnalysisDemo');
  let config: photoAccessHelper.AnalysisConfig = {
    types: [photoAccessHelper.AnalysisType.ANALYSIS_SEARCH_INDEX],
    uris: ['file://media/Photo/14/IMG_1729066473_013/IMG_20241016_122253.jpg']
  };

  try {
    phAccessHelper.stopAssetAnalysis(config);
    console.info('stopAssetAnalysis success');
  } catch (err) {
    console.error(`stopAssetAnalysis failed with error: ${err.code}, ${err.message}`);
  }
}
```

## stopDeepOptimizeSpace

```TypeScript
stopDeepOptimizeSpace(): Promise<void>
```

Stop deep optimize storage space.

**Since:** 26.0.0

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoAccessHelper-stopDeepOptimizeSpace(): Promise<void>--><!--Device-PhotoAccessHelper-stopDeepOptimizeSpace(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    await phAccessHelper.stopDeepOptimizeSpace();
    console.info('stopDeepOptimizeSpace successfully');
  } catch (err) {
    console.error(`stopDeepOptimizeSpace failed with error: ${err.code}, ${err.message}`);
  }
}
```

## stopThumbnailCreationTask

```TypeScript
stopThumbnailCreationTask(taskId: number): void
```

Stops generating a thumbnail.

**Since:** 13

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-stopThumbnailCreationTask(taskId: int): void--><!--Device-PhotoAccessHelper-stopThumbnailCreationTask(taskId: int): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('stopThumbnailCreationTask test start');
    let taskId: number = 75983;
    phAccessHelper.stopThumbnailCreationTask(taskId);
  } catch (err) {
    console.error(`stopThumbnailCreationTask failed, error: ${err.code}, ${err.message}`);
  }
}
```

## updateGalleryFormInfo

```TypeScript
updateGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

Updates the information about a Gallery widget and saves the information to the database. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-updateGalleryFormInfo(info: GalleryFormInfo): Promise<void>--><!--Device-PhotoAccessHelper-updateGalleryFormInfo(info: GalleryFormInfo): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('updateGalleryFormInfoDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  let photoAssetLast: photoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  let uriList: Array<string> = [
    photoAsset.uri,
    photoAssetLast.uri
  ];
  let info: photoAccessHelper.GalleryFormInfo = {
    // formId is a string consisting of only digits. assetUris indicates the URIs of the images or albums in Gallery.
    formId: "20230116123",
    assetUris: uriList,
  }

  phAccessHelper.updateGalleryFormInfo(info).then(() => {
    console.info('updateGalleryFormInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`updateGalleryFormInfo failed with error: ${err.code}, ${err.message}`);
  });
}
```
