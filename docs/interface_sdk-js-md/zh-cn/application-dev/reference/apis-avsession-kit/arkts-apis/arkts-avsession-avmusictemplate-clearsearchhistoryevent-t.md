# ClearSearchHistoryEvent

```TypeScript
type ClearSearchHistoryEvent = () => Promise<OperResult>
```

清除搜索历史事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type ClearSearchHistoryEvent = () => Promise<OperResult>--><!--Device-avMusicTemplate-type ClearSearchHistoryEvent = () => Promise<OperResult>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[OperResult](arkts-avsession-avmusictemplate-operresult-i.md)&gt; | Promise对象，返回清除搜索历史的操作结果的对象。 |
