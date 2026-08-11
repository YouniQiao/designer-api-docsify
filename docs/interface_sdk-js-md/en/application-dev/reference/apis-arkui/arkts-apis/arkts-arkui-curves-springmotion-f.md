# springMotion

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## springMotion

```TypeScript
export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

Creates a spring animation curve.If multiple spring animations are applied to the same attribute of an object,each animation replaces their predecessor and inherits the velocity.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | Duration of one complete oscillation. &lt;br&gt;Default value: **0.55**.&lt;br&gt;Unit: second&lt;br&gt;Value range: (0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. &lt;/p&gt; |
| dampingFraction | double | No | Damping coefficient. **0**: undamped. In this case, the spring oscillates forever.&lt;br&gt;> 0 and < 1: underdamped. In this case, the spring overshoots the equilibrium position.&lt;br&gt;**1**: critically damped. 1: overdamped. In this case, the spring approaches equilibrium gradually.&lt;br&gt;Default value: **0.825**. Unit: second. Value range: [0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;A value less than 0 evaluates to the default value **0.825**. &lt;/p&gt; |
| overlapDuration | double | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duratio if they are different.&lt;br&gt;Default value: **0**&lt;br&gt;Unit: second&lt;br&gt;Value range: [0, +∞). &lt;p&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0**. &lt;br&gt;The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |  |

