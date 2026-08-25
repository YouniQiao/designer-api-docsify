# CanvasAttribute

提供画布组件，用于自定义绘制图形。@extends CommonMethod @interface CanvasAttribute

**继承/实现关系：** CanvasAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<CanvasAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean | undefined): this
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。 需要搭配CanvasRenderingContext2D中的startImageAnalyzer和stopImageAnalyzer一起使用。 不能和overlay属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。 该特性依赖设备能力。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |

## onReady

```TypeScript
onReady(event: Callback<DrawingRenderingContext | undefined> | undefined): this
```

Canvas组件初始化完成或者发生大小变化时的事件回调。 当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取， 可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时， 只触发onAreaChange事件，不触发onReady事件。 onAreaChange事件在onReady事件后触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DrawingRenderingContext](arkts-arkui-canvas-drawingrenderingcontext-c.md) \| undefined & gt; \ | undefined | 是 | Canvas组件初始化完成或者发生大小变化时的回调事件。 关于Callback & lt;DrawingRenderingContext \ |

**返回值：**

| 类型 |
| --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |

## setCanvasOptions

```TypeScript
default setCanvasOptions(context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): this
```

Set Canvas options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

## setCanvasOptions

```TypeScript
default setCanvasOptions(params: CanvasParams): this
```

Set Canvas options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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
