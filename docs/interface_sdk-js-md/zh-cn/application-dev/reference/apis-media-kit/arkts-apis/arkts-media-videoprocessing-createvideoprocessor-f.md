# createVideoProcessor

## 导入模块

```TypeScript
import { videoProcessing } from 'kits/@kit.MediaKit';
```

## createVideoProcessor

```TypeScript
function createVideoProcessor(): VideoProcessor
```

创建视频处理实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 |
| --- |
| [VideoProcessor](arkts-media-videoprocessing-videoprocessor-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200003](../../apis-image-kit/errorcode-videoprocessingengine.md#29200003-创建失败) |
| [29200007](../../apis-image-kit/errorcode-videoprocessingengine.md#29200007-内存不足) |
