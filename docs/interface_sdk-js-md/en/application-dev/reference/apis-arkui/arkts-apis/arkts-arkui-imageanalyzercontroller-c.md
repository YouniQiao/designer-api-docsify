# ImageAnalyzerController

图像AI分析控制器。可以将此对象绑定至支持的组件，并通过该控制器调用其提供的方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class ImageAnalyzerController--><!--Device-unnamed-declare class ImageAnalyzerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAnalyzerController-constructor()--><!--Device-ImageAnalyzerController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getImageAnalyzerSupportTypes

```TypeScript
getImageAnalyzerSupportTypes(): ImageAnalyzerType[]
```

获取此控制器已绑定组件所支持的AI分析类型。调用前需先通过 Image/ImageAnimator 等组件的 aiController 属性将本控制器绑定到组件，否则返回空数组。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAnalyzerController-getImageAnalyzerSupportTypes(): ImageAnalyzerType[]--><!--Device-ImageAnalyzerController-getImageAnalyzerSupportTypes(): ImageAnalyzerType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnalyzerType](arkts-arkui-imageanalyzertype-e.md)[] | 对应组件支持的AI分析类型。 |

