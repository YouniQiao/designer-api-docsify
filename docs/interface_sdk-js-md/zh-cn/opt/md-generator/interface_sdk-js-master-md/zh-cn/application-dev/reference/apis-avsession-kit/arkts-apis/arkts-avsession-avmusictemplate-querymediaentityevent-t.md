# QueryMediaEntityEvent

```TypeScript
type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>
```

媒体实体查询事件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryMediaEntityEvent = (params: QueryMediaEntityParam) => Promise<PageMediaEntity>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [QueryMediaEntityParam](arkts-avsession-avmusictemplate-querymediaentityparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |
