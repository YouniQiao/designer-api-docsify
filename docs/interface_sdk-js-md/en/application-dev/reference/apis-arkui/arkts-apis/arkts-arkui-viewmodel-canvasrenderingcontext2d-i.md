# CanvasRenderingContext2D

CanvasRenderingContext2D allows you to draw rectangles, text, images, and other objects on a canvas. You can call getContext('2d') on canvas to obtain a CanvasRenderingContext2D object.@interface CanvasRenderingContext2D

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void
```

Draws an arc on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| radius | number | Yes |
| startAngle | number | Yes |
| endAngle | number | Yes |
| counterclockwise | boolean | No |

## arcTo

```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void
```

Draws an arc based on the radius and points on the arc.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x1 | number | Yes |
| y1 | number | Yes |
| x2 | number | Yes |
| y2 | number | Yes |
| radius | number | Yes |

## beginPath

```TypeScript
beginPath(): void
```

Creates a drawing path.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void
```

Draws a cubic bezier curve on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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
clearRect(x: number, y: number, width: number, height: number): void
```

Clears the content in a rectangle on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| width | number | Yes |
| height | number | Yes |

## clip

```TypeScript
clip(): void
```

Sets a path as the clipping path.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closePath

```TypeScript
closePath(): void
```

Draws a closed path.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## createImageData

```TypeScript
createImageData(width: number, height: number): ImageData
```

Creates an ImageData object.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](../arkts-components/arkts-arkui-imagedata-c.md) |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

Creates an ImageData object.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

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

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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
createPattern(image: Image, repetition: string): object
```

Creates a pattern for image filling based on a specified source image and repetition mode.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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
| object |

## createRadialGradient

```TypeScript
createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient
```

Creates a radial gradient color.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

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
drawImage(image: Image, dx: number, dy: number, dWidth: number, dHeight: number): void
```

Draws an image.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dWidth | number | Yes |
| dHeight | number | Yes |

## drawImage

```TypeScript
drawImage(
    image: Image,
    sx: number,
    sy: number,
    sWidth: number,
    sHeight: number,
    dx: number,
    dy: number,
    dWidth: number,
    dHeight: number,
  ): void
```

Draws an image.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| sx | number | Yes |
| sy | number | Yes |
| sWidth | number | Yes |
| sHeight | number | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dWidth | number | Yes |
| dHeight | number | Yes |

## drawImage

```TypeScript
drawImage(image: image.PixelMap, dx: number, dy: number, dWidth: number, dHeight: number): void
```

Draws an image.

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
| dWidth | number | Yes |
| dHeight | number | Yes |

## drawImage

```TypeScript
drawImage(
    image: image.PixelMap,
    sx: number,
    sy: number,
    sWidth: number,
    sHeight: number,
    dx: number,
    dy: number,
    dWidth: number,
    dHeight: number,
  ): void
```

Draws an image.

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
| sWidth | number | Yes |
| sHeight | number | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dWidth | number | Yes |
| dHeight | number | Yes |

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
    counterclockwise?: number,
  ): void
```

Draws an ellipse based on the coordinate and radius.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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
| counterclockwise | number | No |

## fill

```TypeScript
fill(): void
```

Fills the area inside a closed path.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillRect

```TypeScript
fillRect(x: number, y: number, width: number, height: number): void
```

Fills a rectangle on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| width | number | Yes |
| height | number | Yes |

## fillText

```TypeScript
fillText(text: string, x: number, y: number): void
```

Draws filled text on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | number | Yes |
| y | number | Yes |

## getImageData

```TypeScript
getImageData(sx: number, sy: number, sw: number, sh: number): ImageData
```

ImageData object created with pixels in the specified area on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

## getLineDash

```TypeScript
getLineDash(): Array<number>
```

Obtains the dash line style.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

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

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

Connects the current point to a target position using a straight line.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Moves a drawing path to a target position on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Puts the ImageData onto a rectangular area on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Puts the ImageData onto a rectangular area on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Draws a quadratic curve on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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
rect(x: number, y: number, width: number, height: number): void
```

Creates a rectangular.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| width | number | Yes |
| height | number | Yes |

## restore

```TypeScript
restore: () => void
```

Restores the saved drawing context.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(rotate: number): void
```

Rotates a canvas clockwise around its coordinate axes.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [rotate](#rotate) | number | Yes |

## save

```TypeScript
save: () => void
```

Saves the current drawing context.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: number, y: number): void
```

Scales a canvas based on scaling factors.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Sets the dash line style.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| segments | Array & lt;number & gt; | Yes |

## setTransform

```TypeScript
setTransform(
    scaleX: number,
    skewX: number,
    skewY: number,
    scaleY: number,
    translateX: number,
    translateY: number,
  ): void
```

Uses same parameters as the transform() function to reset the existing transformation matrix and create a new transformation matrix.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scaleX | number | Yes |
| [skewX](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| [skewY](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| scaleY | number | Yes |
| translateX | number | Yes |
| translateY | number | Yes |

## stroke

```TypeScript
stroke(): void
```

Draws a border stroke.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stroke

```TypeScript
stroke(path: Path2D): void
```

Draws a path stroke.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes |

## strokeRect

```TypeScript
strokeRect(x: number, y: number, width: number, height: number): void
```

Draws a rectangle stroke on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| width | number | Yes |
| height | number | Yes |

## strokeText

```TypeScript
strokeText(text: string, x: number, y: number): void
```

Draws a text stroke on the canvas.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | number | Yes |
| y | number | Yes |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

Draws the Bitmap to the current canvas.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-canvas-imagebitmap-c.md) | Yes |

## transform

```TypeScript
transform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void
```

Defines a transformation matrix. To transform a graph, you only need to set parameters of the matrix. The coordinates of the corresponding graph are multiplied by the matrix values to obtain new coordinates of the transformed graph. You can use the matrix to implement multiple transform effects.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scaleX | number | Yes |
| [skewX](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| [skewY](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| scaleY | number | Yes |
| translateX | number | Yes |
| translateY | number | Yes |

## translate

```TypeScript
translate(x: number, y: number): void
```

Moves the origin of the coordinate system.

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

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

Sets the style of a paint to fill an area. Paint color used to fill the area. Canvas gradient object used by the paint. You can call createLinearGradient() to create a CanvasGradient object. Canvas pattern. You can call createPattern() to create a CanvasPattern object.

**Type:** string \| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) \| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md)

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font: string
```

Sets the font style. Font style. The default value is 10px sans-serif in tv, phone, tablet, wearable. The default value is 30px SourceHanSansSC-Regular in smartVision.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalAlpha

```TypeScript
globalAlpha: number
```

Sets the alpha value. Global alpha value to set. The value ranges from 0.0 (completely transparent) to 1.0 (completely opaque).

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalCompositeOperation

```TypeScript
globalCompositeOperation: string
```

Sets the composite operation type. source-over Default value. Displays the new drawing above the existing drawing. source-atop Displays the new drawing on the top of the existing drawing. source-in Displays the new drawing inside the existing drawing. source-out Displays part of the new drawing that is outside of the existing drawing. destination-over Displays the existing drawing above the new drawing. destination-atop Displays the existing drawing above the new drawing. destination-in Displays the existing drawing inside the new drawing. destination-out Displays part of the existing drawing that is outside of the new drawing. lighter Displays both the new drawing and the existing drawing. copy Displays the new drawing and neglects the existing drawing. xor Combines the new drawing and existing drawing using the XOR operation.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingEnabled

```TypeScript
imageSmoothingEnabled: boolean
```

Sets whether an image is smooth. default value is true.

**Type:** boolean

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineCap

```TypeScript
lineCap: string
```

Sets the style of line endpoints. Style of line endpoints. Available values include: butt (default): The endpoints of the line are in square. round: The endpoints of the line are rounded. square: The endpoints of the line are in square, and each end of the line is added with a rectangle whose length is the same as the line thickness and whose width is half of the line thickness.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineDashOffset

```TypeScript
lineDashOffset: number
```

Sets the dash line offset. Dash line offset. The value is a float number starting from 0.0.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineJoin

```TypeScript
lineJoin: string
```

Sets the style for an intersection point where a line joins another. Style of the intersection point of lines. Available values include: round: The intersection part is a sector. The radius of a rounded corner is equal to the line width. bevel: The intersection part is a triangle. The rectangular corner of each line is independent. miter (default): The intersection part has a miter corner by extending the outside edges of the lines until they meet. You can view the effect of this attribute in miterLimit.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineWidth

```TypeScript
lineWidth?: number
```

Sets the width of a line.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## miterLimit

```TypeScript
miterLimit: number
```

Sets the maximum miter length. The miter length is the distance between the inner corner and the outer corner where two lines meet. Maximum miter length. The default value is 10.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowBlur

```TypeScript
shadowBlur: number
```

Sets the shadow blur degree. Shadow blur degree. A larger value indicates a more blurred shadow. The value is of the float type, and the default value is 0.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
shadowColor: string
```

Sets the shadow color.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetX

```TypeScript
shadowOffsetX: number
```

Sets the x-axis shadow offset relative to the original object. X-axis shadow offset relative to the original object.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetY

```TypeScript
shadowOffsetY: number
```

Sets the y-axis shadow offset relative to the original object. Y-axis shadow offset relative to the original object.

**Type:** number

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
strokeStyle?: string | CanvasGradient | CanvasPattern
```

Sets the stroke paint style. Color of the stroke paint. Canvas gradient object used by the paint. You can call createLinearGradient() to create a CanvasGradient object. Canvas pattern. You can call createPattern() to create a CanvasPattern object.

**Type:** string \| [CanvasGradient](arkts-arkui-viewmodel-canvasgradient-i.md) \| [CanvasPattern](arkts-arkui-canvaspattern-canvaspattern-i.md)

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign: "left" | "right" | "center" | "start" | "end"
```

Sets the text alignment mode. Text alignment mode. Available values include: left (default): The text is left-aligned. right: The text is right-aligned. center: The text is center-aligned. start: The text is aligned with the start bound. Can't be supported by smartVision. end: The text is aligned with the end bound. Can't be supported by smartVision. NOTE In the ltr layout mode, the value start equals to left. In the rtl layout mode, the value start equals to right.

**Type:** "left" \| "right" \| "center" \| "start" \| "end"

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBaseline

```TypeScript
textBaseline: string
```

Sets a text baseline in the horizontal direction for text alignment. Text baseline. Available values include: alphabetic (default): The text baseline is the normal alphabetic baseline. top: The text baseline is on the top of the text bounding box. hanging: The text baseline is a hanging baseline over the text. middle: The text baseline is in the middle of the text bounding box. ideographic: The text baseline is the ideographic baseline. If a character exceeds the alphabetic baseline, the ideographic baseline is located at the bottom of the excessive character. bottom: The text baseline is at the bottom of the text bounding box. Its difference from the ideographic baseline is that the ideographic baseline does not consider letters in the next line.

**Type:** string

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
