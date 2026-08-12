# cubicBezierCurve

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## cubicBezierCurve

```TypeScript
export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve
```

Creates a cubic Bezier curve. The curve values must be between 0 and 1.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve--><!--Device-curves-export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | double | Yes | X coordinate of the first point on the Bezier curve.&lt;br&gt;Value range: [0, 1]. &lt;p&gt;**NOTE：**: &lt;br&gt;A value less than 0 is handed as **0**. A value greater than 1 is handed as **1**. &lt;/p&gt; |
| y1 | double | Yes | Y coordinate of the first point on the Bezier curve.&lt;br&gt;Value range: (-∞, +∞). |
| x2 | double | Yes | X coordinate of the second point on the Bezier curve.&lt;br&gt;Value range: [0, 1]. &lt;p&gt;**NOTE：**: &lt;br&gt;A value less than 0 is handed as **0**. A value greater than 1 is handed as **1**. &lt;/p&gt; |
| y2 | double | Yes | Y coordinate of the second point on the Bezier curve.&lt;br&gt;Value range: (-∞, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Interpolation curve. |

