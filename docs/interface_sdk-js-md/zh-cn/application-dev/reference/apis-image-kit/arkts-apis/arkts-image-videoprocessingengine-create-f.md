# create

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## create

```TypeScript
function create(): ImageProcessor
```

Create an image processing instance.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-videoProcessingEngine-function create(): ImageProcessor--><!--Device-videoProcessingEngine-function create(): ImageProcessor-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) | Returns the ImageProcessor instance if &lt;br&gt;the operation is successful; returns null otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function create can not work correctly due to limited &lt;br&gt;device capabilities. |
| 29200007 | Out of memory. |
| 29200003 | Failed to create image processing instance. For example, &lt;br&gt;the number of instances exceeds the upper limit. |

## 示例

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  await videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```

