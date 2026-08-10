# steps

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## steps

```TypeScript
function steps(count: number, end: boolean): string
```

构造阶梯曲线对象。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。建议使用[Curves. stepsCurve](arkts-arkui-curves-stepscurve-f.md#stepscurve)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [curves.stepsCurve](arkts-arkui-curves-stepscurve-f.md#stepscurve)

<!--Device-curves-function steps(count: number, end: boolean): string--><!--Device-curves-function steps(count: number, end: boolean): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | number | Yes | 阶梯的数量，需要为正整数。 |
| end | boolean | Yes | 在每个间隔的起点或是终点发生阶跃变化。&lt;br&gt;-true：在终点发生阶跃变化。&lt;br&gt;-false：在起点发生阶跃变化。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回阶梯曲线对象。 |

