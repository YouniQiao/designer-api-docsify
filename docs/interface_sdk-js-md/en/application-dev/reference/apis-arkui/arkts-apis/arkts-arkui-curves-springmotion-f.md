# springMotion

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## springMotion

```TypeScript
function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve--><!--Device-curves-function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | Duration of one complete oscillation.&lt;br&gt;Default value: **0.55**&lt;br&gt;Unit: second&lt;br&gt; Value range: (0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. |
| dampingFraction | number | No | Damping coefficient.&lt;br&gt;**0**: undamped. In this case, the spring oscillates forever.&lt;br&gt;> 0 and &lt; 1: underdamped. In this case, the spring overshoots the equilibrium position.<br>**1**: critically damped.<br>&gt;&lt;br&gt;**1**: critically damped.&lt;br&gt;> 1: overdamped. In this case, the spring approaches equilibrium gradually.&lt;br&gt;Default value: **0.825**&lt;br&gt;Unit: second&lt;br&gt;Value range: 0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0.825**. |
| overlapDuration | number | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different.&lt;br&gt; Default value: **0**&lt;br&gt;Unit: second&lt;br&gt;Value range: [0, +∞)&lt;br&gt; **NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0**.&lt;br&gt; The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. &lt;br&gt;**NOTE：**&lt;br&gt;The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation]{ |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI'
curves.springMotion() // Create a spring animation curve with default settings.
curves.springMotion(0.5) // Create a spring animation curve with the specified response value.
curves.springMotion(0.5, 0.6) // Create a spring animation curve with the specified response and dampingFraction values.
curves.springMotion(0.5, 0.6, 0) // Create a spring animation curve with the specified parameter values.
```

