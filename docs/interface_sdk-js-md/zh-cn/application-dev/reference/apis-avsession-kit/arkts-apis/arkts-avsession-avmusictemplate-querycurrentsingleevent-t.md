# QueryCurrentSingleEvent

```TypeScript
type QueryCurrentSingleEvent = () => Promise<Single>
```

当前单曲查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryCurrentSingleEvent = () => Promise<Single>--><!--Device-avMusicTemplate-type QueryCurrentSingleEvent = () => Promise<Single>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[Single](arkts-avsession-avmusictemplate-single-i.md)&gt; | Promise对象，返回Single对象。 |
