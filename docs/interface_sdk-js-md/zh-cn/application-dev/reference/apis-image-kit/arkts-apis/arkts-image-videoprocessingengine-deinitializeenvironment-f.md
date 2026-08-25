# deinitializeEnvironment

## 导入模块

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## deinitializeEnvironment

```TypeScript
function deinitializeEnvironment(): Promise<void>
```

反初始化图像处理的全局环境。

**起始版本：** 18

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [29200006](../errorcode-videoprocessingengine.md#29200006-不被允许的操作) |
