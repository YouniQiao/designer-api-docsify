# @ohos.curves

/*
 Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace curves--><!--Device-unnamed-declare namespace curves-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { curves } from 'curves';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cubicBezier](arkts-arkui-curves-cubicbezier-f.md#cubicBezier) | Creates a cubic Bézier curve. The curve values must be between 0 and 1. |
| [cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md#cubicBezierCurve) | Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1. |
| [customCurve](arkts-arkui-curves-customcurve-f.md#customCurve) | Creates a custom curve. |
| [init](arkts-arkui-curves-init-f.md#init) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [initCurve](arkts-arkui-curves-initcurve-f.md#initCurve) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingSpring) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md#responsiveSpringMotion) | Creates a responsive spring animation curve. It is a special case of [springMotion](../../apis-na/arkts-apis/arkts-na-curves-springmotion-f.md#springMotion), with the only difference in the default values. It can be used together with **springMotion**. |
| [spring](arkts-arkui-curves-spring-f.md#spring) | Constructs a spring curve object. |
| [springCurve](arkts-arkui-curves-springcurve-f.md#springCurve) | Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**. |
| [springMotion](arkts-arkui-curves-springmotion-f.md#springMotion) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
| [steps](arkts-arkui-curves-steps-f.md#steps) | Creates a step curve. |
| [stepsCurve](arkts-arkui-curves-stepscurve-f.md#stepsCurve) | Creates a step curve. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [trailOptimizedInterpolatingSpring](arkts-arkui-curves-trailoptimizedinterpolatingspring-f-sys.md#trailOptimizedInterpolatingSpring) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [trailOptimizedResponsiveSpringMotion](arkts-arkui-curves-trailoptimizedresponsivespringmotion-f-sys.md#trailOptimizedResponsiveSpringMotion) | Creates a responsive spring animation curve. It is a special case of [springMotion](../../apis-na/arkts-apis/arkts-na-curves-springmotion-f.md#springMotion), with the only difference in the default values. It can be used together with **springMotion**. |
| [trailOptimizedSpringMotion](arkts-arkui-curves-trailoptimizedspringmotion-f-sys.md#trailOptimizedSpringMotion) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) | Represents a curve object. Different types of curve objects can be created using APIs in this module, including [curves.cubicBezierCurve](../../apis-na/arkts-apis/arkts-na-curves-cubicbeziercurve-f.md#cubicBezierCurve) and [curves.interpolatingSpring](../../apis-na/arkts-apis/arkts-na-curves-interpolatingspring-f.md#interpolatingSpring). The curve object provides interpolation functionality through its member method [interpolate](../../apis-na/arkts-apis/arkts-na-curves-icurve-i.md#interpolate). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [TrailOptimization](arkts-arkui-curves-trailoptimization-i-sys.md) | Trail optimization configuration for spring animations. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [Curve](arkts-arkui-curves-curve-e.md) | Defines an interpolation curve. For details about the curves and animations, see &lt;!--RP1--&gt; [Bezier Curve](../../../../design/ux-design/animation-attributes.md)&lt;!--RP1End--&gt;. |

