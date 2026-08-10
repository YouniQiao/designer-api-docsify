# customCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## customCurve

```TypeScript
export function customCurve(interpolate: (fraction: double) => double): ICurve
```

构造自定义曲线对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve--><!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interpolate | (fraction: double) =&gt; double | Yes | 用户自定义的插值回调函数。&lt;br/&gt;fraction为动画开始时的插值输入x值。取值范围：[0,1]&lt;br/&gt;返回值为曲线的y值。取值范围：[0,1]&lt;br /&gt;**说明：**&lt;br /&gt;fraction等于0时，返回值为0对应动画起点，返回不为0，动画在起点处有跳变效果。&lt;br/&gt;fraction等于1时，返回值为1对应动画终点，返回值不为1将导致动画的终值不是状态变量的 值，出现大于或者小于状态变量值，再跳变到状态变量值的效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线的插值对象。 |

