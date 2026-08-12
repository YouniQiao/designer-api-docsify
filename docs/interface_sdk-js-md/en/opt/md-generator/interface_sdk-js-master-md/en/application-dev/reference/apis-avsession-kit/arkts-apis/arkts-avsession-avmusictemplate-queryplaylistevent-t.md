# QueryPlaylistEvent

```TypeScript
type QueryPlaylistEvent = (pageIndex: number, sort: Sort) => Promise<PageMediaEntity>
```

The query play list event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryPlaylistEvent = (pageIndex: int, sort: Sort) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryPlaylistEvent = (pageIndex: int, sort: Sort) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| sort | [Sort](arkts-avsession-avmusictemplate-sort-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageMediaEntity](arkts-avsession-avmusictemplate-pagemediaentity-i.md)&gt; |
