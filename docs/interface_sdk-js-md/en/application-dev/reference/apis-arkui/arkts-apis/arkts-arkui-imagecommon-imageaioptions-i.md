# ImageAIOptions

图像AI分析选项。

> **说明：**
> 
> 该特性中的参数types优先级高于[ImageAnalyzerConfig](arkts-arkui-imagecommon-imageanalyzerconfig-i.md)中的参数types，两者同时设置时以该特性设置的值为准。
> 
> 该特性依赖设备能力，且需要和对应组件的[enableAnalyzer](arkts-arkui-image-imageattribute-i.md#enableanalyzer)接口
> （例如[Image组件](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)）搭配使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ImageAIOptions--><!--Device-unnamed-export declare interface ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aiController

```TypeScript
aiController?: ImageAnalyzerController | ESValue
```

图像AI分析控制器，需要对应组件的enableAnalyzer接口（例如Image组件的[enableAnalyzer](arkts-arkui-image-imageattribute-i.md#enableanalyzer)接口）设置为true才能生效。目前只支持ESValue类型。

**Type:** [ImageAnalyzerController](arkts-arkui-imagecommon-imageanalyzercontroller-c.md) \| ESValue

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageAIOptions-aiController?: ImageAnalyzerController | ESValue--><!--Device-ImageAIOptions-aiController?: ImageAnalyzerController | ESValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types?: ImageAnalyzerType[]
```

图像AI分析类型。

**Type:** [ImageAnalyzerType](arkts-arkui-imageanalyzertype-e.md)[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageAIOptions-types?: ImageAnalyzerType[]--><!--Device-ImageAIOptions-types?: ImageAnalyzerType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

