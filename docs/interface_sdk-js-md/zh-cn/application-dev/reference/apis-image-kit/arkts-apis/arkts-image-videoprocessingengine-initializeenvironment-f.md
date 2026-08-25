# initializeEnvironment

## 导入模块

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';
```

## initializeEnvironment

```TypeScript
function initializeEnvironment(): Promise<void>
```

初始化图像处理的全局环境。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29200002](../errorcode-videoprocessingengine.md#29200002-初始化失败) |
| [29200006](../errorcode-videoprocessingengine.md#29200006-不被允许的操作) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-内存不足) |

**示例**

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  await videoProcessingEngine.initializeEnvironment();
}
```
