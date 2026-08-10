# createVideoProcessor

## 导入模块

```TypeScript
import { videoProcessing } from 'kits/@kit.MediaKit';
```

## createVideoProcessor

```TypeScript
function createVideoProcessor(): VideoProcessor
```

Create a video processing instance.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-videoProcessing-function createVideoProcessor(): VideoProcessor--><!--Device-videoProcessing-function createVideoProcessor(): VideoProcessor-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessor](arkts-media-videoprocessing-videoprocessor-i.md) | Returns the VideoProcessor instance if the operation is successful; returns null otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function createVideoProcessor can not work correctly due to limited device capabilities. |
| 29200007 | Out of memory. |
| 29200003 | Failed to create video processing instance. For example, the number of instances exceeds the upper limit. |

