# QueryRecommendMediaEntityListEvent

```TypeScript
type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>
```

推荐媒体实体列表查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>--><!--Device-avMusicTemplate-type QueryRecommendMediaEntityListEvent = () => Promise<MediaEntity[]>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)[]&gt; | Promise对象，返回推荐的媒体实体的数组。 |
