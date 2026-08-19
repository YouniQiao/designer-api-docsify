# OffscreenCanvasRenderingContext2DInterface

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。 离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。 离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。 &gt; **说明：** &gt; &gt; OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用， &gt; ServiceExtensionAbility中建议使用 &gt; [Drawing模块](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md) &gt; 进行离屏绘制。 &gt; &gt; beginPath、moveTo、lineTo、closePath、bezierCurveTo、quadraticCurveTo、arc、arcTo、ellipse、rect和 &gt; roundRect接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对 &gt; [CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md) &gt; 和[Path2D](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-path2d.md) &gt; 对象中设置的路径生效。

**起始版本：** 8

<!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface--><!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

**起始版本：** 8

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 |  |
| height | number | 是 |  |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## constructor

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D
```

**起始版本：** 12

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 |  |
| height | number | 是 |  |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |  |
| unit | LengthMetricsUnit | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
