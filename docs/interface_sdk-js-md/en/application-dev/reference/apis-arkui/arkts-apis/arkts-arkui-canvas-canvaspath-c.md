# CanvasPath

Path object, which provides basic methods for drawing paths.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CanvasPath--><!--Device-unnamed-export declare class CanvasPath-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(x: double, y: double, radius: double, startAngle: double, endAngle: double, counterclockwise?: boolean): void
```

Draw an arc path

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-arc(x: double, y: double, radius: double, startAngle: double, endAngle: double, counterclockwise?: boolean): void--><!--Device-CanvasPath-arc(x: double, y: double, radius: double, startAngle: double, endAngle: double, counterclockwise?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the center (center of the circle) of the arc. |
| y | double | Yes | The y-axis coordinate of the center (center of the circle) of the arc. |
| radius | double | Yes | Radius of the arc. |
| startAngle | double | Yes | Start point of an arc, which starts to be calculated in the x-axis direction. The unit is radian. |
| endAngle | double | Yes | The end point of the arc, in radians. |
| counterclockwise | boolean | No | If the value is true, the arc is drawn counterclockwise. Otherwise, the arc is drawn clockwise. The default value is false. |

## arcTo

```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, radius: double): void
```

Draw arc paths based on control points and radius

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-arcTo(x1: double, y1: double, x2: double, y2: double, radius: double): void--><!--Device-CanvasPath-arcTo(x1: double, y1: double, x2: double, y2: double, radius: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | double | Yes | The x-axis coordinate of the first control point. |
| y1 | double | Yes | The y-axis coordinate of the first control point. |
| x2 | double | Yes | The x-axis coordinate of the second control point. |
| y2 | double | Yes | The y-axis coordinate of the second control point. |
| radius | double | Yes | Radius of the arc. |

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: double, cp1y: double, cp2x: double, cp2y: double, x: double, y: double): void
```

Drawing Cubic Bessel Curve Paths

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-bezierCurveTo(cp1x: double, cp1y: double, cp2x: double, cp2y: double, x: double, y: double): void--><!--Device-CanvasPath-bezierCurveTo(cp1x: double, cp1y: double, cp2x: double, cp2y: double, x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cp1x | double | Yes | The x-axis coordinate of the first control point. |
| cp1y | double | Yes | The y-axis coordinate of the first control point. |
| cp2x | double | Yes | The x-axis coordinate of the second control point. |
| cp2y | double | Yes | The y-axis coordinate of the second control point. |
| x | double | Yes | x-axis coordinate of the end point. |
| y | double | Yes | y-axis coordinate of the end point. |

## closePath

```TypeScript
closePath(): void
```

Returns the pen point to the start point of the current sub-path

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-closePath(): void--><!--Device-CanvasPath-closePath(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ellipse

```TypeScript
ellipse(x: double, y: double, radiusX: double, radiusY: double, rotation: double, startAngle: double,
    endAngle: double, counterclockwise?: boolean): void
```

Draw an Elliptic Path

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-ellipse(x: double, y: double, radiusX: double, radiusY: double, rotation: double, startAngle: double,    endAngle: double, counterclockwise?: boolean): void--><!--Device-CanvasPath-ellipse(x: double, y: double, radiusX: double, radiusY: double, rotation: double, startAngle: double,    endAngle: double, counterclockwise?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | x-axis coordinate of the center of the ellipse. |
| y | double | Yes | y-axis coordinate of the center of the ellipse. |
| radiusX | double | Yes | Radius of the major axis of the ellipse. |
| radiusY | double | Yes | Radius of the minor axis of the ellipse. |
| rotation | double | Yes | The rotation angle of the ellipse, in radians (not angular degrees). |
| startAngle | double | Yes | The angle of the starting point to be drawn, measured from the x-axis in radians (not angular degrees). |
| endAngle | double | Yes | The angle, in radians, at which the ellipse is to be drawn (not angular degrees). |
| counterclockwise | boolean | No | If the value is true, the ellipse is drawn counterclockwise. Otherwise, the ellipse is drawn clockwise. The default value is false. |

## lineTo

```TypeScript
lineTo(x: double, y: double): void
```

Connect sub-path using straight lines

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-lineTo(x: double, y: double): void--><!--Device-CanvasPath-lineTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the end point of the line. |
| y | double | Yes | The y-axis coordinate of the end point of the line. |

## moveTo

```TypeScript
moveTo(x: double, y: double): void
```

Moves the start point of a new sub-path to the (x, y) coordinate.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-moveTo(x: double, y: double): void--><!--Device-CanvasPath-moveTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the point. |
| y | double | Yes | The y-axis coordinate of the point. |

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: double, cpy: double, x: double, y: double): void
```

Draw quadratic Bezier curve paths

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-quadraticCurveTo(cpx: double, cpy: double, x: double, y: double): void--><!--Device-CanvasPath-quadraticCurveTo(cpx: double, cpy: double, x: double, y: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cpx | double | Yes | The x-axis coordinate of the control point. |
| cpy | double | Yes | The y-axis coordinate of the control point. |
| x | double | Yes | x-axis coordinate of the end point. |
| y | double | Yes | y-axis coordinate of the end point. |

## rect

```TypeScript
rect(x: double, y: double, w: double, h: double): void
```

Draw Rectangular Paths

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-rect(x: double, y: double, w: double, h: double): void--><!--Device-CanvasPath-rect(x: double, y: double, w: double, h: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the start point of the rectangle. |
| y | double | Yes | The y-axis coordinate of the start point of the rectangle. |
| w | double | Yes | Width of the rectangle. |
| h | double | Yes | Height of the rectangle. |

## roundRect

```TypeScript
roundRect(x: double, y: double, w: double, h: double, radii?: double | Array<double>): void
```

Draw rounded Rectangular Paths

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasPath-roundRect(x: double, y: double, w: double, h: double, radii?: double | Array<double>): void--><!--Device-CanvasPath-roundRect(x: double, y: double, w: double, h: double, radii?: double | Array<double>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | The x-axis coordinate of the start point of the rectangle. |
| y | double | Yes | The y-axis coordinate of the start point of the rectangle. |
| w | double | Yes | Width of the rectangle. |
| h | double | Yes | Height of the rectangle. |
| radii | double \| Array&lt;double&gt; | No | A number or list specifying the radii of the circular arc to be used for the corners of the rectangle. The default value is 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | Parameter error. Possible causes: &lt;br&gt; 1. The param radii is a list that has zero or more than four elements. &lt;br&gt; 2. The param radii contains negative value. |

