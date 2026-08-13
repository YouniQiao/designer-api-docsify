# OffscreenCanvas

Draw an object off the screen. The drawing content is not directly displayed on the screen.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class OffscreenCanvas--><!--Device-unnamed-export declare class OffscreenCanvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, unit?: LengthMetricsUnit)
```

Constructor of the off-screen canvas, which is used to create an off-screen canvas object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-constructor(width: double, height: double, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: double, height: double, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | Width of the off-screen canvas. |
| height | double | Yes | Height of the off-screen canvas. |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | No | the unit mode |

## getContext

```TypeScript
getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

Creates the context from the current OffscreenCanvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: '2d', options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextType | '2d' | Yes | The context type, only '2d' be supported now. '2d': Creates a [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md#OffscreenCanvasRenderingContext2D) object representing a two-dimensional rendering context. |
| options | [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md) | No | Drawing attribute. For details, see [RenderingContextSettings](arkts-arkui-canvas-renderingcontextsettings-c.md#RenderingContextSettings). |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-offscreencanvasrenderingcontext2d-c.md) | The rendering context of offscreen canvas, see { |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap | undefined
```

Exports rendered content as an ImageBitmap object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap | undefined--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) |  |

