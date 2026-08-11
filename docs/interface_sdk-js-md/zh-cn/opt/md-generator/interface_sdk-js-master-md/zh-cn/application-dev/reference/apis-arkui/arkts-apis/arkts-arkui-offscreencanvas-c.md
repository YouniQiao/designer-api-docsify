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

**起始版本：** 8

<!--Device-unnamed-declare class OffscreenCanvas--><!--Device-unnamed-declare class OffscreenCanvas-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number)
```

构造用于创建离屏画布对象的OffscreenCanvas。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvas-constructor(width: number, height: number)--><!--Device-OffscreenCanvas-constructor(width: number, height: number)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [width](#width) | number | 是 |
| [height](#height) | number | 是 |

## constructor

```TypeScript
constructor(width: number, height: number, unit: LengthMetricsUnit)
```

构造用于创建离屏画布对象的OffscreenCanvas，支持配置OffscreenCanvas的单位模式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [width](#width) | number | 是 |
| [height](#height) | number | 是 |
| unit | [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md) | 是 |

## getContext

```TypeScript
getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

返回OffscreenCanvas组件的绘图上下文。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| contextType | "2d" | 是 |
| options | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md) |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

从OffscreenCanvas组件中最近渲染的图像创建一个ImageBitmap对象。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) |

## height

```TypeScript
height: number
```

OffscreenCanvas组件的高度。&lt;br&gt;默认单位为vp。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvas-height: number--><!--Device-OffscreenCanvas-height: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

OffscreenCanvas组件的宽度。&lt;br&gt;默认单位为vp。

**类型：** number

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-OffscreenCanvas-width: number--><!--Device-OffscreenCanvas-width: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
