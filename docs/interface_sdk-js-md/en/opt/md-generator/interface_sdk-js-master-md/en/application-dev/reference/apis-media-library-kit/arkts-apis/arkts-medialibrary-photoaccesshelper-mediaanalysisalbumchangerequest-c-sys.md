# MediaAnalysisAlbumChangeRequest (System API)

Provides APIs for managing the analysis album change request.

**Inheritance/Implementation:** MediaAnalysisAlbumChangeRequest extends [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md#MediaAlbumChangeRequest)

**Since:** 18

<!--Device-photoAccessHelper-class MediaAnalysisAlbumChangeRequest extends MediaAlbumChangeRequest--><!--Device-photoAccessHelper-class MediaAnalysisAlbumChangeRequest extends MediaAlbumChangeRequest-End-->

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

**Since:** 18

<!--Device-MediaAnalysisAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaAnalysisAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

## createAnalysisAlbumRequest

```TypeScript
static createAnalysisAlbumRequest(
      context:Context,
      name: string,
      subtype: AlbumSubtype
    ): MediaAnalysisAlbumChangeRequest
```

Creates a change request for the **Analysis** album.

> **NOTE：**
> 
> The album name must meet the following requirements:
> 
> - The album name string length ranges from 1 to 255.
> 
> - The album name cannot contain any of the following characters:.. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest--><!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| subtype | [AlbumSubtype](arkts-medialibrary-photoaccesshelper-albumsubtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

For details about how to create a photoAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper).

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createAlbumRequestDemo');
  try {
    let albumName: string = 'newAlbumName' + new Date().getTime();
    let albumChangeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest = photoAccessHelper.MediaAnalysisAlbumChangeRequest.createAnalysisAlbumRequest(context, albumName, photoAccessHelper.AlbumSubtype.PORTRAIT);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('apply createAlbumRequest successfully');
  } catch (err) {
    console.error(`createAlbumRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setDefaultCoverUri

```TypeScript
setDefaultCoverUri(coverUri: string): void
```

Sets the default cover image for the smart album.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaAnalysisAlbumChangeRequest-setDefaultCoverUri(coverUri: string): void--><!--Device-MediaAnalysisAlbumChangeRequest-setDefaultCoverUri(coverUri: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coverUri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('setDefaultCoverUri');
  try {
    let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albumFetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, albumFetchOption);
    if (albumFetchResult.getCount() === 0) {
      console.error('No album');
      return;
    }
    let portraitAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    albumFetchResult.close();
    // Obtain resources from the album.
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await portraitAlbum.getAssets(fetchOption);
    if (fetchResult.getCount() === 0) {
      console.error('No asset in album');
      fetchResult.close();
      return;
    }
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let coverUri: string = asset.uri;
    fetchResult.close();
    // Set the default cover.
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(portraitAlbum);
    changeRequest.setDefaultCoverUri(coverUri);
    await helper.applyChanges(changeRequest);
    console.info('setDefaultCoverUri success');
  } catch (err) {
    console.error(`setDefaultCoverUri error: ${err}`);
  }
}
```

## setOrderPosition

```TypeScript
setOrderPosition(assets: Array<PhotoAsset>, position: Array<number>): void
```

Sets the sequence of assets in the **Analysis** album.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAnalysisAlbumChangeRequest-setOrderPosition(assets: Array<PhotoAsset>, position: Array<int>): void--><!--Device-MediaAnalysisAlbumChangeRequest-setOrderPosition(assets: Array<PhotoAsset>, position: Array<int>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |
| position | Array & lt;number & gt; | Yes |

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

async function example(context: Context) {
  try {
    console.info('setOrderPosition');
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
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    const fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await highlightAlbum.getAssets(fetchOption);
    let assets: photoAccessHelper.PhotoAsset[] = await fetchResult.getAllObjects();
    let indexes: number[] = [];
    for (let i = 0; i < assets.length; i++) {
      indexes.push(i);
    }
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(highlightAlbum);
    changeRequest.setOrderPosition(assets, indexes);
    await helper.applyChanges(changeRequest);
    console.info(`setOrderPosition ${indexes}`);
  } catch (err) {
    console.error(`setOrderPosition error: ${err}`);
  }
}
```

## setRelationship

```TypeScript
setRelationship(relationship: string): Promise<void>
```

Sets the relationships of a person in the portrait album.

The supported relationship names include:  
| Unique ID | Description |
| ---------- | ------- |
| me | Me|
| son | Son|
| daughter | Daughter|
| wife | Wife|
| husband | Husband|
| father | Father|
| mother | Mother|
| colleague | Colleague|
| friend | Friend|
| classmate | Classmate|
| best_friend_female | Best female friend|
| boyfriend | Boyfriend|
| girlfriend | Girlfriend|
| family | Family|
| maternal_grandfather | Maternal grandfather|
| maternal_grandmother | Maternal grandmother|
| paternal_grandfather | Paternal grandfather|
| paternal_grandmother | Paternal grandmother|
| older_brother | Older brother|
| older_sister | Older sister|
| younger_brother | Younger brother|
| younger_sister | Younger sister|
| relative | Relative|
| other |

**Since:** 21

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAnalysisAlbumChangeRequest-setRelationship(relationship: string): Promise<void>--><!--Device-MediaAnalysisAlbumChangeRequest-setRelationship(relationship: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relationship | string | Yes |

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

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function SetRelationshipExample(context: Context, relationship: string) {
  try {
    console.info('setRelationship');
    let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albumFetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, albumFetchOption);
    if (albumFetchResult.getCount() === 0) {
      console.error('No album');
      return;
    }
    let portraitAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    albumFetchResult.close();
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(portraitAlbum);
    changeRequest.setRelationship(relationship);
    await helper.applyChanges(changeRequest);
    console.info(`setRelationship ${relationship}`);
  } catch (err) {
    console.error(`setRelationship error: ${err}`);
  }
}
```
