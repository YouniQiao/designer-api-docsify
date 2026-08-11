# Path

A compound geometric path consisting of line segments, arcs, quadratic Bezier curves, and cubic Bezier curves.

> **NOTE：**
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 11

<!--Device-drawing-class Path--><!--Device-drawing-class Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## addArc

```TypeScript
addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void
```

Adds an arc to this path.When **startAngle** and **sweepAngle** meet the following conditions, an oval instead of an arc is added:

1. The result of **startAngle** modulo 90 is close to 0.2. The value of **sweepAngle** is not in the range of (-360, 360).In other cases, this API adds an arc by applying the result of **sweepAngle** modulo 360 to the path.

**Since:** 12

<!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void--><!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| startAngle | number | Yes |
| sweepAngle | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addCircle

```TypeScript
addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void
```

Adds a circle to this path in the specified direction. The start point of the circle is (x + radius, y).

**Since:** 12

<!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void--><!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| radius | number | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addOval

```TypeScript
addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void
```

Adds the inscribed ellipse of a rectangle to this path in the specified direction.

**Since:** 12

<!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void--><!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| start | number | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

Transforms the points in a path by a matrix and stores the resulting path in the current **Path** object.

**Since:** 12

<!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void--><!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

Adds a polygon to this path.

**Since:** 12

<!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void--><!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | Yes |
| [close](#close) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

Adds a rectangle to a path in the specified direction. The start point is the upper left corner of the rectangle.

**Since:** 12

<!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void--><!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

Adds a rounded rectangle to a path in the specified direction. When the path direction is clockwise, the start point is at the intersection of the rounded rectangle's left boundary and its lower left corner. When the path direction is counterclockwise, the start point is at the intersection point between the left boundary and the upper left corner.

**Since:** 12

<!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void--><!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## approximate

```TypeScript
approximate(acceptableError: number): Array<number>
```

Converts the existing path into an approximate path consisting of consecutive line segments.

> **NOTE：**
> 
> - Avoid setting **acceptableError** to **0** as it heavily divides the curve path, significantly impacting
> performance and memory usage.
> 
> - Setting a high **acceptableError** simplifies the path greatly by keeping only essential points, potentially
> distorting the original shape.
> 
> - When you set a high **acceptableError** for curves such as ellipses, the fitting process often simplifies
> them to polygons by keeping just the start and end points of their Bezier curve segments.

**Since:** 20

<!--Device-Path-approximate(acceptableError: number): Array<number>--><!--Device-Path-approximate(acceptableError: number): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| acceptableError | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## arcTo

```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void
```

Draws an arc to this path using angle arc mode. This mode first defines a rectangle and takes its inscribed ellipse. Then, it specifies a start angle and a sweep angle. The arc is the portion of the ellipse's circumference defined by the start angle and the sweep angle. By default, a line segment from the last point of the path to the start point of the arc is also added.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void--><!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x1 | number | Yes |
| y1 | number | Yes |
| x2 | number | Yes |
| y2 | number | Yes |
| startDeg | number | Yes |
| sweepDeg | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

Parses the path represented by an SVG string.

**Since:** 12

<!--Device-Path-buildFromSvgString(str: string): boolean--><!--Device-Path-buildFromSvgString(str: string): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| str | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## close

```TypeScript
close(): void
```

Closes this path by adding a line segment from the start point to the last point of the path.

**Since:** 11

<!--Device-Path-close(): void--><!--Device-Path-close(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## conicTo

```TypeScript
conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

Draws a conic curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ctrlX | number | Yes |
| ctrlY | number | Yes |
| endX | number | Yes |
| endY | number | Yes |
| weight | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## constructor

```TypeScript
constructor()
```

Constructs a path.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor()--><!--Device-Path-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(path: Path)
```

Constructs a copy of an existing path.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor(path: Path)--><!--Device-Path-constructor(path: Path)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

## contains

```TypeScript
contains(x: number, y: number): boolean
```

Checks whether a coordinate point is included in this path. For details, see  
[PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md).

**Since:** 12

<!--Device-Path-contains(x: double, y: double): boolean--><!--Device-Path-contains(x: double, y: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## cubicTo

```TypeScript
cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

Draws a cubic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ctrlX1 | number | Yes |
| ctrlY1 | number | Yes |
| ctrlX2 | number | Yes |
| ctrlY2 | number | Yes |
| endX | number | Yes |
| endY | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

Obtains the minimum bounding rectangle that encloses this path.

**Since:** 12

<!--Device-Path-getBounds(): common2D.Rect--><!--Device-Path-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## getConicWeightData

```TypeScript
getConicWeightData(): Array<number>
```

Gets path conic weight data.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getConicWeightData(): Array<double>--><!--Device-Path-getConicWeightData(): Array<double>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

## getFillType

```TypeScript
getFillType(): PathFillType
```

Obtains the fill type of a path.

**Since:** 20

<!--Device-Path-getFillType(): PathFillType--><!--Device-Path-getFillType(): PathFillType-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Point |

## getLength

```TypeScript
getLength(forceClosed: boolean): number
```

Obtains the path length.

**Since:** 12

<!--Device-Path-getLength(forceClosed: boolean): double--><!--Device-Path-getLength(forceClosed: boolean): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMatrix

```TypeScript
getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean
```

Obtains a transformation matrix at a specific position along the path, which represents the coordinates and orientation of that point.

**Since:** 12

<!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean--><!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |
| distance | number | Yes |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

Obtains the operation iterator of this path.

**Since:** 18

<!--Device-Path-getPathIterator(): PathIterator--><!--Device-Path-getPathIterator(): PathIterator-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;common2D.Point&gt; |

## getPositionAndTangent

```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean
```

Obtains the coordinates and tangent at a distance from the start point of this path.

**Since:** 12

<!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean--><!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |
| distance | number | Yes |
| position | common2D.Point | Yes |
| tangent | common2D.Point | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getSegment

```TypeScript
getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean
```

Extracts a segment of a path and appends it to a destination path.

**Since:** 18

<!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean--><!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |
| start | number | Yes |
| stop | number | Yes |
| startWithMoveTo | boolean | Yes |
| dst | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;PathIteratorVerb&gt; |

## interpolate

```TypeScript
interpolate(other: Path, weight: number, interpolatedPath: Path): boolean
```

Interpolates between the existing path and another path based on the given weight and stores the result in the target path object. Interpolation is achievable if the two paths have the same number of points. The target path is created based on the structure of the existing path.

**Since:** 20

<!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean--><!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| weight | number | Yes |
| interpolatedPath | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## isClosed

```TypeScript
isClosed(): boolean
```

Checks whether a path is closed.

**Since:** 12

<!--Device-Path-isClosed(): boolean--><!--Device-Path-isClosed(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether a path is empty.

**Since:** 20

<!--Device-Path-isEmpty(): boolean--><!--Device-Path-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInterpolate

```TypeScript
isInterpolate(other: Path): boolean
```

Checks whether the existing path and another path are compatible for interpolation in terms of structure and operation sequence. If the paths contain conic operations, the weight values of the operations must be the same.

**Since:** 20

<!--Device-Path-isInterpolate(other: Path): boolean--><!--Device-Path-isInterpolate(other: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInverseFillType

```TypeScript
isInverseFillType(): boolean
```

Checks whether the current path fill type is the inverse fill type. For example, the fill types **Winding** and  
**EvenOdd** are not inverse types, while **InverseWinding** and **InverseEvenOdd** are inverse types.

**Since:** 23

<!--Device-Path-isInverseFillType(): boolean--><!--Device-Path-isInverseFillType(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRect

```TypeScript
isRect(rect: common2D.Rect | null): boolean
```

Checks whether a path forms a rectangle.

**Since:** 20

<!--Device-Path-isRect(rect: common2D.Rect | null): boolean--><!--Device-Path-isRect(rect: common2D.Rect | null): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

Draws a line segment from the last point of this path to the target point. If the path is empty, the start point(0, 0) is used.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-lineTo(x: double, y: double): void--><!--Device-Path-lineTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

Sets the start point of this path.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-moveTo(x: double, y: double): void--><!--Device-Path-moveTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the  
**Path** object returned.

**Since:** 12

<!--Device-Path-offset(dx: number, dy: number): Path--><!--Device-Path-offset(dx: number, dy: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | number | Yes |
| dy | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

Combines this path with the passed-in path based on the specified operation mode.

**Since:** 12

<!--Device-Path-op(path: Path, pathOp: PathOp): boolean--><!--Device-Path-op(path: Path, pathOp: PathOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| pathOp | [PathOp](arkts-arkgraphics2d-drawing-pathop-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## quadTo

```TypeScript
quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void
```

Draws a quadratic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void--><!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ctrlX | number | Yes |
| ctrlY | number | Yes |
| endX | number | Yes |
| endY | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rConicTo

```TypeScript
rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

Draws a conic curve from the last point of this path to a point relative to the last point. If the path is empty,the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ctrlX | number | Yes |
| ctrlY | number | Yes |
| endX | number | Yes |
| endY | number | Yes |
| weight | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rCubicTo

```TypeScript
rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

Draws a cubic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ctrlX1 | number | Yes |
| ctrlY1 | number | Yes |
| ctrlX2 | number | Yes |
| ctrlY2 | number | Yes |
| endX | number | Yes |
| endY | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rLineTo

```TypeScript
rLineTo(dx: number, dy: number): void
```

Draws a line segment from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rLineTo(dx: double, dy: double): void--><!--Device-Path-rLineTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | number | Yes |
| dy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rMoveTo

```TypeScript
rMoveTo(dx: number, dy: number): void
```

Sets the start position relative to the last point of this path. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rMoveTo(dx: double, dy: double): void--><!--Device-Path-rMoveTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | number | Yes |
| dy | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## rQuadTo

```TypeScript
rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void
```

Draws a quadratic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void--><!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx1 | number | Yes |
| dy1 | number | Yes |
| dx2 | number | Yes |
| dy2 | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## reset

```TypeScript
reset(): void
```

Resets the path data.

**Since:** 11

<!--Device-Path-reset(): void--><!--Device-Path-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## rewind

```TypeScript
rewind(): void
```

Rewinds a path by clearing all its points and lines but reserves the memory space.

**Since:** 20

<!--Device-Path-rewind(): void--><!--Device-Path-rewind(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## set

```TypeScript
set(src: Path): void
```

Updates the existing path with another path.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-set(src: Path): void--><!--Device-Path-set(src: Path): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

Sets the fill type of this path. The fill type determines how "inside" of the path is drawn. For example, when the fill type **Winding** is used, "inside" of the path is determined by a non-zero sum of signed edge crossings.When **EvenOdd** is used, "inside" of the path is determined by an odd number of edge crossings.

**Since:** 12

<!--Device-Path-setFillType(pathFillType: PathFillType): void--><!--Device-Path-setFillType(pathFillType: PathFillType): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setLastPoint

```TypeScript
setLastPoint(x: number, y: number): void
```

Sets the last point of a path.

**Since:** 20

<!--Device-Path-setLastPoint(x: double, y: double): void--><!--Device-Path-setLastPoint(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## toggleInverseFillType

```TypeScript
toggleInverseFillType(): void
```

Toggles the fill type of the path to the inverse type. For example, if the **Winding** fill type is used, the fill type after inversion is **InverseWinding**. If the **EvenOdd** fill type is used, the fill type after inversion is **InverseEvenOdd**. The same applies to the other two types.

**Since:** 23

<!--Device-Path-toggleInverseFillType(): void--><!--Device-Path-toggleInverseFillType(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## transform

```TypeScript
transform(matrix: Matrix): void
```

Transforms the points in a path by matrix.

**Since:** 12

<!--Device-Path-transform(matrix: Matrix): void--><!--Device-Path-transform(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
