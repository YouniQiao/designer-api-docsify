# RoundRect

Rounded rectangle. > **NOTE：**> > - The initial APIs of this class are supported since API version 12. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class RoundRect--><!--Device-drawing-class RoundRect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(roundRect: RoundRect)
```

Copies a rounded rectangle.

**Since:** 23

<!--Device-RoundRect-constructor(roundRect: RoundRect)--><!--Device-RoundRect-constructor(roundRect: RoundRect)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes |

## constructor

```TypeScript
constructor(rect: common2D.Rect, xRadii: number, yRadii: number)
```

A constructor used to create a **RoundRect** object. A rounded rectangle is created when both **xRadii** and **yRadii** are greater than 0. Otherwise, only a rectangle is created.

**Since:** 23

<!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)--><!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rect | common2D.Rect | Yes |
| xRadii | number | Yes |
| yRadii | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point
```

Obtains the radii of the specified rounded corner in this rounded rectangle.

**Since:** 12

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Point |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point | undefined
```

Obtains the radii of the specified rounded corner in this rounded rectangle.

**Since:** 23

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Point |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## offset

```TypeScript
offset(dx: number, dy: number): void
```

Translates this rounded rectangle by an offset along the X axis and Y axis.

**Since:** 23

<!--Device-RoundRect-offset(dx: double, dy: double): void--><!--Device-RoundRect-offset(dx: double, dy: double): void-End-->

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

## setCorner

```TypeScript
setCorner(pos: CornerPos, x: number, y: number): void
```

Sets the radii of the specified rounded corner in this rounded rectangle.

**Since:** 23

<!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void--><!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes |
| x | number | Yes |
| y | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
