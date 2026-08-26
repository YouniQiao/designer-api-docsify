# trailOptimizedSpringMotion (System API)

## Modules to Import

```TypeScript
import curves from '@kit.ArkUI';
```

## trailOptimizedSpringMotion

```TypeScript
function trailOptimizedSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number, trail?: TrailOptimization): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | Duration of one complete oscillation.Default value: **0.55**Unit: second Value range: (0, +∞)   **NOTE：**If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. |
| dampingFraction | number | No | Damping coefficient.   **0**: undamped. In this case, the spring oscillates forever.  > 0 and &lt; 1: underdamped. In this case, the spring overshoots the equilibrium position. **1**: critically damped.  &gt; 1: overdamped. In this case, the spring approaches equilibrium gradually. Default value: **0.825**Unit: second Value range: 0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.825**. |
| overlapDuration | number | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different.Default value: **0**Unit: second Value range: [0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0**.The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. |
| trail | [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | No | Trail optimization configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) | Curve. |
