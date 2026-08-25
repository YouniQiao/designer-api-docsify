# Matrix

Implements a matrix. A 3 x 3 matrix is shown as below. Elements in the matrix from left to right and from top to bottom respectively represent a horizontal scale coefficient, a horizontal skew coefficient, a horizontal translation coefficient, a vertical skew coefficient, a vertical scale coefficient, a vertical translation coefficient, an X-axis perspective coefficient, a Y-axis perspective coefficient, and a perspective scale coefficient. If (x&lt;sub&gt;1&lt;/sub&gt;, y&lt;sub&gt;1&lt;/sub&gt;) is the source coordinate point, (x&lt;sub&gt;2&lt;/sub&gt;, y&lt;sub&gt;2&lt;/sub&gt;) is the coordinate point obtained by transforming the source coordinate point using the matrix, then the relationship between the two coordinate points is as follows:

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 12.&gt;
> - This module uses the physical pixel unit, px.&gt;
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

Creates a **Matrix** object.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(matrix: Matrix)
```

Copies a matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

## getAll

```TypeScript
getAll(): Array<number>
```

Obtains all element values of this matrix.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getValue

```TypeScript
getValue(index: number): number
```

Obtains a matrix value of a given index, which ranges from 0 to 8.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## invert

```TypeScript
invert(matrix: Matrix): boolean
```

Inverts this matrix and returns the result.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isAffine

```TypeScript
isAffine(): boolean
```

Checks whether the existing matrix is an affine matrix, which includes transformations such as translation, rotation, and scaling.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEqual

```TypeScript
isEqual(matrix: Matrix): boolean
```

Checks whether two **OH_Drawing_Matrix** objects are equal.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isIdentity

```TypeScript
isIdentity(): boolean
```

Checks whether an **OH_Drawing_Matrix** object is an identity matrix:

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point>
```

Maps a source point array to a destination point array by means of matrix transformation.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Array & lt;common2D.Point & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## mapRadius

```TypeScript
mapRadius(radius: number): number
```

Returns the average radius of the ellipse formed after a circle with the specified **radius** is mapped by the existing matrix. The square of the average radius is the product of the major axis length and minor axis length of the ellipse. If the matrix contains perspective transformation, the result is meaningless.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## mapRect

```TypeScript
mapRect(dst: common2D.Rect, src: common2D.Rect): boolean
```

Sets the destination rectangle to the bounding rectangle of the shape obtained after transforming the source rectangle with a matrix transformation. As shown in the figure below, the blue rectangle represents the source rectangle, and the yellow rectangle is the shape obtained after a matrix transformation is applied to the source rectangle. Since the edges of the yellow rectangle are not aligned with the coordinate axes, it cannot be represented by a rectangle object. To address this issue, a destination rectangle (black rectangle) is defined as the bounding rectangle.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | common2D.Rect | Yes |
| src | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## postConcat

```TypeScript
postConcat(matrix: Matrix): void
```

Right-multiply the existing matrix by another matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

## postRotate

```TypeScript
postRotate(degree: number, px: number, py: number): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degree | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## postScale

```TypeScript
postScale(sx: number, sy: number, px: number, py: number): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been scaled with the coefficient (sx, sy) at the scale point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## postSkew

```TypeScript
postSkew(kx: number, ky: number, px: number, py: number): void
```

Right-multiply the existing matrix by a skew transformation matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| kx | number | Yes |
| ky | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

## postTranslate

```TypeScript
postTranslate(dx: number, dy: number): void
```

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

**Since:** 12

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

## preConcat

```TypeScript
preConcat(matrix: Matrix): void
```

Preconcats the existing matrix with the passed-in matrix.

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

## preRotate

```TypeScript
preRotate(degree: number, px: number, py: number): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degree | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## preScale

```TypeScript
preScale(sx: number, sy: number, px: number, py: number): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been scaled with the coefficient (sx, sy) at the scale point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## preSkew

```TypeScript
preSkew(kx: number, ky: number, px: number, py: number): void
```

Left-multiply the existing matrix by a skew transformation matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| kx | number | Yes |
| ky | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

## preTranslate

```TypeScript
preTranslate(dx: number, dy: number): void
```

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

**Since:** 12

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

## rectStaysRect

```TypeScript
rectStaysRect(): boolean
```

Checks whether a rectangle stays a rectangle after being mapped by a matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

Resets this matrix to an identity matrix.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## setConcat

```TypeScript
setConcat(matrixA: Matrix, matrixB: Matrix): void
```

Updates the existing matrix with the product of two matrices.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| matrixA | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |
| matrixB | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

## setMatrix

```TypeScript
setMatrix(values: Array<number>): void
```

Sets parameters for this matrix.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Array & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setMatrix

```TypeScript
setMatrix(matrix: Array<number> | Matrix): void
```

Updates the existing matrix with another matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | Array & lt;number & gt; \ | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes |

## setPolyToPoly

```TypeScript
setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean
```

Sets this matrix to a transformation matrix that maps the source point array to the destination point array. Both the number of source points and that of destination points must be in the range [0, 4].

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Array & lt;common2D.Point & gt; | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | Array & lt;common2D.Point & gt; | Yes |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setRectToRect

```TypeScript
setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean
```

Sets this matrix to a transformation matrix that maps a source rectangle to a destination rectangle.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | common2D.Rect | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | common2D.Rect | Yes |
| scaleToFit | [ScaleToFit](arkts-arkgraphics2d-drawing-scaletofit-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setRotation

```TypeScript
setRotation(degree: number, px: number, py: number): void
```

Sets this matrix as an identity matrix and rotates it by a given degree around the rotation point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degree | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setScale

```TypeScript
setScale(sx: number, sy: number, px: number, py: number): void
```

Sets this matrix as an identity matrix and scales it with the coefficients (sx, sy) at the scale point (px, py).

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | Yes |
| sy | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setSinCos

```TypeScript
setSinCos(sinValue: number, cosValue: number, px: number, py: number): void
```

Sets the matrix to rotate around the rotation center (px, py) with the specified sine and cosine values.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sinValue | number | Yes |
| cosValue | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

## setSkew

```TypeScript
setSkew(kx: number, ky: number, px: number, py: number): void
```

Sets the skew coefficients of a matrix.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| kx | number | Yes |
| ky | number | Yes |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | number | Yes |
| py | number | Yes |

## setTranslation

```TypeScript
setTranslation(dx: number, dy: number): void
```

Sets this matrix as an identity matrix and translates it by a given distance (dx, dy).

**Since:** 12

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
