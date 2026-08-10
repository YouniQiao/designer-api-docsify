# CanvasGradient

OffscreenCanvas支持以下属性：

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class CanvasGradient--><!--Device-unnamed-declare class CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

设置渐变断点值，包括偏移和颜色。调用多次addColorStop可设置多个断点，断点按offset值从小到大排序，渲染时在相邻断点间进行颜色插值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasGradient-addColorStop(offset: number, color: string): void--><!--Device-CanvasGradient-addColorStop(offset: number, color: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | 设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。 &lt;br&gt;设置offset&lt;0或offset&gt;1无渐变效果。 &lt;br&gt;异常值undefined和null按无效值处理，不添加该断点。NaN会导致CanvasGradient对象异常，无法正常生成渐变效果；Infinity会导致整个CanvasGradient不生效。 |
| color | string | Yes | 设置渐变的颜色。string类型支持'rgb(255, 255, 255)'、'rgba(255, 255, 255, 1.0)'、'#RGB'、'#ARGB'、'#RRGGBB '、'#AARRGGBB'格式，参考[ResourceColor](arkts-arkui-resourcecolor-t.md)中string类型说明。 &lt;br&gt;未按格式设置颜色无渐变效果。设置null和undefined时按无效值处理，不添加该断点。 |

## addColorStop

```TypeScript
addColorStop(offset: number, color: string | ColorMetrics): void
```

设置渐变断点值，包括偏移和颜色。支持设置rgb或argb格式颜色。支持通过传入[ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)类型设置P3广色域颜色值，从API版本26.0.0开始，新增支持BT2020广色域和HDR提亮。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CanvasGradient-addColorStop(offset: number, color: string | ColorMetrics): void--><!--Device-CanvasGradient-addColorStop(offset: number, color: string | ColorMetrics): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | 设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。 &lt;br&gt;设置offset&lt;0或offset&gt;1无渐变效果。 &lt;br&gt;异常值undefined和null按无效值处理，不添加该断点。NaN会导致CanvasGradient对象异常，无法正常生成渐变效果；Infinity会导致整个CanvasGradient不生效。 |
| color | string \| ColorMetrics | Yes | 设置渐变的颜色。string类型支持'rgb(255, 255, 255)'、'rgba(255, 255, 255, 1.0)'、'#RGB'、' #ARGB'、'#RRGGBB'、'#AARRGGBB'格式。 &lt;br&gt;可以使用[colorWithSpace](arkts-arkui-graphics-colormetrics-c.md#colorwithspace)方法构造指定色域属性的颜色。ColorMetrics类型 可以构造指定色域属性[ColorSpace](arkts-arkui-enums-colorspace-e.md)为sRGB或DISPLAY_P3的颜色。从API版本26.0.0开始，新增支持构造BT2020色域的颜色，并支持HDR提亮。同一 CanvasGradient对象中的所有渐变断点必须使用相同的色域属性，设置不同色域时将抛出异常，错误码：103701，此时不会添加该断点，CanvasGradient对象保持之前的状态。 &lt;br&gt;未按格式设置颜色无渐变效果。设置null和undefined时按无效值处理，不添加该断点。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 103701 | The color's ColorSpace is not the same as the last color's. |

