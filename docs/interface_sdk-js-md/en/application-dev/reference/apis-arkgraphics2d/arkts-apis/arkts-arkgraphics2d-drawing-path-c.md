# Path

A compound geometric path consisting of line segments, arcs, quadratic Bezier curves, and cubic Bezier curves.

> **NOTE：**&gt;
> - This module uses the physical pixel unit, px.&gt;
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 11

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## addArc

```TypeScript
addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void
```

Adds an arc to this path. When **startAngle** and **sweepAngle** meet the following conditions, an oval instead of an arc is added:
1. The result of **startAngle** modulo 90 is close to 0.
2. The value of **sweepAngle** is not in the range of (-360, 360).
In other cases, this API adds an arc by applying the result of **sweepAngle** modulo 360 to the path.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addCircle

```TypeScript
addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void
```

Adds a circle to this path in the specified direction. The start point of the circle is (x + radius, y).

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addOval

```TypeScript
addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void
```

Adds the inscribed ellipse of a rectangle to this path in the specified direction.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

Transforms the points in a path by a matrix and stores the resulting path in the current **Path** object.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

Adds a polygon to this path.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | Yes |
| [close](#close) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

Adds a rectangle to a path in the specified direction. The start point is the upper left corner of the rectangle.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

Adds a rounded rectangle to a path in the specified direction. When the path direction is clockwise, the start point is at the intersection of the rounded rectangle's left boundary and its lower left corner. When the path direction is counterclockwise, the start point is at the intersection point between the left boundary and the upper left corner.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [roundRect](../../apis-arkui/arkts-components/arkts-arkui-canvaspath-c.md) | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| acceptableError | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

Parses the path represented by an SVG string.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## close

```TypeScript
close(): void
```

Closes this path by adding a line segment from the start point to the last point of the path.

**Since:** 11

**System capability:** SystemCapability.Graphics.Drawing

## conicTo

```TypeScript
conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

Draws a conic curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## constructor

```TypeScript
constructor()
```

Constructs a path.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(path: Path)
```

Constructs a copy of an existing path.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

## contains

```TypeScript
contains(x: number, y: number): boolean
```

Checks whether a coordinate point is included in this path. For details, see [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md).

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## convertToSvgString

```TypeScript
convertToSvgString(): string
```

Converts path to an SVG string.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

Obtains the minimum bounding rectangle that encloses this path.

**Since:** 12

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

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getFillType

```TypeScript
getFillType(): PathFillType
```

Obtains the fill type of a path.

**Since:** 20

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

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |
| distance | number | Yes |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

Obtains the operation iterator of this path.

**Since:** 18

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

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## getPositionAndTangent

```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean
```

Obtains the coordinates and tangent at a distance from the start point of this path.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getSegment

```TypeScript
getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean
```

Extracts a segment of a path and appends it to a destination path.

**Since:** 18

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceClosed | boolean | Yes |
| start | number | Yes |
| stop | number | Yes |
| startWithMoveTo | boolean | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

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

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md)&gt; |

## interpolate

```TypeScript
interpolate(other: Path, weight: number, interpolatedPath: Path): boolean
```

Interpolates between the existing path and another path based on the given weight and stores the result in the target path object. Interpolation is achievable if the two paths have the same number of points. The target path is created based on the structure of the existing path.

**Since:** 20

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

Checks whether the current path fill type is the inverse fill type. For example, the fill types **Winding** and **EvenOdd** are not inverse types, while **InverseWinding** and **InverseEvenOdd** are inverse types.

**Since:** 23

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

Draws a line segment from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

Sets the start point of this path.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the **Path** object returned.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

Combines this path with the passed-in path based on the specified operation mode.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## quadTo

```TypeScript
quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void
```

Draws a quadratic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## rConicTo

```TypeScript
rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

Draws a conic curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## rCubicTo

```TypeScript
rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

Draws a cubic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## reset

```TypeScript
reset(): void
```

Resets the path data.

**Since:** 11

**System capability:** SystemCapability.Graphics.Drawing

## rewind

```TypeScript
rewind(): void
```

Rewinds a path by clearing all its points and lines but reserves the memory space.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

## rLineTo

```TypeScript
rLineTo(dx: number, dy: number): void
```

Draws a line segment from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## rMoveTo

```TypeScript
rMoveTo(dx: number, dy: number): void
```

Sets the start position relative to the last point of this path. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## rQuadTo

```TypeScript
rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void
```

Draws a quadratic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## set

```TypeScript
set(src: Path): void
```

Updates the existing path with another path.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

Sets the fill type of this path. The fill type determines how "inside" of the path is drawn. For example, when the fill type **Winding** is used, "inside" of the path is determined by a non-zero sum of signed edge crossings. When **EvenOdd** is used, "inside" of the path is determined by an odd number of edge crossings.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setLastPoint

```TypeScript
setLastPoint(x: number, y: number): void
```

Sets the last point of a path.

**Since:** 20

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

**System capability:** SystemCapability.Graphics.Drawing

## transform

```TypeScript
transform(matrix: Matrix): void
```

Transforms the points in a path by matrix.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
