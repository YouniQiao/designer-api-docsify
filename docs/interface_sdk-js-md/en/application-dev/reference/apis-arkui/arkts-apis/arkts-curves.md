# @ohos.curves

The **Curves** module provides APIs for interpolation calculation to create step, cubic Bezier, and spring curves.

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import curves from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cubicBezier](arkts-arkui-curves-cubicbezier-f.md) | Creates a cubic Bézier curve. The curve values must be between 0 and 1. |
| [cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md) | Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1. |
| [customCurve](arkts-arkui-curves-customcurve-f.md) | Creates a custom curve. |
| [init](arkts-arkui-curves-init-f.md) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [initCurve](arkts-arkui-curves-initcurve-f.md) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md) | Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md), with the only difference in the default values. It can be used together with **springMotion**. |
| [spring](arkts-arkui-curves-spring-f.md) | Constructs a spring curve object. |
| [springCurve](arkts-arkui-curves-springcurve-f.md) | Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**. |
| [springMotion](arkts-arkui-curves-springmotion-f.md) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
| [steps](arkts-arkui-curves-steps-f.md) | Creates a step curve. |
| [stepsCurve](arkts-arkui-curves-stepscurve-f.md) | Creates a step curve. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [trailOptimizedInterpolatingSpring](arkts-arkui-curves-trailoptimizedinterpolatingspring-f-sys.md) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [trailOptimizedResponsiveSpringMotion](arkts-arkui-curves-trailoptimizedresponsivespringmotion-f-sys.md) | Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md), with the only difference in the default values. It can be used together with **springMotion**. |
| [trailOptimizedSpringMotion](arkts-arkui-curves-trailoptimizedspringmotion-f-sys.md) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | Represents a curve object. Different types of curve objects can be created using APIs in this module, including [curves.cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md) and [curves.interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md). The curve object provides interpolation functionality through its member method [interpolate](arkts-arkui-curves-icurve-i.md#interpolate). |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | Trail optimization configuration for spring animations. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [Curve](arkts-arkui-curves-curve-e.md) | Defines an interpolation curve. For details about the curves and animations, see <!--RP1--> [Bezier Curve](../../../../design/ux-design/animation-attributes.md)<!--RP1End-->. |
