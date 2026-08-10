# QueryCompilationEvent

```TypeScript
type QueryCompilationEvent = (compilationId: string, pageIndex: int) => Promise<PageMediaEntity>
```

合集查询事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryCompilationEvent = (compilationId: string, pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryCompilationEvent = (compilationId: string, pageIndex: int) => Promise<PageMediaEntity>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compilationId | string | Yes | 合集的ID。 |
| pageIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 页面的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PageMediaEntity&gt; | Promise对象，返回查询的合集媒体实体对象。 |

