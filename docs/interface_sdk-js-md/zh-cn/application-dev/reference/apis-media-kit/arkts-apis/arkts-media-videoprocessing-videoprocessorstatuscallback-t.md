# VideoProcessorStatusCallback

```TypeScript
type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void
```

Status change callback type for video processor notifications.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-videoProcessing-type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void--><!--Device-videoProcessing-type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [VideoProcessorStatus](arkts-media-videoprocessing-videoprocessorstatus-i.md) | 是 | The type of video processor status. |

