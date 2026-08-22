# springCurve

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## springCurve

```TypeScript
export function springCurve(velocity: double, mass: double, stiffness: double, damping: double): ICurve
```

Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function springCurve(velocity: double, mass: double, stiffness: double, damping: double): ICurve--><!--Device-curves-export function springCurve(velocity: double, mass: double, stiffness: double, damping: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | double | Yes | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value.Value range: (-∞, +∞). |
| mass | double | Yes | Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. Value range: (0, +∞). <p>**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value 1 is used. </p> |
| stiffness | double | Yes | Stiffness.It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position.Value range: (0, +∞). <p>**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value 1 is used. </p> |
| damping | double | Yes | Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.Value range: (0, +∞). <p>**NOTE：**: <br>If this parameter is set to a value less than or equal to 0, the value 1 is used. </p> |

**Return value:**

| Type | Description |
| --- | --- |
| ICurve | Interpolation curve. |

