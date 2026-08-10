# deinitializeEnvironment

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## deinitializeEnvironment

```TypeScript
function deinitializeEnvironment(): Promise<void>
```

Deinitialize global environment for image processing.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 29200006 | The operation is not permitted. This may be caused by incorrect status. |

## 示例

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function deinitializeEnvironment() {
  await videoProcessingEngine.initializeEnvironment();
  await videoProcessingEngine.deinitializeEnvironment();
}
```

