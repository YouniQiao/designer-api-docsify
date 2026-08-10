# ImageAIOptions

图像AI分析选项。

> **说明：**
> 
> 该特性中的参数types优先级高于[ImageAnalyzerConfig](arkts-arkui-imageanalyzerconfig-i.md)中的参数types，两者同时设置时以该特性设置的值为准。
> 
> 该特性依赖设备能力，且需要和对应组件的[enableAnalyzer](arkts-arkui-image-imageattribute-i.md#enableanalyzer)接口（例如[Image组件](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)）搭配使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface ImageAIOptions--><!--Device-unnamed-declare interface ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aiController

```TypeScript
aiController?: ImageAnalyzerController
```

图像AI分析控制器。

**Type:** [ImageAnalyzerController](arkts-arkui-imagecommon-imageanalyzercontroller-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAIOptions-aiController?: ImageAnalyzerController--><!--Device-ImageAIOptions-aiController?: ImageAnalyzerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types?: ImageAnalyzerType[]
```

图像AI分析类型。

**Type:** [ImageAnalyzerType](arkts-arkui-imageanalyzertype-e.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAIOptions-types?: ImageAnalyzerType[]--><!--Device-ImageAIOptions-types?: ImageAnalyzerType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

