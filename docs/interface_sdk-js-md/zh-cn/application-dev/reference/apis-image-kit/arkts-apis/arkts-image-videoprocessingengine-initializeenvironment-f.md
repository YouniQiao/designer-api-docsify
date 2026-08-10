# initializeEnvironment

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## initializeEnvironment

```TypeScript
function initializeEnvironment(): Promise<void>
```

Initialize global environment for image processing.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function initializeEnvironment can not work correctly &lt;br&gt;due to limited device capabilities. |
| 29200007 | Out of memory. |
| 29200006 | The operation is not permitted. This may be caused by incorrect status. |
| 29200002 | The global environment initialization for image processing failed, &lt;br&gt;such as failure to initialize the GPU environment. |

## 示例

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  await videoProcessingEngine.initializeEnvironment();
}
```

