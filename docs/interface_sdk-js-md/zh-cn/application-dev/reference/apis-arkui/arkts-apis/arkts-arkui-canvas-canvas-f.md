# Canvas

## Canvas

```TypeScript
export declare function Canvas(
  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions
): CanvasAttribute
```

创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。 CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象。 DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象。 异常值null和undefined按未设置context处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvas-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-canvas-drawingrenderingcontext-c.md) | 否 |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |


## Canvas

```TypeScript
export declare function Canvas(
  params: CanvasParams
): CanvasAttribute
```

使用CanvasParams创建不缓存指令的Canvas组件。 创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。 Canvas组件未设置固定尺寸时，默认扩展至其最大可用尺寸。

> **说明：**&gt;
> - 使用本接口创建的Canvas组件将在onReady回调的入参中返回一个
> DrawingRenderingContext对象，可用于在该Canvas组件上进行绘制。&gt;
> - 使用这个接口创建的Canvas组件在组件不可见时将不响应绘制指令。&gt;
> - 不可见场景主要包括组件所在的页面进入后台、组件滑到窗口外、
> 设置visibility属性为隐藏等，不包括组件被其他组件或是其他窗口遮挡导致不可见的场景。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [CanvasParams](arkts-arkui-canvas-canvasparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |


## Canvas

```TypeScript
export declare function Canvas(
    style_: CustomBuilderT<CanvasAttribute>
): CanvasAttribute
```

Defines Canvas Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |
