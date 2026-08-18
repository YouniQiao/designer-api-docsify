# CanvasRenderer

After the **CanvasRenderingContext2D** object is bound to the **Canvas** component, you can draw shapes, texts, and images on the **Canvas** component. > **NOTE：**> > * It is recommended that the **CanvasRenderingContext2D** object and the **Canvas** component be > encapsulated into the same custom component, ensuring a one-to-one correspondence and consistent > lifecycle between them. > > * When you call drawing APIs in this module, the commands are stored in the associated **Canvas** > component's command queue. These commands are only executed when the current frame enters the rendering > phase and the associated **Canvas** component is visible. Therefore, when the **Canvas** component is > invisible (for example, off-screen or hidden), avoid frequent drawing calls to prevent command queue > buildup and excessive memory usage. > > * When the width or height of the **Canvas** component exceeds 8000 px, rendering via the CPU causes > significant performance degradation.

**Inheritance/Implementation:** CanvasRenderer extends [CanvasPath](arkts-arkui-canvaspath-c.md#canvaspath)

**Since:** 8

<!--Device-unnamed-declare class CanvasRenderer--><!--Device-unnamed-declare class CanvasRenderer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## beginPath

```TypeScript
beginPath(): void
```

Creates a drawing path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-beginPath(): void--><!--Device-CanvasRenderer-beginPath(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearRect

```TypeScript
clearRect(x: number, y: number, w: number, h: number): void
```

Clears the content in a rectangle on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-clearRect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasRenderer-clearRect(x: number, y: number, w: number, h: number): void-End-->

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
clip(fillRule?: CanvasFillRule): void
```

Sets the current path to a clipping path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## clip

```TypeScript
clip(path: Path2D, fillRule?: CanvasFillRule): void
```

Sets a specified path as the clipping path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-clip(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## createConicGradient

```TypeScript
createConicGradient(
    startAngle: number,
    x: number,
    y: number
  ): CanvasGradient
```

Creates a conic gradient.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CanvasRenderer-createConicGradient(    startAngle: number,    x: number,    y: number  ): CanvasGradient--><!--Device-CanvasRenderer-createConicGradient(    startAngle: number,    x: number,    y: number  ): CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startAngle | number | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) |

## createImageData

```TypeScript
createImageData(sw: number, sh: number): ImageData
```

Creates a blank ImageData object of a specified size. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it. The createImageData example is identical to the putImageData example.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-createImageData(sw: number, sh: number): ImageData--><!--Device-CanvasRenderer-createImageData(sw: number, sh: number): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sw | number | Yes |
| sh | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](arkts-arkui-imagedata-c.md) |

## createImageData

```TypeScript
createImageData(imageData: ImageData): ImageData
```

Creates an **ImageData** object with the same width and height of an existing **ImageData** object. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData--><!--Device-CanvasRenderer-createImageData(imageData: ImageData): ImageData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageData](arkts-arkui-imagedata-c.md) |

## createLinearGradient

```TypeScript
createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient
```

Creates a linear gradient.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient--><!--Device-CanvasRenderer-createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient-End-->

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
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) |

## createPattern

```TypeScript
createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null
```

Creates a pattern for image filling based on a specified source image and repetition mode.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null--><!--Device-CanvasRenderer-createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-imagebitmap-c.md) | Yes |
| repetition | string \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasPattern](arkts-arkui-canvaspattern-i.md) |

## createRadialGradient

```TypeScript
createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient
```

Creates a radial gradient.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient--><!--Device-CanvasRenderer-createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient-End-->

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
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void
```

Draws an image on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-imagebitmap-c.md) \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |

## drawImage

```TypeScript
drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void
```

Draws an image by stretching or compressing it to the specified dimensions.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void--><!--Device-CanvasRenderer-drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-imagebitmap-c.md) \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## drawImage

```TypeScript
drawImage(
    image: ImageBitmap | PixelMap,
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

Draws a cropped portion of an image by stretching or compressing it to the specified dimensions.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-drawImage(    image: ImageBitmap | PixelMap,    sx: number,    sy: number,    sw: number,    sh: number,    dx: number,    dy: number,    dw: number,    dh: number,  ): void--><!--Device-CanvasRenderer-drawImage(    image: ImageBitmap | PixelMap,    sx: number,    sy: number,    sw: number,    sh: number,    dx: number,    dy: number,    dw: number,    dh: number,  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [ImageBitmap](arkts-arkui-imagebitmap-c.md) \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |
| sx | number | Yes |
| sy | number | Yes |
| sw | number | Yes |
| sh | number | Yes |
| dx | number | Yes |
| dy | number | Yes |
| dw | number | Yes |
| dh | number | Yes |

## fill

```TypeScript
fill(fillRule?: CanvasFillRule): void
```

Fills the current path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## fill

```TypeScript
fill(path: Path2D, fillRule?: CanvasFillRule): void
```

Fills a specified path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void--><!--Device-CanvasRenderer-fill(path: Path2D, fillRule?: CanvasFillRule): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes |
| fillRule | [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | No |

## fillRect

```TypeScript
fillRect(x: number, y: number, w: number, h: number): void
```

Fills a rectangle on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-fillRect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasRenderer-fillRect(x: number, y: number, w: number, h: number): void-End-->

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
fillText(text: string, x: number, y: number, maxWidth?: number): void
```

Draws filled text on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-fillText(text: string, x: number, y: number, maxWidth?: number): void--><!--Device-CanvasRenderer-fillText(text: string, x: number, y: number, maxWidth?: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | number | Yes |
| y | number | Yes |
| maxWidth | number | No |

## getImageData

```TypeScript
getImageData(sx: number, sy: number, sw: number, sh: number): ImageData
```

Obtains the **ImageData** object created with the pixels within the specified area on the canvas. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-getImageData(sx: number, sy: number, sw: number, sh: number): ImageData--><!--Device-CanvasRenderer-getImageData(sx: number, sy: number, sw: number, sh: number): ImageData-End-->

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
| [ImageData](arkts-arkui-imagedata-c.md) |

## getLineDash

```TypeScript
getLineDash(): number[]
```

Obtains the dash line style.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-getLineDash(): number[]--><!--Device-CanvasRenderer-getLineDash(): number[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## getPixelMap

```TypeScript
getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap
```

Obtains the **PixelMap** object created with the pixels within the specified area on the canvas. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CanvasRenderer-getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap--><!--Device-CanvasRenderer-getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap-End-->

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
| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) |

## getTransform

```TypeScript
getTransform(): Matrix2D
```

Obtains the current transformation matrix being applied to the context.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-getTransform(): Matrix2D--><!--Device-CanvasRenderer-getTransform(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](../arkts-apis/arkts-arkui-matrix2d-c.md) |

## measureText

```TypeScript
measureText(text: string): TextMetrics
```

Returns a **TextMetrics** object used to obtain the width of specified text. Note that the width obtained may vary by device.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-measureText(text: string): TextMetrics--><!--Device-CanvasRenderer-measureText(text: string): TextMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextMetrics](arkts-arkui-textmetrics-i.md) |

## putImageData

```TypeScript
putImageData(imageData: ImageData, dx: number | string, dy: number | string): void
```

Puts an **ImageData** object onto a rectangular area on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: number | string, dy: number | string): void--><!--Device-CanvasRenderer-putImageData(imageData: ImageData, dx: number | string, dy: number | string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes |
| dx | number \| string | Yes |
| dy | number \| string | Yes |

## putImageData

```TypeScript
putImageData(
    imageData: ImageData,
    dx: number | string,
    dy: number | string,
    dirtyX: number | string,
    dirtyY: number | string,
    dirtyWidth: number | string,
    dirtyHeight: number | string
  ): void
```

Fills the new rectangular area with the **ImageData** data after cropping.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-putImageData(    imageData: ImageData,    dx: number | string,    dy: number | string,    dirtyX: number | string,    dirtyY: number | string,    dirtyWidth: number | string,    dirtyHeight: number | string  ): void--><!--Device-CanvasRenderer-putImageData(    imageData: ImageData,    dx: number | string,    dy: number | string,    dirtyX: number | string,    dirtyY: number | string,    dirtyWidth: number | string,    dirtyHeight: number | string  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageData | [ImageData](arkts-arkui-imagedata-c.md) | Yes |
| dx | number \| string | Yes |
| dy | number \| string | Yes |
| dirtyX | number \| string | Yes |
| dirtyY | number \| string | Yes |
| dirtyWidth | number \| string | Yes |
| dirtyHeight | number \| string | Yes |

## reset

```TypeScript
reset(): void
```

Resets this **CanvasRenderingContext2D** object to its default state and clears the background buffer, drawing state stack, defined paths, and styles.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasRenderer-reset(): void--><!--Device-CanvasRenderer-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetTransform

```TypeScript
resetTransform(): void
```

Resets the current transform to the identity matrix.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-resetTransform(): void--><!--Device-CanvasRenderer-resetTransform(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restore

```TypeScript
restore(): void
```

Restores the saved drawing context. > **NOTE：**> > When the number of calls to **restore()** does not exceed the number of calls to **save()**, > this API pops the saved drawing state from the stack and restores the attributes, clipping > path, and transformation matrix of the **CanvasRenderingContext2D** object.<br> > If the number of calls to **restore()** exceeds the number of calls to **save()**, this API > does nothing.<br> > If there is no saved state, this API does nothing.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-restore(): void--><!--Device-CanvasRenderer-restore(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## restoreLayer

```TypeScript
restoreLayer(): void
```

Restores the image transformation and cropping state to the state before **saveLayer**, and then draws the layer onto the canvas. For the sample code, see the code for **saveLayer**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasRenderer-restoreLayer(): void--><!--Device-CanvasRenderer-restoreLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotate

```TypeScript
rotate(angle: number): void
```

Rotates a canvas clockwise around its coordinate axes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-rotate(angle: number): void--><!--Device-CanvasRenderer-rotate(angle: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## save

```TypeScript
save(): void
```

Saves the current drawing context.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-save(): void--><!--Device-CanvasRenderer-save(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saveLayer

```TypeScript
saveLayer(): void
```

Saves this layer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasRenderer-saveLayer(): void--><!--Device-CanvasRenderer-saveLayer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale(x: number, y: number): void
```

Scales the canvas based on the given scale factors.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-scale(x: number, y: number): void--><!--Device-CanvasRenderer-scale(x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## setLineDash

```TypeScript
setLineDash(segments: number[]): void
```

Sets the dash line style.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-setLineDash(segments: number[]): void--><!--Device-CanvasRenderer-setLineDash(segments: number[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| segments | number[] | Yes |

## setPixelMap

```TypeScript
setPixelMap(value?: PixelMap): void
```

Draws the input **PixelMap** object on the canvas. The example is the same as that of **getPixelMap**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void--><!--Device-CanvasRenderer-setPixelMap(value?: PixelMap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | No |

## setTransform

```TypeScript
setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void
```

Resets the existing transformation matrix and creates a new transformation matrix by using the same parameters as the **transform()** API. > **NOTE：**> > The coordinates of each point in the graph after transformation can be calculated > using the following formula: > > **x** and **y** represent coordinates before transformation, and **x'** and **y'** > represent coordinates after transformation. > > - x' = `a * x + c * y + e` > > - y' = `b * x + d * y + f`

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void--><!--Device-CanvasRenderer-setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | number | Yes |
| b | number | Yes |
| c | number | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| e | number | Yes |
| [f](../../apis-na/arkts-apis/arkts-na-float-c.md) | number | Yes |

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

Resets the current transformation to the identity matrix, and then creates a new transformation matrix based on the specified **Matrix2D** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void--><!--Device-CanvasRenderer-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transform](#transform) | [Matrix2D](../arkts-apis/arkts-arkui-matrix2d-c.md) | No |

## stroke

```TypeScript
stroke(): void
```

Strokes (outlines) this path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-stroke(): void--><!--Device-CanvasRenderer-stroke(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stroke

```TypeScript
stroke(path: Path2D): void
```

Strokes (outlines) a specified path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-stroke(path: Path2D): void--><!--Device-CanvasRenderer-stroke(path: Path2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes |

## strokeRect

```TypeScript
strokeRect(x: number, y: number, w: number, h: number): void
```

Draws an outlined rectangle on the canvas without filling its interior.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-strokeRect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasRenderer-strokeRect(x: number, y: number, w: number, h: number): void-End-->

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
strokeText(text: string, x: number, y: number, maxWidth?: number): void
```

Draws stroked text on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-strokeText(text: string, x: number, y: number, maxWidth?: number): void--><!--Device-CanvasRenderer-strokeText(text: string, x: number, y: number, maxWidth?: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| x | number | Yes |
| y | number | Yes |
| maxWidth | number | No |

## transferFromImageBitmap

```TypeScript
transferFromImageBitmap(bitmap: ImageBitmap): void
```

Displays the specified **ImageBitmap** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void--><!--Device-CanvasRenderer-transferFromImageBitmap(bitmap: ImageBitmap): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bitmap | [ImageBitmap](arkts-arkui-imagebitmap-c.md) | Yes |

## transform

```TypeScript
transform(a: number, b: number, c: number, d: number, e: number, f: number): void
```

Defines a transformation matrix. To transform a graph, you only need to set parameters of the matrix. The coordinates of the graph are multiplied by the matrix values to obtain new coordinates of the transformed graph. You can use the matrix to implement multiple transform effects. > **NOTE：**> > The coordinates of each point in the graph after transformation can be calculated > using the following formula: > > **x** and **y** represent coordinates before transformation, and **x'** and **y'** > represent coordinates after transformation. > > - x' = `a * x + c * y + e` > > - y' = `b * x + d * y + f`

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-transform(a: number, b: number, c: number, d: number, e: number, f: number): void--><!--Device-CanvasRenderer-transform(a: number, b: number, c: number, d: number, e: number, f: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| a | number | Yes |
| b | number | Yes |
| c | number | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| e | number | Yes |
| [f](../../apis-na/arkts-apis/arkts-na-float-c.md) | number | Yes |

## translate

```TypeScript
translate(x: number, y: number): void
```

Moves the origin of the coordinate system.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-translate(x: number, y: number): void--><!--Device-CanvasRenderer-translate(x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## antialias

```TypeScript
antialias: boolean | undefined
```

Sets whether to enable anti-aliasing for drawing graphics and text. Setting this API overrides the anti-aliasing effect in [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md#renderingcontextsettings). If this API is not specified, the default value is **undefined** and the anti-aliasing effect in [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md#renderingcontextsettings) is used. Whether to enable anti-aliasing for drawing graphics and text. **true**: Anti-aliasing is enabled. **false**: Anti-aliasing is disabled. When the value is **undefined**, the anti-aliasing effect in [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md#renderingcontextsettings) is used.

**Type:** boolean \| undefined

**Default:** undefined

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CanvasRenderer-antialias: boolean | undefined--><!--Device-CanvasRenderer-antialias: boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: CanvasDirection
```

Sets the text direction. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. For details, see [CanvasDirection](arkts-arkui-canvasdirection-t.md#canvasdirection). Default value: **"inherit"**

**Type:** [CanvasDirection](arkts-arkui-canvasdirection-t.md)

**Default:** inherit

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-direction: CanvasDirection--><!--Device-CanvasRenderer-direction: CanvasDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fillStyle

```TypeScript
fillStyle: string | number | CanvasGradient | CanvasPattern
```

Sets the fill color for rendering. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. - When the type is string, this attribute indicates the color of the fill area. For details about the color format, see the description for the string type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md#resourcecolor). - When the type is number, this attribute indicates the color of the fill area. Fully transparent colors are not supported. For details about the color format, see the description for the number type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md#resourcecolor). - When the type is **CanvasGradient**, this attribute indicates a gradient object, which is created via the [createLinearGradient](#createlineargradient) API. - When the type is **CanvasPattern**, this attribute indicates a pattern, which is created via the [createPattern](#createpattern) API. Default value: **'#000000'** (black) Invalid values do not take effect. The effect before the setting is retained.

**Type:** string \| number \| [CanvasGradient](arkts-arkui-canvasgradient-c.md) \| [CanvasPattern](arkts-arkui-canvaspattern-i.md)

**Default:** #000000 (black)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-fillStyle: string | number | CanvasGradient | CanvasPattern--><!--Device-CanvasRenderer-fillStyle: string | number | CanvasGradient | CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## filter

```TypeScript
filter: string
```

Sets the filter for an image. Any number of filters can be combined. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. > **NOTE：**> > The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting > from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not > packaged by default when a project or module is created. To package these resources, go to **buildOption** in the > module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. > For details, see the description of copyCodeResource. Available values are as follows: - **'none'**: no filter effect. - **'blur(`&lt;length&gt;`)'**: applies the Gaussian blur to the image. The value must be greater than or equal to 0. The unit can be px, vp, or rem. The default value is **blur(0px)**. - **'brightness([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: applies a linear multiplier to the image to adjust its brightness. The value can be a number or a percentage, and must be greater than or equal to 0. The default value is **brightness(1)**. - **'contrast([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: adjusts the contrast of the image. The value can be a number or a percentage, and must be greater than or equal to 0. The default value is **contrast(1)**. - **'grayscale([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: converts the image to grayscale. The value can be a number or a percentage, and must be within the range of [0, 1]. The default value is **grayscale(0)**. - **'hue-rotate(`&lt;angle&gt;`)'**: applies hue rotation to the image. The value ranges from **0deg** to **360deg**. The default value is **hue-rotate(0deg)**. - **'invert([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: inverts the input image. The value can be a number or a percentage, and must be within the range of [0, 1]. The default value is **invert(0)**. - **'opacity([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: adjusts the opacity of the image. The value can be a number or a percentage, and must be within the range of [0, 1]. The default value is **opacity(1)**. - **'saturate([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: adjusts the saturation of the image. The value can be a number or a percentage, and must be greater than or equal to 0. The default value is **saturate(1)**. - **'sepia([`&lt;number&gt;`\|`&lt;percentage&gt;`])'**: converts the image to sepia. The value can be a number or a percentage, and must be within the range of [0, 1]. The default value is **sepia(0)**.

**Type:** string

**Default:** none

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-filter: string--><!--Device-CanvasRenderer-filter: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font: string
```

Sets the text font. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Syntax: ctx.font = 'font-style font-weight font-size font-family' - (Optional) **font-style**: font style. Available values are **normal** and **italic**. - (Optional) **font-weight**: font weight. Available values are as follows: **normal**, **bold**, **bolder**, **lighter**, **100**, **200**, **300**, **400**, **500**, **600**, **700**, **800**, **900**. - (Optional) **font-size**: font size and line height. The unit can be px or vp and must be specified. - (Optional) **font-family**: font family. Available values are **sans-serif**, **serif**, and **monospace**. Starting from API version 20, this API is used to set registered custom fonts (the DevEco Studio Previewer does not support custom fonts). You can register a custom font in either of the following ways: Register a custom font by calling the asynchronous API this.uiContext.getFont().registerFont of ArkUI. Immediate rendering after calling this API may result in the custom font not taking effect. Directly call the fontCollection.[loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync) API of the font engine to register the custom font. In this case, the **fontCollection** instance must be **text.FontCollection.getGlobalInstance()** because the component loads fonts from this instance by default. If you use another instance, the custom font may not take effect.

**Type:** string

**Default:** normal normal 14px sans-serif

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-font: string--><!--Device-CanvasRenderer-font: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalAlpha

```TypeScript
globalAlpha: number
```

Sets the opacity. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. The value range is [0.0, 1.0]. **0.0** indicates completely transparent, and **1.0** indicates completely opaque. If the set value is less than 0.0, **0.0** will be used. If the set value is greater than 1.0, **1.0** will be used. In versions earlier than API version 18, if **NaN** or **Infinity** is set, rendering APIs cannot be called for rendering after this API. In API version 18 and later versions, if **NaN** or **Infinity** is set, the current API does not take effect, and other rendering APIs with valid arguments can be called normally. Default value: **1.0**

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-globalAlpha: number--><!--Device-CanvasRenderer-globalAlpha: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalCompositeOperation

```TypeScript
globalCompositeOperation: string
```

Sets the composite operation. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Available values are as follows: | Name | Description | | ------ | ------ | | source-over | Displays the new drawing above the existing drawing. Default value. | | source-atop | Displays the new drawing on the top of the existing drawing. | | source-in | Displays the new drawing inside the existing drawing. | | source-out | Displays part of the new drawing that is outside of the existing drawing. | | destination-over | Displays the existing drawing above the new drawing. | | destination-atop | Displays the existing drawing on the top of the new drawing. | | destination-in | Displays the existing drawing inside the new drawing. | | destination-out | Displays the existing drawing outside the new drawing. | | lighter | Displays both the new and existing drawing. | | copy | Displays the new drawing and neglects the existing drawing. | | xor | Combines the new drawing and existing drawing using the XOR operation. | Default value: **'source-over'**

**Type:** string

**Default:** source-over

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-globalCompositeOperation: string--><!--Device-CanvasRenderer-globalCompositeOperation: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingEnabled

```TypeScript
imageSmoothingEnabled: boolean
```

Indicates whether to apply image smoothing adjustments when drawing images. The value **true** means to enable smoothing, and **false** means to disable it. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **true**. > **NOTE：**> > The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting > from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not > packaged by default when a project or module is created. To package these resources, go to **buildOption** in the > module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. > For details, see the description of copyCodeResource in **resOptions**.

**Type:** boolean

**Default:** true

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-imageSmoothingEnabled: boolean--><!--Device-CanvasRenderer-imageSmoothingEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSmoothingQuality

```TypeScript
imageSmoothingQuality: ImageSmoothingQuality
```

Sets the image smoothing quality when **imageSmoothingEnabled** is set to **true**. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. For details, see [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md#imagesmoothingquality). Default value: **"low"** > **NOTE：**> > The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting > from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not > packaged by default when a project or module is created. To package these resources, go to **buildOption** in the > module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. > For details, see the description of copyCodeResource in **resOptions**.

**Type:** [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md)

**Default:** low

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-imageSmoothingQuality: ImageSmoothingQuality--><!--Device-CanvasRenderer-imageSmoothingQuality: ImageSmoothingQuality-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
letterSpacing: LengthMetrics | string
```

Sets the letter spacing. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Spacing between characters. When the LengthMetrics type is used: The spacing is set according to the specified unit. The FP, PERCENT, and LPX units are not supported and will be treated as invalid values. Negative and fractional values are supported. When set to a fraction, the spacing is not rounded. When the string type is used: Percentage values are not supported and will be treated as invalid. Negative and decimal values are supported. When set to a decimal value, the spacing is not rounded. If no unit is specified (for example, **letterSpacing = '10'**) and **LengthMetricsUnit** is not set, the default unit is vp. If **LengthMetricsUnit** is set to px, the default unit is px. If the value of **letterSpacing** is specified with a unit (for example, **letterSpacing='10vp'**), the letter spacing is set based on the specified unit. Default value: **0** (Invalid values are treated as the default value.) > **NOTE：**> > The LengthMetrics type is recommended for better performance.

**Type:** LengthMetrics \| string

**Default:** 0vp

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CanvasRenderer-letterSpacing: LengthMetrics | string--><!--Device-CanvasRenderer-letterSpacing: LengthMetrics | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineCap

```TypeScript
lineCap: CanvasLineCap
```

Sets the line caps. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, undefined will be returned.

**Type:** [CanvasLineCap](arkts-arkui-canvaslinecap-t.md)

**Default:** butt

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-lineCap: CanvasLineCap--><!--Device-CanvasRenderer-lineCap: CanvasLineCap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineDashOffset

```TypeScript
lineDashOffset: number
```

Sets the dashed line offset of the canvas. The value is of the float type. This attribute takes effect only when **setLineDash** is set. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **0.0** Default unit: vp Invalid values **NaN** and **Infinity** are treated as the default value.

**Type:** number

**Default:** 0.0

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-lineDashOffset: number--><!--Device-CanvasRenderer-lineDashOffset: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineJoin

```TypeScript
lineJoin: CanvasLineJoin
```

Sets the line join. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. For details, see [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md#canvaslinejoin). <br>Available values are as follows: <br>- **'round'**: The shape used to join line segments is a sector, whose radius at the rounded corner is equal to the line width. <br>- **'bevel'**: The shape used to join line segments is a triangle. The rectangular corner of each line is independent. <br>- **'miter'**: The shape used to join line segments has a mitered corner by extending the outside edges of the lines until they meet. You can view the effect of this attribute in **miterLimit**. <br>Default value: **'miter'**

**Type:** [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md)

**Default:** miter

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-lineJoin: CanvasLineJoin--><!--Device-CanvasRenderer-lineJoin: CanvasLineJoin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineWidth

```TypeScript
lineWidth: number
```

Sets the line width. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **1** (px) Default unit: vp The value does not support **0** or negative numbers. **0**, negative numbers, and **NaN** are handled as the default value. The value **Infinity** is invalid and no drawing is performed.

**Type:** number

**Default:** 1(px)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-lineWidth: number--><!--Device-CanvasRenderer-lineWidth: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## miterLimit

```TypeScript
miterLimit: number
```

Sets the miter limit, which specifies the distance between the inner and outer angles at line joins. This attribute takes effect only when **lineJoin** is set to **miter**. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **10px** Unit: px The value of **miterLimit** cannot be **0** or a negative number. Values of **0**, negative numbers, and **NaN** are handled with the default value. **Infinity** will cause an exception on the **miterLimit** attribute.

**Type:** number

**Default:** 10(px)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-miterLimit: number--><!--Device-CanvasRenderer-miterLimit: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowBlur

```TypeScript
shadowBlur: number
```

Sets the blur level for drawing shadows. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Blur level. A larger value produces a greater blur effect. The value is of float type and must be greater than or equal to 0. Default value: **0.0** Unit: px The value of **shadowBlur** cannot be a negative number. A negative number, **NaN**, and **Infinity** are treated as the default value.

**Type:** number

**Default:** 0

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-shadowBlur: number--><!--Device-CanvasRenderer-shadowBlur: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
shadowColor: string
```

Sets the shadow color. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. For details about the color format, see the description for the string type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md#resourcecolor). Default value: **'#00000000'** (transparent black)

**Type:** string

**Default:** transparent black

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-shadowColor: string--><!--Device-CanvasRenderer-shadowColor: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetX

```TypeScript
shadowOffsetX: number
```

Sets the horizontal offset between the drawn shadow and the original object. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **0.0** Default unit: vp Invalid values **NaN** and **Infinity** are treated as the default value.

**Type:** number

**Default:** 0

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-shadowOffsetX: number--><!--Device-CanvasRenderer-shadowOffsetX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffsetY

```TypeScript
shadowOffsetY: number
```

Sets the vertical offset between the drawn shadow and the original object. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **0.0** Default unit: vp Invalid values **NaN** and **Infinity** are treated as the default value.

**Type:** number

**Default:** 0

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-shadowOffsetY: number--><!--Device-CanvasRenderer-shadowOffsetY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeStyle

```TypeScript
strokeStyle: string | number | CanvasGradient | CanvasPattern
```

Sets the stroke color. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. - When the type is string, this attribute indicates the stroke color. For details about the color format, see the description for the string type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md#resourcecolor). - When the type is number, this attribute indicates the stroke color. Fully transparent colors are not supported. For details about the color format, see the description for the number type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md#resourcecolor). - When the type is **CanvasGradient**, this attribute indicates a gradient object, which is created via the [createLinearGradient](#createlineargradient) API. - When the type is **CanvasPattern**, this attribute indicates a pattern, which is created via the createPattern API. Default value: **'#000000'** (black) Invalid values do not take effect. The effect before the setting is retained.

**Type:** string \| number \| [CanvasGradient](arkts-arkui-canvasgradient-c.md) \| [CanvasPattern](arkts-arkui-canvaspattern-i.md)

**Default:** #000000 (black)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-strokeStyle: string | number | CanvasGradient | CanvasPattern--><!--Device-CanvasRenderer-strokeStyle: string | number | CanvasGradient | CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign: CanvasTextAlign
```

Sets the text alignment type. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. In the **ltr** layout mode, the value **'start'** equals **'left'**. In the **rtl** layout mode, the value **'start'** equals **'right'**. Default value: **'left'**

**Type:** [CanvasTextAlign](arkts-arkui-canvastextalign-t.md)

**Default:** left

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-textAlign: CanvasTextAlign--><!--Device-CanvasRenderer-textAlign: CanvasTextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBaseline

```TypeScript
textBaseline: CanvasTextBaseline
```

Sets the horizontal alignment baseline for text rendering. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned. Default value: **'alphabetic'**

**Type:** [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md)

**Default:** alphabetic

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasRenderer-textBaseline: CanvasTextBaseline--><!--Device-CanvasRenderer-textBaseline: CanvasTextBaseline-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
