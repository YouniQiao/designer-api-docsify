# Lattice

Lattice object. which is used to divide an image by lattice. > **NOTE：**> > - The initial APIs of this class are supported since API version 12. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

**Deprecated since:** -1

<!--Device-drawing-class Lattice--><!--Device-drawing-class Lattice-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice
```

Divides the image into lattices. The lattices on both even columns and even rows are fixed, and they are drawn at their original size if the target is large enough. If the target is too small to hold the fixed lattices, all the fixed lattices are scaled down to fit the target, and the lattices that are not on even columns and even rows are scaled to accommodate the remaining space.

**Since:** 12

**Deprecated since:** -1

<!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice--><!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | Yes |
| yDivs | Array & lt;number & gt; | Yes |
| fXCount | number | Yes |
| fYCount | number | Yes |
| fBounds | common2D.Rect \| null | No |
| fRectTypes | Array & lt;RectType & gt; \ | null | No |
| fColors | Array & lt;common2D.Color & gt; \ | null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice | undefined
```

Divides the image into lattices. The lattices on both even columns and even rows are fixed, and they are drawn at their original size if the target is large enough. If the target is too small to hold the fixed lattices, all the fixed lattices are scaled down to fit the target, and the lattices that are not on even columns and even rows are scaled to accommodate the remaining space.

**Since:** 23

**Deprecated since:** -1

<!--Device-Lattice-static createImageLattice(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice | undefined--><!--Device-Lattice-static createImageLattice(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | Yes |
| yDivs | Array & lt;number & gt; | Yes |
| fXCount | number | Yes |
| fYCount | number | Yes |
| fBounds | common2D.Rect \| null | No |
| fRectTypes | Array & lt;RectType & gt; \ | null | No |
| fColors | Array & lt;common2D.Color & gt; \ | null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice
```

Divides the image into lattices. The lattices on both even columns and even rows are fixed, and they are drawn at their original size if the target is large enough. If the target is too small to hold the fixed lattices, all the fixed lattices are scaled down to fit the target, and the lattices that are not on even columns and even rows are scaled to accommodate the remaining space.

**Since:** 18

**Deprecated since:** -1

<!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice--><!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | Yes |
| yDivs | Array & lt;number & gt; | Yes |
| fXCount | number | Yes |
| fYCount | number | Yes |
| fBounds | common2D.Rect \| null | No |
| fRectTypes | Array & lt;RectType & gt; \ | null | No |
| fColors | Array & lt;number & gt; \ | null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createImageLatticeWithArrayInt

```TypeScript
static createImageLatticeWithArrayInt(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice | undefined
```

Divides the image into lattices. The lattices on both even columns and even rows are fixed, and they are drawn at their original size if the target is large enough. If the target is too small to hold the fixed lattices, all the fixed lattices are scaled down to fit the target, and the lattices that are not on even columns and even rows are scaled to accommodate the remaining space.

**Since:** 23

**Deprecated since:** -1

<!--Device-Lattice-static createImageLatticeWithArrayInt(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<int> | null): Lattice | undefined--><!--Device-Lattice-static createImageLatticeWithArrayInt(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<int> | null): Lattice | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | Yes |
| yDivs | Array & lt;number & gt; | Yes |
| fXCount | number | Yes |
| fYCount | number | Yes |
| fBounds | common2D.Rect \| null | No |
| fRectTypes | Array & lt;RectType & gt; \ | null | No |
| fColors | Array & lt;number & gt; \ | null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
