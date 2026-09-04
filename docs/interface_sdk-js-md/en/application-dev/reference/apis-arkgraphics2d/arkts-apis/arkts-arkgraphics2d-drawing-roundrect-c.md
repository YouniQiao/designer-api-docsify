# RoundRect

Rounded rectangle.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor(roundRect: RoundRect)
```

Copies a rounded rectangle.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| roundRect | RoundRect | Yes | Rounded rectangle to be copied. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
let roundRect2 = new drawing.RoundRect(roundRect);
```

## constructor

```TypeScript
constructor(rect: common2D.Rect, xRadii: number, yRadii: number)
```

A constructor used to create a **RoundRect** object. A rounded rectangle is created when both **xRadii** and **yRadii** are greater than 0. Otherwise, only a rectangle is created.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | [common2D.Rect](arkts-arkgraphics2d-common2d-rect-i.md) | Yes | Rectangle that encloses the rounded rectangle to create. |
| xRadii | number | Yes | Radius of the rounded corner on the X axis. The value is a floating point number. A negative number is invalid. |
| yRadii | number | Yes | Radius of the rounded corner on the Y axis. The value is a floating point number. A negative number is invalid. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
```

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point
```

Obtains the radii of the specified rounded corner in this rounded rectangle.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes | Position of the rounded corner. |

**Return value:**

| Type | Description |
| --- | --- |
| [common2D.Point](arkts-arkgraphics2d-common2d-point-i.md) | Point. The horizontal coordinate indicates the radius of the rounded corner on the X axis, and the vertical coordinate indicates the radius on the Y axis. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;  2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
let cornerRadius = roundRect.getCorner(drawing.CornerPos.BOTTOM_LEFT_POS);
console.info("getCorner---"+cornerRadius.x)
console.info("getCorner---"+cornerRadius.y)
```

## offset

```TypeScript
offset(dx: number, dy: number): void
```

Translates this rounded rectangle by an offset along the X axis and Y axis.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | number | Yes | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| dy | number | Yes | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;  2. Incorrect parameter types. |

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

## setCorner

```TypeScript
setCorner(pos: CornerPos, x: number, y: number): void
```

Sets the radii of the specified rounded corner in this rounded rectangle.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes | Position of the rounded corner. |
| x | number | Yes | Radius of the rounded corner on the X axis. The value is a floating point number. A negative number is invalid. |
| y | number | Yes | Radius of the rounded corner on the Y axis. The value is a floating point number. A negative number is invalid. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;  2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
roundRect.setCorner(drawing.CornerPos.TOP_LEFT_POS, 150, 150);
```
