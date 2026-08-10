# QueryMediaEntityByKeywordEvent

```TypeScript
type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,
    pageIndex: int) => Promise<PageMediaEntity>
```

通过关键字查询媒体数据的回调事件

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyword | string | Yes |  |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | Yes | 搜索内容的类型 |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 页面索引 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | 通过promise返回PageMediaEntity |

