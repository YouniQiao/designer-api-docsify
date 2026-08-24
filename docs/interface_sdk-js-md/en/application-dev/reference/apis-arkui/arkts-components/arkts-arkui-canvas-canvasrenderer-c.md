# CanvasRenderer

Canvas renderer for drawing shapes, text, images and other objects@extends CanvasPath

**Inheritance/Implementation:** CanvasRenderer extends [CanvasPath](arkts-arkui-canvas-canvaspath-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class CanvasRenderer--><!--Device-unnamed-export declare class CanvasRenderer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## beginPath

```TypeScript
beginPath(): void
```

Clear the sub-path list and start a new path.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-beginPath(): void--><!--Device-CanvasRenderer-beginPath(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearRect

```TypeScript
clearRect(x: double, y: double, w: double, h: double): void
```

Clears the drawing content of a rectangular area.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clearRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-clearRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the start point of the rectangle. |
| y | double | Yes | The y-axis coordinate of the start point of the rectangle. |
| w | double | Yes | Width of the rectangle. |
| h | double | Yes | Height of the rectangle. |

## clip

```TypeScript
clip(fillRule?: CanvasFillRule): void
```

Sets the currently created path as the current clipping path

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | Algorithm rule. For details, see [CanvasFillRule](arkts-arkui-canvasfillrule-t.md). |

## clip

```TypeScript
clip(path: Path2D, fillRule?: CanvasFillRule): void
```

Tailoring according to the specified path

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | Yes | Path to be cut. |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | Algorithm rule. For details, see [CanvasFillRule](arkts-arkui-canvasfillrule-t.md). |

## createConicGradient

```TypeScript
createConicGradient(startAngle: double, x: double, y: double): CanvasGradient
```

Creates a gradient around a point with given coordinates.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createConicGradient(startAngle: double, x: double, y: double): CanvasGradient--><!--Device-CanvasRenderer-createConicGradient(startAngle: double, x: double, y: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startAngle | double | Yes | The angle at which to begin the gradient, in radians. Angle measurements start horizontally the right of the center and move around clockwise. |
| x | double | Yes | The x-axis coordinate of the center of the gradient. |
| y | double | Yes | The y-axis coordinate of the center of the gradient. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) | A CanvasGradient object that draws a conic gradient around the given coordinates. |

## createImageData

```TypeScript
createImageData(sw: double, sh: double): ImageData
```

Creates a new, empty ImageData object of the specified size

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createImageData(sw: double, sh: double): ImageData--><!--Device-CanvasRenderer-createImageData(sw: double, sh: double): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sw | double | Yes | Width of the ImageData object. |
| sh | double | Yes | Height of the ImageData object. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |  |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

From an existing ImageData object, copy an object with the same width and height as the image. The image content is not copied.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData--><!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes | ImageData object to be copied. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |  |

## createLinearGradient

```TypeScript
createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient
```

Creates a linear gradient object that is specified along the parameter coordinates

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient--><!--Device-CanvasRenderer-createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x0 | double | Yes | The x-axis coordinate of the start point. |
| y0 | double | Yes | The y-axis coordinate of the start point. |
| x1 | double | Yes | x-axis coordinate of the end point. |
| y1 | double | Yes | y-axis coordinate of the end point. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |  |

## createPattern

```TypeScript
createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null
```

Creates a template object using the specified image

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null--><!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes | Objects as duplicate image sources |
| repetition | string \| null | Yes | Specifies how to repeat images. The following four modes are supported:"repeat": Repeated images in both X and Y directions"repeat-x": Repeated images in the X-axis direction but not in the Y-axis direction"repeat-y": Repeated images in the Y axis direction, but not in the X axis direction."no-repeat": Non-repeating images in both X and Y directions"clamp": Replicate the edge color if the shader draws outside of its original bounds."mirror": Repeat the shader's image horizontally and vertically, alternating mirror images so that adjacent images always seam. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasPattern](arkts-arkui-canvas-canvaspattern-i.md) \| null |  |

## createRadialGradient

```TypeScript
createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient
```

Creates a radioactive gradient object based on parameters that determine the coordinates of two circles

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient--><!--Device-CanvasRenderer-createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x0 | double | Yes | The x-axis coordinate of the start circle. |
| y0 | double | Yes | The y-axis coordinate of the start circle. |
| r0 | double | Yes | Radius of the starting circle. |
| x1 | double | Yes | The x-axis coordinate of the end circle. |
| y1 | double | Yes | The y-axis coordinate of the end circle. |
| r1 | double | Yes | Radius of the end circle. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |  |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) | Yes | Picture objects drawn to the canvas. |
| dx | double | Yes | x-axis coordinate of the upper left corner of the image on the target canvas. |
| dy | double | Yes | y-axis coordinate of the upper left corner of the image on the target canvas. |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) | Yes | Picture objects drawn to the canvas. |
| dx | double | Yes | x-axis coordinate of the upper left corner of the image on the target canvas. |
| dy | double | Yes | y-axis coordinate of the upper left corner of the image on the target canvas. |
| dw | double | Yes | Specifies the drawing width of the image on the target canvas. The width of the drawn image will be scaled. |
| dh | double | Yes | Specifies the drawing height of the image on the target canvas. The height of the drawn image will be scaled. |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,
    dw: double, dh: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,    dw: double, dh: double): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,    dw: double, dh: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) | Yes | Picture objects drawn to the canvas. |
| sx | double | Yes | x coordinate of the upper left corner of the rectangle (cropping) selection box of the image. |
| sy | double | Yes | y coordinate of the upper left corner of the rectangle (cropping) selection box of the image. |
| sw | double | Yes | Width of the rectangle (cropping) selection box of the image. |
| sh | double | Yes | Height of the rectangle (cropping) selection box of the image. |
| dx | double | Yes | x-axis coordinate of the upper left corner of the image on the target canvas. |
| dy | double | Yes | y-axis coordinate of the upper left corner of the image on the target canvas. |
| dw | double | Yes | Specifies the drawing width of the image on the target canvas. The width of the drawn image will be scaled. |
| dh | double | Yes | Specifies the drawing height of the image on the target canvas. The height of the drawn image will be scaled. |

## fill

```TypeScript
fill(fillRule?: CanvasFillRule): void
```

Fills existing paths according to the current fill style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | Algorithm rule. For details, see [CanvasFillRule](arkts-arkui-canvasfillrule-t.md). |

## fill

```TypeScript
fill(path: Path2D, fillRule?: CanvasFillRule): void
```

Fills the specified path according to the current fill style

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | Yes | Path to be filled. |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No | Algorithm rule. For details, see [CanvasFillRule](arkts-arkui-canvasfillrule-t.md). |

## fillRect

```TypeScript
fillRect(x: double, y: double, w: double, h: double): void
```

Fills a specified rectangular area

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fillRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-fillRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the start point of the rectangle. |
| y | double | Yes | The y-axis coordinate of the start point of the rectangle. |
| w | double | Yes | Width of the rectangle. |
| h | double | Yes | Height of the rectangle. |

## fillText

```TypeScript
fillText(text: string, x: double, y: double, maxWidth?: double): void
```

Fills the specified text at the specified location

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-fillText(text: string, x: double, y: double, maxWidth?: double): void--><!--Device-CanvasRenderer-fillText(text: string, x: double, y: double, maxWidth?: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text string to be drawn. |
| x | double | Yes | The x-axis coordinate of the start point of the text. |
| y | double | Yes | The y-axis coordinate of the start point of the text. |
| maxWidth | double | No | Maximum width of the drawing. |

## getImageData

```TypeScript
getImageData(sx: double, sy: double, sw: double, sh: double): ImageData
```

Obtains the pixel data of a specified area on the current canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getImageData(sx: double, sy: double, sw: double, sh: double): ImageData--><!--Device-CanvasRenderer-getImageData(sx: double, sy: double, sw: double, sh: double): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | x coordinate of the upper left corner of the rectangular area of the image data to be extracted. |
| sy | double | Yes | y coordinate of the upper left corner of the rectangular area of the image data to be extracted. |
| sw | double | Yes | The width of the rectangular area of the image data to be extracted. |
| sh | double | Yes | The height of the rectangular area of the image data to be extracted. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |  |

## getLineDash

```TypeScript
getLineDash(): double[]
```

Gets the current segment style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getLineDash(): double[]--><!--Device-CanvasRenderer-getLineDash(): double[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double[] |  |

## getPixelMap

```TypeScript
getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined
```

Obtains the PixelMap of a specified area on the current canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined--><!--Device-CanvasRenderer-getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | x coordinate of the upper left corner of the rectangular area of the PixelMap to be extracted. |
| sy | double | Yes | y coordinate of the upper left corner of the rectangular area of the PixelMap to be extracted. |
| sw | double | Yes | The width of the rectangular area of the PixelMap to be extracted. |
| sh | double | Yes | The height of the rectangular area of the PixelMap to be extracted. |

**Return value:**

| Type | Description |
| --- | --- |
| [PixelMap](arkts-arkui-pixelmap-t.md) \| undefined |  |

## getTransform

```TypeScript
getTransform(): Matrix2D
```

Obtains the currently applied transformation matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-getTransform(): Matrix2D--><!--Device-CanvasRenderer-getTransform(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](../arkts-apis/arkts-arkui-matrix2d-c.md) |  |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

Measure the size of a specified text. For details about the return value, see [TextMetrics](arkts-arkui-canvas-textmetrics-i.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-measureText(text: string): TextMetrics--><!--Device-CanvasRenderer-measureText(text: string): TextMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text string to be measured. |

**Return value:**

| Type | Description |
| --- | --- |
| [TextMetrics](arkts-arkui-canvas-textmetrics-i.md) |  |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string): void
```

Draws the specified ImageData object onto the canvas

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string): void--><!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes | ImageData object to be drawn. |
| dx | double \| string | Yes | Position offset of the source image data in the target canvas (the offset in the x-axis direction). |
| dy | double \| string | Yes | Position offset of the source image data in the target canvas (the offset in the y-axis direction). |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,
    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void
```

Draws the specified ImageData object onto the canvas

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void--><!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes | ImageData object to be drawn. |
| dx | double \| string | Yes | Position offset of the source image data in the target canvas (the offset in the x-axis direction). |
| dy | double \| string | Yes | Position offset of the source image data in the target canvas (the offset in the y-axis direction). |
| dirtyX | double \| string | Yes | Position of the upper left corner of the rectangular area in the source image data. The default is the upper left corner (x coordinate) of the entire image data. |
| dirtyY | double \| string | Yes | Position of the upper left corner of the rectangular area in the source image data. The default is the upper left corner (y coordinate) of the entire image data. |
| dirtyWidth | double \| string | Yes | Width of the rectangular area in the source image data. The default is the width of the image data. |
| dirtyHeight | double \| string | Yes | Height of the rectangular area in the source image data. The default is the height of the image data. |

## reset

```TypeScript
reset(): void
```

Clear the backing buffer, drawing state stack, any defined paths, and styles.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-reset(): void--><!--Device-CanvasRenderer-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetTransform

```TypeScript
resetTransform(): void
```

Resets the current transformation matrix using the identity matrix

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-resetTransform(): void--><!--Device-CanvasRenderer-resetTransform(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

Top of the stack pop-up state in the drawing state stack

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-restore(): void--><!--Device-CanvasRenderer-restore(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restoreLayer

```TypeScript
restoreLayer(): void
```

Remove changes to transform and clip since saveLayer was last called and draw the layer on canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-restoreLayer(): void--><!--Device-CanvasRenderer-restoreLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: double): void
```

Adds the effect of a rotation

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-rotate(angle: double): void--><!--Device-CanvasRenderer-rotate(angle: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double | Yes | The radian of clockwise rotation, which can be converted to an angle value using the formula: degree * Math.PI / 180. |

## save

```TypeScript
save(): void
```

Saves the current drawing state to the drawing state stack

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-save(): void--><!--Device-CanvasRenderer-save(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saveLayer

```TypeScript
saveLayer(): void
```

Allocate a layer for subsequent drawing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-saveLayer(): void--><!--Device-CanvasRenderer-saveLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: double, y: double): void
```

Increases the scaling effect of the X and Y axes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-scale(x: double, y: double): void--><!--Device-CanvasRenderer-scale(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Horizontal scaling factor |
| y | double | Yes | Vertical scaling factor |

## setLineDash

```TypeScript
setLineDash(segments: double[]): void
```

Sets the dashed line mode for line drawing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setLineDash(segments: double[]): void--><!--Device-CanvasRenderer-setLineDash(segments: double[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segments | double[] | Yes | A set of doubles that describe the length of alternating drawn lines segments and spacing (coordinate space units). |

## setPixelMap

```TypeScript
setPixelMap(value?: PixelMap): void
```

Set a PixelMap to the current context. The drawing content is synchronized to the PixelMap.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void--><!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-arkui-pixelmap-t.md) | No | PixelMap object |

## setTransform

```TypeScript
setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

Adds 2D transformation effects, including rotation, translation, and scaling. The current transformation matrix will not be overwritten. Multiple transformations will be superimposed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void--><!--Device-CanvasRenderer-setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| a | double | Yes | Horizontal Zoom |
| b | double | Yes | Vertical Tilt |
| c | double | Yes | Horizontal Tilt |
| d | double | Yes | Vertical Zoom |
| e | double | Yes | Horizontal movement |
| f | double | Yes | Vertical movement |

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

The 2D transformation effect is added. The current transformation matrix is not overwritten and the transformations are superimposed for multiple times.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void--><!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix2D](../arkts-apis/arkts-arkui-matrix2d-c.md) | No | 2D transformation matrix. For details, see Matrix2D. |

## stroke

```TypeScript
stroke(path?: Path2D): void
```

Draws the specified path according to the current stroke style

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-stroke(path?: Path2D): void--><!--Device-CanvasRenderer-stroke(path?: Path2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | No | Specified stroke path object |

## strokeRect

```TypeScript
strokeRect(x: double, y: double, w: double, h: double): void
```

Stroke Specify Rectangular Area

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-strokeRect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasRenderer-strokeRect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the start point of the rectangle. |
| y | double | Yes | The y-axis coordinate of the start point of the rectangle. |
| w | double | Yes | Width of the rectangle. |
| h | double | Yes | Height of the rectangle. |

## strokeText

```TypeScript
strokeText(text: string, x: double, y: double, maxWidth?: double): void
```

Stroke specified text at specified position

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-strokeText(text: string, x: double, y: double, maxWidth?: double): void--><!--Device-CanvasRenderer-strokeText(text: string, x: double, y: double, maxWidth?: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text string to be stroked. |
| x | double | Yes | The x-axis coordinate of the start point of the text. |
| y | double | Yes | The y-axis-axis coordinate of the start point of the text. |
| maxWidth | double | No | Maximum width of the stroke. |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

transfer ImageBitmap to content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void--><!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes |  |

## transform

```TypeScript
transform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

Adds the 2D transformation effect, including rotation, translation, and scaling, and overwrites the current transformation matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-transform(a: double, b: double, c: double, d: double, e: double, f: double): void--><!--Device-CanvasRenderer-transform(a: double, b: double, c: double, d: double, e: double, f: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| a | double | Yes | Horizontal Zoom |
| b | double | Yes | Vertical Tilt |
| c | double | Yes | Horizontal Tilt |
| d | double | Yes | Vertical Zoom |
| e | double | Yes | Horizontal movement |
| f | double | Yes | Vertical movement |

## translate

```TypeScript
translate(x: double, y: double): void
```

Increases the translation effect of the X and Y axes

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasRenderer-translate(x: double, y: double): void--><!--Device-CanvasRenderer-translate(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | Horizontal movement distance |
| y | double | Yes | Vertical travel distance |

