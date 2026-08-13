# OnFrameFetched

```TypeScript
type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void
```

批量获取缩略图回调函数。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void--><!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| frameInfo | [FrameInfo](arkts-media-media-frameinfo-i.md) | 是 |
| err | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | 否 |
