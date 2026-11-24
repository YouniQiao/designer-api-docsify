# QueryHotWordsEvent

```TypeScript
type QueryHotWordsEvent = () => Promise<string[]>
```

热词查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryHotWordsEvent = () => Promise<string[]>--><!--Device-avMusicTemplate-type QueryHotWordsEvent = () => Promise<string[]>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string[]&gt; | Promise对象，返回热词的数组。 |
