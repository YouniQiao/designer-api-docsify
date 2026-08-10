# OnFrameFetched

```TypeScript
type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void
```

批量获取缩略图回调函数。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void--><!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameInfo | [FrameInfo](arkts-media-media-frameinfo-i.md) | Yes | 返回的缩略图信息。 |
| err | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | No | 获取缩略图时发生错误，默认值为null。 |

