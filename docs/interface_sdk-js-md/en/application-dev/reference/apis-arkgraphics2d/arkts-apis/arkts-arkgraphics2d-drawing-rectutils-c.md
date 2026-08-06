# RectUtils

This module provides tools for processing rectangles.Use scenarios:

1. Quickly create rectangles and get their basic features, like making a new rectangle, copying one, and obtaining its width, height, and center point.2. Calculate and adjust boundaries, such as obtaining the inclusion relationship, calculating and updating intersections and unions between rectangles, and updating boundary values.
    **NOTE**  
    
    - The initial APIs of this class are supported since API version 20.  
    
    - This module uses the physical pixel unit, px.  
    
    - This module operates under a single-threaded model. The caller needs to manage thread safety and context state  
    transitions.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-drawing-class RectUtils--><!--Device-drawing-class RectUtils-End-->

**System capability:** SystemCapability.Graphics.Drawing

## centerX

ArkTS-Dyn:
```TypeScript
static centerX(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static centerX(rect: common2D.Rect): double
```

Obtains the X coordinate of the rectangle center.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static centerX(rect: common2D.Rect): double--><!--Device-RectUtils-static centerX(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | X coordinate of the rectangle center. |

## centerY

ArkTS-Dyn:
```TypeScript
static centerY(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static centerY(rect: common2D.Rect): double
```

Obtains the Y coordinate of the rectangle center.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static centerY(rect: common2D.Rect): double--><!--Device-RectUtils-static centerY(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Y coordinate of the rectangle center. |

## contains

```TypeScript
static contains(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether a rectangle completely contains another rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static contains(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |
| other | common2D.Rect | Yes | Another rectangle object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a rectangle completely contains another rectangle. **true** means yes; **false** otherwise. An empty rectangle does not contain any other rectangle. |

## contains

ArkTS-Dyn:
```TypeScript
static contains(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): boolean
```

ArkTS-Sta:
```TypeScript
static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean
```

Checks whether a rectangle completely contains another rectangle (which is marked by the coordinates of the upper left and lower right corners).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |
| left | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| top | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |
| right | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| bottom | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a rectangle completely contains another rectangle defined by the coordinates of its upper left and lower right corners. **true** means yes; **false** otherwise. An empty rectangle does not contain any other rectangle. |

## contains

ArkTS-Dyn:
```TypeScript
static contains(rect: common2D.Rect, x: number, y: number): boolean
```

ArkTS-Sta:
```TypeScript
static contains(rect: common2D.Rect, x: double, y: double): boolean
```

Checks whether a rectangle completely contains a specified point.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static contains(rect: common2D.Rect, x: double, y: double): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, x: double, y: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |
| x | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of a point. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| y | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of a point. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the rectangle completely contains the point **(x, y)**. **true** means yes; **false** otherwise. An empty rectangle does not contain any point. |

## getHeight

ArkTS-Dyn:
```TypeScript
static getHeight(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static getHeight(rect: common2D.Rect): double
```

Obtains the height of a rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static getHeight(rect: common2D.Rect): double--><!--Device-RectUtils-static getHeight(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Height of the rectangle. If the top boundary is greater than the bottom, the height is negative. If the top boundary is less than the bottom, the height is positive. |

## getWidth

ArkTS-Dyn:
```TypeScript
static getWidth(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static getWidth(rect: common2D.Rect): double
```

Obtains the width of a rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static getWidth(rect: common2D.Rect): double--><!--Device-RectUtils-static getWidth(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Width of a rectangle. If the left boundary is greater than the right, the width is negative. If the left boundary is less than the right, the width is positive. |

## inset

ArkTS-Dyn:
```TypeScript
static inset(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

ArkTS-Sta:
```TypeScript
static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void
```

Adds the input left, top, right, and bottom values to the left, top, right, and bottom boundaries of a specified rectangle, respectively.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void--><!--Device-RectUtils-static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |
| left | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Value to be added to the left boundary of the rectangle (X coordinate of the upper left corner of the rectangle). The value is a floating point number. **0** indicates that no operation is performed. A positive number indicates addition, and a negative number indicates subtraction. |
| top | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Value to be added to the top boundary of the rectangle (Y coordinate of the upper left corner of the rectangle). The value is a floating point number. **0** indicates that no operation is performed. A positive number indicates addition, and a negative number indicates subtraction. |
| right | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Value to be added to the right boundary of the rectangle (X coordinate of the lower right corner of the rectangle). The value is a floating point number. **0** indicates that no operation is performed. A positive number indicates addition, and a negative number indicates subtraction. |
| bottom | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Value to be added to the bottom boundary of the rectangle (Y coordinate of the lower right corner of the rectangle). The value is a floating point number. **0** indicates that no operation is performed. A positive number indicates addition, and a negative number indicates subtraction. |

## intersect

```TypeScript
static intersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

Calculates the intersection of two rectangles and updates the intersection result to the rectangle represented by the first input parameter.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static intersect(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static intersect(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Original rectangle used to calculate the intersection. |
| other | common2D.Rect | Yes | Another rectangle used to calculate the intersection. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether two rectangles have an intersection. **true** means yes; **false** otherwise. |

## isEmpty

```TypeScript
static isEmpty(rect: common2D.Rect): boolean
```

Checks whether a rectangle is empty (the left boundary is greater than or equal to the right boundary or the top boundary is greater than or equal to the bottom boundary).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static isEmpty(rect: common2D.Rect): boolean--><!--Device-RectUtils-static isEmpty(rect: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object to be checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the rectangle is empty. **true** means yes; **false** otherwise. |

## isEqual

```TypeScript
static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether two rectangles are equal.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Original rectangle. |
| other | common2D.Rect | Yes | Another rectangle. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether two rectangles are equal. **true** means yes; **false** otherwise. |

## isIntersect

```TypeScript
static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether two rectangles intersect.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Original rectangle used to calculate the intersection. |
| other | common2D.Rect | Yes | Another rectangle used to calculate the intersection. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether two rectangles have an intersection. **true** means yes; **false** otherwise. If the two rectangles only overlap on the edge or intersect at a point, **false** is returned. |

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect
```

Copies a rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect--><!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | common2D.Rect | Yes | Rectangle to be copied. |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | Created rectangle. |

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect | undefined
```

Makes a deep copy of a 2D rectangular object.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect | undefined--><!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | common2D.Rect | Yes | Indicates the source rectangle to copy. |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect |  Returns an Rect object has the same boundary coordinates with the source. |

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect
```

Creates a rectangle with the top, bottom, left, and right boundary coordinates all being **0**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-RectUtils-static makeEmpty(): common2D.Rect--><!--Device-RectUtils-static makeEmpty(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | Created rectangle object. |

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect | undefined
```

Makes an uninitialized 2D rectangular object with zero dimensions and origin at (0, 0).

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RectUtils-static makeEmpty(): common2D.Rect | undefined--><!--Device-RectUtils-static makeEmpty(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect |  Returns an empty Rect object with all coordinates (left, top, right, bottom) set to 0. |

## makeLtrb

```TypeScript
static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect
```

Creates a rectangle with specified top, bottom, left, and right boundaries.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-RectUtils-static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect--><!--Device-RectUtils-static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | number | Yes | X coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| top | number | Yes | Y coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |
| right | number | Yes | X coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| bottom | number | Yes | Y coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | Created rectangle. |

## makeLtrb

```TypeScript
static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined
```

Makes a 2D rectangular object from boundary coordinates.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RectUtils-static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined--><!--Device-RectUtils-static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | double | Yes | Indicates the X-coordinate of the left edge. |
| top | double | Yes | Indicates the Y-coordinate of the top edge. |
| right | double | Yes | Indicates the X-coordinate of the right edge. |
| bottom | double | Yes | Indicates the Y-coordinate of the bottom edge. |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect |  Returns an Rect object with the specific coordinates (left, top, right, bottom). |

## offset

ArkTS-Dyn:
```TypeScript
static offset(rect: common2D.Rect, dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
static offset(rect: common2D.Rect, dx: double, dy: double): void
```

Translates a rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static offset(rect: common2D.Rect, dx: double, dy: double): void--><!--Device-RectUtils-static offset(rect: common2D.Rect, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle to be translated. |
| dx | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Horizontal translation distance. The value is a floating point number. **0** indicates no translation. A negative value indicates translation to the left, and a positive value indicates translation to the right. |
| dy | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Vertical translation distance. The value is a floating point number. **0** indicates no translation. A negative value indicates translation upwards, and a positive value indicates translation downwards. |

## offsetTo

ArkTS-Dyn:
```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: number, newTop: number): void
```

ArkTS-Sta:
```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void
```

Translates a rectangle to a specified position.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void--><!--Device-RectUtils-static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle to be translated. |
| newLeft | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of the position to which the rectangle is translated. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| newTop | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of the position to which the rectangle is translated. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

## setEmpty

```TypeScript
static setEmpty(rect: common2D.Rect): void
```

Sets the left, right, top, and bottom boundaries of the rectangle to **0**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static setEmpty(rect: common2D.Rect): void--><!--Device-RectUtils-static setEmpty(rect: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Empty rectangle object. |

## setLtrb

ArkTS-Dyn:
```TypeScript
static setLtrb(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

ArkTS-Sta:
```TypeScript
static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void
```

Updates the top, bottom, left, and right boundary values of the existing rectangle using the input top, bottom,left, and right values, respectively.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void--><!--Device-RectUtils-static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |
| left | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| top | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of the upper left corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |
| right | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | X coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point to the right of the coordinate origin, while a negative value places the point to the left. |
| bottom | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Y coordinate of the lower right corner of the rectangle. The value is a floating point number. **0** indicates the coordinate origin. A positive value places the point below the coordinate origin, while a negative value places the point above the coordinate origin. |

## setRect

```TypeScript
static setRect(rect: common2D.Rect, other: common2D.Rect): void
```

Assigns the existing rectangle with another rectangle.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static setRect(rect: common2D.Rect, other: common2D.Rect): void--><!--Device-RectUtils-static setRect(rect: common2D.Rect, other: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Original rectangle. |
| other | common2D.Rect | Yes | Another rectangle. |

## sort

```TypeScript
static sort(rect: common2D.Rect): void
```

If the rectangle is reversed (that is, the left boundary is greater than the right boundary or the top boundary is greater than the bottom boundary), the top and bottom (left and right) boundary values of the rectangle are exchanged, so that the top boundary is less than the bottom boundary (the left boundary is less than the right boundary).If the rectangle is not reversed (that is, the left boundary is less than or equal to the right boundary or the top boundary is less than or equal to the bottom boundary), no operation is performed.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RectUtils-static sort(rect: common2D.Rect): void--><!--Device-RectUtils-static sort(rect: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Rectangle object. |

## union

```TypeScript
static union(rect: common2D.Rect, other: common2D.Rect): void
```

Calculates the union of two rectangles and updates the union result to the rectangle represented by the first input parameter. If the first input parameter is empty, the union result is updated to the rectangle represented by the second input parameter. If the second input parameter is empty, no operation is performed.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-RectUtils-static union(rect: common2D.Rect, other: common2D.Rect): void--><!--Device-RectUtils-static union(rect: common2D.Rect, other: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | Original rectangle used to calculate the union. |
| other | common2D.Rect | Yes | Another rectangle used to calculate the union. |

