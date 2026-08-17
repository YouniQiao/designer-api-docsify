# stepsCurve

## stepsCurve

```TypeScript
export function stepsCurve(count: int, end: boolean): ICurve
```

Creates a step curve.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function stepsCurve(count: int, end: boolean): ICurve--><!--Device-curves-export function stepsCurve(count: int, end: boolean): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int | Yes | Number of steps. The value must be a positive integer.<br>Value range: [1, INT_MAX]. &lt;p&gt;**NOTE：**: <br>A value less than 1 evaluates to the value **1**. &lt;/p&gt; |
| end | boolean | Yes | Whether jumping occurs when the interpolation ends. **true**: Jumping occurs when the interpolation ends. **false**: Jumping occurs when the interpolation starts. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Interpolation curve. |

