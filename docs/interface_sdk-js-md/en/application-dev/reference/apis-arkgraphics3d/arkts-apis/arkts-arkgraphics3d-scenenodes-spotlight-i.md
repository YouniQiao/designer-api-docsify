# SpotLight

Spotlight, which inherits from [Light](arkts-arkgraphics3d-scenenodes-light-i.md).

A spotlight emits a conical beam of light in a specific direction,with the intensity of the light decaying according to the angles defined by the innerAngle and outerAngle parameters.Like a point light, a spotlight's intensity also diminishes with distance from the source.

> **NOTE：**
> 
> Ensure that the innerAngle and outerAngle values are proper.
> If the value set for outerAngle is greater than PI/2, it is forcibly set to PI/2 internally.
> If the value set for outerAngle is less than innerAngle, it is forcibly set to innerAngle internally.

**Inheritance/Implementation:** SpotLight extends [Light](arkts-arkgraphics3d-scenenodes-light-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface SpotLight extends Light--><!--Device-unnamed-export interface SpotLight extends Light-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## innerAngle

```TypeScript
innerAngle?: double
```

The inner angle of the spot light, the unit is radian.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** 0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SpotLight-innerAngle?: double--><!--Device-SpotLight-innerAngle?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## outerAngle

```TypeScript
outerAngle?: double
```

The outer angle of the spot light, the unit is radian.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** PI / 4.0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SpotLight-outerAngle?: double--><!--Device-SpotLight-outerAngle?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

