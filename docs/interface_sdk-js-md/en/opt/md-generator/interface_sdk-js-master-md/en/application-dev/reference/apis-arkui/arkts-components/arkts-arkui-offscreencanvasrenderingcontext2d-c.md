# OffscreenCanvasRenderingContext2D

Use **OffscreenCanvasRenderingContext2D** to draw shapes, images, and text offscreen onto a canvas. Rendering offscreen onto a canvas is a process where content to draw onto the canvas is first drawn in the buffer, and then converted into a picture, and finally the picture is drawn on the canvas. Since off-screen rendering utilizes the CPU, its performance is relatively slow. Therefore, it should be avoided in scenarios where drawing speed is a critical requirement. > **NOTE：**> > **OffscreenCanvasRenderingContext2D** cannot be used in **ServiceExtensionAbility**. It is > recommended that you use the > [drawing module](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md) > for offscreen rendering in **ServiceExtensionAbility**. > > The following path-related APIs apply only to paths created within > **OffscreenCanvasRenderingContext2D** and do not affect paths defined in > [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md#CanvasRenderingContext2D) > or [Path2D](arkts-arkui-path2d-c.md#Path2D): > [beginPath](arkts-arkui-canvasrenderer-c.md#beginPath), [moveTo](#moveto), [lineTo](#lineto), [closePath](arkts-arkui-canvaspath-c.md#closePath), > [bezierCurveTo](arkts-arkui-canvaspath-c.md#bezierCurveTo), [quadraticCurveTo](arkts-arkui-canvaspath-c.md#quadraticCurveTo), [arc](arkts-arkui-canvaspath-c.md#arc), > [arcTo](#arcto), [ellipse](#ellipse), [rect](#rect), and [roundRect](#roundrect20).

**Inheritance/Implementation:** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](arkts-arkui-canvasrenderer-c.md#CanvasRenderer)

**Since:** 8

**Deprecated since:** -1

<!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D--><!--Device-unnamed-declare class OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings)
```

Creates an offscreen canvas object. You can configure the canvas width, canvas height, and parameters of the **OffscreenCanvasRenderingContext2D** object.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No |

## constructor

```TypeScript
constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

Creates an offscreen canvas object. You can configure the canvas width, canvas height, and parameters and their unit of the **OffscreenCanvasRenderingContext2D** object.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No |
| unit | [LengthMetricsUnit](../../apis-na/arkts-apis/arkts-na-lengthmetricsunit-t.md) | No |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: any): string
```

Creates a data URL that contains a representation of an image. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string--><!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: any): string-End-->

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

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

Creates an **ImageBitmap** object from the most recently rendered image of the offscreen canvas.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) |
