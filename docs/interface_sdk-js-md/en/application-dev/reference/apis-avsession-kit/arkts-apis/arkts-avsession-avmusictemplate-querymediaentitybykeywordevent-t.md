# QueryMediaEntityByKeywordEvent

```TypeScript
type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,
    pageIndex: int) => Promise<PageMediaEntity>
```

The query media entity by keyword event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyword | string | Yes | keyword |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Yes | search type |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | page index |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | (PageMediaEntity) returned through promise |

