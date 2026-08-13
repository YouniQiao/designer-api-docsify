# CanvasRenderingContext2D

After the **CanvasRenderingContext2D** object is bound to the **Canvas** component, you can draw shapes, texts, and images on the **Canvas** component. > **NOTE：**> > * It is recommended that the **CanvasRenderingContext2D** object and the **Canvas** component be > encapsulated into the same custom component, ensuring a one-to-one correspondence and consistent > lifecycle between them. > > * When you call drawing APIs in this module, the commands are stored in the associated **Canvas** > component's command queue. These commands are only executed when the current frame enters the > rendering phase and the associated **Canvas** component is visible. Therefore, when the **Canvas** > component is invisible (for example, off-screen or hidden), avoid frequent drawing calls to prevent > command queue buildup and excessive memory usage. For best practices, see > [Controlling Canvas Rendering Based on Component Visibility](../../../ui/arkts-drawing-customization-on-canvas.md#controlling-canvas-rendering-based-on-component-visibility). > > * The following path-related APIs apply only to paths created within **CanvasRenderingContext2D** > and do not affect paths defined in > [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md#OffscreenCanvasRenderingContext2D) > or [Path2D](arkts-arkui-path2d-c.md#Path2D): > [beginPath](arkts-arkui-canvasrenderer-c.md#beginPath), [moveTo](#moveto), [lineTo](#lineto), [closePath](arkts-arkui-canvaspath-c.md#closePath), > [bezierCurveTo](arkts-arkui-canvaspath-c.md#bezierCurveTo), [quadraticCurveTo](arkts-arkui-canvaspath-c.md#quadraticCurveTo), [arc](arkts-arkui-canvaspath-c.md#arc), > [arcTo](#arcto), [ellipse](#ellipse), [rect](#rect), and [roundRect](#roundrect20). > > * When the width or height of the **Canvas** component exceeds 8000 px, rendering via the CPU > causes significant performance degradation.

**Inheritance/Implementation:** CanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvasrenderer-c.md#CanvasRenderer)

**Since:** 8

**Deprecated since:** -1

<!--Device-unnamed-declare class CanvasRenderingContext2D--><!--Device-unnamed-declare class CanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(settings?: RenderingContextSettings)
```

Constructs a canvas object, which supports configuration of parameters for the **CanvasRenderingContext2D** object.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings)--><!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No |

## constructor

```TypeScript
constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

Creates a **CanvasRenderingContext2D** object, allowing for initial configuration of rendering parameters and unit mode.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | No |

## getContext2DFromDrawingContext

```TypeScript
static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D
```

Obtains a **CanvasRenderingContext2D** object from a **DrawingRenderingContext** object. This **CanvasRenderingContext2D** object is bound to the same **Canvas** component as the input **DrawingRenderingContext** object. > **NOTE：**> > - The **CanvasRenderingContext2D** object obtained via this API cannot be used as a > parameter to create a Canvas > component. Otherwise, the application crashes. > > - If the input **DrawingRenderingContext** object is not bound to a **Canvas** component, > an error code is returned.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D--><!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| drawingContext | [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | Yes |
| options | [RenderingContextOptions](arkts-arkui-renderingcontextoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [103702](../errorcode-canvas.md#103702-drawing-context-is-not-bound-to-any-canvas-component) |

## off_onAttach

```TypeScript
off(type: 'onAttach', callback?: Callback<void>): void
```

Unsubscribes from the event when a **CanvasRenderingContext2D** object is bound to a **Canvas** component.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CanvasRenderingContext2D-off(type: 'onAttach', callback?: Callback<void>): void--><!--Device-CanvasRenderingContext2D-off(type: 'onAttach', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'onAttach' | Yes |
| callback | Callback & lt;void & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_onDetach

```TypeScript
off(type: 'onDetach', callback?: Callback<void>): void
```

Unsubscribes from the event when a **CanvasRenderingContext2D** object is unbound from a **Canvas** component.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CanvasRenderingContext2D-off(type: 'onDetach', callback?: Callback<void>): void--><!--Device-CanvasRenderingContext2D-off(type: 'onDetach', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'onDetach' | Yes |
| callback | Callback & lt;void & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_onAttach

```TypeScript
on(type: 'onAttach', callback: Callback<void>): void
```

Subscribes to the event when a **CanvasRenderingContext2D** object is bound to a **Canvas** component. > **NOTE：**> > A **CanvasRenderingContext2D** object can only be bound to one **Canvas** component > at a time.&lt;br&gt; > When a **CanvasRenderingContext2D** object is bound to a **Canvas** component, the > **onAttach** callback is triggered, indicating that the > [canvas](#canvas) > object is accessible.&lt;br&gt; > Avoid performing drawing operations in the **onAttach** callback. Make sure the > **Canvas** component has completed its > onReady > event before performing any drawing.&lt;br&gt; > The **onAttach** callback is triggered when:&lt;br&gt; > 1. A **Canvas** component is created and bound to a **CanvasRenderingContext2D** > object.&lt;br&gt; > 2. A **CanvasRenderingContext2D** object is bound to a new **Canvas** component.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CanvasRenderingContext2D-on(type: 'onAttach', callback: Callback<void>): void--><!--Device-CanvasRenderingContext2D-on(type: 'onAttach', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'onAttach' | Yes |
| callback | Callback & lt;void & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_onDetach

```TypeScript
on(type: 'onDetach', callback: Callback<void>): void
```

Subscribes to the event when a **CanvasRenderingContext2D** object is unbound from a **Canvas** component. > **NOTE：**> > When a **CanvasRenderingContext2D** object is unbound from a **Canvas** component, > the **onDetach** callback is triggered. In this case, cease any drawing operations.&lt;br&gt; > The **onDetach** callback is triggered when:&lt;br&gt; > 1. A **Canvas** component is destroyed and unbound from a **CanvasRenderingContext2D** > object.&lt;br&gt; > 2. A **CanvasRenderingContext2D** object is bound to a different **Canvas** component, > causing the existing binding to be released.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CanvasRenderingContext2D-on(type: 'onDetach', callback: Callback<void>): void--><!--Device-CanvasRenderingContext2D-on(type: 'onDetach', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'onDetach' | Yes |
| callback | Callback & lt;void & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## startImageAnalyzer

```TypeScript
startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>
```

Configures and starts the AI analyzer. This API uses a promise to return the result. Before use, set enableAnalyzer to **true** to enable the image AI analyzer.&lt;br&gt;Because the image frame used for analysis is the one captured when this API is called, pay attention to the invoking time of this API.&lt;br&gt; Repeated calls to this method before completion trigger an error callback. For the sample code, see the code for **stopImageAnalyzer**. > **NOTE：**> > The image analysis type cannot be dynamically modified. > When image changes are detected, the analysis result is automatically destroyed. You can > call this API again to start analysis. > This API depends on device capabilities. If it is called on an incompatible device, an > error code is returned.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>--><!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ImageAnalyzerConfig](../arkts-apis/arkts-arkui-imageanalyzerconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [110001](../arkui-ts/errorcode-image-analyzer.md#110001-ai-image-analysis-not-supported) |
| [110003](../arkui-ts/errorcode-image-analyzer.md#110003-ai-image-analysis-terminated) |
| [110002](../arkui-ts/errorcode-image-analyzer.md#110002-ai-image-analysis-already-in-progress) |

## stopImageAnalyzer

```TypeScript
stopImageAnalyzer(): void
```

Stops AI image analysis. The content displayed by the AI image analyzer will be destroyed. > **NOTE：**> > If this API is called when the **startImageAnalyzer** API has not yet returned any result, > an error is reported. > This feature depends on device capabilities.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasRenderingContext2D-stopImageAnalyzer(): void--><!--Device-CanvasRenderingContext2D-stopImageAnalyzer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: any): string
```

Creates a data URL that contains a representation of an image. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string--><!--Device-CanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | No |
| quality | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## canvas

```TypeScript
readonly canvas: FrameNode
```

FrameNode instance of the **Canvas** component associated with **CanvasRenderingContext2D**. It can be used to listen for the visibility status of the associated **Canvas** component. Default value: **null**

**Type:** [FrameNode](arkts-arkui-framenode-t.md)

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CanvasRenderingContext2D-readonly canvas: FrameNode--><!--Device-CanvasRenderingContext2D-readonly canvas: FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
readonly height: number
```

Component height. Default unit: vp

**Type:** number

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderingContext2D-readonly height: number--><!--Device-CanvasRenderingContext2D-readonly height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

Component width. Default unit: vp

**Type:** number

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderingContext2D-readonly width: number--><!--Device-CanvasRenderingContext2D-readonly width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
