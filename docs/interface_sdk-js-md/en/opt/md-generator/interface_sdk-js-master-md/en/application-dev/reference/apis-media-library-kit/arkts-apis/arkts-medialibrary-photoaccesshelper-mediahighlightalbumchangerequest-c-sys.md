# MediaHighlightAlbumChangeRequest (System API)

Provides APIs for managing the media album change request. It inherits from   
[MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md#MediaAnalysisAlbumChangeRequest).

**Inheritance/Implementation:** MediaHighlightAlbumChangeRequest extends [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md#MediaAnalysisAlbumChangeRequest)

**Since:** 21

<!--Device-photoAccessHelper-class MediaHighlightAlbumChangeRequest extends MediaAnalysisAlbumChangeRequest--><!--Device-photoAccessHelper-class MediaHighlightAlbumChangeRequest extends MediaAnalysisAlbumChangeRequest-End-->

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

**Since:** 21

<!--Device-MediaHighlightAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaHighlightAlbumChangeRequest-constructor(album: Album)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-library-kit/errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

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

## setHighlightAttribute

```TypeScript
setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void
```

Sets the specified attribute value in the highlights album.

**Since:** 21

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaHighlightAlbumChangeRequest-setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void--><!--Device-MediaHighlightAlbumChangeRequest-setHighlightAttribute(attribute: HighlightAlbumChangeAttribute, value: string): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attribute | [HighlightAlbumChangeAttribute](arkts-medialibrary-photoaccesshelper-highlightalbumchangeattribute-e-sys.md) | Yes |
| value | string | Yes |

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
