# @ohos.curves

Contains interpolator functions such as initialization, third-order Bezier curves, and spring curves.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace curves--><!--Device-unnamed-declare namespace curves-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md#cubicbeziercurve) | Creates a cubic Bezier curve. The curve values must be between 0 and 1. |
| [customCurve](arkts-arkui-curves-customcurve-f.md#customcurve) | Creates a custom curve. |
| [initCurve](arkts-arkui-curves-initcurve-f.md#initcurve) | Implements initialization for the interpolation curve,which is used to create an interpolation curve based on the input parameter. |
| [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingspring) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md#responsivespringmotion) | Creates a responsive spring animation curve. It is a special case of [springMotion](#curvesspringmotion9),with the only difference in the default values. It can be used together with **springMotion**. |
| [springCurve](arkts-arkui-curves-springcurve-f.md#springcurve) | Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**. |
| [springMotion](arkts-arkui-curves-springmotion-f.md#springmotion) | Creates a spring animation curve.If multiple spring animations are applied to the same attribute of an object,each animation replaces their predecessor and inherits the velocity. |
| [stepsCurve](arkts-arkui-curves-stepscurve-f.md#stepscurve) | Creates a step curve. |

### Interfaces

| Name | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | Interface for curve object. |

### Enums

| Name | Description |
| --- | --- |
| [Curve](arkts-arkui-curves-curve-e.md) | enum Curve. |

