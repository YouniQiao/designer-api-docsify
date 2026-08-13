# QueryMediaEntityByKeywordEvent

```TypeScript
type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,
    pageIndex: number) => Promise<PageMediaEntity>
```

通过关键字查询媒体数据的回调事件

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryMediaEntityByKeywordEvent = (keyword: string, searchType: EntityType,    pageIndex: int) => Promise<PageMediaEntity>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyword | string | 是 |
| searchType | [EntityType](arkts-avsession-avmusictemplate-entitytype-e.md) | 是 |
| pageIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |
