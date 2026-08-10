# hasRecoverCacheInGeneratorDialog（系统接口）

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## hasRecoverCacheInGeneratorDialog

```TypeScript
function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean
```

Check whether cache files that can be restored exist in GeneratorDialog.The persistent cache file is used to store configuration parameters for AI image generation.

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-imageGeneration-function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean--><!--Device-imageGeneration-function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c-sys.md) | 是 | the context of dialog for ui display. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if cache can be recovered in GeneratorDialog, false otherwise. |

