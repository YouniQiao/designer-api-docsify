# ShadowLayer

Implements a shadow layer. > **NOTE：**> > - The initial APIs of this class are supported since API version 12. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class ShadowLayer--><!--Device-drawing-class ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer
```

Creates a **ShadowLayer** object.

**Since:** 12

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| x | number | Yes |
| y | number | Yes |
| color | common2D.Color | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer | undefined
```

Creates a ShadowLayer object.

**Since:** 23

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| x | number | Yes |
| y | number | Yes |
| color | common2D.Color | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer
```

Creates a **ShadowLayer** object.

**Since:** 18

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| x | number | Yes |
| y | number | Yes |
| color | common2D.Color \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer | undefined
```

Creates a ShadowLayer object.

**Since:** 23

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| x | number | Yes |
| y | number | Yes |
| color | common2D.Color \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
