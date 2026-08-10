# interpolatingSpring

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## interpolatingSpring

```TypeScript
export function interpolatingSpring(velocity: double, mass: double, stiffness: double, damping: double): ICurve
```

构造插值器弹簧曲线对象，生成一条从0到1的动画曲线，实际动画值根据曲线进行插值计算。动画时间由曲线参数决定，不受animation、animateTo中的duration参数控制。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-curves-export function interpolatingSpring(velocity: double, mass: double, stiffness: double, damping: double): ICurve--><!--Device-curves-export function interpolatingSpring(velocity: double, mass: double, stiffness: double, damping: double): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | double | Yes | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value.&lt;br&gt;Value range: (-∞, +∞). |
| mass | double | Yes | Mass, which influences the inertia in the spring system. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. &lt;br&gt;Value range: (0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |
| stiffness | double | Yes | Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position.&lt;br&gt;Value range: (0, +∞). &lt;p&gt;**NOTE：**: &lt;br&gt;If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |
| damping | double | Yes | Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.&lt;br&gt;Value range: (0, +∞)&lt;br&gt; &lt;p&gt;**NOTE：**: &lt;br&gt;If this parameter is set to a value less than or equal to 0, the value **1** is used. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | 曲线对象。 &lt;br&gt;**说明:** 弹性动画曲线为物理曲线，[animation]{ |

