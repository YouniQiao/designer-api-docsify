# PointUtils

This class offers a comprehensive set of operations for handling common2D Point objects.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-drawing-class PointUtils--><!--Device-drawing-class PointUtils-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'drawing';
```

## negate

```TypeScript
static negate(point: common2D.Point): void
```

Negates the point's coordinates.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointUtils-static negate(point: common2D.Point): void--><!--Device-PointUtils-static negate(point: common2D.Point): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | common2D.Point | Yes | Specifies the point to be negated. |

## offset

```TypeScript
static offset(point: common2D.Point, dx: double, dy: double): void
```

Offsets the point's coordinates by dx, dy.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointUtils-static offset(point: common2D.Point, dx: double, dy: double): void--><!--Device-PointUtils-static offset(point: common2D.Point, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | common2D.Point | Yes | Specifies the point to be offset. |
| dx | double | Yes | Indicates the distance to offset on the x-axis in pixels. |
| dy | double | Yes | Indicates the distance to offset on the y-axis in pixels. |

