# Matrix

Implements a matrix. A 3 x 3 matrix is shown as below.  Elements in the matrix from left to right and from top to bottom respectively represent a horizontal scale coefficient, a horizontal skew coefficient, a horizontal translation coefficient, a vertical skew coefficient, a vertical scale coefficient, a vertical translation coefficient, an X-axis perspective coefficient, a Y-axis perspective coefficient, and a perspective scale coefficient. If (x&lt;sub&gt;1&lt;/sub&gt;, y&lt;sub&gt;1&lt;/sub&gt;) is the source coordinate point, (x&lt;sub&gt;2&lt;/sub&gt;, y&lt;sub&gt;2&lt;/sub&gt;) is the coordinate point obtained by transforming the source coordinate point using the matrix, then the relationship between the two coordinate points is as follows: 

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 23

<!--Device-drawing-class Matrix--><!--Device-drawing-class Matrix-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

Creates a **Matrix** object.

**Since:** 23

<!--Device-Matrix-constructor()--><!--Device-Matrix-constructor()-End-->

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
constructor(matrix: Matrix)
```

Copies a matrix.

**Since:** 23

<!--Device-Matrix-constructor(matrix: Matrix)--><!--Device-Matrix-constructor(matrix: Matrix)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix to be copied. |

**Examples**

See [constructor](#constructor)

## getAll

```TypeScript
getAll(): Array<number>
```

Obtains all element values of this matrix.

**Since:** 12

<!--Device-Matrix-getAll(): Array<number>--><!--Device-Matrix-getAll(): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;number&gt; | Array of matrix values obtained. The length is 9. Each value is a floating point number. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
console.info("matrix "+ matrix.getAll());
```

## getAll

```TypeScript
getAll(): Array<double> | undefined
```

Obtains all element values of this matrix.

**Since:** 23

<!--Device-Matrix-getAll(): Array<double> | undefined--><!--Device-Matrix-getAll(): Array<double> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; \| undefined | nine scalar values contained by Matrix. |

**Examples**

See [getAll](#getall)

## getValue

```TypeScript
getValue(index: int): double
```

Obtains a matrix value of a given index, which ranges from 0 to 8.

**Since:** 23

<!--Device-Matrix-getValue(index: int): double--><!--Device-Matrix-getValue(index: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index. The value is an integer ranging from 0 to 8. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Value obtained, which is an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
for (let i = 0; i < 9; i++) {
    console.info("matrix "+matrix.getValue(i).toString());
}
```

## invert

```TypeScript
invert(matrix: Matrix): boolean
```

Inverts this matrix and returns the result.

**Since:** 23

<!--Device-Matrix-invert(matrix: Matrix): boolean--><!--Device-Matrix-invert(matrix: Matrix): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix** object used to store the inverted matrix. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the matrix is revertible and the **matrix** object is set to its inverse, and **false** means that the matrix is not revertible and the **matrix** object remains unchanged. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
if (matrix1.invert(matrix2)) {
  console.info("matrix1 is invertible and matrix2 is set as an inverse matrix of the matrix1.");
} else {
  console.info("matrix1 is not invertible and matrix2 is not changed.");
}
```

## isAffine

```TypeScript
isAffine(): boolean
```

Checks whether the existing matrix is an affine matrix, which includes transformations such as translation, rotation, and scaling.

**Since:** 24

<!--Device-Matrix-isAffine(): boolean--><!--Device-Matrix-isAffine(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the existing matrix is an affine matrix. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
let isAff = matrix.isAffine();
console.info('isAff :', isAff);
```

## isEqual

```TypeScript
isEqual(matrix: Matrix): boolean
```

Checks whether two **OH_Drawing_Matrix** objects are equal.

**Since:** 23

<!--Device-Matrix-isEqual(matrix: Matrix): boolean--><!--Device-Matrix-isEqual(matrix: Matrix): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Comparison result of the two matrices. The value **true** means that the two matrices are equal, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

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

## isIdentity

```TypeScript
isIdentity(): boolean
```

Checks whether an **OH_Drawing_Matrix** object is an identity matrix:

**Since:** 23

<!--Device-Matrix-isIdentity(): boolean--><!--Device-Matrix-isIdentity(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the matrix is an identity matrix, and **false** means the opposite. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
if (matrix.isIdentity()) {
  console.info("matrix is identity.");
} else {
  console.info("matrix is not identity.");
}
```

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point>
```

Maps a source point array to a destination point array by means of matrix transformation.

**Since:** 12

<!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point>--><!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Array&lt;common2D.Point&gt; | Yes | Array of source points. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | Array of points obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing, common2D } from "@kit.ArkGraphics2D";

let src: Array<common2D.Point> = [];
src.push({x: 15, y: 20});
src.push({x: 20, y: 15});
src.push({x: 30, y: 10});
let matrix = new drawing.Matrix();
let dst: Array<common2D.Point> = matrix.mapPoints(src);
console.info("matrix= src: "+JSON.stringify(src));
console.info("matrix= dst: "+JSON.stringify(dst));
```

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point> | undefined
```

Maps a source point array to a destination point array by means of matrix transformation.

**Since:** 23

<!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point> | undefined--><!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Array&lt;common2D.Point&gt; | Yes | Array of source points. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; \| undefined | Return mapped points array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

See [mapPoints](#mappoints)

## mapRadius

```TypeScript
mapRadius(radius: double): double
```

Returns the average radius of the ellipse formed after a circle with the specified **radius** is mapped by the existing matrix. The square of the average radius is the product of the major axis length and minor axis length of the ellipse. If the matrix contains perspective transformation, the result is meaningless.

**Since:** 24

<!--Device-Matrix-mapRadius(radius: double): double--><!--Device-Matrix-mapRadius(radius: double): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double | Yes | Radius of the circle used for calculation. The value is a floating point number. The absolute value is used if the number is negative. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Average radius after transformation. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D"

let matrix = new drawing.Matrix();
matrix.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let radius = matrix.mapRadius(10);
console.info('radius', radius);
```

## mapRect

```TypeScript
mapRect(dst: common2D.Rect, src: common2D.Rect): boolean
```

Sets the destination rectangle to the bounding rectangle of the shape obtained after transforming the source rectangle with a matrix transformation. As shown in the figure below, the blue rectangle represents the source rectangle, and the yellow rectangle is the shape obtained after a matrix transformation is applied to the source rectangle. Since the edges of the yellow rectangle are not aligned with the coordinate axes, it cannot be represented by a rectangle object. To address this issue, a destination rectangle (black rectangle) is defined as the bounding rectangle. 

**Since:** 23

<!--Device-Matrix-mapRect(dst: common2D.Rect, src: common2D.Rect): boolean--><!--Device-Matrix-mapRect(dst: common2D.Rect, src: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dst | common2D.Rect | Yes | Rectangle** object, which is used to store the bounding rectangle. |
| src | common2D.Rect | Yes | Source rectangle. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the shape retains a rectangular form, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing, common2D } from "@kit.ArkGraphics2D";

let dst: common2D.Rect = { left: 100, top: 20, right: 130, bottom: 60 };
let src: common2D.Rect = { left: 100, top: 80, right: 130, bottom: 120 };
let matrix = new drawing.Matrix();
if (matrix.mapRect(dst, src)) {
    console.info("matrix= dst "+JSON.stringify(dst));
}
```

## postConcat

```TypeScript
postConcat(matrix: Matrix): void
```

Right-multiply the existing matrix by another matrix.

**Since:** 24

<!--Device-Matrix-postConcat(matrix: Matrix): void--><!--Device-Matrix-postConcat(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix used for calculation. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
if (matrix.isIdentity()) {
  console.info("matrix is identity.");
} else {
  console.info("matrix is not identity.");
}
let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
matrix1.postConcat(matrix2);
```

## postRotate

```TypeScript
postRotate(degree: double, px: double, py: double): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

**Since:** 23

<!--Device-Matrix-postRotate(degree: double, px: double, py: double): void--><!--Device-Matrix-postRotate(degree: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | double | Yes | Angle to rotate, in degrees. A positive number indicates a clockwise rotation, and a negative number indicates a counterclockwise rotation. The value is a floating point number. |
| px | double | Yes | X coordinate of the rotation point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the rotation point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: number = 2;
let px: number = 3;
let py: number = 4;
matrix.postRotate(degree, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

## postScale

```TypeScript
postScale(sx: double, sy: double, px: double, py: double): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been scaled with the coefficient (sx, sy) at the scale point (px, py).

**Since:** 23

<!--Device-Matrix-postScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-postScale(sx: double, sy: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | Scale coefficient along the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| sy | double | Yes | Scale coefficient along the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| px | double | Yes | X coordinate of the scale point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the scale point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: number = 2;
let sy: number = 0.5;
let px: number = 1;
let py: number = 1;
matrix.postScale(sx, sy, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

## postSkew

```TypeScript
postSkew(kx: double, ky: double, px: double, py: double): void
```

Right-multiply the existing matrix by a skew transformation matrix.

**Since:** 24

<!--Device-Matrix-postSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-postSkew(kx: double, ky: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| kx | double | Yes | Amount of tilt on the X axis. The value is a floating point number. A positive number tilts the drawing rightwards along the positive direction of the Y axis, and a negative number tilts the drawing leftwards along the positive direction of the Y axis. |
| ky | double | Yes | Amount of tilt on the Y axis. The value is a floating point number. A positive number tilts the drawing downwards along the positive direction of the X axis, and a negative number tilts the drawing upwards along the positive direction of the X axis. |
| px | double | Yes | X coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center to the right of the coordinate origin, while a negative value places the center to the left. |
| py | double | Yes | Y coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center below the coordinate origin, while a negative value places the center above the coordinate origin. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D"

let matrix = new drawing.Matrix();
matrix.postSkew(2.0, 1.0, 2.0, 1.0);
```

## postTranslate

```TypeScript
postTranslate(dx: double, dy: double): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

**Since:** 23

<!--Device-Matrix-postTranslate(dx: double, dy: double): void--><!--Device-Matrix-postTranslate(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| dy | double | Yes | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: number = 3;
let dy: number = 4;
matrix.postTranslate(dx, dy);
console.info("matrix= "+matrix.getAll().toString());
```

## preConcat

```TypeScript
preConcat(matrix: Matrix): void
```

Preconcats the existing matrix with the passed-in matrix.

**Since:** 23

<!--Device-Matrix-preConcat(matrix: Matrix): void--><!--Device-Matrix-preConcat(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix** object, which is on the right of a multiplication expression. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
matrix1.preConcat(matrix2);
```

## preRotate

```TypeScript
preRotate(degree: double, px: double, py: double): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

**Since:** 23

<!--Device-Matrix-preRotate(degree: double, px: double, py: double): void--><!--Device-Matrix-preRotate(degree: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | double | Yes | Angle to rotate, in degrees. A positive number indicates a clockwise rotation, and a negative number indicates a counterclockwise rotation. The value is a floating point number. |
| px | double | Yes | X coordinate of the rotation point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the rotation point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: number = 2;
let px: number = 3;
let py: number = 4;
matrix.preRotate(degree, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

## preScale

```TypeScript
preScale(sx: double, sy: double, px: double, py: double): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been scaled with the coefficient (sx, sy) at the scale point (px, py).

**Since:** 23

<!--Device-Matrix-preScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-preScale(sx: double, sy: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | Scale coefficient along the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| sy | double | Yes | Scale coefficient along the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| px | double | Yes | X coordinate of the scale point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the scale point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: number = 2;
let sy: number = 0.5;
let px: number = 1;
let py: number = 1;
matrix.preScale(sx, sy, px, py);
console.info("matrix"+matrix.getAll().toString());
```

## preSkew

```TypeScript
preSkew(kx: double, ky: double, px: double, py: double): void
```

Left-multiply the existing matrix by a skew transformation matrix.

**Since:** 24

<!--Device-Matrix-preSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-preSkew(kx: double, ky: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| kx | double | Yes | Amount of tilt on the X axis. The value is a floating point number. A positive number tilts the drawing rightwards along the positive direction of the Y axis, and a negative number tilts the drawing leftwards along the positive direction of the Y axis. |
| ky | double | Yes | Amount of tilt on the Y axis. The value is a floating point number. A positive number tilts the drawing downwards along the positive direction of the X axis, and a negative number tilts the drawing upwards along the positive direction of the X axis. |
| px | double | Yes | X coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center to the right of the coordinate origin, while a negative value places the center to the left. |
| py | double | Yes | Y coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center below the coordinate origin, while a negative value places the center above the coordinate origin. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D"

let matrix = new drawing.Matrix();
matrix.preSkew(2.0, 1.0, 2.0, 1.0);
```

## preTranslate

```TypeScript
preTranslate(dx: double, dy: double): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

**Since:** 23

<!--Device-Matrix-preTranslate(dx: double, dy: double): void--><!--Device-Matrix-preTranslate(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| dy | double | Yes | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: number = 3;
let dy: number = 4;
matrix.preTranslate(dx, dy);
console.info("matrix"+matrix.getAll().toString());
```

## rectStaysRect

```TypeScript
rectStaysRect(): boolean
```

Checks whether a rectangle stays a rectangle after being mapped by a matrix.

**Since:** 24

<!--Device-Matrix-rectStaysRect(): boolean--><!--Device-Matrix-rectStaysRect(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a rectangle stays a rectangle after being mapped by a matrix. **true** means yes; false otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
let matrix2 = new drawing.Matrix(matrix);
let isRect = matrix2.rectStaysRect();
console.info('isRect :', isRect);
```

## reset

```TypeScript
reset(): void
```

Resets this matrix to an identity matrix.

**Since:** 23

<!--Device-Matrix-reset(): void--><!--Device-Matrix-reset(): void-End-->

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

## setConcat

```TypeScript
setConcat(matrixA: Matrix, matrixB: Matrix): void
```

Updates the existing matrix with the product of two matrices.

**Since:** 24

<!--Device-Matrix-setConcat(matrixA: Matrix, matrixB: Matrix): void--><!--Device-Matrix-setConcat(matrixA: Matrix, matrixB: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrixA | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix A used for calculation. |
| matrixB | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Matrix B used for calculation. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
matrix1.setConcat(matrix2, matrix1);
```

## setMatrix

```TypeScript
setMatrix(values: Array<double>): void
```

Sets parameters for this matrix.

**Since:** 23

<!--Device-Matrix-setMatrix(values: Array<double>): void--><!--Device-Matrix-setMatrix(values: Array<double>): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | Array&lt;double&gt; | Yes | Floating-point array that holds the parameter values, with the array length set to 9. The values in the array respectively represent a horizontal scale coefficient, a horizontal skew coefficient, a horizontal translation coefficient, a vertical skew coefficient, a vertical scale coefficient, a vertical translation coefficient, an X-axis perspective coefficient, a Y-axis perspective coefficient, and a perspective scale coefficient, in ascending order of indexes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let matrix = new drawing.Matrix()
    matrix.setMatrix([5, 0, 0, 0, 1, 1, 0, 0, 1]);
    canvas.setMatrix(matrix);
    canvas.drawRect({left: 10, right: 200, top: 100, bottom: 500});
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
let value : Array<number> = [2, 2, 2, 2, 2, 2, 2, 2, 2];
matrix.setMatrix(value);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix1.setMatrix(matrix2);
```

## setMatrix

```TypeScript
setMatrix(matrix: Array<double> | Matrix): void
```

Updates the existing matrix with another matrix.

**Since:** 24

<!--Device-Matrix-setMatrix(matrix: Array<double> | Matrix): void--><!--Device-Matrix-setMatrix(matrix: Array<double> | Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | Array&lt;double&gt; \| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | Array or matrix for the update. |

**Examples**

See [setMatrix](#setmatrix)

## setPolyToPoly

```TypeScript
setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean
```

Sets this matrix to a transformation matrix that maps the source point array to the destination point array. Both the number of source points and that of destination points must be in the range [0, 4].

**Since:** 23

<!--Device-Matrix-setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean--><!--Device-Matrix-setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Array&lt;common2D.Point&gt; | Yes | Array of source points. The array length must be the same as the value of **count**. |
| dst | Array&lt;common2D.Point&gt; | Yes | Array of destination points. The array length must be the same as the value of **count**. |
| count | int | Yes | Number of points in each array. The value is an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the setting is successful, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing, common2D } from "@kit.ArkGraphics2D";

let srcPoints: Array<common2D.Point> = [ {x: 10, y: 20}, {x: 200, y: 150} ];
let dstPoints: Array<common2D.Point> = [{ x:0, y: 10 }, { x:300, y: 600 }];
let matrix = new drawing.Matrix();
if (matrix.setPolyToPoly(srcPoints, dstPoints, 2)) {
    console.info("matrix"+matrix.getAll().toString());
}
```

## setRectToRect

```TypeScript
setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean
```

Sets this matrix to a transformation matrix that maps a source rectangle to a destination rectangle.

**Since:** 23

<!--Device-Matrix-setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean--><!--Device-Matrix-setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | common2D.Rect | Yes | Source rectangle. |
| dst | common2D.Rect | Yes | Destination rectangle. |
| scaleToFit | [ScaleToFit](arkts-arkgraphics2d-drawing-scaletofit-e.md) | Yes | Mapping mode from the source rectangle to the target rectangle. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the matrix can represent the mapping, and **false** means the opposite. If either the width or the height of the source rectangle is less than or equal to 0, the API returns **false** and sets the matrix to an identity matrix. If either the width or height of the destination rectangle is less than or equal to 0, the API returns **true** and sets the matrix to a matrix with all values **0**, except for a perspective scaling coefficient of **1**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { drawing, common2D } from "@kit.ArkGraphics2D";

let src: common2D.Rect = { left: 100, top: 100, right: 300, bottom: 300 };
let dst: common2D.Rect = { left: 200, top: 200, right: 600, bottom: 600 };
let scaleToFit: drawing.ScaleToFit = drawing.ScaleToFit.FILL_SCALE_TO_FIT
let matrix = new drawing.Matrix();
if (matrix.setRectToRect(src, dst, scaleToFit)) {
    console.info("matrix"+matrix.getAll().toString());
}
```

## setRotation

```TypeScript
setRotation(degree: double, px: double, py: double): void
```

Sets this matrix as an identity matrix and rotates it by a given degree around the rotation point (px, py).

**Since:** 23

<!--Device-Matrix-setRotation(degree: double, px: double, py: double): void--><!--Device-Matrix-setRotation(degree: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | double | Yes | Angle to rotate, in degrees. A positive number indicates a clockwise rotation, and a negative number indicates a counterclockwise rotation. The value is a floating point number. |
| px | double | Yes | X coordinate of the rotation point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the rotation point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setRotation(90, 100, 100);
```

## setScale

```TypeScript
setScale(sx: double, sy: double, px: double, py: double): void
```

Sets this matrix as an identity matrix and scales it with the coefficients (sx, sy) at the scale point (px, py).

**Since:** 23

<!--Device-Matrix-setScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-setScale(sx: double, sy: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | Yes | Scale coefficient along the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| sy | double | Yes | Scale coefficient along the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| px | double | Yes | X coordinate of the scale point. The value is a floating point number. |
| py | double | Yes | Y coordinate of the scale point. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setScale(100, 100, 150, 150);
```

## setSinCos

```TypeScript
setSinCos(sinValue: double, cosValue: double, px: double, py: double): void
```

Sets the matrix to rotate around the rotation center (px, py) with the specified sine and cosine values.

**Since:** 24

<!--Device-Matrix-setSinCos(sinValue: double, cosValue: double, px: double, py: double): void--><!--Device-Matrix-setSinCos(sinValue: double, cosValue: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sinValue | double | Yes | Sine value of the rotation angle. Only if the sum of the squares of the sine and cosine values is **1**, the rotation transformation is performed. Otherwise, the matrix may contain other transformations such as translation and scaling. |
| cosValue | double | Yes | Cosine value of the rotation angle. Only if the sum of the squares of the sine and cosine values is **1**, the rotation transformation is performed. Otherwise, the matrix may contain other transformations such as translation and scaling. |
| px | double | Yes | X coordinate of the rotation center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center to the right of the coordinate origin, while a negative value places the center to the left. |
| py | double | Yes | Y coordinate of the rotation center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center below the coordinate origin, while a negative value places the center above the coordinate origin. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
matrix.setSinCos(0, 1, 1, 0);
```

## setSkew

```TypeScript
setSkew(kx: double, ky: double, px: double, py: double): void
```

Sets the skew coefficients of a matrix.

**Since:** 24

<!--Device-Matrix-setSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-setSkew(kx: double, ky: double, px: double, py: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| kx | double | Yes | Amount of tilt on the X axis. The value is a floating point number. A positive number tilts the drawing rightwards along the positive direction of the Y axis, and a negative number tilts the drawing leftwards along the positive direction of the Y axis. |
| ky | double | Yes | Amount of tilt on the Y axis. The value is a floating point number. A positive number tilts the drawing downwards along the positive direction of the X axis, and a negative number tilts the drawing upwards along the positive direction of the X axis. |
| px | double | Yes | X coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center to the right of the coordinate origin, while a negative value places the center to the left. |
| py | double | Yes | Y coordinate of the shear center. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the center below the coordinate origin, while a negative value places the center above the coordinate origin. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
matrix.setSkew(2, 0.5, 0.5, 2);
```

## setTranslation

```TypeScript
setTranslation(dx: double, dy: double): void
```

Sets this matrix as an identity matrix and translates it by a given distance (dx, dy).

**Since:** 23

<!--Device-Matrix-setTranslation(dx: double, dy: double): void--><!--Device-Matrix-setTranslation(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| dy | double | Yes | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setTranslation(100, 100);
```

