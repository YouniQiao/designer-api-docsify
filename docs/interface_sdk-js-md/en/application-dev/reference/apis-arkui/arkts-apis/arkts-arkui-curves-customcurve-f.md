# customCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## customCurve

```TypeScript
export function customCurve(interpolate: (fraction: double) => double): ICurve
```

Creates a custom curve.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve--><!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interpolate | (fraction: double) =&gt; double | Yes | Custom interpolation callback.fraction: input x value for interpolation. when the animation starts. Value range: [0, 1]The return value is the y value of the curve. Value range: [0, 1]. &lt;p&gt;**NOTE：**: &lt;br&gt;If fraction is 0, the return value 0 corresponds to the animation start point; &lt;br&gt;any other return value means that the animation jumps at the start point.If fraction is 1, the return &lt;br&gt;value 1 corresponds to the animation end point; any other return value means that the end value &lt;br&gt;of the animation is not the value of the state variable, which will result in an effect of transitions &lt;br&gt;from that end value to the value of the state variable. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | Interpolation curve. |

