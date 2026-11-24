# QuerySearchHistoryEvent

```TypeScript
type QuerySearchHistoryEvent = () => Promise<string[]>
```

搜索历史查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QuerySearchHistoryEvent = () => Promise<string[]>--><!--Device-avMusicTemplate-type QuerySearchHistoryEvent = () => Promise<string[]>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string[]&gt; | Promise对象，返回搜索历史的数组。 |
