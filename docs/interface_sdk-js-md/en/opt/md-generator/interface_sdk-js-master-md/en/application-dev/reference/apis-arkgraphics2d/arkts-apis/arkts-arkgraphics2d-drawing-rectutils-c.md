# RectUtils

This module provides tools for processing rectangles. Use scenarios: 1. Quickly create rectangles and get their basic features, like making a new rectangle, copying one, and obtaining its width, height, and center point. 2. Calculate and adjust boundaries, such as obtaining the inclusion relationship, calculating and updating intersections and unions between rectangles, and updating boundary values. > **NOTE：**> > - The initial APIs of this class are supported since API version 20. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class RectUtils--><!--Device-drawing-class RectUtils-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## centerX

```TypeScript
static centerX(rect: common2D.Rect): number
```

Obtains the X coordinate of the rectangle center.

**Since:** 24

<!--Device-RectUtils-static centerX(rect: common2D.Rect): double--><!--Device-RectUtils-static centerX(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## centerY

```TypeScript
static centerY(rect: common2D.Rect): number
```

Obtains the Y coordinate of the rectangle center.

**Since:** 24

<!--Device-RectUtils-static centerY(rect: common2D.Rect): double--><!--Device-RectUtils-static centerY(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## contains

```TypeScript
static contains(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether a rectangle completely contains another rectangle.

**Since:** 23

<!--Device-RectUtils-static contains(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## contains

```TypeScript
static contains(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): boolean
```

Checks whether a rectangle completely contains another rectangle (which is marked by the coordinates of the upper left and lower right corners).

**Since:** 24

<!--Device-RectUtils-static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## contains

```TypeScript
static contains(rect: common2D.Rect, x: number, y: number): boolean
```

Checks whether a rectangle completely contains a specified point.

**Since:** 24

<!--Device-RectUtils-static contains(rect: common2D.Rect, x: double, y: double): boolean--><!--Device-RectUtils-static contains(rect: common2D.Rect, x: double, y: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getHeight

```TypeScript
static getHeight(rect: common2D.Rect): number
```

Obtains the height of a rectangle.

**Since:** 23

<!--Device-RectUtils-static getHeight(rect: common2D.Rect): double--><!--Device-RectUtils-static getHeight(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWidth

```TypeScript
static getWidth(rect: common2D.Rect): number
```

Obtains the width of a rectangle.

**Since:** 23

<!--Device-RectUtils-static getWidth(rect: common2D.Rect): double--><!--Device-RectUtils-static getWidth(rect: common2D.Rect): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## inset

```TypeScript
static inset(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

Adds the input left, top, right, and bottom values to the left, top, right, and bottom boundaries of a specified rectangle, respectively.

**Since:** 23

<!--Device-RectUtils-static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void--><!--Device-RectUtils-static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

## intersect

```TypeScript
static intersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

Calculates the intersection of two rectangles and updates the intersection result to the rectangle represented by the first input parameter.

**Since:** 23

<!--Device-RectUtils-static intersect(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static intersect(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEmpty

```TypeScript
static isEmpty(rect: common2D.Rect): boolean
```

Checks whether a rectangle is empty (the left boundary is greater than or equal to the right boundary or the top boundary is greater than or equal to the bottom boundary).

**Since:** 23

<!--Device-RectUtils-static isEmpty(rect: common2D.Rect): boolean--><!--Device-RectUtils-static isEmpty(rect: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEqual

```TypeScript
static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether two rectangles are equal.

**Since:** 23

<!--Device-RectUtils-static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isIntersect

```TypeScript
static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

Checks whether two rectangles intersect.

**Since:** 24

<!--Device-RectUtils-static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean--><!--Device-RectUtils-static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect
```

Copies a rectangle.

**Since:** 20

<!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect--><!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect | undefined
```

Makes a deep copy of a 2D rectangular object.

**Since:** 24

<!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect | undefined--><!--Device-RectUtils-static makeCopy(src: common2D.Rect): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | common2D.Rect | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect
```

Creates a rectangle with the top, bottom, left, and right boundary coordinates all being **0**.

**Since:** 20

<!--Device-RectUtils-static makeEmpty(): common2D.Rect--><!--Device-RectUtils-static makeEmpty(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect | undefined
```

Makes an uninitialized 2D rectangular object with zero dimensions and origin at (0, 0).

**Since:** 24

<!--Device-RectUtils-static makeEmpty(): common2D.Rect | undefined--><!--Device-RectUtils-static makeEmpty(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeLtrb

```TypeScript
static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect
```

Creates a rectangle with specified top, bottom, left, and right boundaries.

**Since:** 20

<!--Device-RectUtils-static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect--><!--Device-RectUtils-static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeLtrb

```TypeScript
static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect | undefined
```

Makes a 2D rectangular object from boundary coordinates.

**Since:** 24

<!--Device-RectUtils-static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined--><!--Device-RectUtils-static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## offset

```TypeScript
static offset(rect: common2D.Rect, dx: number, dy: number): void
```

Translates a rectangle.

**Since:** 23

<!--Device-RectUtils-static offset(rect: common2D.Rect, dx: double, dy: double): void--><!--Device-RectUtils-static offset(rect: common2D.Rect, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| dx | number | Yes |
| dy | number | Yes |

## offsetTo

```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: number, newTop: number): void
```

Translates a rectangle to a specified position.

**Since:** 24

<!--Device-RectUtils-static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void--><!--Device-RectUtils-static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| newLeft | number | Yes |
| newTop | number | Yes |

## setEmpty

```TypeScript
static setEmpty(rect: common2D.Rect): void
```

Sets the left, right, top, and bottom boundaries of the rectangle to **0**.

**Since:** 24

<!--Device-RectUtils-static setEmpty(rect: common2D.Rect): void--><!--Device-RectUtils-static setEmpty(rect: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

## setLtrb

```TypeScript
static setLtrb(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

Updates the top, bottom, left, and right boundary values of the existing rectangle using the input top, bottom, left, and right values, respectively.

**Since:** 24

<!--Device-RectUtils-static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void--><!--Device-RectUtils-static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

## setRect

```TypeScript
static setRect(rect: common2D.Rect, other: common2D.Rect): void
```

Assigns the existing rectangle with another rectangle.

**Since:** 24

<!--Device-RectUtils-static setRect(rect: common2D.Rect, other: common2D.Rect): void--><!--Device-RectUtils-static setRect(rect: common2D.Rect, other: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |

## sort

```TypeScript
static sort(rect: common2D.Rect): void
```

If the rectangle is reversed (that is, the left boundary is greater than the right boundary or the top boundary is greater than the bottom boundary), the top and bottom (left and right) boundary values of the rectangle are exchanged, so that the top boundary is less than the bottom boundary (the left boundary is less than the right boundary). If the rectangle is not reversed (that is, the left boundary is less than or equal to the right boundary or the top boundary is less than or equal to the bottom boundary), no operation is performed.

**Since:** 23

<!--Device-RectUtils-static sort(rect: common2D.Rect): void--><!--Device-RectUtils-static sort(rect: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |

## union

```TypeScript
static union(rect: common2D.Rect, other: common2D.Rect): void
```

Calculates the union of two rectangles and updates the union result to the rectangle represented by the first input parameter. If the first input parameter is empty, the union result is updated to the rectangle represented by the second input parameter. If the second input parameter is empty, no operation is performed.

**Since:** 24

<!--Device-RectUtils-static union(rect: common2D.Rect, other: common2D.Rect): void--><!--Device-RectUtils-static union(rect: common2D.Rect, other: common2D.Rect): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| other | common2D.Rect | Yes |
