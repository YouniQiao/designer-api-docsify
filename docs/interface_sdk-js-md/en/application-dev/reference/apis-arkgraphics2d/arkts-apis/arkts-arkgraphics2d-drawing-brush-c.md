# Brush

Defines a brush, which is used to describe the style and color to fill in a shape.

> **NOTE：**&gt;
> - This module uses the physical pixel unit, px.&gt;
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 23

<!--Device-drawing-class Brush--><!--Device-drawing-class Brush-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Brush** object.

**Since:** 23

<!--Device-Brush-constructor()--><!--Device-Brush-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
const brushColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
brush.setColor(brushColor);
const newBrush = new drawing.Brush(brush);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { image } from '@kit.ImageKit';

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  const canvas = new drawing.Canvas(pixelMap);
})
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
let matrix2 = new drawing.Matrix(matrix);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
path.close();
let path1: drawing.Path =  new drawing.Path(path);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
const penColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
pen.setColor(penColor);
pen.setStrokeWidth(10);
const newPen = new drawing.Pen(pen);
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    let region2 = new drawing.Region(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region(100, 100, 200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
let roundRect2 = new drawing.RoundRect(roundRect);
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let typeFaceArgument = new drawing.TypefaceArguments();
```

## constructor

```TypeScript
constructor(brush: Brush)
```

Copies a **Brush** object to create a new one.

**Since:** 23

<!--Device-Brush-constructor(brush: Brush)--><!--Device-Brush-constructor(brush: Brush)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | Yes | Brush** object to copy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

See [constructor](#constructor)

## getAlpha

```TypeScript
getAlpha(): int
```

Obtains the alpha value of this brush.

**Since:** 23

<!--Device-Brush-getAlpha(): int--><!--Device-Brush-getAlpha(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| int | Alpha value of the brush. The return value is an integer ranging from 0 to 255. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let alpha = brush.getAlpha();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let alpha = pen.getAlpha();
```

## getColor

```TypeScript
getColor(): common2D.Color
```

Obtains the color of this brush.

**Since:** 12

<!--Device-Brush-getColor(): common2D.Color--><!--Device-Brush-getColor(): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | Color of the brush. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const brush = new drawing.Brush();
brush.setColor(color);
let colorGet = brush.getColor();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const pen = new drawing.Pen();
pen.setColor(color);
let colorGet = pen.getColor();
```

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

Obtains the color of this brush.

**Since:** 23

<!--Device-Brush-getColor(): common2D.Color | undefined--><!--Device-Brush-getColor(): common2D.Color | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color \| undefined | Returns a 32-bit (ARGB) variable that describes the color. |

**Examples**

See [getColor](#getcolor)

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

Obtains the brush color. The difference between this method and [getColor](#getcolor) is that this method returns a floating point number.

**Since:** 20

<!--Device-Brush-getColor4f(): common2D.Color4f--><!--Device-Brush-getColor4f(): common2D.Color4f-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f | Color of the brush. |

**Examples**

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const brush = new drawing.Brush();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
brush.setColor4f(color4f, colorSpace);
let color = brush.getColor4f();
```

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const pen = new drawing.Pen();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
pen.setColor4f(color4f, colorSpace);
let color = pen.getColor4f();
```

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

Obtains the color of a brush. The color is used by the brush to outline a shape.

**Since:** 24

<!--Device-Brush-getColor4f(): common2D.Color4f | undefined--><!--Device-Brush-getColor4f(): common2D.Color4f | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f \| undefined | Returns four floating point values that describes the color. |

**Examples**

See [getColor4f](#getcolor4f)

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

Obtains the color filter of this brush.

**Since:** 12

<!--Device-Brush-getColorFilter(): ColorFilter--><!--Device-Brush-getColorFilter(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ColorFilter | Color filter. |

**Examples**

```TypeScript
import {drawing} from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let setColorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
brush.setColorFilter(setColorFilter);
let filter = brush.getColorFilter();
```

```TypeScript
import {drawing} from '@kit.ArkGraphics2D';

let pen = new drawing.Pen();
let colorfilter = drawing.ColorFilter.createLumaColorFilter();
pen.setColorFilter(colorfilter);
let filter = pen.getColorFilter();
```

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

Obtains the color filter of this brush.

**Since:** 23

<!--Device-Brush-getColorFilter(): ColorFilter | undefined--><!--Device-Brush-getColorFilter(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ColorFilter \| undefined | ColorFilter. |

**Examples**

See [getColorFilter](#getcolorfilter)

## getHexColor

```TypeScript
getHexColor(): int
```

Obtains the color of this brush.

**Since:** 23

<!--Device-Brush-getHexColor(): int--><!--Device-Brush-getHexColor(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| int | Color, represented as a 32-bit unsigned integer in hexadecimal ARGB format. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
let brush = new drawing.Brush();
brush.setColor(color);
let hex_color: number = brush.getHexColor();
console.info('getHexColor: ', hex_color.toString(16));
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
let pen = new drawing.Pen();
pen.setColor(color);
let hex_color: number = pen.getHexColor();
console.info('getHexColor: ', hex_color.toString(16));
```

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

Checks whether anti-aliasing is enabled for this brush.

**Since:** 23

<!--Device-Brush-isAntiAlias(): boolean--><!--Device-Brush-isAntiAlias(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that anti-aliasing is enabled, and **false** means the opposite. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let isAntiAlias = brush.isAntiAlias();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let isAntiAlias = pen.isAntiAlias();
```

## reset

```TypeScript
reset(): void
```

Resets this brush to the initial state.

**Since:** 23

<!--Device-Brush-reset(): void--><!--Device-Brush-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.reset();
```

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
matrix.postScale(2, 3, 4, 5);
matrix.reset();
console.info("matrix= "+matrix.getAll().toString());
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(10, 10, 10, 10, 15, 15);
path.reset();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.reset();
```

## setAlpha

```TypeScript
setAlpha(alpha: int): void
```

Sets an alpha value for this brush.

**Since:** 23

<!--Device-Brush-setAlpha(alpha: int): void--><!--Device-Brush-setAlpha(alpha: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | int | Yes | Alpha value. The value is an integer in the range [0, 255]. If a floating point number is passed in, the value is rounded down. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setAlpha(128);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setAlpha(128);
```

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

Enables anti-aliasing for this brush. Anti-aliasing makes the edges of the content smoother. If this API is not called, anti-aliasing is disabled by default.

**Since:** 23

<!--Device-Brush-setAntiAlias(aa: boolean): void--><!--Device-Brush-setAntiAlias(aa: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aa | boolean | Yes | Whether to enable anti-aliasing. The value **true** means to enable anti-aliasing, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setAntiAlias(true);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setAntiAlias(true);
```

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

Sets a blend mode for this brush. If this API is not called, the default blend mode is **SRC_OVER**.

**Since:** 23

<!--Device-Brush-setBlendMode(mode: BlendMode): void--><!--Device-Brush-setBlendMode(mode: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | BlendMode | Yes | Blend mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setBlendMode(drawing.BlendMode.SRC);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setBlendMode(drawing.BlendMode.SRC);
```

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

Sets a color for this brush.

**Since:** 23

<!--Device-Brush-setColor(color: common2D.Color): void--><!--Device-Brush-setColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | common2D.Color | Yes | Color in ARGB format. The value of each color channel is an integer ranging from 0 to 255. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const brush = new drawing.Brush();
brush.setColor(color);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setColor(255, 255, 0, 0);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setColor(0xffff0000);
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const pen = new drawing.Pen();
pen.setColor(color);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setColor(255, 255, 0, 0);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setColor(0xffff0000);
```

## setColor

```TypeScript
setColor(alpha: int, red: int, green: int, blue: int): void
```

Sets a color for this brush. This API provides better performance than [setColor](#setcolor) and is recommended.

**Since:** 23

<!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | int | Yes | Alpha channel value of the color in ARGB format. The value is an integer ranging from 0 to 255. Any passed-in floating point number is rounded down. |
| red | int | Yes | Red channel value of the color in ARGB format. The value is an integer ranging from 0 to 255. Any passed-in floating point number is rounded down. |
| green | int | Yes | Green channel value of the color in ARGB format. The value is an integer ranging from 0 to 255. Any passed-in floating point number is rounded down. |
| blue | int | Yes | Blue channel value of the color in ARGB format. The value is an integer ranging from 0 to 2 55. Any passed-in floating point number is rounded down. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

See [setColor](#setcolor)

## setColor

```TypeScript
setColor(color: int): void
```

Sets a color for this brush.

**Since:** 23

<!--Device-Brush-setColor(color: int): void--><!--Device-Brush-setColor(color: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | int | Yes | Color in hexadecimal ARGB format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

See [setColor](#setcolor)

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

Sets the color and standard color gamut for this brush. The difference between this method and [setColor](#setcolor) is that the color gamut can be set separately.

**Since:** 24

<!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color4f | common2D.Color4f | Yes | Color in the ARGB format. The value of each color channel is a floating point number ranging from 0.0 to 1.0. Values above 1.0 default to **1.0**, and values below 0.0 default to **0.0**. |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | Yes | Standard color gamut object. **null** indicates SRGB. |

**Examples**

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const brush = new drawing.Brush();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
brush.setColor4f(color4f, colorSpace);
```

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const pen = new drawing.Pen();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f:common2D.Color4f = {alpha:1, red:0.5, green:0.4, blue:0.7};
pen.setColor4f(color4f, colorSpace);
```

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

Sets a color filter for this brush.

**Since:** 23

<!--Device-Brush-setColorFilter(filter: ColorFilter | null): void--><!--Device-Brush-setColorFilter(filter: ColorFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | ColorFilter \| null | Yes | Defines a color filter. If **null** is passed in, the color filter is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
brush.setColorFilter(colorFilter);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
pen.setColorFilter(colorFilter);
```

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

Sets an image filter for this brush.

**Since:** 23

<!--Device-Brush-setImageFilter(filter: ImageFilter | null): void--><!--Device-Brush-setImageFilter(filter: ImageFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | Yes | Image filter. If **null** is passed in, the image filter effect of the brush will be cleared. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import {drawing} from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.DECAL);
brush.setImageFilter(imgFilter);
brush.setImageFilter(null);
```

```TypeScript
import {drawing} from '@kit.ArkGraphics2D';

let colorfilter = drawing.ColorFilter.createSRGBGammaToLinear();
let imgFilter = drawing.ImageFilter.createFromColorFilter(colorfilter);
let pen = new drawing.Pen();
pen.setImageFilter(imgFilter);
pen.setImageFilter(null);
```

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

Adds a mask filter for this brush.

**Since:** 23

<!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | Yes | Mask filter. If **null** is passed in, the mask filter is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const brush = new drawing.Brush();
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
    brush.setMaskFilter(maskFilter);
  }
}
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
    pen.setMaskFilter(maskFilter);
  }
}
```

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

Sets the shader effect for this brush.

**Since:** 23

<!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | Yes | ShaderEffect** object. If **null** is passed in, the shader effect will be cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
brush.setShaderEffect(shaderEffect);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
pen.setShaderEffect(shaderEffect);
```

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

Sets a shadow layer for this brush. The shadow layer effect takes effect only when text is drawn.

**Since:** 23

<!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | Yes | Implements a shadow layer. If **null** is passed in, the shadow layer is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(60);

    let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);

    let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(pen_color);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 100);
    canvas.detachPen();

    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();

    let brush = new drawing.Brush();
    let brush_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    brush.setColor(brush_color);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 100);
    canvas.detachBrush();

    brush.setShadowLayer(shadowLayer);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 200);
    canvas.detachBrush();
  }
}
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(60);
    let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);
    let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(pen_color);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 100);
    canvas.detachPen();
    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();
  }
}
```

