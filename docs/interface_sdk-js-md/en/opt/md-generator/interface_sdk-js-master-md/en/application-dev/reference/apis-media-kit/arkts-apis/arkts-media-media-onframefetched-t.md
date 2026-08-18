# OnFrameFetched

```TypeScript
type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void
```

Describes the callback invoked when thumbnails are obtained in batches.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void--><!--Device-media-type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| frameInfo | [FrameInfo](arkts-media-media-frameinfo-i.md) | Yes |
| err | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | No |
