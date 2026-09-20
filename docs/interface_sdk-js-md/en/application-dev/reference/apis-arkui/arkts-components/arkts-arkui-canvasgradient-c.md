# CanvasGradient

```TypeScript
declare class CanvasGradient
```

A gradient object that allows multiple color breakpoints to be set through the **addColorStop** method, achieving smooth color transitions. It is suitable for canvas filling and stroking scenarios.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

Sets the gradient breakpoint value, including the offset and color. You can call **addColorStop** multiple times to set multiple breakpoints. The breakpoints are sorted by **offset** value in ascending order, and color interpolation is performed between adjacent breakpoints during rendering.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Proportion of the distance from the gradient breakpoint to the start point to the total length. The value range is [0, 1].<br> Setting **offset** &lt; 0 or **offset**   > 1 produces no gradient effect.<br> Abnormal values **undefined** and **null** are treated as invalid, and the gradient breakpoint is not added. NaN causes the **CanvasGradient** object to be abnormal and unable to generate gradient effects properly. Infinity causes the entire **CanvasGradient** to not take effect. |
| color | string | Yes | Gradient color. The string type supports the following formats: **'rgb(255, 255, 255)'**, **'rgba(255, 255, 255, 1.0)'**, **'#RGB'**, **'#ARGB'**, **'#RRGGBB'**, and **'#AARRGGBB'**. For details, see the **string** type description in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md).<br> If the color is not set in the specified format, no gradient effect is produced. When **null** or **undefined** is set, it is treated as invalid and the breakpoint is not added. |

**Examples**

```TypeScript
Set the gradient breakpoint value through addColorStop, including the offset and color.
```

```TypeScript
This example demonstrates how to set the gradient stop value of a specified color gamut using addColorStop, including the offset and color. For details about how to set the color gamut mode of the window to wide color gamut, see [setWindowColorSpace](../arkts-apis-window-Window.md#setwindowcolorspace).
```

```TypeScript


The following example demonstrates the brightness difference between SDR and HDR gradients. Through ColorMetrics, you can construct HDR colors in the BT2020 color gamut, where color component values can exceed 1.0. The portion exceeding 1.0 is used to represent highlight effects beyond the normal screen brightness range. The left side uses an sRGB red-to-white-to-green gradient, while the right side uses HDR colors in the BT2020 color gamut with a highlight white brightness multiplier of 1.5. On an HDR-capable screen, the highlight area on the right is noticeably brighter than that on the left.

> NOTE
> 
> When using HDR colors, you must set the color gamut mode of the window where the Canvas component is located to the wide gamut mode (WIDE_GAMUT) through the [setWindowColorSpace](../arkts-apis-window-Window.md#setwindowcolorspace) method. Otherwise, the HDR brightening effect will not take effect.

Since API version 26.0.0, the [addColorStop](#addcolorstop) API additionally supports HDR brightening through the ColorMetrics type input parameter.
```

<a id="addcolorstop-1"></a>

## addColorStop

```TypeScript
addColorStop(offset: number, color: string | ColorMetrics): void
```

Sets the gradient breakpoint value, including the offset and color. Colors in RGB or ARGB format are supported. P3 wide color gamut color values can be set by passing in the ColorMetrics type. Since API version 26.0.0, BT2020 wide color gamut and HDR brightening are also supported.

> **NOTE:** 
> 
> Only the fillStyle and
> strokeStyle attributes of the
> [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) object support setting a
> wide color gamut **CanvasGradient** object. When using HDR colors, you must set the
> color gamut mode of the window where the **Canvas** component is located to the wide
> gamut mode **WIDE_GAMUT** through the
> [setWindowColorSpace](../arkts-apis/arkts-arkui-window-window-i.md#setwindowcolorspace) method. If the preceding
> conditions are not met, the wide color gamut color settings will not take effect.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Proportion of the distance from the gradient breakpoint to the start point to the total length. The value range is [0, 1].<br> Setting **offset** &lt; 0 or **offset**   > 1 produces no gradient effect.<br> Abnormal values **undefined** and **null** are treated as invalid, and the gradient breakpoint is not added. NaN causes the **CanvasGradient** object to be abnormal and unable to generate gradient effects properly. Infinity causes the entire **CanvasGradient** to not take effect. |
| color | string &#124; [ColorMetrics](../arkts-apis/arkts-arkui-colormetrics-t.md) | Yes | Color of the gradient. The string type supports the following formats: **'rgb(255, 255, 255)'**, **'rgba(255, 255, 255, 1.0)'**, **'#RGB'**, **'#ARGB'**, **'#RRGGBB'**, and **'#AARRGGBB'**.<br> You can use the [colorWithSpace](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md#colorwithspace) method to construct a color with a specified color space attribute. The **ColorMetrics** type can construct a color with the specified color space attribute ColorSpace set to **sRGB** or **DISPLAY_P3**. Since API version 26.0.0, constructing a color in the BT2020 color space is supported, along with HDR brightening. All gradient breakpoints in the same **CanvasGradient** object must use the same color space attribute. If different color spaces are set, an exception is thrown with error code 103701, the breakpoint is not added, and the **CanvasGradient** object retains its previous state.<br> No gradient effect is produced when the color is not set in the required format. **null** and **undefined** are treated as invalid, and the breakpoint is not added. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | The color's ColorSpace is not the same as the last color's. |

**Examples**

See [addColorStop](#addcolorstop)
