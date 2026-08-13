# CanvasRenderingContext2D

Draw context object for the Canvas component.

**Inheritance/Implementation:** CanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvas-canvasrenderer-c.md#CanvasRenderer)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class CanvasRenderingContext2D--><!--Device-unnamed-export declare class CanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

Constructor of the canvas drawing context object, which is used to create a drawing context object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| settings | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | Drawing attribute. For details, see [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md#RenderingContextSettings). |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | the unit mode |

## getContext2DFromDrawingContext

```TypeScript
static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D
```

Retrieves a 2D rendering context from the specified drawing context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D--><!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| drawingContext | [DrawingRenderingContext](arkts-arkui-canvas-drawingrenderingcontext-c.md) | Yes | A drawing rendering context. |
| options | [RenderingContextOptions](arkts-arkui-canvas-renderingcontextoptions-i.md) | No | options of the 2D rendering context. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasRenderingContext2D](arkts-arkui-canvas-canvasrenderingcontext2d-c.md) | Returns a 2D rendering context that is bound to the same canvas component as the input drawingContext. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103702](../errorcode-canvas.md#103702-drawing-context-is-not-bound-to-any-canvas-component) | The drawingContext is not bound to a canvas component. @static |

## offAttach

```TypeScript
offAttach(callback?: VoidCallback): void
```

Unregister the listener that watches if the canvasrenderingcontext2d attached to the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-offAttach(callback?: VoidCallback): void--><!--Device-CanvasRenderingContext2D-offAttach(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## offDetach

```TypeScript
offDetach(callback?: VoidCallback): void
```

Unregister the listener that watches if the canvasrenderingcontext2d detached from the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-offDetach(callback?: VoidCallback): void--><!--Device-CanvasRenderingContext2D-offDetach(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onAttach

```TypeScript
onAttach(callback: VoidCallback): void
```

Register the listener that watches if the canvasrenderingcontext2d attached to the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-onAttach(callback: VoidCallback): void--><!--Device-CanvasRenderingContext2D-onAttach(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onDetach

```TypeScript
onDetach(callback: VoidCallback): void
```

Register the listener that watches if the canvasrenderingcontext2d detached from the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-onDetach(callback: VoidCallback): void--><!--Device-CanvasRenderingContext2D-onDetach(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## startImageAnalyzer

```TypeScript
startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>
```

Start image analyzer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>--><!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](../../apis-na/arkts-apis/arkts-na-imagecommon-imageanalyzerconfig-i.md) | Yes | Image analyzer config. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [110001](../arkui-ts/errorcode-image-analyzer.md#110001-ai-image-analysis-not-supported) | Image analysis feature is not supported. |
| [110003](../arkui-ts/errorcode-image-analyzer.md#110003-ai-image-analysis-terminated) | Image analysis is stopped. |
| [110002](../arkui-ts/errorcode-image-analyzer.md#110002-ai-image-analysis-already-in-progress) | Image analysis is currently being executed. |

## stopImageAnalyzer

```TypeScript
stopImageAnalyzer(): void
```

Stop image analyzer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-stopImageAnalyzer(): void--><!--Device-CanvasRenderingContext2D-stopImageAnalyzer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: double): string
```

Generate a character string in the data url format.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string--><!--Device-CanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | No | Image format. The default value is image/png. |
| quality | double | No | If the image format is image/jpeg or image/webp, you can select the image quality from 0 to 1. If the value is out of the range, the default value 0.92 is used. |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

