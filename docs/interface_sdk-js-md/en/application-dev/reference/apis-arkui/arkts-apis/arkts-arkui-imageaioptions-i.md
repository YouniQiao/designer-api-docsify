# ImageAIOptions

Provides the AI image analysis options. &gt; **NOTE：**&gt; &gt; The **types** parameter of this API has a higher priority than that of &gt; [ImageAnalyzerConfig](arkts-arkui-imageanalyzerconfig-i.md). This means that, if both parameters are set, the value set by &gt; this API takes precedence. &gt; &gt; This API depends on device capabilities and must be used together with the &gt; enableAnalyzer API of the corresponding component (for example, the &gt; Image component).

**Since:** 12

<!--Device-unnamed-declare interface ImageAIOptions--><!--Device-unnamed-declare interface ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## aiController

```TypeScript
aiController?: ImageAnalyzerController
```

AI image analysis controller.

**Type:** [ImageAnalyzerController](arkts-arkui-imageanalyzercontroller-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAIOptions-aiController?: ImageAnalyzerController--><!--Device-ImageAIOptions-aiController?: ImageAnalyzerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types?: ImageAnalyzerType[]
```

AI image analysis types.

**Type:** [ImageAnalyzerType](arkts-arkui-imageanalyzertype-e.md)[]

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAIOptions-types?: ImageAnalyzerType[]--><!--Device-ImageAIOptions-types?: ImageAnalyzerType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

