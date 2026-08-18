# customCurve

## Modules to Import

```TypeScript
```

## customCurve

```TypeScript
export function customCurve(interpolate: (fraction: double) => double): ICurve
```

Creates a custom curve.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve--><!--Device-curves-export function customCurve(interpolate: (fraction: double) => double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interpolate | (fraction: double) =&gt; double | Yes | Custom interpolation callback.fraction: input x value for interpolation. when the animation starts. Value range: [0, 1]The return value is the y value of the curve. Value range: [0, 1]. &lt;p&gt;**NOTE：**: <br>If fraction is 0, the return value 0 corresponds to the animation start point; <br>any other return value means that the animation jumps at the start point.If fraction is 1, the return <br>value 1 corresponds to the animation end point; any other return value means that the end value <br>of the animation is not the value of the state variable, which will result in an effect of transitions <br>from that end value to the value of the state variable. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Interpolation curve. |

