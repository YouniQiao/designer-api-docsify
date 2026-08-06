# CanvasRenderingContext2D

Draw context object for the Canvas component.

**Inheritance/Implementation:** CanvasRenderingContext2D extends [CanvasRenderer](canvas-canvasrenderer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CanvasRenderingContext2D extends CanvasRenderer--><!--Device-unnamed-export declare class CanvasRenderingContext2D extends CanvasRenderer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

Constructor of the canvas drawing context object, which is used to create a drawing context object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-CanvasRenderingContext2D-constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| settings | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Drawing attribute. For details, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| unit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the unit mode |

## getContext2DFromDrawingContext

```TypeScript
static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D
```

Retrieves a 2D rendering context from the specified drawing context.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D--><!--Device-CanvasRenderingContext2D-static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| drawingContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | A drawing rendering context. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | options of the 2D rendering context. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Returns a 2D rendering context that is bound to the same canvas component as the input drawingContext. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103702](../../errorcode-canvas.md#103702-drawing-context-is-not-bound-to-any-canvas-component) | The drawingContext is not bound to a canvas component. @static |

## offAttach

```TypeScript
offAttach(callback?: VoidCallback): void
```

Unregister the listener that watches if the canvasrenderingcontext2d attached to the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-offAttach(callback?: VoidCallback): void--><!--Device-CanvasRenderingContext2D-offAttach(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## offDetach

```TypeScript
offDetach(callback?: VoidCallback): void
```

Unregister the listener that watches if the canvasrenderingcontext2d detached from the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-offDetach(callback?: VoidCallback): void--><!--Device-CanvasRenderingContext2D-offDetach(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onAttach

```TypeScript
onAttach(callback: VoidCallback): void
```

Register the listener that watches if the canvasrenderingcontext2d attached to the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-onAttach(callback: VoidCallback): void--><!--Device-CanvasRenderingContext2D-onAttach(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onDetach

```TypeScript
onDetach(callback: VoidCallback): void
```

Register the listener that watches if the canvasrenderingcontext2d detached from the Canvas frameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-onDetach(callback: VoidCallback): void--><!--Device-CanvasRenderingContext2D-onDetach(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## startImageAnalyzer

```TypeScript
startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>
```

Start image analyzer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>--><!--Device-CanvasRenderingContext2D-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Image analyzer config. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [110001](../../arkui-ts/errorcode-image-analyzer.md#110001-ai-image-analysis-not-supported) | Image analysis feature is not supported. |
| [110002](../../arkui-ts/errorcode-image-analyzer.md#110002-ai-image-analysis-already-in-progress) | Image analysis is currently being executed. |
| [110003](../../arkui-ts/errorcode-image-analyzer.md#110003-ai-image-analysis-terminated) | Image analysis is stopped. |

## stopImageAnalyzer

```TypeScript
stopImageAnalyzer(): void
```

Stop image analyzer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

## canvas

```TypeScript
get canvas(): FrameNode | null
```

Frame node of the canvas. The default value is null.

**Type:** FrameNode

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-get canvas(): FrameNode | null--><!--Device-CanvasRenderingContext2D-get canvas(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
get height(): double
```

The default value is 0, which is bound to the height of the specified canvas. The value is read-only.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-get height(): double--><!--Device-CanvasRenderingContext2D-get height(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
get width(): double
```

The default value is 0, which is bound to the width of the specified canvas. The value is read-only.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderingContext2D-get width(): double--><!--Device-CanvasRenderingContext2D-get width(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

