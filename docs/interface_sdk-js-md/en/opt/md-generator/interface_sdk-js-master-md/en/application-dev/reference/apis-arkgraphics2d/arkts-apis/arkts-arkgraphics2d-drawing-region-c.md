# Region

Describes a region, which is used to describe the region where the shape can be drawn.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

<!--Device-drawing-class Region--><!--Device-drawing-class Region-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

Constructs a **Region** object.

**Since:** 20

<!--Device-Region-constructor()--><!--Device-Region-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(region: Region)
```

Copies a **Region** object.

**Since:** 20

<!--Device-Region-constructor(region: Region)--><!--Device-Region-constructor(region: Region)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |

## constructor

```TypeScript
constructor(left: number, top: number, right: number, bottom: number)
```

Constructs a rectangular region.

**Since:** 20

<!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)--><!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| left | number | Yes |
| top | number | Yes |
| right | number | Yes |
| bottom | number | Yes |

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path
```

Obtains a new path that is the boundary of the existing region.

**Since:** 20

<!--Device-Region-getBoundaryPath(): Path--><!--Device-Region-getBoundaryPath(): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

Obtains the boundaries of the existing region.

**Since:** 20

<!--Device-Region-getBounds(): common2D.Rect--><!--Device-Region-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## isComplex

```TypeScript
isComplex(): boolean
```

Checks whether this region contains multiple rectangles.

**Since:** 20

<!--Device-Region-isComplex(): boolean--><!--Device-Region-isComplex(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether the existing region is empty.

**Since:** 20

<!--Device-Region-isEmpty(): boolean--><!--Device-Region-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEqual

```TypeScript
isEqual(other: Region): boolean
```

Checks whether another region is equal to this region.

**Since:** 20

<!--Device-Region-isEqual(other: Region): boolean--><!--Device-Region-isEqual(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPointContained

```TypeScript
isPointContained(x: number, y:number): boolean
```

Checks whether a point is contained in this region.

**Since:** 12

<!--Device-Region-isPointContained(x: int, y:int): boolean--><!--Device-Region-isPointContained(x: int, y:int): boolean-End-->

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

## isRect

```TypeScript
isRect(): boolean
```

Checks whether this region is the same as a single rectangle.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-isRect(): boolean--><!--Device-Region-isRect(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRegionContained

```TypeScript
isRegionContained(other: Region): boolean
```

Checks whether another region is contained in this region.

**Since:** 12

<!--Device-Region-isRegionContained(other: Region): boolean--><!--Device-Region-isRegionContained(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## offset

```TypeScript
offset(dx: number, dy: number): void
```

Translates a region.

**Since:** 20

<!--Device-Region-offset(dx: int, dy: int): void--><!--Device-Region-offset(dx: int, dy: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | number | Yes |
| dy | number | Yes |

## op

```TypeScript
op(region: Region, regionOp: RegionOp): boolean
```

Performs an operation on this region and another region, and stores the resulting region in this **Region**object.

**Since:** 12

<!--Device-Region-op(region: Region, regionOp: RegionOp): boolean--><!--Device-Region-op(region: Region, regionOp: RegionOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |
| regionOp | [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## quickContains

```TypeScript
quickContains(left: number, top: number, right: number, bottom: number): boolean
```

Checks whether this region is the same as a single rectangle and contains the specified rectangle.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean-End-->

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
| boolean |

## quickReject

```TypeScript
quickReject(left: number, top: number, right: number, bottom: number): boolean
```

Checks whether a rectangle do not intersect with this region. Actually, this API determines whether the rectangle does not intersect with the bounding rectangle of the region, and therefore the result may not be accurate.

**Since:** 12

<!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean-End-->

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
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## quickRejectRegion

```TypeScript
quickRejectRegion(region: Region): boolean
```

Checks whether the existing region does not intersect with another region. Actually, the outer rectangles of the two regions are compared to determine whether they do not intersect. Therefore, there may be an error.

**Since:** 20

<!--Device-Region-quickRejectRegion(region: Region): boolean--><!--Device-Region-quickRejectRegion(region: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setEmpty

```TypeScript
setEmpty(): void
```

Set the existing region to empty.

**Since:** 20

<!--Device-Region-setEmpty(): void--><!--Device-Region-setEmpty(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## setPath

```TypeScript
setPath(path: Path, clip: Region): boolean
```

Sets a region that matches the outline of a path within the cropping area.

**Since:** 12

<!--Device-Region-setPath(path: Path, clip: Region): boolean--><!--Device-Region-setPath(path: Path, clip: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| clip | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setRect

```TypeScript
setRect(left: number, top: number, right: number, bottom: number): boolean
```

Sets a rectangle.

**Since:** 12

<!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean-End-->

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
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setRegion

```TypeScript
setRegion(region: Region): void
```

Sets the existing region to another region.

**Since:** 20

<!--Device-Region-setRegion(region: Region): void--><!--Device-Region-setRegion(region: Region): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | Yes |
