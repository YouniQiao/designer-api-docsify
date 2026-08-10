# CanvasGradient

渐变对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CanvasGradient--><!--Device-unnamed-export declare class CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: double, color: string | ColorMetrics): void
```

设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。支持通过传入  
[ColorMetrics](../../../reference/apis-arkui/js-apis-arkui-graphics.md#colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasGradient-addColorStop(offset: double, color: string | ColorMetrics): void--><!--Device-CanvasGradient-addColorStop(offset: double, color: string | ColorMetrics): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | double | Yes | 设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。 设置offset&lt;0或offset&gt;1无渐变效果。&lt;br&gt;异常值undefined和null按无效值处理， 不设置本次断点值，NaN会导致CanvasGradient异常，Infinity会导致整个CanvasGradient不生效。 |
| color | string \| ColorMetrics | Yes | 设置渐变填充的颜色。&lt;br&gt;可以使用 [colorWithSpace](../../../reference/apis-arkui/js-apis-arkui-graphics.md#colorwithspace20) 方法构造指定色域属性 [ColorSpace](../../../reference/apis-arkui/arkui-ts/ts-appendix-enums.md#colorspace20) 为SRGB或DISPLAY_P3的颜色。每个渐变ColorMetrics的色域属性应当统一， 设置不同色域的属性时将抛出异常，错误码：103701。&lt;br&gt; 设置null和undefined无效，忽略本次断点值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 103701 | The color's ColorSpace is not the same as the last color's. |

