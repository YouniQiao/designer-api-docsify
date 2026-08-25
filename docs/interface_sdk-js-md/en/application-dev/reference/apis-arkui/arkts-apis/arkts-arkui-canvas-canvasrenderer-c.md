# CanvasRenderer

Canvas renderer for drawing shapes, text, images and other objects@extends CanvasPath

**Inheritance/Implementation:** CanvasRenderer extends [CanvasPath](arkts-arkui-canvas-canvaspath-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## beginPath

```TypeScript
beginPath(): void
```

Clear the sub-path list and start a new path.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearRect

```TypeScript
clearRect(x: double, y: double, w: double, h: double): void
```

Clears the drawing content of a rectangular area.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| w | double | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | Yes |

## clip

```TypeScript
clip(fillRule?: CanvasFillRule): void
```

Sets the currently created path as the current clipping path

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## clip

```TypeScript
clip(path: Path2D, fillRule?: CanvasFillRule): void
```

Tailoring according to the specified path

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | Yes |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## createConicGradient

```TypeScript
createConicGradient(startAngle: double, x: double, y: double): CanvasGradient
```

Creates a gradient around a point with given coordinates.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startAngle | double | Yes |
| x | double | Yes |
| y | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## createImageData

```TypeScript
createImageData(sw: double, sh: double): ImageData
```

Creates a new, empty ImageData object of the specified size

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sw | double | Yes |
| sh | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

From an existing ImageData object, copy an object with the same width and height as the image. The image content is not copied.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## createLinearGradient

```TypeScript
createLinearGradient(x0: double, y0: double, x1: double, y1: double): CanvasGradient
```

Creates a linear gradient object that is specified along the parameter coordinates

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x0 | double | Yes |
| y0 | double | Yes |
| x1 | double | Yes |
| y1 | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## createPattern

```TypeScript
createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null
```

Creates a template object using the specified image

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes |
| repetition | string \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasPattern](arkts-arkui-canvas-canvaspattern-i.md) \| null |

## createRadialGradient

```TypeScript
createRadialGradient(x0: double, y0: double, r0: double, x1: double, y1: double, r1: double): CanvasGradient
```

Creates a radioactive gradient object based on parameters that determine the coordinates of two circles

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x0 | double | Yes |
| y0 | double | Yes |
| r0 | double | Yes |
| x1 | double | Yes |
| y1 | double | Yes |
| r1 | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-canvas-canvasgradient-c.md) |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | Yes |
| dx | double | Yes |
| dy | double | Yes |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: double, dy: double, dw: double, dh: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | Yes |
| dx | double | Yes |
| dy | double | Yes |
| dw | double | Yes |
| dh | double | Yes |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, sx: double, sy: double, sw: double, sh: double, dx: double, dy: double,
    dw: double, dh: double): void
```

Draw an image on a canvas

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | Yes |
| sx | double | Yes |
| sy | double | Yes |
| sw | double | Yes |
| sh | double | Yes |
| dx | double | Yes |
| dy | double | Yes |
| dw | double | Yes |
| dh | double | Yes |

## fill

```TypeScript
fill(fillRule?: CanvasFillRule): void
```

Fills existing paths according to the current fill style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## fill

```TypeScript
fill(path: Path2D, fillRule?: CanvasFillRule): void
```

Fills the specified path according to the current fill style

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | Yes |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## fillRect

```TypeScript
fillRect(x: double, y: double, w: double, h: double): void
```

Fills a specified rectangular area

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| w | double | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | Yes |

## fillText

```TypeScript
fillText(text: string, x: double, y: double, maxWidth?: double): void
```

Fills the specified text at the specified location

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | double | Yes |
| y | double | Yes |
| maxWidth | double | No |

## getImageData

```TypeScript
getImageData(sx: double, sy: double, sw: double, sh: double): ImageData
```

Obtains the pixel data of a specified area on the current canvas.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | double | Yes |
| sy | double | Yes |
| sw | double | Yes |
| sh | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](arkts-arkui-canvas-imagedata-c.md) |

## getLineDash

```TypeScript
getLineDash(): double[]
```

Gets the current segment style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| double[] |

## getPixelMap

```TypeScript
getPixelMap(sx: double, sy: double, sw: double, sh: double): PixelMap | undefined
```

Obtains the PixelMap of a specified area on the current canvas.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | double | Yes |
| sy | double | Yes |
| sw | double | Yes |
| sh | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| undefined |

## getTransform

```TypeScript
getTransform(): Matrix2D
```

Obtains the currently applied transformation matrix.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

Measure the size of a specified text. For details about the return value, see [TextMetrics](arkts-arkui-canvas-textmetrics-i.md).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextMetrics](arkts-arkui-canvas-textmetrics-i.md) |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string): void
```

Draws the specified ImageData object onto the canvas

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes |
| dx | double \| string | Yes |
| dy | double \| string | Yes |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: double | string, dy: double | string, dirtyX: double | string,
    dirtyY: double | string, dirtyWidth: double | string, dirtyHeight: double | string): void
```

Draws the specified ImageData object onto the canvas

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-canvas-imagedata-c.md) | Yes |
| dx | double \| string | Yes |
| dy | double \| string | Yes |
| dirtyX | double \| string | Yes |
| dirtyY | double \| string | Yes |
| dirtyWidth | double \| string | Yes |
| dirtyHeight | double \| string | Yes |

## reset

```TypeScript
reset(): void
```

Clear the backing buffer, drawing state stack, any defined paths, and styles.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetTransform

```TypeScript
resetTransform(): void
```

Resets the current transformation matrix using the identity matrix

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

Top of the stack pop-up state in the drawing state stack

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restoreLayer

```TypeScript
restoreLayer(): void
```

Remove changes to transform and clip since saveLayer was last called and draw the layer on canvas.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: double): void
```

Adds the effect of a rotation

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | double | Yes |

## save

```TypeScript
save(): void
```

Saves the current drawing state to the drawing state stack

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saveLayer

```TypeScript
saveLayer(): void
```

Allocate a layer for subsequent drawing.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: double, y: double): void
```

Increases the scaling effect of the X and Y axes.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |

## setLineDash

```TypeScript
setLineDash(segments: double[]): void
```

Sets the dashed line mode for line drawing.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| segments | double[] | Yes |

## setPixelMap

```TypeScript
setPixelMap(value?: PixelMap): void
```

Set a PixelMap to the current context. The drawing content is synchronized to the PixelMap.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | No |

## setTransform

```TypeScript
setTransform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

Adds 2D transformation effects, including rotation, translation, and scaling. The current transformation matrix will not be overwritten. Multiple transformations will be superimposed.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | double | Yes |
| b | double | Yes |
| c | double | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | Yes |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | Yes |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | double | Yes |

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

The 2D transformation effect is added. The current transformation matrix is not overwritten and the transformations are superimposed for multiple times.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transform](#transform) | [Matrix2D](arkts-arkui-matrix2d-c.md) | No |

## stroke

```TypeScript
stroke(path?: Path2D): void
```

Draws the specified path according to the current stroke style

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-canvas-path2d-c.md) | No |

## strokeRect

```TypeScript
strokeRect(x: double, y: double, w: double, h: double): void
```

Stroke Specify Rectangular Area

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| w | double | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | Yes |

## strokeText

```TypeScript
strokeText(text: string, x: double, y: double, maxWidth?: double): void
```

Stroke specified text at specified position

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | double | Yes |
| y | double | Yes |
| maxWidth | double | No |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

transfer ImageBitmap to content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes |

## transform

```TypeScript
transform(a: double, b: double, c: double, d: double, e: double, f: double): void
```

Adds the 2D transformation effect, including rotation, translation, and scaling, and overwrites the current transformation matrix.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | double | Yes |
| b | double | Yes |
| c | double | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | Yes |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | double | Yes |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | double | Yes |

## translate

```TypeScript
translate(x: double, y: double): void
```

Increases the translation effect of the X and Y axes

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |

## antialias

```TypeScript
set antialias(antialias: boolean | undefined)
```

Set the status whether anti-aliasing is enabled for canvas. The value true indicates that anti-aliasing is enabled. The value false indicates that anti-aliasing is disabled. The value undefined indicates that anti-aliasing is determined by the RenderingContextSettings#antialias property. The default value is undefined.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
set direction(direction: CanvasDirection)
```

Set the text drawing direction. For details, see [CanvasDirection](arkts-arkui-canvasdirection-t.md).

**Type:** [CanvasDirection](arkts-arkui-canvasdirection-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillStyle

```TypeScript
set fillStyle(fillStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

Set the attributes specifie the color, gradient, or pattern to use inside shapes. The options are as follows:

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## filter

```TypeScript
set filter(filter: string)
```

Provides filter effects such as blur and grayscale. You can set the following filter effects: blur(&lt;length&gt;): Adds a Gaussian blur effect to the drawing brightness(&lt;percentage&gt;): Provides a linear multiplication for the drawing and adjusts the brightness level. contrast(&lt;percentage&gt;): Adjusts the contrast of the image. When the value is 0%, the image is completely black. When the value is 100%, there is no change in the image. grayscale(&lt;percentage&gt;): Converts the image to a gray image. When the value is 100%, the image is completely gray. When the value is 0%, there is no change in the image. hue-rotate(&lt;degree&gt;): Perform color rotation on an image. When the value is 0 degrees, there is no change in the image. invert(&lt;percentage&gt;): Inverted image (representing the effect of a photographic negative). When the value is 100%, the image is completely inverted. When the value is 0%, there is no change in the image. opacity(&lt;percentage&gt;): Transparency of the image. At 0%, the image is completely transparent. When the value is 100%, there is no change in the image. saturate(&lt;percentage&gt;): Perform saturation processing on the image. At 0%, the image is completely un-saturated. When the value is 100%, there is no change in the image. sepia(&lt;percentage&gt;): The image is sepia (nostalgic style). At 100%, the image turns completely sepia. When the value is 0%, there is no change in the image. none: Turn off filter effects

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
set font(font: string)
```

Set the font style.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalAlpha

```TypeScript
set globalAlpha(globalAlpha: double)
```

Set transparency. The value ranges from 0.0 (completely transparent) to 1.0 (completely opaque). If the value is out of range, the assignment is invalid.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalCompositeOperation

```TypeScript
set globalCompositeOperation(globalCompositeOperation: string)
```

Set the type of composition operation applied when drawing a new shape. The following types are supported: source-over: (Default) Draws a new drawing on top of an existing canvas context. source-in: The new drawing is drawn only where the new drawing overlaps the target canvas. Everything else is transparent. source-out: Draws a new drawing where it does not overlap with the existing canvas content. source-atop: The new drawing is drawn only where it overlaps the content of the existing canvas. destination-over: Draws a new graphic behind the existing canvas content. destination-in: Existing canvas content remains where the new drawing overlaps the existing canvas content. Everything else is transparent. destination-out: Existing content remains where the new drawing does not overlap. destination-atop: The existing canvas retains only the part that overlaps with the new drawing, which is drawn behind the canvas content. lighter: The color of two overlapping shapes is determined by adding the color values. copy: Only new graphics are displayed. xor: In the image, those overlaps and other places outside of the normal drawing are transparent.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingEnabled

```TypeScript
set imageSmoothingEnabled(imageSmoothingEnabled: boolean)
```

Set the status whether to smooth the image. The value true indicates that the image is smooth. The value false indicates that the image is not smooth.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingQuality

```TypeScript
set imageSmoothingQuality(imageSmoothingQuality: ImageSmoothingQuality)
```

Set the smoothness level of the current image. For details, see [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md).

**Type:** [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
set letterSpacing(letterSpacing: LengthMetrics | string)
```

Set spacing for letter.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineCap

```TypeScript
set lineCap(lineCap: CanvasLineCap)
```

Set the line segment endpoint attribute. For details, see [CanvasLineCap](arkts-arkui-canvaslinecap-t.md).

**Type:** [CanvasLineCap](arkts-arkui-canvaslinecap-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineDashOffset

```TypeScript
set lineDashOffset(lineDashOffset: double)
```

Set the dotted line offset attribute.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineJoin

```TypeScript
set lineJoin(lineJoin: CanvasLineJoin)
```

Set the line segment connection point attribute. For details, see [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md).

**Type:** [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineWidth

```TypeScript
set lineWidth(lineWidth: double)
```

Set the line thickness attribute. The value cannot be 0 or a negative double.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## miterLimit

```TypeScript
set miterLimit(miterLimit: double)
```

Set the value of this parameter cannot be 0 or a negative double.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowBlur

```TypeScript
set shadowBlur(shadowBlur: double)
```

Set the shadow blur radius. The value cannot be a negative double.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
set shadowColor(shadowColor: string)
```

Set the shadow color.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetX

```TypeScript
set shadowOffsetX(shadowOffsetX: double)
```

Set the horizontal offset distance of the shadow.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetY

```TypeScript
set shadowOffsetY(shadowOffsetY: double)
```

Set the vertical offset distance of the shadow.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
set strokeStyle(strokeStyle: string | Color | int | CanvasGradient | CanvasPattern)
```

Set the attributes specifie the color, gradient, or pattern to use for the strokes (outlines) around shapes. The options are as follows:

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
set textAlign(textAlign: CanvasTextAlign)
```

Set the text alignment mode. For details, see [CanvasTextAlign](arkts-arkui-canvastextalign-t.md).

**Type:** [CanvasTextAlign](arkts-arkui-canvastextalign-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBaseline

```TypeScript
set textBaseline(textBaseline: CanvasTextBaseline)
```

Set the text baseline. For details, see [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md).

**Type:** [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
