# MediaAnalysisAlbumChangeRequest (System API)

Provides APIs for managing the analysis album change request.

**Inheritance/Implementation:** MediaAnalysisAlbumChangeRequest extends [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md)

**Since:** 18

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## constructor

```TypeScript
constructor(album: Album)
```

Constructor.

**Since:** 18

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createAnalysisAlbumRequest

```TypeScript
static createAnalysisAlbumRequest(
      context:Context,
      name: string,
      subtype: AlbumSubtype
    ): MediaAnalysisAlbumChangeRequest
```

Creates a change request for the **Analysis** album.

> **NOTE：**&gt;
> The album name must meet the following requirements:&gt;
> - The album name string length ranges from 1 to 255.&gt;
> - The album name cannot contain any of the following characters:.. \ / : * ? " ' ` &lt;
&gt; | { } [ ]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| name | string | Yes |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## setDefaultCoverUri

```TypeScript
setDefaultCoverUri(coverUri: string): void
```

Sets the default cover image for the smart album.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| coverUri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |

## setOrderPosition

```TypeScript
setOrderPosition(assets: Array<PhotoAsset>, position: Array<number>): void
```

Sets the sequence of assets in the **Analysis** album.

**Since:** 18

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## setRelationship

```TypeScript
setRelationship(relationship: string): Promise<void>
```

Sets the relationships of a person in the portrait album.The supported relationship names include: | Unique ID | Description | | ---------- | ------- | | me | Me| | son | Son| | daughter | Daughter| | wife | Wife| | husband | Husband| | father | Father| | mother | Mother| | colleague | Colleague| | friend | Friend| | classmate | Classmate| | best_friend_female | Best female friend| | boyfriend | Boyfriend| | girlfriend | Girlfriend| | family | Family| | maternal_grandfather | Maternal grandfather| | maternal_grandmother | Maternal grandmother| | paternal_grandfather | Paternal grandfather| | paternal_grandmother | Paternal grandmother| | older_brother | Older brother| | older_sister | Older sister| | younger_brother | Younger brother| | younger_sister | Younger sister| | relative | Relative| | other | Other|

**Since:** 21

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
