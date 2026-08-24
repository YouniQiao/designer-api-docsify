# Path

A compound geometric path consisting of line segments, arcs, quadratic Bezier curves, and cubic Bezier curves.

> **NOTE：**&gt;
> - This module uses the physical pixel unit, px.&gt;
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 23

<!--Device-drawing-class Path--><!--Device-drawing-class Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## addArc

```TypeScript
addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void
```

Adds an arc to this path. When **startAngle** and **sweepAngle** meet the following conditions, an oval instead of an arc is added:
1. The result of **startAngle** modulo 90 is close to 0.
2. The value of **sweepAngle** is not in the range of (-360, 360).
In other cases, this API adds an arc by applying the result of **sweepAngle** modulo 360 to the path.

**Since:** 23

<!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void--><!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangular boundary that encapsulates the oval including the arc. |
| startAngle | double | Yes | Start angle of the arc, in degrees. The value 0 indicates the positive direction of the X axis. The value is a floating point number. |
| sweepAngle | double | Yes | Angle to sweep, in degrees. A positive value indicates a clockwise sweep, and a negative value indicates a counterclockwise sweep. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addArc(rect, 90, 180);
```

## addCircle

```TypeScript
addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void
```

Adds a circle to this path in the specified direction. The start point of the circle is (x + radius, y).

**Since:** 23

<!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void--><!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate of the center of the circle. The value is a floating point number. |
| y | double | Yes | Y coordinate of the center of the circle. The value is a floating point number. |
| radius | double | Yes | Radius of the circle. The value is a floating point number. If the value is less than or equal to 0, there is no effect. |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | Direction of the path. The default direction is clockwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.addCircle(100, 200, 50, drawing.PathDirection.CLOCKWISE);
```

## addOval

```TypeScript
addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void
```

Adds the inscribed ellipse of a rectangle to this path in the specified direction.

**Since:** 23

<!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void--><!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangular boundary of the oval. |
| start | int | Yes | Start point of the oval, where 0, 1, 2, and 3 correspond to the upper, right, lower, and left points, respectively. The value is an integer greater than or equal to 0. If the value is greater than or equal to 4, the remainder of 4 is used. |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | Direction of the path. The default direction is clockwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addOval(rect, 5, drawing.PathDirection.CLOCKWISE);
```

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

Transforms the points in a path by a matrix and stores the resulting path in the current **Path** object.

**Since:** 23

<!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void--><!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Source **Path** object. |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | Matrix** object. The default value is an identity matrix. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
let dstPath = new drawing.Path();
dstPath.addPath(path, matrix);
```

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

Adds a polygon to this path.

**Since:** 23

<!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void--><!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | Yes | Array that holds the vertex coordinates of the polygon. |
| close | boolean | Yes | Whether to close the path, that is, whether to add a line segment from the start point to the end point of the path. The value **true** means to close the path, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let pointsArray = new Array<common2D.Point>();
const point1: common2D.Point = { x: 200, y: 200 };
const point2: common2D.Point = { x: 400, y: 200 };
const point3: common2D.Point = { x: 100, y: 400 };
const point4: common2D.Point = { x: 300, y: 400 };
pointsArray.push(point1);
pointsArray.push(point2);
pointsArray.push(point3);
pointsArray.push(point4);
const path = new drawing.Path();
path.addPolygon(pointsArray, false);
```

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

Adds a rectangle to a path in the specified direction. The start point is the upper left corner of the rectangle.

**Since:** 23

<!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void--><!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle. |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | Direction of the path. The default direction is clockwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
```

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

Adds a rounded rectangle to a path in the specified direction. When the path direction is clockwise, the start point is at the intersection of the rounded rectangle's left boundary and its lower left corner. When the path direction is counterclockwise, the start point is at the intersection point between the left boundary and the upper left corner.

**Since:** 23

<!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void--><!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| roundRect | RoundRect | Yes | Rounded rectangle. |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | Direction of the path. The default direction is clockwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
```

## approximate

```TypeScript
approximate(acceptableError: number): Array<number>
```

Converts the existing path into an approximate path consisting of consecutive line segments.

> **NOTE：**&gt;
> - Avoid setting **acceptableError** to **0** as it heavily divides the curve path, significantly impacting
> performance and memory usage.&gt;
> - Setting a high **acceptableError** simplifies the path greatly by keeping only essential points, potentially
> distorting the original shape.&gt;
> - When you set a high **acceptableError** for curves such as ellipses, the fitting process often simplifies
> them to polygons by keeping just the start and end points of their Bezier curve segments.

**Since:** 20

<!--Device-Path-approximate(acceptableError: number): Array<number>--><!--Device-Path-approximate(acceptableError: number): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| acceptableError | number | Yes | Acceptable error of each line segment on a path. The value is a floating point number. If the value is less than 0, an error is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;number&gt; | An array of points in the approximate path, which contains at least two points. Each point consists of three values: <br>1. Length ratio of the point to the start point of the path. The value range is [0.0, 1.0]. <br>2. X coordinate of a point. <br>3. Y coordinate of a point. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(100, 100);
path.lineTo(500, 500);
let points: number[] = path.approximate(0.5);
for (let i = 0; i < points.length; i += 3) {
  console.info("PathApproximate Fraction =" + points[i] + ", X =" + points[i + 1] + ", Y =" + points[i + 2] + "\n");
}
```

## approximate

```TypeScript
approximate(acceptableError: double): Array<double> | undefined
```

Approximates the path with a series of line segments.

**Since:** 24

<!--Device-Path-approximate(acceptableError: double): Array<double> | undefined--><!--Device-Path-approximate(acceptableError: double): Array<double> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| acceptableError | double | Yes | Indicates the acceptable error for a line on the path. Should be no less than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; \| undefined | Returns with the array containing point components. <br>There are three components for each point: <br>1. Fraction along the length of the path that the point resides [0.0, 1.0]. <br>2. The x coordinate of the point. <br>3. The y coordinate of the point. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

**Examples**

See [approximate](#approximate)

## arcTo

```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void
```

Draws an arc to this path using angle arc mode. This mode first defines a rectangle and takes its inscribed ellipse. Then, it specifies a start angle and a sweep angle. The arc is the portion of the ellipse's circumference defined by the start angle and the sweep angle. By default, a line segment from the last point of the path to the start point of the arc is also added.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void--><!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | double | Yes | X coordinate of the upper left corner of the rectangle. The value is a floating point number. |
| y1 | double | Yes | Y coordinate of the upper left corner of the rectangle. The value is a floating point number. |
| x2 | double | Yes | X coordinate of the lower right corner of the rectangle. The value is a floating point number. |
| y2 | double | Yes | Y coordinate of the lower right corner of the rectangle. The value is a floating point number. |
| startDeg | double | Yes | Start angle. The start direction (0��) of the angle is the positive direction of the X axis. |
| sweepDeg | double | Yes | Angle to sweep, in degrees. A positive value indicates a clockwise sweep, and a negative value indicates a counterclockwise sweep. The actual swipe degree is the modulo operation result of the input parameter by 360. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.arcTo(10, 15, 10, 10, 10, 10);
```

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

Parses the path represented by an SVG string.

**Since:** 23

<!--Device-Path-buildFromSvgString(str: string): boolean--><!--Device-Path-buildFromSvgString(str: string): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | String in SVG format, which is used to describe the path. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Result of the parsing operation. The value **true** means that the operation is successful, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let svgStr: string =  "M150 100 L75 300 L225 300 Z";
if(path.buildFromSvgString(svgStr)) {
  console.info("buildFromSvgString return true");
} else {
  console.info("buildFromSvgString return false");
}
```

## close

```TypeScript
close(): void
```

Closes this path by adding a line segment from the start point to the last point of the path.

**Since:** 23

<!--Device-Path-close(): void--><!--Device-Path-close(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(10, 10, 10, 10, 15, 15);
path.close();
```

## conicTo

```TypeScript
conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

Draws a conic curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | double | Yes | X coordinate of the control point. The value is a floating point number. |
| ctrlY | double | Yes | Y coordinate of the control point. The value is a floating point number. |
| endX | double | Yes | X coordinate of the target point. The value is a floating point number. |
| endY | double | Yes | Y coordinate of the target point. The value is a floating point number. |
| weight | double | Yes | Weight of the curve, which determines its shape. The larger the value, the closer of the curve to the control point. If the value is less than or equal to 0, this API has the same effect as [lineTo](#lineto). If the value is 1, it has the same effect as [quadTo](#quadto). The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.conicTo(200, 400, 100, 200, 0);
```

## constructor

```TypeScript
constructor()
```

Constructs a path.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor()--><!--Device-Path-constructor()-End-->

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
constructor(path: Path)
```

Constructs a copy of an existing path.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor(path: Path)--><!--Device-Path-constructor(path: Path)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path to copy. |

**Examples**

See [constructor](#constructor)

## contains

```TypeScript
contains(x: double, y: double): boolean
```

Checks whether a coordinate point is included in this path. For details, see [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md).

**Since:** 23

<!--Device-Path-contains(x: double, y: double): boolean--><!--Device-Path-contains(x: double, y: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate. The value is a floating point number. |
| y | double | Yes | Y coordinate. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the coordinate point is included in the path, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
let rect : common2D.Rect = {left: 50, top: 50, right: 250, bottom: 250};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
console.info("test contains: " + path.contains(0, 0));
console.info("test contains: " + path.contains(60, 60));
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 40, 40);
let isContains = drawing.RectUtils.contains(rect2, rect);
console.info('isContains: ', isContains);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20, 30, 40);
console.info('isContains :', isContains);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20);
console.info('isContains: ', isContains);
```

## convertToSvgString

```TypeScript
convertToSvgString(): string
```

Converts path to an SVG string.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-convertToSvgString(): string--><!--Device-Path-convertToSvgString(): string-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| string | The SVG string of the path. |

## cubicTo

```TypeScript
cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void
```

Draws a cubic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX1 | double | Yes | X coordinate of the first control point. The value is a floating point number. |
| ctrlY1 | double | Yes | Y coordinate of the first control point. The value is a floating point number. |
| ctrlX2 | double | Yes | X coordinate of the second control point. The value is a floating point number. |
| ctrlY2 | double | Yes | Y coordinate of the second control point. The value is a floating point number. |
| endX | double | Yes | X coordinate of the target point. The value is a floating point number. |
| endY | double | Yes | Y coordinate of the target point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.cubicTo(100, 100, 80, 150, 300, 150);
```

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

Obtains the minimum bounding rectangle that encloses this path.

**Since:** 12

<!--Device-Path-getBounds(): common2D.Rect--><!--Device-Path-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | Minimum bounding rectangle. |

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

Obtains the minimum bounding rectangle that encloses this path.

**Since:** 23

<!--Device-Path-getBounds(): common2D.Rect | undefined--><!--Device-Path-getBounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect \| undefined | Rect object. |

**Examples**

See [getBounds](#getbounds)

## getConicWeightData

```TypeScript
getConicWeightData(): Array<double>
```

Gets path conic weight data.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getConicWeightData(): Array<double>--><!--Device-Path-getConicWeightData(): Array<double>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | path conic weight array. |

## getFillType

```TypeScript
getFillType(): PathFillType
```

Obtains the fill type of a path.

**Since:** 20

<!--Device-Path-getFillType(): PathFillType--><!--Device-Path-getFillType(): PathFillType-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | Fill type of a path. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
let type = path.getFillType();
console.info("type :" + type);
```

## getFillType

```TypeScript
getFillType(): PathFillType | undefined
```

Gets fill type, the rule used to fill path.

**Since:** 24

<!--Device-Path-getFillType(): PathFillType | undefined--><!--Device-Path-getFillType(): PathFillType | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) \| undefined | Returns the pathFillType. |

**Examples**

See [getFillType](#getfilltype)

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point
```

Gets the last point of the path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getLastPoint(): common2D.Point--><!--Device-Path-getLastPoint(): common2D.Point-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point | Returns the last point of the path. |

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point | undefined
```

Gets the last point of the path.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getLastPoint(): common2D.Point | undefined--><!--Device-Path-getLastPoint(): common2D.Point | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point \| undefined | Returns the last point of the path, or undefined if the path is empty. |

## getLength

```TypeScript
getLength(forceClosed: boolean): double
```

Obtains the path length.

**Since:** 23

<!--Device-Path-getLength(forceClosed: boolean): double--><!--Device-Path-getLength(forceClosed: boolean): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Path length. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.arcTo(20, 20, 180, 180, 180, 90);
let len = path.getLength(false);
console.info("path length = " + len);
```

## getMatrix

```TypeScript
getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean
```

Obtains a transformation matrix at a specific position along the path, which represents the coordinates and orientation of that point.

**Since:** 23

<!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean--><!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| distance | double | Yes | Distance from the start point. If a negative number is passed in, the value **0** is used. If a value greater than the path length is passed in, the path length is used. The value is a floating point number. |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix** object used to store the matrix obtained. |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | Yes | Type of the matrix information obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the transformation matrix is obtained. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let matrix = new drawing.Matrix();
if(path.getMatrix(false, 10, matrix, drawing.PathMeasureMatrixFlags.GET_TANGENT_MATRIX)) {
  console.info("path.getMatrix return true");
} else {
  console.info("path.getMatrix return false");
}
```

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

Obtains the operation iterator of this path.

**Since:** 18

<!--Device-Path-getPathIterator(): PathIterator--><!--Device-Path-getPathIterator(): PathIterator-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) | Iterator** object of the path. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter = path.getPathIterator();
```

## getPathIterator

```TypeScript
getPathIterator(): PathIterator | undefined
```

Obtains the operation iterator of this path.

**Since:** 23

<!--Device-Path-getPathIterator(): PathIterator | undefined--><!--Device-Path-getPathIterator(): PathIterator | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) \| undefined | Indicates the pointer to an pathIterator object. |

**Examples**

See [getPathIterator](#getpathiterator)

## getPointData

```TypeScript
getPointData(): Array<common2D.Point>
```

Gets path point data.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getPointData(): Array<common2D.Point>--><!--Device-Path-getPointData(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | path points array. |

## getPositionAndTangent

```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean
```

Obtains the coordinates and tangent at a distance from the start point of this path.

**Since:** 23

<!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean--><!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| distance | double | Yes | Distance from the start point. If a negative number is passed in, the value **0** is used. If a value greater than the path length is passed in, the path length is used. The value is a floating point number. |
| position | common2D.Point | Yes | Coordinates obtained. |
| tangent | common2D.Point | Yes | Tangent obtained, where **tangent.x** and **tangent.y** represent the cosine and sine of the tangent of the point, respectively. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that they are obtained, and **false** means the opposite. The values of **position** and **tangent** are not changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
let position: common2D.Point = { x: 0.0, y: 0.0 };
let tangent: common2D.Point = { x: 0.0, y: 0.0 };
if (path.getPositionAndTangent(false, 0.1, position, tangent)) {
  console.info("getPositionAndTangent-----position:  "+ position.x);
  console.info("getPositionAndTangent-----position:  "+ position.y);
  console.info("getPositionAndTangent-----tangent:  "+ tangent.x);
  console.info("getPositionAndTangent-----tangent:  "+ tangent.y);
}
```

## getSegment

```TypeScript
getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean
```

Extracts a segment of a path and appends it to a destination path.

**Since:** 23

<!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean--><!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| start | double | Yes | Distance from the start point of the path to the start point of the segment. If it is less than 0, it defaults to 0. If it is greater than or equal to **stop**, the extraction fails. The value is a floating point number. |
| stop | double | Yes | Distance from the start point of the path to the end point of the segment. If it is less than or equal to **start**, the extraction fails. If it is greater than the path length, it defaults to the path length. The value is a floating point number. |
| startWithMoveTo | boolean | Yes | Whether to execute [moveTo](#moveto) in the destination path to move to its start point. The value **true** means to move to the start point, and **false** means the opposite. |
| dst | Path | Yes | Destination path. If the extraction succeeds, the segment is appended to the path. If the extraction fails, nothing changes. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Extraction result. The value **true** means that the extraction is successful, and **false** means the opposite. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
let dstPath: drawing.Path = new drawing.Path();
console.info("getSegment-----result:  "+ path.getSegment(true, 10.0, 20.0, true, dstPath));
```

## getVerbData

```TypeScript
getVerbData(): Array<PathIteratorVerb>
```

Gets path verb data.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getVerbData(): Array<PathIteratorVerb>--><!--Device-Path-getVerbData(): Array<PathIteratorVerb>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md)&gt; | path verbs array. |

## interpolate

```TypeScript
interpolate(other: Path, weight: double, interpolatedPath: Path): boolean
```

Interpolates between the existing path and another path based on the given weight and stores the result in the target path object. Interpolation is achievable if the two paths have the same number of points. The target path is created based on the structure of the existing path.

**Since:** 24

<!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean--><!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Path | Yes | Another path object. |
| weight | double | Yes | Interpolation weight, which must be within the range of [0.0, 1.0]. The value is a floating point number. |
| interpolatedPath | Path | Yes | Target path object used to store the interpolation result. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether interpolation is successful. **true** means yes; **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(50, 50);
path.lineTo(100, 100);
path.lineTo(200, 200);
let other: drawing.Path = new drawing.Path();
other.moveTo(80, 80);
other.lineTo(300, 300);
let interpolatedPath: drawing.Path = new drawing.Path();
if (path.interpolate(other, 0.0, interpolatedPath)) {
  console.info('interpolate return true');
} else {
  console.info('interpolate return false');
}
```

## isClosed

```TypeScript
isClosed(): boolean
```

Checks whether a path is closed.

**Since:** 23

<!--Device-Path-isClosed(): boolean--><!--Device-Path-isClosed(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the path is closed, and **false** means the opposite. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
if (path.isClosed()) {
  console.info("path is closed.");
} else {
  console.info("path is not closed.");
}
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether a path is empty.

**Since:** 24

<!--Device-Path-isEmpty(): boolean--><!--Device-Path-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a path is empty. **true** means yes; **false** otherwise. |

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
isEqual(path: Path): boolean
```

Checks if two paths are equal.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-isEqual(path: Path): boolean--><!--Device-Path-isEqual(path: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Another Path object to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the two paths are equal, otherwise returns false. |

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

## isInterpolate

```TypeScript
isInterpolate(other: Path): boolean
```

Checks whether the existing path and another path are compatible for interpolation in terms of structure and operation sequence. If the paths contain conic operations, the weight values of the operations must be the same.

**Since:** 24

<!--Device-Path-isInterpolate(other: Path): boolean--><!--Device-Path-isInterpolate(other: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Path | Yes | Another path object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the existing path and another path are compatible for interpolation. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
let other: drawing.Path = new drawing.Path();
other.moveTo(0, 1);
other.lineTo(200, 200);
if (path.isInterpolate(other)) {
  console.info('isInterpolate return true');
} else {
  console.info('isInterpolate return false');
}
```

## isInverseFillType

```TypeScript
isInverseFillType(): boolean
```

Checks whether the current path fill type is the inverse fill type. For example, the fill types **Winding** and **EvenOdd** are not inverse types, while **InverseWinding** and **InverseEvenOdd** are inverse types.

**Since:** 23

<!--Device-Path-isInverseFillType(): boolean--><!--Device-Path-isInverseFillType(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the current path fill type is the inverse fill type. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
if (path.isInverseFillType()) {
  console.info("path is inverse FillType.");
} else {
  console.info("path is not inverse FillType.");
}
```

## isRect

```TypeScript
isRect(rect: common2D.Rect | null): boolean
```

Checks whether a path forms a rectangle.

**Since:** 23

<!--Device-Path-isRect(rect: common2D.Rect | null): boolean--><!--Device-Path-isRect(rect: common2D.Rect | null): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect \| null | Yes | Rectangle object, which is used as an output parameter. If the path forms a rectangle, the rectangle object is overwritten with the rectangle represented by the path. Otherwise, the rectangle object remains unchanged. The value can be **null**, indicating that the rectangle represented by the path does not need to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a path forms a rectangle. **true** means yes; **false** otherwise. |

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

## lineTo

```TypeScript
lineTo(x: double, y: double): void
```

Draws a line segment from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-lineTo(x: double, y: double): void--><!--Device-Path-lineTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate of the target point. The value is a floating point number. |
| y | double | Yes | Y coordinate of the target point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(10, 15);
```

## moveTo

```TypeScript
moveTo(x: double, y: double): void
```

Sets the start point of this path.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-moveTo(x: double, y: double): void--><!--Device-Path-moveTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate of the start point. The value is a floating point number. |
| y | double | Yes | Y coordinate of the start point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
```

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the **Path** object returned.

**Since:** 12

<!--Device-Path-offset(dx: number, dy: number): Path--><!--Device-Path-offset(dx: number, dy: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | number | Yes | X offset. A positive number indicates an offset towards the positive direction of the X axis, and a negative number indicates an offset towards the negative direction of the X axis. The value is a floating point number. |
| dy | number | Yes | Y offset. A positive number indicates an offset towards the positive direction of the Y axis, and a negative number indicates an offset towards the negative direction of the Y axis. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| Path | New path generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

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

## offset

```TypeScript
offset(dx: double, dy: double): Path | undefined
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the Path object returned.

**Since:** 23

<!--Device-Path-offset(dx: double, dy: double): Path | undefined--><!--Device-Path-offset(dx: double, dy: double): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | X offset. A positive number indicates an offset towards the positive direction of the X axis, and a negative number indicates an offset towards the negative direction of the X axis. The value is a floating point number. |
| dy | double | Yes | Y offset. A positive number indicates an offset towards the positive direction of the Y axis, and a negative number indicates an offset towards the negative direction of the Y axis. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| Path \| undefined | New path generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

See [offset](#offset)

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

Combines this path with the passed-in path based on the specified operation mode.

**Since:** 23

<!--Device-Path-op(path: Path, pathOp: PathOp): boolean--><!--Device-Path-op(path: Path, pathOp: PathOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path object, which will be combined with the current path. |
| pathOp | [PathOp](arkts-arkgraphics2d-drawing-pathop-e.md) | Yes | Defines an enum for the operation modes available for a path. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Result of the path combination result. The value **true** means that the path combination is successful, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

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

## quadTo

```TypeScript
quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void
```

Draws a quadratic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void--><!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | double | Yes | X coordinate of the control point. The value is a floating point number. |
| ctrlY | double | Yes | Y coordinate of the control point. The value is a floating point number. |
| endX | double | Yes | X coordinate of the target point. The value is a floating point number. |
| endY | double | Yes | Y coordinate of the target point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10,10);
path.quadTo(10, 15, 10, 10);
```

## rConicTo

```TypeScript
rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

Draws a conic curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | double | Yes | X offset of the control point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| ctrlY | double | Yes | Y offset of the control point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |
| endX | double | Yes | X offset of the target point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| endY | double | Yes | Y offset of the target point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |
| weight | double | Yes | Weight of the curve, which determines its shape. The larger the value, the closer of the curve to the control point. If the value is less than or equal to 0, this API is equivalent to [rLineTo](#rlineto), that is, adding a line segment from the last point of the path to the target point. If the value is 1, this API is equivalent to [rQuadTo](#rquadto). The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rConicTo(200, 400, 100, 200, 0);
```

## rCubicTo

```TypeScript
rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void
```

Draws a cubic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX1 | double | Yes | X offset of the first control point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| ctrlY1 | double | Yes | Y offset of the first control point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |
| ctrlX2 | double | Yes | X offset of the second control point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| ctrlY2 | double | Yes | Y offset of the second control point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |
| endX | double | Yes | X offset of the target point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| endY | double | Yes | Y offset of the target point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rCubicTo(200, 0, 0, 200, -20, 0);
```

## reset

```TypeScript
reset(): void
```

Resets the path data.

**Since:** 23

<!--Device-Path-reset(): void--><!--Device-Path-reset(): void-End-->

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

## rewind

```TypeScript
rewind(): void
```

Rewinds a path by clearing all its points and lines but reserves the memory space.

**Since:** 24

<!--Device-Path-rewind(): void--><!--Device-Path-rewind(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10,10);
path.lineTo(20,20);
path.rewind();
let empty = path.isEmpty();
console.info('empty : ', empty);
```

## rLineTo

```TypeScript
rLineTo(dx: double, dy: double): void
```

Draws a line segment from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rLineTo(dx: double, dy: double): void--><!--Device-Path-rLineTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | X offset of the target point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| dy | double | Yes | Y offset of the target point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rLineTo(400, 200);
```

## rMoveTo

```TypeScript
rMoveTo(dx: double, dy: double): void
```

Sets the start position relative to the last point of this path. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rMoveTo(dx: double, dy: double): void--><!--Device-Path-rMoveTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | X offset of the start point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| dy | double | Yes | Y offset of the start point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rMoveTo(10, 10);
```

## rQuadTo

```TypeScript
rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void
```

Draws a quadratic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void--><!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx1 | double | Yes | X offset of the control point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| dy1 | double | Yes | Y offset of the control point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |
| dx2 | double | Yes | X offset of the target point relative to the last point. A positive number indicates a rightward shift from the last point, and a negative number indicates a leftward shift from the last point. The value is a floating point number. |
| dy2 | double | Yes | Y offset of the target point relative to the last point. A positive number indicates an upward shift from the last point, and a negative number indicates a downward shift from the last point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rQuadTo(100, 0, 0, 200);
```

## set

```TypeScript
set(src: Path): void
```

Updates the existing path with another path.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-set(src: Path): void--><!--Device-Path-set(src: Path): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Path | Yes | Path for the update. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
path.close();
let path1: drawing.Path = new drawing.Path();
path1.set(path);
```

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

Sets the fill type of this path. The fill type determines how "inside" of the path is drawn. For example, when the fill type **Winding** is used, "inside" of the path is determined by a non-zero sum of signed edge crossings. When **EvenOdd** is used, "inside" of the path is determined by an odd number of edge crossings.

**Since:** 23

<!--Device-Path-setFillType(pathFillType: PathFillType): void--><!--Device-Path-setFillType(pathFillType: PathFillType): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | Yes | Fill type of the path. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
```

## setLastPoint

```TypeScript
setLastPoint(x: double, y: double): void
```

Sets the last point of a path.

**Since:** 24

<!--Device-Path-setLastPoint(x: double, y: double): void--><!--Device-Path-setLastPoint(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X coordinate of a point. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| y | double | Yes | Y coordinate of a point. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.reset();
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.setLastPoint(50, 50);
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

## toggleInverseFillType

```TypeScript
toggleInverseFillType(): void
```

Toggles the fill type of the path to the inverse type. For example, if the **Winding** fill type is used, the fill type after inversion is **InverseWinding**. If the **EvenOdd** fill type is used, the fill type after inversion is **InverseEvenOdd**. The same applies to the other two types.

**Since:** 23

<!--Device-Path-toggleInverseFillType(): void--><!--Device-Path-toggleInverseFillType(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
path.toggleInverseFillType();
console.info("path fillType = ", path.getFillType());
```

## transform

```TypeScript
transform(matrix: Matrix): void
```

Transforms the points in a path by matrix.

**Since:** 23

<!--Device-Path-transform(matrix: Matrix): void--><!--Device-Path-transform(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
matrix.setScale(1.5, 1.5, 10, 10);
const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
let roundRect = new drawing.RoundRect(rect, 50, 50);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
path.transform(matrix);
```

