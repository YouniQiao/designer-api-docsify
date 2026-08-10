# OffscreenCanvasRenderingContext2DInterface

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

> **说明：**
> 
> OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，
> ServiceExtensionAbility中建议使用
> [Drawing模块](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md)
> 进行离屏绘制。
> 
> beginPath、moveTo、lineTo、closePath、bezierCurveTo、quadraticCurveTo、arc、arcTo、ellipse、rect和
> roundRect接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对
> [CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)
> 和[Path2D](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-path2d.md)
> 对象中设置的路径生效。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface--><!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes |  |
| height | number | Yes |  |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md) |  |

## [[Call]]

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D
```

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes |  |
| height | number | Yes |  |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No |  |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md) |  |

