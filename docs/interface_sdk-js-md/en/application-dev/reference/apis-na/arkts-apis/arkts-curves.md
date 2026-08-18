# @ohos.curves

Contains interpolator functions such as initialization, third-order Bezier curves, and spring curves.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace curves--><!--Device-unnamed-declare namespace curves-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cubicBezierCurve](arkts-na-curves-cubicbeziercurve-f.md) | Creates a cubic Bezier curve. The curve values must be between 0 and 1. |
| [customCurve](arkts-na-curves-customcurve-f.md) | Creates a custom curve. |
| [initCurve](arkts-na-curves-initcurve-f.md) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [interpolatingSpring](arkts-na-curves-interpolatingspring-f.md) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [responsiveSpringMotion](arkts-na-curves-responsivespringmotion-f.md) | Creates a responsive spring animation curve. It is a special case of springMotion, with the only difference in the default values. It can be used together with **springMotion**. |
| [springCurve](arkts-na-curves-springcurve-f.md) | Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**. |
| [springMotion](arkts-na-curves-springmotion-f.md) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
| [stepsCurve](arkts-na-curves-stepscurve-f.md) | Creates a step curve. |

### Interfaces

| Name | Description |
| --- | --- |
| [ICurve](arkts-na-curves-icurve-i.md) | Interface for curve object. |

### Enums

| Name | Description |
| --- | --- |
| [Curve](arkts-na-curves-curve-e.md) | enum Curve. |

