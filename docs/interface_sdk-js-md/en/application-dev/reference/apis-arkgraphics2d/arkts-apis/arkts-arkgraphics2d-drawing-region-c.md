# Region

Describes a region, which is used to describe the region where the shape can be drawn.

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 12.&gt;
> - This module uses the physical pixel unit, px.&gt;
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 23

<!--Device-drawing-class Region--><!--Device-drawing-class Region-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

Constructs a **Region** object.

**Since:** 23

<!--Device-Region-constructor()--><!--Device-Region-constructor()-End-->

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
constructor(region: Region)
```

Copies a **Region** object.

**Since:** 23

<!--Device-Region-constructor(region: Region)--><!--Device-Region-constructor(region: Region)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Region to be copied. |

**Examples**

See [constructor](#constructor)

## constructor

```TypeScript
constructor(left: int, top: int, right: int, bottom: int)
```

Constructs a rectangular region.

**Since:** 23

<!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)--><!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | int | Yes | Left position of the rectangle (X coordinate of the upper left corner). The value must be an integer. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| top | int | Yes | Top position of the rectangle (Y coordinate of the upper left corner). The value must be an integer. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |
| right | int | Yes | Right position of the rectangle (X coordinate of the lower right corner). The value must be an integer. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| bottom | int | Yes | Bottom position of the rectangle (Y coordinate of the lower right corner). The value must be an integer. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

**Examples**

See [constructor](#constructor)

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path
```

Obtains a new path that is the boundary of the existing region.

**Since:** 20

<!--Device-Region-getBoundaryPath(): Path--><!--Device-Region-getBoundaryPath(): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Path | Path of the boundary of the existing region. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let region = new drawing.Region();
let path = region.getBoundaryPath();
```

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path | undefined
```

Gets the boundary of the region, which represents by a path. Gets the bounds of the region.

**Since:** 24

<!--Device-Region-getBoundaryPath(): Path | undefined--><!--Device-Region-getBoundaryPath(): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Path \| undefined | Returns Path object. |

**Examples**

See [getBoundaryPath](#getboundarypath)

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

Obtains the boundaries of the existing region.

**Since:** 20

<!--Device-Region-getBounds(): common2D.Rect--><!--Device-Region-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | Bounding rectangle of this region. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
let text: string = 'hello world';
let glyphs: number[] = font.textToGlyphs(text);
let fontBounds: Array<common2D.Rect> = font.getBounds(glyphs);
for (let index = 0; index < fontBounds.length; index++) {
  console.info("get fontWidths[", index, "] left:", fontBounds[index].left, " top:", fontBounds[index].top,
    " right:", fontBounds[index].right, " bottom:", fontBounds[index].bottom);
}
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.lineTo(50, 40)
let rect : common2D.Rect = {left: 0, top: 0, right: 0, bottom: 0};
rect = path.getBounds();
console.info("test rect.left: " + rect.left);
console.info("test rect.top: " + rect.top);
console.info("test rect.right: " + rect.right);
console.info("test rect.bottom: " + rect.bottom);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let region = new drawing.Region();
let rect = region.getBounds();
```

## getBounds

```TypeScript
getBounds(): common2D.Rect | undefined
```

Gets the bounds of the region.

**Since:** 24

<!--Device-Region-getBounds(): common2D.Rect | undefined--><!--Device-Region-getBounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect \| undefined | Returns Rect object. |

**Examples**

See [getBounds](#getbounds)

## isComplex

```TypeScript
isComplex(): boolean
```

Checks whether this region contains multiple rectangles.

**Since:** 24

<!--Device-Region-isComplex(): boolean--><!--Device-Region-isComplex(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { RenderNode } from '@kit.ArkUI';

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
    let other = new drawing.Region();
    region.setRect(100, 100, 200, 200);
    region.op(new drawing.Region(220, 200, 280, 280), drawing.RegionOp.UNION);
    let flag: boolean = false;
    flag = region.isComplex();
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether the existing region is empty.

**Since:** 24

<!--Device-Region-isEmpty(): boolean--><!--Device-Region-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,20);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeEmpty();
let isEmpty = drawing.RectUtils.isEmpty(rect);
console.info('isEmpty :', isEmpty);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
isEmpty = drawing.RectUtils.isEmpty(rect2);
console.info('isEmpty :', isEmpty);
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
    let flag: boolean = region.isEmpty();
    console.info('flag: ', flag);
    region.setRect(100, 100, 400, 400);
    flag = region.isEmpty();
    console.info('flag: ', flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isEqual

```TypeScript
isEqual(other: Region): boolean
```

Checks whether another region is equal to this region.

**Since:** 24

<!--Device-Region-isEqual(other: Region): boolean--><!--Device-Region-isEqual(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Region | Yes | Region** object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** if the source rectangle is equal to the destination rectangle; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
if (matrix1.isEqual(matrix2)) {
  console.info("matrix1 and matrix2 are equal.");
} else {
  console.info("matrix1 and matrix2 are not equal.");
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
let rect2 = drawing.RectUtils.makeEmpty();
let isEqual = drawing.RectUtils.isEqual(rect, rect2);
console.info('isEqual :', isEqual);
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
    let other = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    other.setRect(150, 150, 250, 250);
    let flag: boolean = false;
    flag = region.isEqual(other);
    console.info('flag: ', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## isPointContained

```TypeScript
isPointContained(x: int, y:int): boolean
```

Checks whether a point is contained in this region.

**Since:** 23

<!--Device-Region-isPointContained(x: int, y:int): boolean--><!--Device-Region-isPointContained(x: int, y:int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | X coordinate of the point. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| y | int | Yes | Y coordinate of the point. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means yes; **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

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
    region.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.isPointContained(200, 200);
    console.info("region isPointContained : " + flag);
    canvas.drawPoint(200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isRect

```TypeScript
isRect(): boolean
```

Checks whether this region is the same as a single rectangle.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-isRect(): boolean--><!--Device-Region-isRect(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** if this region is the same as a single rectangle; **false** otherwise. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,10);
let isRect = path.isRect(null);
console.info("isRect: ", isRect);
let rect: common2D.Rect = { left : 100, top : 100, right : 400, bottom : 500 };
path.lineTo(20, 20);
path.lineTo(10, 20);
path.lineTo(10, 10);
isRect = path.isRect(rect);
console.info('isRect: ', isRect);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { RenderNode } from '@kit.ArkUI';

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
    let flag: boolean = false;
    flag = region.isRect();
    console.info('flag :', flag);
    region.setRect(100, 100, 200, 200);
    flag = region.isRect();
    console.info('flag :', flag);
    let other = new drawing.Region(220, 200, 280, 280);
    region.op(other, drawing.RegionOp.UNION);
    flag = region.isRect();
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isRegionContained

```TypeScript
isRegionContained(other: Region): boolean
```

Checks whether another region is contained in this region.

**Since:** 23

<!--Device-Region-isRegionContained(other: Region): boolean--><!--Device-Region-isRegionContained(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Region | Yes | Region** object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means yes; **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

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
    let other = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    other.setRect(150, 150, 250, 250);
    let flag: boolean = false;
    flag = region.isRegionContained(other);
    console.info("region isRegionContained : " + flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## offset

```TypeScript
offset(dx: int, dy: int): void
```

Translates a region.

**Since:** 24

<!--Device-Region-offset(dx: int, dy: int): void--><!--Device-Region-offset(dx: int, dy: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | int | Yes | X offset. A positive number indicates an offset towards the positive direction of the X axis, and a negative number indicates an offset towards the negative direction of the X axis. The value is an integer. |
| dy | int | Yes | Y offset. A positive number indicates an offset towards the positive direction of the Y axis, and a negative number indicates an offset towards the negative direction of the Y axis. The value is an integer. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.moveTo(200, 200);
path.lineTo(300, 300);
const dst = path.offset(200, 200);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
drawing.RectUtils.offset(rect, 10, 20);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
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
    region.setRect(100, 100, 400, 400);
    region.offset(10, 20);
    canvas.drawPoint(200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
roundRect.offset(100, 100);
```

## op

```TypeScript
op(region: Region, regionOp: RegionOp): boolean
```

Performs an operation on this region and another region, and stores the resulting region in this **Region** object.

**Since:** 23

<!--Device-Region-op(region: Region, regionOp: RegionOp): boolean--><!--Device-Region-op(region: Region, regionOp: RegionOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Region** object. |
| regionOp | [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) | Yes | Operation mode of the region. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the resulting region is stored in the current **Region** object, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
const path2 = new drawing.Path();
path.addCircle(100, 200, 100, drawing.PathDirection.CLOCKWISE);
console.info("get pathOp: ", path2.op(path, drawing.PathOp.DIFFERENCE));
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
    let othregion = new drawing.Region();
    othregion.setRect(110, 110, 240, 240);
    let flag: boolean = false;
    flag = region.op(othregion, drawing.RegionOp.REPLACE);
    console.info("region op : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## quickContains

```TypeScript
quickContains(left: int, top: int, right: int, bottom: int): boolean
```

Checks whether this region is the same as a single rectangle and contains the specified rectangle.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | int | Yes | Left position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| top | int | Yes | Top position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| right | int | Yes | Right position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| bottom | int | Yes | Bottom position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** if the current region is the same as a single rectangle and contains the specified rectangle; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { RenderNode } from '@kit.ArkUI';

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
    let flag: boolean = false;
    flag = region.quickContains(10, 10, 100, 100);
    console.info('flag :', flag);
    let other = new drawing.Region();
    other.setRect(100, 100, 200, 200);
    flag = other.quickContains(10, 10, 100, 100);
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## quickReject

```TypeScript
quickReject(left: int, top: int, right: int, bottom: int): boolean
```

Checks whether a rectangle do not intersect with this region. Actually, this API determines whether the rectangle does not intersect with the bounding rectangle of the region, and therefore the result may not be accurate.

**Since:** 23

<!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | int | Yes | Left position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| top | int | Yes | Top position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| right | int | Yes | Right position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| bottom | int | Yes | Bottom position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means that the two do not intersect; **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

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
    region.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.quickReject(50, 50, 70, 70);
    console.info("region quickReject : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## quickRejectRegion

```TypeScript
quickRejectRegion(region: Region): boolean
```

Checks whether the existing region does not intersect with another region. Actually, the outer rectangles of the two regions are compared to determine whether they do not intersect. Therefore, there may be an error.

**Since:** 24

<!--Device-Region-quickRejectRegion(region: Region): boolean--><!--Device-Region-quickRejectRegion(region: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Region** object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** if the regions do not intersect; **false** otherwise. The value **true** is returned only if the regions intersect with each other by point or edge. |

**Examples**

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
    let region2 = new drawing.Region();
    region2.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.quickRejectRegion(region2);
    console.info("region quickRejectRegion: " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setEmpty

```TypeScript
setEmpty(): void
```

Set the existing region to empty.

**Since:** 23

<!--Device-Region-setEmpty(): void--><!--Device-Region-setEmpty(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
drawing.RectUtils.setEmpty(rect)
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    let region = new drawing.Region();
    region.setRect(100, 100, 200, 200);
    let isEmpty = region.isEmpty();
    console.info("isEmpty :" + isEmpty);
    region.setEmpty();
    isEmpty = region.isEmpty();
    console.info("isEmpty :" + isEmpty);
  }
}
```

## setPath

```TypeScript
setPath(path: Path, clip: Region): boolean
```

Sets a region that matches the outline of a path within the cropping area.

**Since:** 23

<!--Device-Region-setPath(path: Path, clip: Region): boolean--><!--Device-Region-setPath(path: Path, clip: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path** object. |
| clip | Region | Yes | Region** object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Result of the setting operation. The value **true** is returned if the corked status is successfully set; otherwise, **false** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

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
    let path = new drawing.Path();
    region.setRect(100, 100, 400, 400);
    path.arcTo(50, 50, 300, 300, 0, 359);
    let flag: boolean = false;
    flag = region.setPath(path, region);
    console.info("region setPath : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setRect

```TypeScript
setRect(left: int, top: int, right: int, bottom: int): boolean
```

Sets a rectangle.

**Since:** 23

<!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | int | Yes | Left position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| top | int | Yes | Top position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| right | int | Yes | Right position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |
| bottom | int | Yes | Bottom position of the rectangle. The value must be an integer. If a decimal is passed in, the decimal part is rounded off. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Result of the setting operation. The value **true** means that the setting is successful, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10, 20, 30, 40);
let rect2 = drawing.RectUtils.makeEmpty();
drawing.RectUtils.setRect(rect2, rect);
console.info('rect2.left:', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
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
    let flag: boolean = false;
    flag = region.setRect(50, 50, 300, 300);
    console.info("region setRect : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setRegion

```TypeScript
setRegion(region: Region): void
```

Sets the existing region to another region.

**Since:** 24

<!--Device-Region-setRegion(region: Region): void--><!--Device-Region-setRegion(region: Region): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | Region | Yes | Region to be set. |

**Examples**

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
    region.setRect(100, 100, 200, 200);
    let region2 = new drawing.Region();
    region2.setRegion(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
```

