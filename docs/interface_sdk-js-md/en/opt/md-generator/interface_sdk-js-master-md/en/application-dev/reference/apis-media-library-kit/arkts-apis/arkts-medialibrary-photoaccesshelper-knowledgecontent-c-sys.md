# KnowledgeContent (System API)

Knowledge Content class, used for geting related entity.

**Since:** 23

**Deprecated since:** -1

<!--Device-photoAccessHelper-class KnowledgeContent--><!--Device-photoAccessHelper-class KnowledgeContent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getRelatedEntity

```TypeScript
static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>
```

Get Related Entities, Smart Label

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>--><!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| topic | string | Yes |
| context | [ContextMap](arkts-medialibrary-photoaccesshelper-contextmap-i-sys.md) | Yes |
| option | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Entity[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSearchSuggestion

```TypeScript
static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>
```

Get Search Suggestion.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Model restriction:** This API can be used only in the stage model.

<!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>--><!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchSuggestionTypes | Array&lt;[SearchSuggestionType](arkts-medialibrary-photoaccesshelper-searchsuggestiontype-e-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[SearchSuggestionResult](arkts-medialibrary-photoaccesshelper-searchsuggestionresult-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |
