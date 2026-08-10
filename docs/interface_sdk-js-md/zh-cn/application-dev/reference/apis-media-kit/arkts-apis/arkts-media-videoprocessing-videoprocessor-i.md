# VideoProcessor

Provides the VideoProcessor type, including AIHDR related functions.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-videoProcessing-interface VideoProcessor--><!--Device-videoProcessing-interface VideoProcessor-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

## 导入模块

```TypeScript
import { videoProcessing } from 'kits/@kit.MediaKit';
```

## getStatus

```TypeScript
getStatus(): Promise<VideoProcessorStatus | undefined>
```

Gets the current status of video processor features.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>--><!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;VideoProcessorStatus \| undefined&gt; | Promise used to return VideoProcessorStatus or undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

## offStatusChange

```TypeScript
offStatusChange(callback?: VideoProcessorStatusCallback): void
```

Unregisters a listener for video processor status changes.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | 否 | The callback function to remove. If not provided, all callbacks for this event type will be removed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 29200009 | Input value is invalid. |
| 29200006 | The operation is not permitted. This may be caused by incorrect status. |

## onStatusChange

```TypeScript
onStatusChange(callback: VideoProcessorStatusCallback): void
```

Registers a listener for video processor status changes.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | 是 | The callback function to invoke when status changes. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 29200009 | Input value is invalid. |
| 29200007 | Out of memory. |

