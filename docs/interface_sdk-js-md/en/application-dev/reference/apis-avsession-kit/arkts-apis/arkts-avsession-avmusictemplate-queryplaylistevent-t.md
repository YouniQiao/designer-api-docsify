# QueryPlaylistEvent

```TypeScript
type QueryPlaylistEvent = (pageIndex: int, sort: Sort) => Promise<PageMediaEntity>
```

The query play list event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryPlaylistEvent = (pageIndex: int, sort: Sort) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryPlaylistEvent = (pageIndex: int, sort: Sort) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pageIndex | int | Yes | page index |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | Yes | sort |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; | (PageMediaEntity) returned through promise |

