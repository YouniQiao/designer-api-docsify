# OffscreenCanvas

OffscreenCanvas组件用于绘制自定义图形。使用Canvas组件或CanvasRenderingContext2D对象时，渲染、动画和用户交互通常发生在应用程序的主线程上，与画布动画和渲染相关的计算可能会影响应用程序性能。OffscreenCanvas提供了一个可以在屏幕外渲染的画布，这样可以在单独的线程中运行一些任务，从而避免影响应用程序主线程性能。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class OffscreenCanvas--><!--Device-unnamed-export declare class OffscreenCanvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, unit?: LengthMetricsUnit)
```

构造用于创建离屏画布对象的OffscreenCanvas，支持配置OffscreenCanvas的单位模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-constructor(width: double, height: double, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: double, height: double, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | OffscreenCanvas组件的宽度。 异常值NaN和Infinity按无效值处理。默认单位为vp。 |
| height | double | Yes | OffscreenCanvas组件的高度。 异常值NaN和Infinity按无效值处理。默认单位为vp。 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | 用来配置OffscreenCanvas对象的单位模式， 配置后无法动态更改。异常值NaN和Infinity按默认值处理。默认值：DEFAULT。 |

## getContext

```TypeScript
getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

返回OffscreenCanvas组件的绘图上下文。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextType | '2d' | Yes | OffscreenCanvas组件绘图上下文的类型，当前仅支持"2d"类型。 "2d"：创建一个表示二维渲染上下文的OffscreenCanvasRenderingContext2D对象。 异常值undefined和null按无效值处理，当前接口返回undefined。 |
| options | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | 用来配置OffscreenCanvasRenderingContext2D 对象的参数，见RenderingContextSettings。 异常值undefined和null按RenderingContextSettings的默认值处理。默认值：null。 |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md) | OffscreenCanvas组件的绘图上下文。 如果getContext方法的入参contextType为"2d"以外类型（包括null或者undefined）， 返回undefined，使用前应判断返回值是否为undefined。 |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap | undefined
```

从OffscreenCanvas组件中最近渲染的图像创建一个ImageBitmap对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap | undefined--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | 创建的ImageBitmap对象。 |

## height

```TypeScript
set height(height: double)
```

OffscreenCanvas组件的高度。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-set height(height: double)--><!--Device-OffscreenCanvas-set height(height: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
set width(width: double)
```

OffscreenCanvas组件的宽度。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-set width(width: double)--><!--Device-OffscreenCanvas-set width(width: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

