# QueryCompilationByKeywordEvent

```TypeScript
type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>
```

按关键字查询合集的事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>--><!--Device-avMusicTemplate-type QueryCompilationByKeywordEvent = (keyword: string) => Promise<Compilation[]>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyword | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Compilation[]&gt; | Promise对象，返回与关键字相关的合集数组。 |

