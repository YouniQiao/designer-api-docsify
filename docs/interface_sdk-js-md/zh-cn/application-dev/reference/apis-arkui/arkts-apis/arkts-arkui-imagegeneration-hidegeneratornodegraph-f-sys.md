# hideGeneratorNodeGraph（系统接口）

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## hideGeneratorNodeGraph

```TypeScript
function hideGeneratorNodeGraph(uiContext: UIContext): Promise<void>
```

Hide the AI node graph Sheet.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-imageGeneration-function hideGeneratorNodeGraph(uiContext: UIContext): Promise<void>--><!--Device-imageGeneration-function hideGeneratorNodeGraph(uiContext: UIContext): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c-sys.md) | 是 | The context of dialog for ui display. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Returns the result of hide operation. |

