# springMotion

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## springMotion

```TypeScript
export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve--><!--Device-curves-export function springMotion(response?: double, dampingFraction?: double, overlapDuration?: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | double | No | Duration of one complete oscillation. <br>Default value: **0.55**.<br>Unit: second<br>Value range: (0, +∞). <p>**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the default value **0.55** is used. </p> |
| dampingFraction | double | No | Damping coefficient. **0**: undamped. In this case, the spring oscillates forever.<br>   > 0 and &lt; 1: underdamped. In this case, the spring overshoots the equilibrium position.<br>**1**: critically damped. 1: overdamped. In this case, the spring approaches equilibrium gradually.<br>Default value: **0.825**. Unit: second. Value range: [0, +∞). <p>**NOTE：**: <br>A value less than 0 evaluates to the default value **0.825**. </p> |
| overlapDuration | double | No | Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duratio if they are different.<br>Default value: **0**<br>Unit: second<br>Value range: [0, +∞). <p>**NOTE：**<br>A value less than 0 evaluates to the default value **0**. <br>The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and the previous velocity, rather than the **duration** parameter in animation, animateTo, or pageTransition. The time cannot be normalized. Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve. </p> |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve |  |

