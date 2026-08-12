# PathEffect

Implements a path effect.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

<!--Device-drawing-class PathEffect--><!--Device-drawing-class PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect
```

Creates a path effect by sequentially applying the inner effect and then the outer effect.

**Since:** 18

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: number): PathEffect
```

Creates a path effect that transforms the sharp angle between line segments into a rounded corner with the specified radius.

**Since:** 12

<!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect--><!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect
```

Creates a **PathEffect** object that converts a path into a dotted line.

**Since:** 12

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| intervals | Array & lt;number & gt; | Yes |
| phase | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect
```

Creates an effect that segments the path and scatters the segments in an irregular pattern along the path.

**Since:** 18

<!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect--><!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| segLength | number | Yes |
| [dev](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileio-stat-depr-i.md) | number | Yes |
| seedAssist | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect
```

Creates a dashed path effect based on the shape described by a path.

**Since:** 18

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| advance | number | Yes |
| phase | number | Yes |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect
```

Creates an overlay path effect based on two distinct path effects. Different from **createComposePathEffect**,this API applies each effect separately and then displays them as a simple overlay.

**Since:** 18

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |
