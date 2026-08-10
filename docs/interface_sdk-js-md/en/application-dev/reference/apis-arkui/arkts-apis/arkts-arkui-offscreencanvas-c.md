# OffscreenCanvas

OffscreenCanvas组件用于绘制自定义图形。

使用[Canvas](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-canvas.md)组件或  
[CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)对象时，渲染、动画和用户交互通常发生在应用程序的主线程上，与画布动画和渲染相关的计算可能会影响应用程序性能。OffscreenCanvas提供了一个可以在屏幕外渲染的画布，这样可以在单独的线程中运行一些任务，从而避免影响应用程序主线程性能。

> **说明：**
> 
> OffscreenCanvas无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用
> [Drawing模块](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md)
> 进行离屏绘制。

## 子组件

不支持。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class OffscreenCanvas--><!--Device-unnamed-declare class OffscreenCanvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number)
```

构造用于创建离屏画布对象的OffscreenCanvas。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-constructor(width: number, height: number)--><!--Device-OffscreenCanvas-constructor(width: number, height: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | OffscreenCanvas组件的宽度。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 &lt;br&gt;默认单位为vp。 |
| height | number | Yes | OffscreenCanvas组件的高度。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 &lt;br&gt;默认单位为vp。 |

## constructor

```TypeScript
constructor(width: number, height: number, unit: LengthMetricsUnit)
```

构造用于创建离屏画布对象的OffscreenCanvas，支持配置OffscreenCanvas的单位模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | OffscreenCanvas组件的宽度。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 &lt;br&gt;默认单位为vp。 |
| height | number | Yes | OffscreenCanvas组件的高度。 &lt;br&gt;异常值NaN和Infinity按无效值处理。 &lt;br&gt;默认单位为vp。 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | Yes | 用来配置OffscreenCanvas对象的单位模式，配置后无法动态更改， 配置方法同 [CanvasRenderingContext2D](../../../reference/apis-arkui/arkui-ts/ts-canvasrenderingcontext2d.md)。 &lt;br&gt;异常值NaN和Infinity按默认值处理。 &lt;br&gt;默认值：DEFAULT。 |

## getContext

```TypeScript
getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

返回OffscreenCanvas组件的绘图上下文。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextType | "2d" | Yes | OffscreenCanvas组件绘图上下文的类型，当前仅支持"2d"类型。 &lt;br&gt;"2d"：创建一个表示二维渲染上下文的OffscreenCanvasRenderingContext2D对象。 &lt;br&gt;异常值undefined和null按无效值处理，当前接口返回undefined。 |
| options | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | 用来配置OffscreenCanvasRenderingContext2D对象的参数， 见[RenderingContextSettings](#renderingcontextsettings)。 &lt;br&gt;异常值undefined和null按RenderingContextSettings的默认值处理。 &lt;br&gt;默认值：null。 |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md) | OffscreenCanvas组件的绘图上下文。 如果getContext方法的入参contextType为"2d"以外类型（包括null或者undefined），返回undefined， 使用前应判断返回值是否为undefined。 |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

从OffscreenCanvas组件中最近渲染的图像创建一个ImageBitmap对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 创建的ImageBitmap对象。 |

## height

```TypeScript
height: number
```

OffscreenCanvas组件的高度。&lt;br&gt;默认单位为vp。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-height: number--><!--Device-OffscreenCanvas-height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

OffscreenCanvas组件的宽度。&lt;br&gt;默认单位为vp。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-width: number--><!--Device-OffscreenCanvas-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

