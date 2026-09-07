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

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | number | No | Duration of one complete oscillation.Default value: **0.55**Unit: second Value range: (0, +∞)   **NOTE：**If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. |
| dampingFraction | number | No | Damping coefficient.   **0**: undamped. In this case, the spring oscillates forever.  > 0 and &lt; 1: underdamped. In this case, the spring overshoots the equilibrium position. **1**: critically damped.  &gt; 1: overdamped. In this case, the spring approaches equilibrium gradually. Default value: **0.825**Unit: second Value range: 0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0.825**. |
| overlapDuration | number | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different.Default value: **0**Unit: second Value range: [0, +∞)   **NOTE：**A value less than 0 evaluates to the default value **0**.The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in [animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Curve. |

**Examples**

```TypeScript
import { curves } from '@kit.ArkUI';
curves.springMotion(); // Create a spring animation curve with default settings.
curves.springMotion(0.5); // Create a spring animation curve with the specified response value.
curves.springMotion(0.5, 0.6); // Create a spring animation curve with the specified response and dampingFraction values.
curves.springMotion(0.5, 0.6, 0); // Create a spring animation curve with the specified parameter values.
```
