# QueryPlaylistEvent

```TypeScript
type QueryPlaylistEvent = (pageIndex: number, sort: Sort) => Promise<PageMediaEntity>
```

播放列表查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageIndex | number | 是 |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |
