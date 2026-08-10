# cubicBezierCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## cubicBezierCurve

```TypeScript
export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve
```

构造三阶贝塞尔曲线对象，确保曲线的值在0到1之间。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve--><!--Device-curves-export function cubicBezierCurve(x1: double, y1: double, x2: double, y2: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | double | Yes | 确定贝塞尔曲线第一点横坐标。&lt;br/&gt;取值范围：[0, 1]&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| y1 | double | Yes | 确定贝塞尔曲线第一点纵坐标。&lt;br/&gt;取值范围：(-∞, +∞) |
| x2 | double | Yes | 确定贝塞尔曲线第二点横坐标。&lt;br/&gt;取值范围：[0, 1]&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于0时，按0处理；设置的值大于1时，按1处理。 |
| y2 | double | Yes | 确定贝塞尔曲线第二点纵坐标。&lt;br/&gt;取值范围：(-∞, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线的插值对象。 |

