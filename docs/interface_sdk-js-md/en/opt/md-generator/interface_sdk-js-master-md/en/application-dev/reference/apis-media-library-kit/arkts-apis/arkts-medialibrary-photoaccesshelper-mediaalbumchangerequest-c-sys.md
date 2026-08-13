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

## createAlbumRequest

```TypeScript
static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest
```

Creates a MediaAlbumChangeRequest instance. The album name must meet the following requirements: - The total length of the album name must be between 1 and 255 characters. - It must not contain any invalid characters, which are: . .. \ / : * ? " ' ` &lt; &gt; | { } [ ] - The characters are case insensitive. - Duplicate album names are not allowed.

**Since:** 11

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest--><!--Device-MediaAlbumChangeRequest-static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createAlbumRequestDemo');
  try {
    let albumName: string = 'newAlbumName' + new Date().getTime();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = photoAccessHelper.MediaAlbumChangeRequest.createAlbumRequest(context, albumName);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('apply createAlbumRequest successfully');
  } catch (err) {
    console.error(`createAlbumRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## createAlbumRequest

```TypeScript
static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest | null
```

Creates a MediaAlbumChangeRequest instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest | null--><!--Device-MediaAlbumChangeRequest-static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## deleteAlbums

```TypeScript
static deleteAlbums(context: Context, albums: Array<Album>): Promise<void>
```

Deletes user albums. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAlbumChangeRequest-static deleteAlbums(context: Context, albums: Array<Album>): Promise<void>--><!--Device-MediaAlbumChangeRequest-static deleteAlbums(context: Context, albums: Array<Album>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| albums | Array & lt;Album & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('deleteAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    await photoAccessHelper.MediaAlbumChangeRequest.deleteAlbums(context, [album]);
    console.info('deleteAlbums successfully');
  } catch (err) {
    console.error(`deleteAlbumsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## deleteAlbumsWithUri

```TypeScript
static deleteAlbumsWithUri(context: Context, albumUris: Array<string>): Promise<void>
```

Deletes user albums by URI. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAlbumChangeRequest-static deleteAlbumsWithUri(context: Context, albumUris: Array<string>): Promise<void>--><!--Device-MediaAlbumChangeRequest-static deleteAlbumsWithUri(context: Context, albumUris: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| albumUris | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

```TypeScript
async function example(context: Context, albumUri: string) {
  console.info('deleteAlbumsWithUriDemo');
  try {
    await photoAccessHelper.MediaAlbumChangeRequest.deleteAlbumsWithUri(context, [albumUri]);
    console.info('deleteAlbums successfully');
  } catch (err) {
    console.error(`deleteAlbumsWithUriDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## deleteAssets

```TypeScript
deleteAssets(assets: Array<PhotoAsset>): void
```

Permanently deletes assets from the trash. > **NOTE：**> > This operation is irreversible. The assets deleted cannot be restored. Exercise caution when performing this > operation.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-deleteAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-deleteAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('deleteAssetsPermanentlyDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.TRASH);
    if (albumFetchResult === undefined) {
      console.error('albumFetchResult is undefined');
      return;
    }
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    if (fetchResult === undefined) {
      console.error('fetchResult is undefined');
      return;
    }
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.deleteAssets([asset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('succeed to deleteAssets permanently');
  } catch (err) {
    console.error(`deleteAssetsPermanentlyDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## deleteAssetsWithUri

```TypeScript
deleteAssetsWithUri(assetUris: Array<string>): void
```

Permanently deletes assets from the trash. > **NOTE：**> > This operation is irreversible. The assets deleted cannot be restored. Exercise caution when performing this > operation.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-deleteAssetsWithUri(assetUris: Array<string>): void--><!--Device-MediaAlbumChangeRequest-deleteAssetsWithUri(assetUris: Array<string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## dismiss

```TypeScript
dismiss(): void
```

Removes this group photo album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-dismiss(): void--><!--Device-MediaAlbumChangeRequest-dismiss(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('dismissDemo');
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.GROUP_PHOTO);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.dismiss();
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('dismiss successfully');
  } catch (err) {
    console.error(`dismissDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## dismissAssets

```TypeScript
dismissAssets(assets: Array<PhotoAsset>): void
```

Removes assets from this portrait album or group photo album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-dismissAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-dismissAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('dismissAssets Example')
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo('user_display_level', 2);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();

    let predicatesAsset: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let assetFetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicatesAsset
    };
    let assetFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(assetFetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await assetFetchResult.getFirstObject();

    let changeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    changeRequest.dismissAssets([asset]);
    await phAccessHelper.applyChanges(changeRequest);
  } catch (err) {
    console.error(`dismissAssets failed with error: ${err.code}, ${err.message}`);
  }
}
```

## mergeAlbum

```TypeScript
mergeAlbum(target: Album): void
```

Merges two portrait albums.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-mergeAlbum(target: Album): void--><!--Device-MediaAlbumChangeRequest-mergeAlbum(target: Album): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('mergeAlbum Example')
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo('user_display_level', 2);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    if (fetchResult.isAfterLast()) {
      console.error('lack of album to merge');
      return;
    }
    let target: photoAccessHelper.Album = await fetchResult.getNextObject();

    let changeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    changeRequest.mergeAlbum(target);
    changeRequest.setAlbumName("testName");
    await phAccessHelper.applyChanges(changeRequest);
  } catch (err) {
    console.error(`mergeAlbum failed with error: ${err.code}, ${err.message}`);
  }
}
```

## moveAssets

```TypeScript
moveAssets(assets: Array<PhotoAsset>, targetAlbum: Album): void
```

Moves assets to another album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-moveAssets(assets: Array<PhotoAsset>, targetAlbum: Album): void--><!--Device-MediaAlbumChangeRequest-moveAssets(assets: Array<PhotoAsset>, targetAlbum: Album): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |
| targetAlbum | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('moveAssetsDemo');
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

    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to be moved into');
      return;
    }
    let nextAlbum: photoAccessHelper.Album = await albumFetchResult.getNextObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.moveAssets([asset], nextAlbum);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('moveAssets successfully');
  } catch (err) {
    console.error(`moveAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## moveAssetsWithUri

```TypeScript
moveAssetsWithUri(assetUris: Array<string>, targetAlbum: Album): void
```

Moves assets in an album to another album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-moveAssetsWithUri(assetUris: Array<string>, targetAlbum: Album): void--><!--Device-MediaAlbumChangeRequest-moveAssetsWithUri(assetUris: Array<string>, targetAlbum: Album): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | Yes |
| targetAlbum | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## operateAttribute

```TypeScript
operateAttribute(operation: AlbumOperation): void
```

Operates album attribute.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0 - since 26.0.0: ohos.permission.ACCESS_MEDIALIB_THUMB_DB
- API version 26.1.0+: ohos.permission.ACCESS_MEDIALIB_THUMB_DB or ohos.permission.WRITE_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAlbumChangeRequest-operateAttribute(operation: AlbumOperation): void--><!--Device-MediaAlbumChangeRequest-operateAttribute(operation: AlbumOperation): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operation | [AlbumOperation](arkts-medialibrary-photoaccesshelper-albumoperation-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800201](../errorcode-medialibrary.md#23800201-unsupported-operation-type) |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('operateAttributeDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (album === undefined) {
      console.error('album is undefined');
      return;
    }

    let operation: photoAccessHelper.AlbumOperation = {
      attr: photoAccessHelper.AlbumAttribute.NICK_NAME_ATTR,
      type: photoAccessHelper.AlbumOperationType.UPDATE,
      values: ['newNickname']
    };
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
      new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.operateAttribute(operation);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('operateAttribute successfully');
  } catch (err) {
    console.error(`operateAttribute failed with error: ${err.code}, ${err.message}`);
  }
}
```

## placeBefore

```TypeScript
placeBefore(album: Album): void
```

Places this album before an album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-placeBefore(album: Album): void--><!--Device-MediaAlbumChangeRequest-placeBefore(album: Album): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('placeBeforeDemo');
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let firstAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (albumFetchResult.isAfterLast()) {
      console.error('lack of album to place before');
      return;
    }
    let secondAlbum: photoAccessHelper.Album = await albumFetchResult.getNextObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(secondAlbum);
    albumChangeRequest.placeBefore(firstAlbum);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('placeBefore successfully');
  } catch (err) {
    console.error(`placeBeforeDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## recoverAssets

```TypeScript
recoverAssets(assets: Array<PhotoAsset>): void
```

Restores the assets corresponding to the specified PhotoAsset object array from the trash.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-recoverAssets(assets: Array<PhotoAsset>): void--><!--Device-MediaAlbumChangeRequest-recoverAssets(assets: Array<PhotoAsset>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('recoverAssetsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.TRASH);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.recoverAssets([asset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('recoverAssets successfully');
  } catch (err) {
    console.error(`recoverAssetsDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## recoverAssetsWithUri

```TypeScript
recoverAssetsWithUri(assetUris: Array<string>): void
```

Restores the assets corresponding to the specified URI string array from the trash.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-recoverAssetsWithUri(assetUris: Array<string>): void--><!--Device-MediaAlbumChangeRequest-recoverAssetsWithUri(assetUris: Array<string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 14000016 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## resetCoverUri

```TypeScript
resetCoverUri(): void
```

Resets the cover.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-resetCoverUri(): void--><!--Device-MediaAlbumChangeRequest-resetCoverUri(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](./arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('resetCoverUriDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.resetCoverUri();
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('resetCoverUri successfully');
  } catch (err) {
    console.error(`resetCoverUriDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setAlbumNameByFile

```TypeScript
setAlbumNameByFile(name: string): void
```

set album name by filemanger.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAlbumChangeRequest-setAlbumNameByFile(name: string): void--><!--Device-MediaAlbumChangeRequest-setAlbumNameByFile(name: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes | Album name to set. &lt;br&gt;Value range:1-255 &lt;br&gt;Album name parameter specifications: The album name contains 1 to 255 characters. Invalid English characters, including: \ /: *? "'`&lt; &gt; \|

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

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
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOption);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.setAlbumNameByFile('new_album_name');
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('setAlbumNameByFile successfully');
  } catch (err) {
    console.error(`setAlbumNameByFile failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setCoverUri

```TypeScript
setCoverUri(coverUri: string): void
```

Sets the album cover.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-setCoverUri(coverUri: string): void--><!--Device-MediaAlbumChangeRequest-setCoverUri(coverUri: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coverUri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('setCoverUriDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (albums === undefined) {
      console.error('getHiddenAlbumsViewCallback albums is undefined');
      return;
    }
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset is undefined');
      return;
    }
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.setCoverUri(asset.uri);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('setCoverUri successfully');
  } catch (err) {
    console.error(`setCoverUriDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setDisplayLevel

```TypeScript
setDisplayLevel(displayLevel: number): void
```

Sets the display level of the portrait album.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-setDisplayLevel(displayLevel: int): void--><!--Device-MediaAlbumChangeRequest-setDisplayLevel(displayLevel: int): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayLevel | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('setDisplayLevel Example')
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo('user_display_level', 2);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    let changeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    changeRequest.setDisplayLevel(1);
    await phAccessHelper.applyChanges(changeRequest);
  } catch (err) {
    console.error(`setDisplayLevel failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setHiddenAttribute

```TypeScript
setHiddenAttribute(hiddenState: boolean, isInherited:boolean):void
```

set hidden state of album.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAlbumChangeRequest-setHiddenAttribute(hiddenState: boolean, isInherited:boolean):void--><!--Device-MediaAlbumChangeRequest-setHiddenAttribute(hiddenState: boolean, isInherited:boolean):void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hiddenState | boolean | Yes |
| isInherited | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('albumSetHiddenAttributeDemo');
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOption);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.setHiddenAttribute(true, true);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('album setHiddenAttribute successfully');
  } catch (err) {
    console.error(`album setHiddenAttribute failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setIsMe

```TypeScript
setIsMe(): void
```

Sets the relationship between people in the portrait album to **Me**.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAlbumChangeRequest-setIsMe(): void--><!--Device-MediaAlbumChangeRequest-setIsMe(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    console.info('setIsMe Example')
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo('user_display_level', 2);
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    let changeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    changeRequest.setIsMe();
    await phAccessHelper.applyChanges(changeRequest);
  } catch (err) {
    console.error(`setIsMe failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setUploadStatus

```TypeScript
static setUploadStatus(context: Context, albums: Album[], allowUpload: boolean): Promise<void>
```

Sets whether the albums can be synced to cloud storage or family storage. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAlbumChangeRequest-static setUploadStatus(context: Context, albums: Album[], allowUpload: boolean): Promise<void>--><!--Device-MediaAlbumChangeRequest-static setUploadStatus(context: Context, albums: Album[], allowUpload: boolean): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| albums | [Album[]](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |
| allowUpload | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

```TypeScript
async function example(context: Context, album: photoAccessHelper.Album) {
  console.info('setUploadStatusDemo');
  try {
    let allowUpload = true;
    await photoAccessHelper.MediaAlbumChangeRequest.setUploadStatus(context, [album], allowUpload);
    console.info('setUploadStatus successfully');
  } catch (err) {
    console.error(`setUploadStatus failed with error: ${err.code}, ${err.message}`);
  }
}
```
