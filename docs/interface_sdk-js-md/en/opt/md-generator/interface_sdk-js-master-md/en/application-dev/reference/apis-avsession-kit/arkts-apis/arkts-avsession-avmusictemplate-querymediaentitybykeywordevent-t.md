# QueryMediaEntityByKeywordEvent

```TypeScript
type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,
    pageIndex: number) => Promise<PageMediaEntity>
```

The query media entity by keyword event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyword | string | Yes |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Yes |
| pageIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |
