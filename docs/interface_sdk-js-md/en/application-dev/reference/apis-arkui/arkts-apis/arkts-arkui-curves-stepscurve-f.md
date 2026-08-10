# stepsCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## stepsCurve

```TypeScript
export function stepsCurve(count: int, end: boolean): ICurve
```

构造阶梯曲线对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function stepsCurve(count: int, end: boolean): ICurve--><!--Device-curves-export function stepsCurve(count: int, end: boolean): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int | Yes | 阶梯的数量，需要为正整数。&lt;br/&gt;取值范围：[1, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;设置小于1的值时，按值为1处理。 |
| end | boolean | Yes | 在每个间隔的起点或终点发生阶跃变化。&lt;br&gt;-true：在终点发生阶跃变化。&lt;br&gt;-false：在起点发生阶跃变化。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线的插值对象。 |

