# ColorMetricsLinearGradient

滑轨轨道的线性渐变背景颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare class ColorMetricsLinearGradient--><!--Device-unnamed-declare class ColorMetricsLinearGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(colorStops: ColorMetricsStop[])
```

ColorMetricsLinearGradient的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ColorMetricsLinearGradient-constructor(colorStops: ColorMetricsStop[])--><!--Device-ColorMetricsLinearGradient-constructor(colorStops: ColorMetricsStop[])-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorStops | [ColorMetricsStop](../arkts-apis/arkts-arkui-slider-colormetricsstop-i.md)[] | Yes | 线性渐变颜色断点数组，每个元素描述一个颜色及其在渐变中的断点值。 |

