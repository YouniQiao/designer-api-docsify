# OffscreenCanvasRenderingContext2D

Provides a 2D rendering context for the drawing surface of the &lt; Canvas &gt; element. It is used to draw shapes, text, images and other objects.@interface OffscreenCanvasRenderingContext2D

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(radius: number, x: number, y: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void
```

Draw an arc.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |
| x | number | Yes |
| y | number | Yes |
| startAngle | number | Yes |
| endAngle | number | Yes |
| counterclockwise | boolean | No |

## arcTo

```TypeScript
arcTo(x1: number, x2: number, y1: number, y2: number, radius: number): void
```

Draws an arc from the beginning to the end.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x1 | number | Yes |
| x2 | number | Yes |
| y1 | number | Yes |
| y2 | number | Yes |
| radius | number | Yes |

## beginPath

```TypeScript
beginPath(): void
```

Creates a drawing path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void
```

Draw a third order Bezier curve.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cp1x | number | Yes |
| cp1y | number | Yes |
| cp2x | number | Yes |
| cp2y | number | Yes |
| x | number | Yes |
| y | number | Yes |

## clearRect

```TypeScript
clearRect(x: number, y: number, w: number, h: number): void
```

Clears the contents of the specified rectangular area.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| w | number | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | Yes |

## clip

```TypeScript
clip(): void
```

Crop the current canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closePath

```TypeScript
closePath(): void
```

Closing the current path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## createImageData

```TypeScript
createImageData(sw: number, sh: number): ImageData
```

Create an ImageData object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sw | number | Yes |
| sh | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

Create an ImageData object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) |

## createLinearGradient

```TypeScript
createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient
```

Creates a linear gradient color.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x0 | number | Yes |
| y0 | number | Yes |
| x1 | number | Yes |
| y1 | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) |

## createPath2D

```TypeScript
createPath2D(path?: Path2D): Path2D
```

Creates a path that is later used by the CanvasRenderingContext2D object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path2D](arkts-arkui-viewmodel-path2d-i.md) |

## createPath2D

```TypeScript
createPath2D(cmds?: string): Path2D
```

Creates a path that is later used by the CanvasRenderingContext2D object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cmds | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path2D](arkts-arkui-viewmodel-path2d-i.md) |

## createPattern

```TypeScript
createPattern(image: Image, repetition: string): CanvasPattern
```

Create a drawing style template.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| repetition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md) |

## createRadialGradient

```TypeScript
createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient
```

Create a radial tween object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x0 | number | Yes |
| y0 | number | Yes |
| r0 | number | Yes |
| x1 | number | Yes |
| y1 | number | Yes |
| r1 | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) |

## drawImage

```TypeScript
drawImage(image: Image, dx: number, dy: number, dw: number, dh: number): void
```

Draw an Image object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## drawImage

```TypeScript
drawImage(
    image: Image,
    sx: number,
    sy: number,
    sw: number,
    sh: number,
    dx: number,
    dy: number,
    dw: number,
    dh: number,
  ): void
```

Draw an Image object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| sx | number | Yes |
| sy | number | Yes |
| sw | number | Yes |
| sh | number | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## drawImage

```TypeScript
drawImage(image: image.PixelMap, dx: number, dy: number, dw: number, dh: number): void
```

Draw an Image object.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | image.PixelMap | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## drawImage

```TypeScript
drawImage(
    image: image.PixelMap,
    sx: number,
    sy: number,
    sw: number,
    sh: number,
    dx: number,
    dy: number,
    dw: number,
    dh: number,
  ): void
```

Draw an Image object.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | image.PixelMap | Yes |
| sx | number | Yes |
| sy | number | Yes |
| sw | number | Yes |
| sh | number | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## ellipse

```TypeScript
ellipse(
    x: number,
    y: number,
    radiusX: number,
    radiusY: number,
    rotation: number,
    startAngle: number,
    endAngle: number,
    counterclockwise?: boolean,
  ): void
```

Draw an ellipse.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| radiusX | number | Yes |
| radiusY | number | Yes |
| rotation | number | Yes |
| startAngle | number | Yes |
| endAngle | number | Yes |
| counterclockwise | boolean | No |

## fill

```TypeScript
fill(): void
```

Fills the current canvas with color.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillRect

```TypeScript
fillRect(x: number, y: number, w: number, h: number): void
```

Fills a rectangular area.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| w | number | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | Yes |

## fillText

```TypeScript
fillText(text: string, y: number, x: number /*, maxWidth?: number*/): void
```

Stroke a rectangular area.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| y | number | Yes |
| x | number | Yes |

## getImageData

```TypeScript
getImageData(sx: number, sy: number, sw: number, sh: number): ImageData
```

Get an ImageData object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |
| sw | number | Yes |
| sh | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) |

## getPixelMap

```TypeScript
getPixelMap(sx: number, sy: number, sw: number, sh: number): image.PixelMap
```

Get an PixelMap object.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |
| sw | number | Yes |
| sh | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

## isPointInPath

```TypeScript
isPointInPath(x: number, y: number): boolean
```

Check whether the specified coordinate point is on the Path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPointInPath

```TypeScript
isPointInPath(path: Path2D, x: number, y: number): boolean
```

Check whether the specified coordinate point is on the Path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPointInStroke

```TypeScript
isPointInStroke(x: number, y: number): boolean
```

Checks whether the specified coordinate point is on the stroke edge.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPointInStroke

```TypeScript
isPointInStroke(path: Path2D, x: number, y: number): boolean
```

Checks whether the specified coordinate point is on the stroke edge.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

Draw a straight line.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

Returns a TextMetrics object used to obtain the width of specified text.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextMetrics](arkts-arkui-viewmodel-textmetrics-i.md) |

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

Moves the current canvas to the specified coordinate point.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: number, dy: number): void
```

Draws the specified ImageData object to the canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |

## putImageData

```TypeScript
putImageData(
    imageData: ImageData,
    dx: number,
    dy: number,
    dirtyX: number,
    dirtyY: number,
    dirtyWidth: number,
    dirtyHeight: number,
  ): void
```

Draws the specified ImageData object to the canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dirtyX | number | Yes |
| dirtyY | number | Yes |
| dirtyWidth | number | Yes |
| dirtyHeight | number | Yes |

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void
```

Draw a second order Bezier curve.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cpx | number | Yes |
| cpy | number | Yes |
| x | number | Yes |
| y | number | Yes |

## rect

```TypeScript
rect(x: number, y: number, w: number, h: number): void
```

Draw a rectangle.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| w | number | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | Yes |

## resetTransform

```TypeScript
resetTransform(): void
```

Resets the current matrix transformation effect.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

Restores the configuration information of the last saved canvas context.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: number): void
```

Adds a rotation effect to the current canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## save

```TypeScript
save(): void
```

Saves configuration information for the current canvas context.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: number, y: number): void
```

Adds a zoom effect to the current canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## setLineDash

```TypeScript
setLineDash(segments: Array<number>): void
```

Sets the dotted spacing of a line.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| segments | Array & lt;number & gt; | Yes |

## setTransform

```TypeScript
setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void
```

Set the rotation, pan, and zoom effects.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | number | Yes |
| b | number | Yes |
| c | number | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | number | Yes |

## stroke

```TypeScript
stroke(): void
```

Stroke draws the current path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stroke

```TypeScript
stroke(path: Path2D): void
```

Stroke draws the current path.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes |

## strokeRect

```TypeScript
strokeRect(x: number, y: number, w: number, h: number): void
```

Stroke a rectangular area.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| w | number | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | Yes |

## strokeText

```TypeScript
strokeText(text: string, x: number, y: number /*, maxWidth?: number*/): void
```

Draws the stroke of a text string.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | number | Yes |
| y | number | Yes |

## transform

```TypeScript
transform(a: number, b: number, c: number, d: number, e: number, f: number): void
```

Set the rotation, pan, and zoom effects.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | number | Yes |
| b | number | Yes |
| c | number | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [f](../../apis-arkts/arkts-apis/arkts-arkts-float-c.md) | number | Yes |

## translate

```TypeScript
translate(x: number, y: number): void
```

Adds a pan effect to the current canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## fillStyle

```TypeScript
fillStyle?: string | CanvasGradient | CanvasPattern
```

Fill style attribute. Paint color used to fill the area. Canvas gradient object used by the paint. You can call createLinearGradient() to create a CanvasGradient object. Canvas pattern. You can call createPattern() to create a CanvasPattern object.

**Type:** string \| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) \| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md)

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLineDash

```TypeScript
getLineDash: Array<number>
```

Gets the dotted spacing of a line. Returns the current line segment style array containing an even number of non-negative numbers.

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
strokeStyle?: string | CanvasGradient | CanvasPattern
```

Sets the stroke paint style. Color of the stroke paint. Canvas gradient object used by the paint. You can call createLinearGradient() to create a CanvasGradient object. Canvas pattern. You can call createPattern() to create a CanvasPattern object.

**Type:** string \| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) \| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md)

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
