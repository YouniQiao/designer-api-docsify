# QueryCompilationEvent

```TypeScript
type QueryCompilationEvent = (compilationId: string, pageIndex: number) => Promise<PageMediaEntity>
```

合集查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryCompilationEvent = (compilationId: string, pageIndex: int) => Promise<PageMediaEntity>--><!--Device-avMusicTemplate-type QueryCompilationEvent = (compilationId: string, pageIndex: int) => Promise<PageMediaEntity>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compilationId | string | 是 |
| pageIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;PageMediaEntity&gt; |
