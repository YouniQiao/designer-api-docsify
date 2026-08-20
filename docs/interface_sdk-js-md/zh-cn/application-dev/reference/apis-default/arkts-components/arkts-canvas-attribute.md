# CanvasAttribute

提供画布组件，用于自定义绘制图形。

@extends CommonMethod @interface CanvasAttribute

**继承/实现关系：** CanvasAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface CanvasAttribute--><!--Device-unnamed-export declare interface CanvasAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<CanvasAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CanvasAttribute-attributeModifier(modifier: AttributeModifier<CanvasAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CanvasAttribute-attributeModifier(modifier: AttributeModifier<CanvasAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CanvasAttribute](arkts-canvas-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasAttribute](arkts-canvas-attribute.md) |  |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean | undefined): this
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。 需要搭配CanvasRenderingContext2D中的startImageAnalyzer和stopImageAnalyzer一起使用。 不能和overlay属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。 该特性依赖设备能力。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CanvasAttribute-enableAnalyzer(enable: boolean | undefined): this--><!--Device-CanvasAttribute-enableAnalyzer(enable: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 | 组件支持AI分析，需要组件内容支持主体识别、 文字识别或对象查找。设置为true时，组件可进行AI分析， 设置为false时，组件不可进行AI分析。 异常值null和undefined按默认值处理。默认值：false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasAttribute](arkts-canvas-attribute.md) |  |

## onReady

```TypeScript
onReady(event: Callback<DrawingRenderingContext | undefined> | undefined): this
```

Canvas组件初始化完成或者发生大小变化时的事件回调。 当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取， 可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时， 只触发onAreaChange事件，不触发onReady事件。 onAreaChange事件在onReady事件后触发。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CanvasAttribute-onReady(event: Callback<DrawingRenderingContext | undefined> | undefined): this--><!--Device-CanvasAttribute-onReady(event: Callback<DrawingRenderingContext | undefined> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[DrawingRenderingContext](arkts-canvas-drawingrenderingcontext-c.md) \| undefined&gt; \| undefined | 是 | Canvas组件初始化完成或者发生大小变化时的回调事件。 关于Callback&lt;DrawingRenderingContext \| undefined&gt;类型的入参： 1. 只有使用CanvasParams创建的Canvas组件在该回调中返回DrawingRenderingContext对象， 否则返回undefined。 2. 该回调返回的DrawingRenderingContext对象不允许作为参数创建Canvas组件， 否则会导致应用崩溃。 取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasAttribute](arkts-canvas-attribute.md) |  |

## setCanvasOptions

```TypeScript
setCanvasOptions(context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-CanvasAttribute-setCanvasOptions(context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): this--><!--Device-CanvasAttribute-setCanvasOptions(context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-canvas-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-canvas-drawingrenderingcontext-c.md) | 否 |  |
| imageAIOptions | [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setCanvasOptions

```TypeScript
setCanvasOptions(params: CanvasParams): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-CanvasAttribute-setCanvasOptions(params: CanvasParams): this--><!--Device-CanvasAttribute-setCanvasOptions(params: CanvasParams): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [CanvasParams](arkts-canvas-canvasparams-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

Set Canvas options.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CanvasAttribute-default--><!--Device-CanvasAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

