# VideoProcessorStatusCallback(Provides the capability of video quality processing.)

```TypeScript
type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void
```

Status change callback type for video processor notifications.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-videoProcessing-type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void--><!--Device-videoProcessing-type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | [VideoProcessorStatus](arkts-media-videoprocessing-videoprocessorstatus-i.md) | Yes |
