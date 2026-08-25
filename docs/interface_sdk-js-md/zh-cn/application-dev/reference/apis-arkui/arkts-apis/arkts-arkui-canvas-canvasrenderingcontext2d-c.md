# CanvasRenderingContext2D

CanvasRenderingContext2D对象与Canvas组件绑定后，可在Canvas组件上绘制， 绘制对象可以是形状、文本、图片等。@extends CanvasRenderer

**继承/实现关系：** CanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvas-canvasrenderer-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数和单位模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | 否 |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | 否 |

## getContext2DFromDrawingContext

```TypeScript
static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D
```

从一个DrawingRenderingContext对象中获取一个CanvasRenderingContext2D对象， 该CanvasRenderingContext2D对象与入参的DrawingRenderingContext对象绑定了相同的Canvas组件。

> **说明：**&gt;
> - 从该接口获取的CanvasRenderingContext2D对象不允许作为参数创建Canvas组件，
> 否则会导致应用崩溃。&gt;
> - 当入参的DrawingRenderingContext对象未绑定Canvas组件时，将返回错误码。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawingContext | [DrawingRenderingContext](arkts-arkui-canvas-drawingrenderingcontext-c.md) | 是 |
| options | [RenderingContextOptions](arkts-arkui-canvas-renderingcontextoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [CanvasRenderingContext2D](arkts-arkui-canvas-canvasrenderingcontext2d-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [103702](../errorcode-canvas.md#103702-绘制上下文未绑定canvas组件) |

## offAttach

```TypeScript
offAttach(callback?: VoidCallback): void
```

取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## offDetach

```TypeScript
offDetach(callback?: VoidCallback): void
```

取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onAttach

```TypeScript
onAttach(callback: VoidCallback): void
```

订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

> **说明：**&gt;
> CanvasRenderingContext2D对象在同一时间只能与一个Canvas组件绑定。
> 当CanvasRenderingContext2D对象和Canvas组件发生绑定时，会触发'onAttach'回调，
> 表示可以获取到canvas。
> 避免在'onAttach'中执行绘制方法，应保证Canvas组件已经'onReady'再进行绘制。
> 触发'onAttach'回调的一般场景：
> 1、Canvas组件创建时绑定CanvasRenderingContext2D对象;
> 2、CanvasRenderingContext2D对象新绑定一个Canvas组件时。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onDetach

```TypeScript
onDetach(callback: VoidCallback): void
```

订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

> **说明：**&gt;
> 当CanvasRenderingContext2D对象和Canvas组件解除绑定时，会触发'onDetach'回调，
> 表示应停止绘制行为。
> 触发'onDetach'回调的一般场景：
> 1、Canvas组件销毁时解除绑定CanvasRenderingContext2D对象;
> 2、CanvasRenderingContext2D对象新绑定一个Canvas组件，会先解除已有的绑定。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## startImageAnalyzer

```TypeScript
startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>
```

配置并启动AI分析功能，使用Promise异步回调。 使用前需先设置enableAnalyzer为true，启用图像AI分析能力。 该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机， 避免出现画面和分析内容不一致的情况。 未执行完重复调用该方法会触发错误回调。

> **说明：**&gt;
> 分析类型不支持动态修改。
> 当检测到画面有变化时，分析结果将自动销毁，可重新调用本接口启动分析。
> 该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ImageAnalyzerConfig](arkts-arkui-imagecommon-imageanalyzerconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [110001](../arkui-ts/errorcode-image-analyzer.md#110001-ai图像分析功能不支持) |
| [110002](../arkui-ts/errorcode-image-analyzer.md#110002-ai图像分析正在进行中) |
| [110003](../arkui-ts/errorcode-image-analyzer.md#110003-ai图像分析已停止) |

## stopImageAnalyzer

```TypeScript
stopImageAnalyzer(): void
```

停止AI分析功能，AI分析展示的内容将被销毁。

> **说明：**&gt;
> 在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。
> 该特性依赖设备能力。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: double): string
```

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 否 |
| quality | double | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## canvas

```TypeScript
get canvas(): FrameNode | null
```

获取和CanvasRenderingContext2D关联的Canvas组件的FrameNode实例。 可用于监听关联的Canvas组件的可见状态。默认值：null。

**类型：** [FrameNode](arkts-arkui-framenode-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
get height(): double
```

组件高度，默认单位：vp。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
get width(): double
```

组件宽度，默认单位：vp。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
