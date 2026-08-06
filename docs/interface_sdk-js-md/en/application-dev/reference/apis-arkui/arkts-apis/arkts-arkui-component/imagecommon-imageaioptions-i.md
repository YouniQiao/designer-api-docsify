# ImageAIOptions

Image AI analysis options.
    **Description:**  
    
    The types parameter in this feature has higher priority than the types parameter in  
    [ImageAnalyzerConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. When both are set,  
    the value set in this feature takes precedence.  
    
    This feature depends on device capability and needs to be used with  
    the [enableAnalyzer]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ interface  
    of the corresponding component (for example, [Image component]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ImageAIOptions--><!--Device-unnamed-export declare interface ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aiController

```TypeScript
aiController?: ImageAnalyzerController | ESValue
```

Image AI analysis controller. The enableAnalyzer interface of the corresponding component (for example,the [enableAnalyzer]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_interface of the Image component) must be set to true for this to take effect.

Currently, only ESValue type is supported.

**Type:** ImageAnalyzerController \| ESValue

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageAIOptions-aiController?: ImageAnalyzerController | ESValue--><!--Device-ImageAIOptions-aiController?: ImageAnalyzerController | ESValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types?: ImageAnalyzerType[]
```

Image AI analysis type.

**Type:** ImageAnalyzerType[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageAIOptions-types?: ImageAnalyzerType[]--><!--Device-ImageAIOptions-types?: ImageAnalyzerType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

