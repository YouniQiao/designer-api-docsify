# trailOptimizedInterpolatingSpring (System API)

## Modules to Import

```TypeScript
import { curves } from 'curves';
```

## trailOptimizedInterpolatingSpring

```TypeScript
function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve
```

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve--><!--Device-curves-function trailOptimizedInterpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number, trail?: TrailOptimization): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value.<br>Value range: (-∞, +∞). |
| mass | number | Yes | Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. <br>Value range: (0, +∞). &lt;p&gt;**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |
| stiffness | number | Yes | Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position.<br>Value range: (0, +∞). &lt;p&gt;**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |
| damping | number | Yes | Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.<br>Value range: (0, +∞)<br> &lt;p&gt;**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No | Trail optimization configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. <br>Note: The spring animation curve is physics-based. Its duration depends on the **interpolatingSpring** parameters, rather than the **duration** parameter in [animation]{ |

