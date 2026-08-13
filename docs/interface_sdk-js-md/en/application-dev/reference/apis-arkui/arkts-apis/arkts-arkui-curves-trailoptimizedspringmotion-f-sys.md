# trailOptimizedSpringMotion (System API)

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## trailOptimizedSpringMotion

```TypeScript
function trailOptimizedSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-function trailOptimizedSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve--><!--Device-curves-function trailOptimizedSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | Duration of one complete oscillation.&lt;br&gt;Default value: **0.55**&lt;br&gt;Unit: second&lt;br&gt; Value range: (0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. |
| dampingFraction | number | No | Damping coefficient.&lt;br&gt;**0**: undamped. In this case, the spring oscillates forever.&lt;br&gt;> 0 and &lt; 1: underdamped. In this case, the spring overshoots the equilibrium position.<br>**1**: critically damped.<br>&gt;&lt;br&gt;**1**: critically damped.&lt;br&gt;> 1: overdamped. In this case, the spring approaches equilibrium gradually.&lt;br&gt;Default value: **0.825**&lt;br&gt;Unit: second&lt;br&gt;Value range: 0, +∞)&lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0.825**. |
| overlapDuration | number | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different.&lt;br&gt; Default value: **0**&lt;br&gt;Unit: second&lt;br&gt;Value range: [0, +∞)&lt;br&gt; **NOTE：**&lt;br&gt;A value less than 0 evaluates to the default value **0**.&lt;br&gt; The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No | Trail optimization configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. &lt;br&gt;**NOTE：**&lt;br&gt;The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation]{ |

