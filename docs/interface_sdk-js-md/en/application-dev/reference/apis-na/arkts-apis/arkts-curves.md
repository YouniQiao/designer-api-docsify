# @ohos.curves

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License"),
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


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
| [cubicBezierCurve](arkts-na-curves-cubicbeziercurve-f.md#cubicbeziercurve) | Creates a cubic Bezier curve. The curve values must be between 0 and 1. |
| [customCurve](arkts-na-curves-customcurve-f.md#customcurve) | Creates a custom curve. |
| [initCurve](arkts-na-curves-initcurve-f.md#initcurve) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [interpolatingSpring](arkts-na-curves-interpolatingspring-f.md#interpolatingspring) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**. |
| [responsiveSpringMotion](arkts-na-curves-responsivespringmotion-f.md#responsivespringmotion) | Creates a responsive spring animation curve. It is a special case of springMotion, with the only difference in the default values. It can be used together with **springMotion**. |
| [springCurve](arkts-na-curves-springcurve-f.md#springcurve) | Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**. |
| [springMotion](arkts-na-curves-springmotion-f.md#springmotion) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
| [stepsCurve](arkts-na-curves-stepscurve-f.md#stepscurve) | Creates a step curve. |

### Interfaces

| Name | Description |
| --- | --- |
| [ICurve](arkts-na-curves-icurve-i.md) | Interface for curve object. |

### Enums

| Name | Description |
| --- | --- |
| [Curve](arkts-na-curves-curve-e.md) | enum Curve. |

