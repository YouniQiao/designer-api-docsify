# Canvas

A carrier that carries the drawn content and drawing status. > **NOTE：**> > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions. > > > The canvas comes with a default brush. The brush is black, has anti-aliasing enabled, and has no other style > effects. This default brush is used when no brush or pen is actively set in the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-drawing-class Canvas--><!--Device-drawing-class Canvas-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## attachBrush

```TypeScript
attachBrush(brush: Brush): void
```

Attaches a brush to the canvas. When you draw on the canvas, the brush's style is used to fill the interior of shapes. > **NOTE：**> > If the brush effect changes after this API is called, you must call the API again if you want to use the new > effect in the subsequent drawing.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-attachBrush(brush: Brush): void--><!--Device-Canvas-attachBrush(brush: Brush): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## attachPen

```TypeScript
attachPen(pen: Pen): void
```

Attaches a pen to the canvas. When you draw on the canvas, the pen's style is used to outline shapes. > **NOTE：**> > If the pen effect changes after this API is called, you must call the API again if you want to use the new > effect in the subsequent drawing.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-attachPen(pen: Pen): void--><!--Device-Canvas-attachPen(pen: Pen): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pen | [Pen](arkts-arkgraphics2d-drawing-pen-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clear

```TypeScript
clear(color: common2D.Color): void
```

Clears the canvas with a given color. This API has the same effect as [drawColor](#drawColor).

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clear(color: common2D.Color): void--><!--Device-Canvas-clear(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clear

```TypeScript
clear(color: common2D.Color | number): void
```

Clears the canvas with a given color.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clear(color: common2D.Color | int): void--><!--Device-Canvas-clear(color: common2D.Color | int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color \| number | Yes |

## clipPath

```TypeScript
clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

Clips the drawable area of the canvas using a custom path.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void--><!--Device-Canvas-clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | No |
| doAntiAlias | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clipRect

```TypeScript
clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

Clips the drawable area of the canvas using a rectangle.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void--><!--Device-Canvas-clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | No |
| doAntiAlias | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clipRegion

```TypeScript
clipRegion(region: Region, clipOp?: ClipOp): void
```

Clips a region on the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clipRegion(region: Region, clipOp?: ClipOp): void--><!--Device-Canvas-clipRegion(region: Region, clipOp?: ClipOp): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clipRoundRect

```TypeScript
clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

Clips a rounded rectangle on the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void--><!--Device-Canvas-clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | No |
| doAntiAlias | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## concatMatrix

```TypeScript
concatMatrix(matrix: Matrix): void
```

Multiplies the current canvas matrix by the incoming matrix on the left. This API does not affect previous drawing operations, but subsequent drawing and clipping operations will be influenced by this matrix in terms of shape and position.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-concatMatrix(matrix: Matrix): void--><!--Device-Canvas-concatMatrix(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## constructor

```TypeScript
constructor(pixelmap: image.PixelMap)
```

Creates a **Canvas** object that uses a **PixelMap** as the drawing target.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Canvas-constructor(pixelmap: image.PixelMap)--><!--Device-Canvas-constructor(pixelmap: image.PixelMap)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## detachBrush

```TypeScript
detachBrush(): void
```

Detaches the brush from the canvas. When you draw on the canvas, the brush is no longer used to fill the interior of shapes.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-detachBrush(): void--><!--Device-Canvas-detachBrush(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## detachPen

```TypeScript
detachPen(): void
```

Detaches the pen from the canvas. When you draw on the canvas, the pen is no longer used to outline shapes.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-detachPen(): void--><!--Device-Canvas-detachPen(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## drawArc

```TypeScript
drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void
```

Draws an arc on the canvas. with the start angle and sweep angle specified. If the absolute value of the sweep angle exceeds 360 degrees, an ellipse is drawn.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawArc(arc: common2D.Rect, startAngle: double, sweepAngle: double): void--><!--Device-Canvas-drawArc(arc: common2D.Rect, startAngle: double, sweepAngle: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arc | common2D.Rect | Yes |
| startAngle | number | Yes |
| sweepAngle | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawArcWithCenter

```TypeScript
drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void
```

Draws an arc on the canvas. It enables you to define the start angle, sweep angle, and whether the arc's endpoints should connect to its center.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawArcWithCenter(arc: common2D.Rect, startAngle: double, sweepAngle: double, useCenter: boolean): void--><!--Device-Canvas-drawArcWithCenter(arc: common2D.Rect, startAngle: double, sweepAngle: double, useCenter: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arc | common2D.Rect | Yes |
| startAngle | number | Yes |
| sweepAngle | number | Yes |
| useCenter | boolean | Yes |

## drawBackground

```TypeScript
drawBackground(brush: Brush): void
```

Uses a brush to fill the drawable area of the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawBackground(brush: Brush): void--><!--Device-Canvas-drawBackground(brush: Brush): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawCircle

```TypeScript
drawCircle(x: number, y: number, radius: number): void
```

Draws a circle. If the radius is less than or equal to zero, nothing is drawn. By default, black is used for filling.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawCircle(x: double, y: double, radius: double): void--><!--Device-Canvas-drawCircle(x: double, y: double, radius: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| radius | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawColor

```TypeScript
drawColor(color: common2D.Color, blendMode?: BlendMode): void
```

Fills the drawable area of the canvas with the specified color and [BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md#BlendMode).

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawColor(color: common2D.Color, blendMode?: BlendMode): void--><!--Device-Canvas-drawColor(color: common2D.Color, blendMode?: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |
| blendMode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawColor

```TypeScript
drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void
```

Fills the drawable area of the canvas with the specified color and [BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md#BlendMode). This API provides better performance than [drawColor](#drawColor) and is recommended.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawColor(alpha: int, red: int, green: int, blue: int, blendMode?: BlendMode): void--><!--Device-Canvas-drawColor(alpha: int, red: int, green: int, blue: int, blendMode?: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alpha | number | Yes |
| red | number | Yes |
| green | number | Yes |
| blue | number | Yes |
| blendMode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawColor

```TypeScript
drawColor(color: number, blendMode?: BlendMode): void
```

Fills the drawable area of the canvas with the specified color and [BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md#BlendMode).

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawColor(color: int, blendMode?: BlendMode): void--><!--Device-Canvas-drawColor(color: int, blendMode?: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |
| blendMode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawGlyphs

```TypeScript
drawGlyphs(glyphIds: Array<number>, glyphIdOffset: number, positions: Array<common2D.Point>,
      positionOffset: number, glyphCount: number, font: Font): void
```

Draws the array of glyphs with specified font. Nothing is drawn if glyphCount is smaller than or equals to 0.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Canvas-drawGlyphs(glyphIds: Array<int>, glyphIdOffset: int, positions: Array<common2D.Point>,      positionOffset: int, glyphCount: int, font: Font): void--><!--Device-Canvas-drawGlyphs(glyphIds: Array<int>, glyphIdOffset: int, positions: Array<common2D.Point>,      positionOffset: int, glyphCount: int, font: Font): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphIds | Array & lt;number & gt; | Yes |
| glyphIdOffset | number | Yes |
| positions | Array & lt;common2D.Point & gt; | Yes |
| positionOffset | number | Yes |
| glyphCount | number | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## drawImage

```TypeScript
drawImage(pixelmap: image.PixelMap, left: number, top: number, samplingOptions?: SamplingOptions): void
```

Draws an image. The coordinates of the upper left corner of the image are (left, top).

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawImage(pixelmap: image.PixelMap, left: double, top: double, samplingOptions?: SamplingOptions): void--><!--Device-Canvas-drawImage(pixelmap: image.PixelMap, left: double, top: double, samplingOptions?: SamplingOptions): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| left | number | Yes |
| top | number | Yes |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawImageLattice

```TypeScript
drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect,
      filterMode: FilterMode): void
```

Splits an image into multiple sections based on the lattice object's configuration and draws each section into the specified target rectangle on the canvas. When this API is used, the anti-aliasing enablement setting does not take effect. The intersections of even-numbered rows and columns (starting from 0) are fixed points. If the fixed lattice area fits within the target rectangle, it will be drawn without scaling. Otherwise, it will be scaled proportionally to fit the target rectangle. Any remaining space will be filled by stretching or compressing the remaining sections to cover the entire target rectangle.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect,      filterMode: FilterMode): void--><!--Device-Canvas-drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect,      filterMode: FilterMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| lattice | [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) | Yes |
| dstRect | common2D.Rect | Yes |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawImageNine

```TypeScript
drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect,
      filterMode: FilterMode): void
```

Splits an image into nine sections using two horizontal and two vertical lines: four edge sections, four corner sections, and a central section. When this API is used, the anti-aliasing enablement setting does not take effect. If the four corner sections are smaller than the target rectangle, they will be drawn in the target rectangle without scaling. Otherwise, they will be scaled to fit the target rectangle. Any remaining space will be filled by stretching or compressing the other five sections to cover the entire target rectangle.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect,      filterMode: FilterMode): void--><!--Device-Canvas-drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect,      filterMode: FilterMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| center | common2D.Rect | Yes |
| dstRect | common2D.Rect | Yes |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawImageRect

```TypeScript
drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void
```

Draws an image onto a specified area of the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void--><!--Device-Canvas-drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| dstRect | common2D.Rect | Yes |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawImageRectWithSrc

```TypeScript
drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void
```

Draws a portion of an image onto a specified area of the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void--><!--Device-Canvas-drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| srcRect | common2D.Rect | Yes |
| dstRect | common2D.Rect | Yes |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | No |
| constraint | [SrcRectConstraint](arkts-arkgraphics2d-drawing-srcrectconstraint-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawLine

```TypeScript
drawLine(x0: number, y0: number, x1: number, y1: number): void
```

Draws a line segment from the start point to the end point. If the coordinates of the start point are the same as those of the end point, nothing is drawn.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawLine(x0: double, y0: double, x1: double, y1: double): void--><!--Device-Canvas-drawLine(x0: double, y0: double, x1: double, y1: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x0 | number | Yes |
| y0 | number | Yes |
| x1 | number | Yes |
| y1 | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawNestedRoundRect

```TypeScript
drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void
```

Draws two nested rounded rectangles. The outer rectangle boundary must contain the inner rectangle boundary. Otherwise, there is no drawing effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void--><!--Device-Canvas-drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outer | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |
| inner | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawOval

```TypeScript
drawOval(oval: common2D.Rect): void
```

Draws an oval on the canvas, where the shape and position of the oval are defined by its bounding rectangle.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawOval(oval: common2D.Rect): void--><!--Device-Canvas-drawOval(oval: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oval | common2D.Rect | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawPath

```TypeScript
drawPath(path: Path): void
```

Draws a custom path, which contains a set of path outlines. Each path outline can be open or closed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawPath(path: Path): void--><!--Device-Canvas-drawPath(path: Path): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawPixelMapMesh

```TypeScript
drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number,
      vertices: Array<number>, vertOffset: number, colors: Array<number> | null, colorOffset: number): void
```

Draws a **PixelMap** based on a mesh, with the mesh vertices evenly distributed across the **PixelMap**. (This API works with brushes but not pens.)

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: int, meshHeight: int,      vertices: Array<double>, vertOffset: int, colors: Array<int> | null, colorOffset: int): void--><!--Device-Canvas-drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: int, meshHeight: int,      vertices: Array<double>, vertOffset: int, colors: Array<int> | null, colorOffset: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| meshWidth | number | Yes |
| meshHeight | number | Yes |
| vertices | Array & lt;number & gt; | Yes |
| vertOffset | number | Yes |
| colors | Array & lt;number & gt; \ | null | Yes |
| colorOffset | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawPoint

```TypeScript
drawPoint(x: number, y: number): void
```

Draws a point.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawPoint(x: double, y: double): void--><!--Device-Canvas-drawPoint(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawPoints

```TypeScript
drawPoints(points: Array<common2D.Point>, mode?: PointMode): void
```

Draws a group of points, line segments, or polygons on the canvas, with the specified drawing mode. An array is used to hold these points.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawPoints(points: Array<common2D.Point>, mode?: PointMode): void--><!--Device-Canvas-drawPoints(points: Array<common2D.Point>, mode?: PointMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | Yes |
| mode | [PointMode](arkts-arkgraphics2d-drawing-pointmode-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawRect

```TypeScript
drawRect(rect: common2D.Rect): void
```

Draws a rectangle. By default, black is used for filling.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawRect(rect: common2D.Rect): void--><!--Device-Canvas-drawRect(rect: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawRect

```TypeScript
drawRect(left: number, top: number, right: number, bottom: number): void
```

Draws a rectangle. By default, black is used for filling. This API provides better performance than [drawRect](#drawRect) and is recommended.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawRect(left: double, top: double, right: double, bottom: double): void--><!--Device-Canvas-drawRect(left: double, top: double, right: double, bottom: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawRegion

```TypeScript
drawRegion(region: Region): void
```

Draws a region.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawRegion(region: Region): void--><!--Device-Canvas-drawRegion(region: Region): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawRoundRect

```TypeScript
drawRoundRect(roundRect: RoundRect): void
```

Draws a rounded rectangle.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawRoundRect(roundRect: RoundRect): void--><!--Device-Canvas-drawRoundRect(roundRect: RoundRect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawShadow

```TypeScript
drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number,
      ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag) : void
```

Draws a spot shadow and uses a given path to outline the ambient shadow.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: double,      ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag) : void--><!--Device-Canvas-drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: double,      ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag) : void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| planeParams | common2D.Point3d | Yes |
| devLightPos | common2D.Point3d | Yes |
| lightRadius | number | Yes |
| ambientColor | common2D.Color | Yes |
| spotColor | common2D.Color | Yes |
| flag | [ShadowFlag](arkts-arkgraphics2d-drawing-shadowflag-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawShadow

```TypeScript
drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number,
      ambientColor: common2D.Color | number, spotColor: common2D.Color | number, flag: ShadowFlag) : void
```

Draws a spot shadow and uses a given path to outline the ambient shadow.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: double,      ambientColor: common2D.Color | int, spotColor: common2D.Color | int, flag: ShadowFlag) : void--><!--Device-Canvas-drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: double,      ambientColor: common2D.Color | int, spotColor: common2D.Color | int, flag: ShadowFlag) : void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| planeParams | common2D.Point3d | Yes |
| devLightPos | common2D.Point3d | Yes |
| lightRadius | number | Yes |
| ambientColor | common2D.Color \| number | Yes |
| spotColor | common2D.Color \| number | Yes |
| flag | [ShadowFlag](arkts-arkgraphics2d-drawing-shadowflag-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawSingleCharacter

```TypeScript
drawSingleCharacter(text: string, font: Font, x: number, y: number): void
```

Draws a single character. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawSingleCharacter(text: string, font: Font, x: double, y: double): void--><!--Device-Canvas-drawSingleCharacter(text: string, font: Font, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawSingleCharacterWithFeatures

```TypeScript
drawSingleCharacterWithFeatures(text: string, font: Font, x: number, y: number, features: Array<FontFeature>): void
```

Draws a single character with font features. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character.

**Since:** 24

**Deprecated since:** -1

<!--Device-Canvas-drawSingleCharacterWithFeatures(text: string, font: Font, x: double, y: double, features: Array<FontFeature>): void--><!--Device-Canvas-drawSingleCharacterWithFeatures(text: string, font: Font, x: double, y: double, features: Array<FontFeature>): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| x | number | Yes |
| y | number | Yes |
| features | Array & lt;FontFeature & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## drawTextBlob

```TypeScript
drawTextBlob(blob: TextBlob, x: number, y: number): void
```

Draws a text blob. If the typeface used to construct **blob** does not support a character, that character will not be drawn.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawTextBlob(blob: TextBlob, x: double, y: double): void--><!--Device-Canvas-drawTextBlob(blob: TextBlob, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blob | [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) | Yes |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## drawVertices

```TypeScript
drawVertices(vertexMode: VertexMode, vertexCount: number, positions: Array<common2D.Point>,
      texs: Array<common2D.Point> | null, colors: Array<number> | null, indexCount: number,
      indices: Array<number> | null, mode: BlendMode): void
```

Draws a triangle mesh described by the vertex array.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-drawVertices(vertexMode: VertexMode, vertexCount: int, positions: Array<common2D.Point>,      texs: Array<common2D.Point> | null, colors: Array<int> | null, indexCount: int,      indices: Array<int> | null, mode: BlendMode): void--><!--Device-Canvas-drawVertices(vertexMode: VertexMode, vertexCount: int, positions: Array<common2D.Point>,      texs: Array<common2D.Point> | null, colors: Array<int> | null, indexCount: int,      indices: Array<int> | null, mode: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vertexMode | [VertexMode](arkts-arkgraphics2d-drawing-vertexmode-e.md) | Yes |
| vertexCount | number | Yes |
| positions | Array & lt;common2D.Point & gt; | Yes |
| texs | Array & lt;common2D.Point & gt; \ | null | Yes |
| colors | Array & lt;number & gt; \ | null | Yes |
| indexCount | number | Yes |
| [indices](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-customgeometry-c.md) | Array & lt;number & gt; \ | null | Yes |
| mode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## getHeight

```TypeScript
getHeight(): number
```

Obtains the canvas height.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-getHeight(): int--><!--Device-Canvas-getHeight(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLocalClipBounds

```TypeScript
getLocalClipBounds(): common2D.Rect
```

Obtains the bounds of the cropping region of the canvas.

**Since:** 12

**Deprecated since:** -1

<!--Device-Canvas-getLocalClipBounds(): common2D.Rect--><!--Device-Canvas-getLocalClipBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## getLocalClipBounds

```TypeScript
getLocalClipBounds(): common2D.Rect | undefined
```

Obtains the bounds of the cropping region of the canvas.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-getLocalClipBounds(): common2D.Rect | undefined--><!--Device-Canvas-getLocalClipBounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## getSaveCount

```TypeScript
getSaveCount(): number
```

Obtains the number of canvas states (canvas matrix and clipping area) saved in the stack.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-getSaveCount(): int--><!--Device-Canvas-getSaveCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getTotalMatrix

```TypeScript
getTotalMatrix(): Matrix
```

Obtains the canvas matrix.

**Since:** 12

**Deprecated since:** -1

<!--Device-Canvas-getTotalMatrix(): Matrix--><!--Device-Canvas-getTotalMatrix(): Matrix-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) |

## getTotalMatrix

```TypeScript
getTotalMatrix(): Matrix | undefined
```

Obtains the canvas matrix.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-getTotalMatrix(): Matrix | undefined--><!--Device-Canvas-getTotalMatrix(): Matrix | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) |

## getWidth

```TypeScript
getWidth(): number
```

Obtains the canvas width.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-getWidth(): int--><!--Device-Canvas-getWidth(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isClipEmpty

```TypeScript
isClipEmpty(): boolean
```

Checks whether the region that can be drawn is empty after clipping.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-isClipEmpty(): boolean--><!--Device-Canvas-isClipEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isOpaque

```TypeScript
isOpaque(): boolean
```

Checks whether the current layer that drawn into the device is opaque.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Canvas-isOpaque(): boolean--><!--Device-Canvas-isOpaque(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## quickRejectPath

```TypeScript
quickRejectPath(path: Path): boolean
```

Checks whether the path is not intersecting with the canvas area. The canvas area includes its boundaries.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-quickRejectPath(path: Path): boolean--><!--Device-Canvas-quickRejectPath(path: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## quickRejectRect

```TypeScript
quickRejectRect(rect: common2D.Rect): boolean
```

Checks whether the rectangle is not intersecting with the canvas area. The canvas area includes its boundaries.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-quickRejectRect(rect: common2D.Rect): boolean--><!--Device-Canvas-quickRejectRect(rect: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## resetClip

```TypeScript
resetClip(): void
```

Resets the clip status.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Canvas-resetClip(): void--><!--Device-Canvas-resetClip(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## resetMatrix

```TypeScript
resetMatrix(): void
```

Resets the matrix of this canvas to an identity matrix.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-resetMatrix(): void--><!--Device-Canvas-resetMatrix(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## restore

```TypeScript
restore(): void
```

Restores the canvas state (canvas matrix and clipping area) saved on the top of the stack.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-restore(): void--><!--Device-Canvas-restore(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## restoreToCount

```TypeScript
restoreToCount(count: number): void
```

Restores the canvas state (canvas matrix and clipping area) to a specified number.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-restoreToCount(count: int): void--><!--Device-Canvas-restoreToCount(count: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## rotate

```TypeScript
rotate(degrees: number, sx: number, sy: number) : void
```

Applies a rotation matrix on top of the current canvas matrix (identity matrix by default). Subsequent drawing and clipping operations will automatically have a rotation effect applied to their shapes and positions.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-rotate(degrees: double, sx: double, sy: double) : void--><!--Device-Canvas-rotate(degrees: double, sx: double, sy: double) : void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degrees | number | Yes |
| sx | number | Yes |
| sy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## save

```TypeScript
save(): number
```

Saves the canvas states (canvas matrix and drawable area) to the top of the stack. This API must be used in pair with [restore](#restore).

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-save(): int--><!--Device-Canvas-save(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## saveLayer

```TypeScript
saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): number
```

Saves the matrix and cropping region of the canvas, and allocates a **PixelMap** for subsequent drawing. If you call [restore](#restore), changes made to the matrix and clipping region are discarded, and the PixelMap is drawn.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): long--><!--Device-Canvas-saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): long-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect \| null | No |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## scale

```TypeScript
scale(sx: number, sy: number): void
```

Applies a scaling matrix on top of the current canvas matrix (identity matrix by default). Subsequent drawing and clipping operations will automatically have a scaling effect applied to the shapes and positions.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-scale(sx: double, sy: double): void--><!--Device-Canvas-scale(sx: double, sy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setMatrix

```TypeScript
setMatrix(matrix: Matrix): void
```

Sets a matrix for the canvas. Subsequent drawing and clipping operations will be affected by this matrix in terms of shape and position.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-setMatrix(matrix: Matrix): void--><!--Device-Canvas-setMatrix(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## skew

```TypeScript
skew(sx: number, sy: number) : void
```

Applies a skewing matrix on top of the current canvas matrix (identity matrix by default). Subsequent drawing and clipping operations will automatically have a skewing effect applied to the shapes and positions.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-skew(sx: double, sy: double) : void--><!--Device-Canvas-skew(sx: double, sy: double) : void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## translate

```TypeScript
translate(dx: number, dy: number): void
```

Applies a translation matrix on top of the current canvas matrix (identity matrix by default). Subsequent drawing and clipping operations will automatically have a translation effect applied to the shapes and positions.

**Since:** 23

**Deprecated since:** -1

<!--Device-Canvas-translate(dx: double, dy: double): void--><!--Device-Canvas-translate(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | number | Yes |
| dy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
